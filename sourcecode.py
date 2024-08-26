from textblob import TextBlob
import nltk

# Download required NLTK data
nltk.download('punkt')

def detect_emotion(text):
    # Analyze the sentiment of the text
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    # Determine emotion based on polarity score
    if polarity > 0.1:
        return "happy"
    elif polarity < -0.1:
        return "sad"
    else:
        return "neutral"

def chatbot_response(user_input):
    emotion = detect_emotion(user_input)
    
    if emotion == "happy":
        return "I'm glad to hear that! 😊 What made you feel this way?"
    elif emotion == "sad":
        return "I'm sorry you're feeling down. 😔 Do you want to talk about what's bothering you?"
    else:
        return "I see. Is there something specific on your mind?"

def chat():
    print("Hello! I'm here to talk to you. How are you feeling today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Take care. 😊")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Start the chat
chat()
