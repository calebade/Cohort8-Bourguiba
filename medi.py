import streamlit as st
import time
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def generate_response(question):
    # Tokenize the input question
    input_ids = tokenizer.encode(question, return_tensors="pt")

    # Generate response using the GPT-2 model
    output = model.generate(input_ids, max_length=150, num_return_sequences=1, temperature=0.7)

    # Decode the generated response
    response = tokenizer.decode(output[0], skip_special_tokens=True)
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
    "Tip 10: Laughing is good for your health. Find time for humor.",
    "Tip 11: Stay socially connected with friends and family.",
    "Tip 12: Limit processed food intake and focus on whole foods.",
    "Tip 13: Take breaks from screen time to reduce eye strain.",
    "Tip 14: Practice good oral hygiene for overall health.",
    "Tip 15: Stretch regularly to improve flexibility and reduce muscle tension.",
    "Tip 16: Learn something new to keep your mind active.",
    "Tip 17: Spend time in nature for mental and physical well-being.",
    "Tip 18: Limit caffeine intake, especially in the evening.",
    "Tip 19: Practice mindful eating to savor your meals.",
    "Tip 20: Set realistic health goals and celebrate your achievements."
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
    tip_index = (tip_index + 1) % len(medical_tips)￼Enter
