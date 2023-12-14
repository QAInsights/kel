import pytest
from unittest.mock import patch
from kel.inputs.gatekeeper import gatekeeper_tasks
from kel.gpt.askgpt import gpt
from kel.config.get_configs import get_enable_openai_assistant
from kel.assistant.summon_assistant import summon_assistant
from src.kel.__main__ import main

@patch('kel.config.get_configs.get_enable_openai_assistant')
@patch('kel.assistant.summon_assistant.summon_assistant')
@patch('asyncio.run')
def test_main_when_openai_assistant_enabled(mock_asyncio_run, mock_summon_assistant, mock_get_enable_openai_assistant):
    mock_get_enable_openai_assistant.return_value = True
    main()
    mock_summon_assistant.assert_called_once()
    mock_asyncio_run.assert_not_called()

@patch('kel.config.get_configs.get_enable_openai_assistant')
@patch('kel.assistant.summon_assistant.summon_assistant')
@patch('asyncio.run')
def test_main_when_openai_assistant_disabled(mock_asyncio_run, mock_summon_assistant, mock_get_enable_openai_assistant):
    mock_get_enable_openai_assistant.return_value = False
    main()
    mock_summon_assistant.assert_not_called()
    mock_asyncio_run.assert_called_once_with(gpt())
