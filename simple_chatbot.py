# simple_chatbot.py

class ChatBot:
    def __init__(self):
        self.name = "EcoBot"

    def get_response(self, message):
        # Basic response logic for placeholder
        message = message.lower()
        if "recycle" in message:
            return "You can recycle plastic bottles, paper, and aluminum cans easily."
        elif "reuse" in message:
            return "Consider reusing containers, bags, and jars whenever possible."
        elif "hello" in message or "hi" in message:
            return "Hello! I'm here to help you with sustainability tips."
        else:
            return "I'm still learning. Try asking about recycling or reuse tips."

chatbot = ChatBot()
