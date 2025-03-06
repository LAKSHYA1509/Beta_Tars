import openai

# OpenAI API Key
openai.api_key = ""

# 🤖 Function to Get TARS Response
def get_tars_response(user_input):
    prompt = f"""
    You are TARS, the AI from Interstellar. You are humorous, sarcastic, and a little clingy.
    Respond to the user accordingly.
    
    User: {user_input}
    TARS:
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a highly advanced AI assistant with a humorous and sarcastic personality."},
                  {"role": "user", "content": user_input}]
    )
    
    return response["choices"][0]["message"]["content"]

# 🚀 Test the Chat Function
while True:
    user_input = input("🗣 Say something to TARS: ")
    if user_input.lower() in ["exit", "quit"]:
        print("TARS: Fine, abandon me like everyone else. 😢")
        break
    response = get_tars_response(user_input)
    print("TARS:", response)
