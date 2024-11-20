import streamlit as st
import yaml
from yaml.loader import SafeLoader
import hashlib

from savings import display_savings_overview
from fixed_deposit import display_fixed_deposit_calculator
from stock_market import display_stock_market_data
from gemini_recommendations import display_gemini_recommendations

# Initialize the session state for current section and authentication
if 'current_section' not in st.session_state:
    st.session_state['current_section'] = 'savings'  # Default to Savings Overview
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password):
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    credentials = config['credentials']['usernames']
    if username in credentials:
        if credentials[username]['password'] == hash_password(password):
            return True, credentials[username]['name']
    return False, None

# Function to add a full-screen background
def add_full_screen_background(image_path="images\background.jpeg", color="Blue"):
    """Add a full-screen background using an image or color."""
    background_css = f"""
    <style>
        .stApp {{
            background: url('{image_path}') no-repeat center fixed;
            background-size: cover;
            background-color: {color}; /* Fallback color */
        }}
        h1 {{
            color: dark blue; /* dark blue color for the header */
            text-align: center;
            margin-bottom: 20px;
        }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)

def main():
    # Configure the Streamlit page settings
    st.set_page_config(page_title="Personal Savings Dashboard", layout="wide")

    # Add a background image with fallback color
    add_full_screen_background(image_path="background.jpeg", color="#f0f8ff")

    # Display heading
    st.markdown("<h1>Personal Savings Dashboard</h1>", unsafe_allow_html=True)

    if not st.session_state['authenticated']:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            authenticated, name = authenticate(username, password)
            if authenticated:
                st.session_state['authenticated'] = True
                st.session_state['name'] = name
                st.rerun()
            else:
                st.error("Invalid username or password")
    else:
        st.sidebar.write(f"Welcome, {st.session_state['name']}!")
        if st.sidebar.button("Logout"):
            st.session_state['authenticated'] = False
            st.rerun()

        # Create buttons for navigation
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("Savings Overview"):
                st.session_state['current_section'] = 'savings'
        with col2:
            if st.button("Fixed Deposit Calculator"):
                st.session_state['current_section'] = 'fixed-deposit'
        with col3:
            if st.button("Stock Market Data"):
                st.session_state['current_section'] = 'stock-market'
        with col4:
            if st.button("AI Recommendations"):
                st.session_state['current_section'] = 'gemini_recommendations'

        # Show the current section content
        section = st.session_state['current_section']
        if section == "savings":
            display_savings_overview()
        elif section == "fixed-deposit":
            display_fixed_deposit_calculator()
        elif section == "stock-market":
            display_stock_market_data()
        elif section == "gemini_recommendations":
            display_gemini_recommendations()

if __name__ == "__main__":
    main()

# Display a reminder on how to start the app
print("To run the Personal Savings Dashboard, use the command: streamlit run main.py")
