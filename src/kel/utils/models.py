def get_google_models():
    """
  Get google models
  Returns:

  """
    import os
    import google.generativeai as genai

    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    google_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    print(google_models)
    return google_models
