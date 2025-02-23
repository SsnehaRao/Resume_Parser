from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

def main():
    # Chatbot Configuration
    print("Welcome to the Chatbot!")
    model = "mixtral-8x7b-32768"  # Fixed model
    conversational_memory_length = 10  # Fixed memory length

    # Initialize chat memory
    memory = ConversationBufferWindowMemory(k=conversational_memory_length)

    # Initialize Groq Langchain chat object with API key directly
    groq_chat = ChatGroq(
        groq_api_key="",  # Replace with your actual API key
        model_name=model
    )
    conversation = ConversationChain(
        llm=groq_chat,
        memory=memory,
        output_key="response"  # Explicit output key
    )

    print("\nChatbot initialized. Type 'exit' to end the conversation.\n")

    while True:
        # User input
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Ending the conversation. Goodbye!")
            break

        # Get response from the model
        try:
            response = conversation.run(user_input)  # Using .run() directly
        except ValueError as e:
            print(f"Error: {e}")
            continue

        # Print AI response
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()