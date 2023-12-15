import google.generativeai as genai

from kel.config import get_configs as config
from kel.utils.utils import print_in_color


def ask_google(client=None, question=None, prompt=None, model=None, temperature=None):
    """
    Ask Google GPT

    :param client:
    :param question:
    :param prompt:
    :param model:
    :param temperature:
    :return:
    """
    model = genai.GenerativeModel(model)
    # Get safety settings
    safety_settings = []
    print(prompt)
    question = question + prompt
    if config.get_google_safety_settings() is not None:
        for k, v in config.get_google_safety_settings().items():
            safety_settings.append({"category": k, "threshold": v})

    print("Safety settings are:", safety_settings)

    if config.get_default_google_streaming_response():
        response = model.generate_content(question,
                                          stream=True,
                                          safety_settings=safety_settings)
        for chunk in response:
            try:
                print_in_color(chunk.text, config.get_response_color())
            except Exception as e:
                print(f'{type(e).__name__}: {e}')
    else:
        response = model.generate_content(question,
                                          safety_settings=safety_settings)
        print_in_color(response.text, config.get_response_color())

    if config.get_google_prompt_feedback():
        # TODO in rich table
        print_in_color(response.prompt_feedback, config.get_info_color())

    if config.get_view_all_response_candidates():
        for count, response in enumerate(response.candidates):
            if count > 0:
                print(response.content.parts[0].text)
