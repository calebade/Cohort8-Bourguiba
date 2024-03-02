import streamlit as st
import time
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)

# Initialize the Langchain chat model
chat_model = ChatOpenAI(engine="davinci")

# Define conversation memory
conversation_memory = ConversationBufferWindowMemory(max_length=3)

# Initialize the conversation chain
conversation_chain = ConversationChain(
    chat_model=chat_model,
    memory=conversation_memory,
    human_message_template=HumanMessagePromptTemplate(),
    system_message_template=SystemMessagePromptTemplate(),
    chat_prompt_template=ChatPromptTemplate(),
    messages_placeholder=MessagesPlaceholder(),
)

def generate_response(question):
    # Get response from the conversation chain
    response = conversation_chain.respond_to_message(question)
    return response

# Medical tips
medical_tips = [
    "Tip 1: Stay hydrated. Drink plenty of water throughout the day.",
    "Tip 2: Get regular exercise to maintain a healthy lifestyle.",
    "Tip 3: Ensure a balanced diet with a variety of fruits and vegetables.",
    "Tip 4: Prioritize good sleep. Aim for 7-9 hours per night.",
    "Tip 5: Wash your hands regularly to prevent the spread of germs.",
    "Tip 6: Manage stress through activities like meditation or deep breathing.",
    "Tip 7: Avoid smoking and limit alcohol consumption.",
    "Tip 8: Wear sunscreen to protect your skin from harmful UV rays.",
    "Tip 9: Practice proper posture to prevent back and neck pain.",
    "Tip 10: Laughing is good for your health. Find time for humor."
]

# Streamlit app
st.title("MediPal Chatbot")
user_input = st.text_input("Ask a medical question:")
if st.button("Get Answer"):
    if user_input:
        response = generate_response(user_input)
        st.subheader("Chatbot Response:")
        st.write(response)
    else:
        st.warning("Please enter a medical question.")

# Random medical tips section
st.sidebar.title("Random Medical Tips")

# Display a new tip every 30 seconds
tip_index = 0
while True:
    st.sidebar.subheader("Medical Tip of the Day:")
    st.sidebar.write(medical_tips[tip_index])
    time.sleep(30)  # Wait for 30 seconds before changing the tip
    tip_index = (tip_index + 1) % len(medical_tips)
