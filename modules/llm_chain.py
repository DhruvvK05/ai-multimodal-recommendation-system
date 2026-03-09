from langchain_ollama import ChatOllama

# initialize LLM
llm = ChatOllama(model="llama3")


def get_ai_recommendation(emotion, weather, time_of_day, mood_goal, energy_level):

    prompt = f"""
User context:

Emotion: {emotion}
Weather: {weather}
Time of Day: {time_of_day}
Goal: {mood_goal}
Energy Level: {energy_level}/10

Suggest:
1 movie
1 activity
Explain briefly why it suits the user.
"""

    response = llm.invoke(prompt)

    return response.content