import streamlit as st
import time
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
model.eval()

def generate_response(question):
    prompt = f"Question: {question}\nAnswer: "
    generated = torch.tensor(tokenizer.encode(prompt)).unsqueeze(0)
    generated = generated.to(device)

    sample_outputs = model.generate(
        generated,
        do_sample=True,
        top_k=50,
        max_length=300,
        top_p=0.95,
        num_return_sequences=3
    )

    responses = [tokenizer.decode(sample_output, skip_special_tokens=True) for sample_output in sample_outputs]
    return responses

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
st.title("MedPal Chatbot")
user_input = st.text_input("Ask a medical question:")
if st.button("Get Answer"):
    if user_input:
        responses = generate_response(user_input)
        st.subheader("Chatbot Response:")
        for i, response in enumerate(responses):
            st.write(f"Option {i + 1}: {response}")
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
