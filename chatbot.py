# Εισάγουμε τις απαραίτητες βιβλιοθήκες
# Importing necessary libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Δημιουργία του chatbot
# Creating the chatbot
chatbot = ChatBot("MyBot")

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Ξεκινάμε μια συνομιλία με το chatbot
# Starting a conversation with the chatbot
print("Γράψε μια ερώτηση και το chatbot θα σου απαντήσει! (Πληκτρολόγησε 'exit' για έξοδο)")
print("Type a question and the chatbot will respond! (Type 'exit' to quit)")

# Βρόχος για συνεχή συνομιλία με τον χρήστη μέχρι να γράψει 'exit'
# Loop for continuous conversation with the user until they type 'exit'
while True:
    try:
        # Πάρε την είσοδο του χρήστη
        # Get user input
        user_input = input("Εσύ: ")  # User: 

        # Έλεγχος αν ο χρήστης θέλει να τερματίσει τη συνομιλία
        # Check if the user wants to end the conversation
        if user_input.lower() == 'exit':
            print("Αντίο!")
            break

        # Ζήτα από το chatbot να δώσει απάντηση
        # Ask the chatbot to respond
        response = chatbot.get_response(user_input)

        # Εκτύπωση της απάντησης του chatbot
        # Print the chatbot's response
        print("Bot: ", response)

    # Διαχείριση εξαιρέσεων σε περίπτωση σφάλματος
    # Handle exceptions in case of an error
    except Exception as e:
        print("Παρουσιάστηκε σφάλμα: ", e)
        break
