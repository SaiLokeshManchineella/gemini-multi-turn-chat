# Gemini Multi-Turn Chat

This is a simple console-based chatbot using the Google Gemini Free API. The script demonstrates multi-turn conversation with context preservation and allows you to set model parameters like temperature.

## Features
- Multi-turn chat: The bot remembers previous messages in the session.
- Context-aware: Each message is sent with conversation history.
- Adjustable creativity: Set the model's temperature parameter at runtime.
- Console-based: No GUI, just input and output in the terminal.

## Requirements
- Python 3.8+
- `google-generativeai` Python package
- A valid Gemini API key (get one from Google AI Studio)

## Setup
1. Install dependencies:
   ```bash
   pip install google-generativeai
   ```
2. Set your Gemini API key as an environment variable (optional):
   ```bash
   export GEMINI_API_KEY=your_api_key_here
   ```
   Or, you can enter it when prompted by the script.

## Usage
Run the script in your terminal:
```bash
python gemini_chat.py
```
- Enter your Gemini API key if prompted.
- Set the temperature (0.0-1.0) for model creativity.
- Chat with Gemini! The script will prompt you for two turns and print the final response.

## Notes
- You can extend the script for more turns by repeating the input/response block.
- The script uses the `gemini-1.5-flash` model by default. 