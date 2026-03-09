from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")

def get_ai_recommendation(emotion, weather):

    prompt = f"""
    A user feels {emotion} and the weather is {weather}.

    Suggest:
    1 movie
    1 activity

    Then explain briefly why this helps the user's mood.
    """

    response = llm.invoke(prompt)

    return response.content