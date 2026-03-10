from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3", temperature=0.7)

def get_ai_recommendation(emotion, weather, city, time_of_day, mood_goal, energy_level):

    prompt = f"""
You are an AI lifestyle assistant.

User Context:
Emotion: {emotion}
Weather: {weather}
City: {city}
Time: {time_of_day}
Goal: {mood_goal}
Energy Level: {energy_level}/10

Give recommendations in this format:

Activity:
Place to Visit in {city}:
Suggestions:
Reason:

Keep it short and point-wise.
"""

    response = llm.invoke(prompt)

    return response.content