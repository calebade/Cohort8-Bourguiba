import streamlit as st
import time
import random

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
        # Check for common keywords in the user input and provide a relevant response
        if "headache" in user_input.lower():
            response = "You could try taking some over-the-counter pain relievers like ibuprofen or acetaminophen. If the headache persists or worsens, it's best to consult with a healthcare professional."
        elif "fever" in user_input.lower():
            response = "Make sure to rest and stay hydrated. You can also take some fever-reducing medication like acetaminophen. If the fever persists or is accompanied by other symptoms, seek medical attention."
        elif "cough" in user_input.lower():
            response = "Try staying hydrated and using cough drops or cough syrup to soothe your throat. If the cough persists for more than a few days or is severe, consult with a doctor."
        elif "sore throat" in user_input.lower():
            response = "Gargling with warm salt water and staying hydrated can help alleviate a sore throat. If the sore throat persists or is accompanied by other symptoms, consult with a healthcare professional."
        else:
            response = "I'm sorry, I don't have information on that topic. It's best to consult with a healthcare professional for personalized advice."
        
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
