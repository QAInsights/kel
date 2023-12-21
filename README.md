# 💬 Kel

[![Install with pip](https://img.shields.io/badge/Install_with-pip-blue)](https://pypi.org/project/kel-cli)
![PyPI - Version](https://img.shields.io/pypi/v/kel-cli)

Kel is your AI assistant in your CLI. 

> Kel `கேள்` means `ask` in Tamil.

## 🎥 Demo

![Kel-Demo](https://raw.githubusercontent.com/QAInsights/kel-docs/main/static/img/kel-demo.gif)

## ✅ Features

- Free and Open Source
- Bring your own API keys
- Supports multiple Large Language Models (LLMs) like GPT-4, Claude, ollama2, and Google.
- Supports OpenAI assistants to chat with your documents
- Customizable

## 🧩 Installation

### Pre-requisites
- Python 3.6 or higher
- pip3
- API keys for OpenAI and other LLMs

### ⛳ Steps

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install kel-cli

# copy the default config file to current user's home directory
curl -O https://raw.githubusercontent.com/QAInsights/kel/main/config.toml
mkdir -p ~/.kel
mv config.toml ~/.kel/config.toml 
```
Open the config file to customize the settings.

Update the LLM API keys in the OS environment variables. 

## Usage

```bash
kel -v
```

```bash
kel -h
```

```bash
kel "git command to rebase"
```

```bash
kel "command to get active connections in linux"
```

```bash
kel "What was the population of India in 1990?"

> I'm sorry, I can only assist with questions related to software engineering and command line tools. 
I am unable to provide information on the population of India in 1990.
```

Now change the prompt and ask the same question.
```bash
kel "What was the population of India in 1990?" -p "You are a demography expert" 

> The population of India in 1990 was around 874 million people.
```

Now change the LLM and ask the same question.
```bash
kel "What was the population of India in 1990?" -p "You are a demography expert" -c ollama -m llama2 
```

To view the config file details, run the following command.
```bash
kel -s openai
```

> [!IMPORTANT]  
> LLMs price varies based on the usage. Please check the pricing before using it.  
> LLMs can make mistakes. Review the answers before using it.  


## 🧰 Configuration

Kel can be configured using a [config file](./config.toml). It is a TOML file and supports vast number of options. 

The default config file is `~/.kel/config.toml` or `~/.config/kel/config.toml` or `KEL_CONFIG_FILE` environment variable.

## ⚙️ Defaults

- OpenAI's `gpt-3.5-turbo-1106`
- Display stats
- Default prompt focuses on developers
- Copies the answer to clipboard
- and more...

## 💰 Support

If you like this project, please consider donating to the following addresses.

- Buy me a coffee: https://www.buymeacoffee.com/qainsights



