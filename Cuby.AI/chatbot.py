import json
import random
import command_speak

def chatbot(inp):
    with open('cuby.json') as file:
        intents = json.load(file)["intents"]

    matched_intents = []
    for intent in intents:
        if inp in intent["patterns"]:
            matched_intents.append(intent)

    if matched_intents:
        selected_intent = random.choice(matched_intents)
        response = random.choice(selected_intent["responses"])
        command_speak.speak(response)
        return response
    else:
        ""

