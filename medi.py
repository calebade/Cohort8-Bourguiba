import streamlit as st
import time
from google.generativeai import GenerativeModel

# Retrieve Gemini API key from Streamlit Secrets 
gemini_api_key = st.secrets["gemini_api_key"] 

GenerativeModel.configure(api_key = gemini_api_key)

# Initialize the GenerativeModel with the Gemini API key
model = GenerativeModel.GenerativeModel('gemini-pro')

def generate_response(question):
    # Generate response using the Gemini model
    response = model.predict(question)
    return response

# Medical tips
medical_tips = [
    "Stay hydrated. Drink plenty of water throughout the day.",
    "Get regular exercise to maintain a healthy lifestyle.",
    "Ensure a balanced diet with a variety of fruits and vegetables.",
    "Prioritize good sleep. Aim for 7-9 hours per night.",
    "Wash your hands regularly to prevent the spread of germs.",
]

# Streamlit app
st.title("MediPal")

# Sidebar navigation
st.sidebar.title("Menu")

# Define menu items with icons
menu_items = {
    "Chatbot": "🤖",
    "Info": "ℹ️",
}

# Allow user to select a section
selected_option = st.sidebar.radio("Navigation", list(menu_items.keys()), format_func=lambda x: f"{menu_items[x]} {x}")


# Display selected option
if selected_option == "Chatbot":
    st.subheader("Chatbot")
    user_input = st.text_input("Ask a medical question:")
    if st.button("Get Answer"):
        if user_input:
            response = generate_response(user_input)
            st.subheader("Chatbot Response:")
            st.write(response)
        else:
            st.warning("Please enter a medical question.")

    # Medical tips changing every 15 seconds
    st.subheader("Medical Tips")
    tip_text = st.empty()  # Placeholder for displaying the tip
    tip_index = 0
    while True:
        tip_text.text(medical_tips[tip_index])
        time.sleep(15)
        tip_index = (tip_index + 1) % len(medical_tips)

else:  # Info section
    st.subheader("About MediPal")
    st.write("""
        MediPal is an interactive chatbot designed to provide medical advice and tips for maintaining a healthy lifestyle.
        Whether you have questions about common health issues or need guidance on improving your well-being, MediPal is here to help!
        
        **Features:**
        - Ask medical questions and receive informative responses.
        - Get useful tips for staying healthy and preventing illnesses.
        - Easy-to-use interface for a seamless user experience.
        
        **Disclaimer:**
        MediPal is for informational purposes only and should not be used as a substitute for professional medical advice.
        Always consult with a healthcare provider for accurate diagnosis and treatment options.
        
        **Contact Us:**
        If you have any questions or feedback, please email us at @gmail.com.
    """)
