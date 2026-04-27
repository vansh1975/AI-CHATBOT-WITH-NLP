pip install nltk spacy
import nltk
from nltk.tokenize import word_tokenize
import random
# Download required NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')  # extra safety for newer versions
# Sample responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm fine!", "Doing great!", "All good!"],
    "bye": ["Goodbye!", "See you!", "Bye!"]
}
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        # Tokenize input (safe)
        try:
            tokens = word_tokenize(user_input)
        except:
            tokens = user_input.split()
        found = False
        
        for key in responses:
            if key in user_input:
                print("Chatbot:", random.choice(responses[key]))
                found = True
                break
        
        if not found:
            print("Chatbot: Sorry, I don't understand.")
        if "bye" in user_input:
            break
# Run chatbot
chatbot()
