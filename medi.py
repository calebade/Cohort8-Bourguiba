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
