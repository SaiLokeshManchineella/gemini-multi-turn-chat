import os
import google.generativeai as genai

# Get API key from environment variable or prompt user
API_KEY = os.getenv('GEMINI_API_KEY')
if not API_KEY:
    API_KEY = input('Enter your Gemini API key: ')

genai.configure(api_key=API_KEY)

# Allow user to set temperature (creativity)
def get_temperature():
    try:
        temp = float(input('Set model temperature (0.0-1.0, default 0.5): ') or '0.5')
        if 0.0 <= temp <= 1.0:
            return temp
        else:
            print('Temperature must be between 0.0 and 1.0. Using default 0.5.')
            return 0.5
    except ValueError:
        print('Invalid input. Using default 0.5.')
        return 0.5

def get_num_turns():
    try:
        n = int(input('How many chat turns? (default 5): ') or '5')
        if n > 0:
            return n
        else:
            print('Number of turns must be positive. Using default 5.')
            return 5
    except ValueError:
        print('Invalid input. Using default 5.')
        return 5

temperature = get_temperature()
num_turns = get_num_turns()

# Initialize Gemini chat session
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

conversation = []
last_response = None

for turn in range(num_turns):
    user_input = input('You: ')
    conversation.append({'role': 'user', 'parts': [user_input]})
    response = chat.send_message(user_input, generation_config={"temperature": temperature})
    conversation.append({'role': 'model', 'parts': [response.text]})
    print(f"Gemini: {response.text}\n")
    last_response = response.text

# Print the final Gemini response (from the last turn)
print(f"Final Gemini response: {last_response}") 