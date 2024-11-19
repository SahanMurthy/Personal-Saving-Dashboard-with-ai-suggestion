import streamlit as st
import google.generativeai as genai
from config import GEMINI_API_KEY

def display_gemini_recommendations():
    st.header("Gemini Generated Recommendations")
    
    user_input = st.text_area("Ask for saving tricks or stock market strategies:")
    
    if st.button("Get Recommendations"):
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(user_input)
            
            st.write("Gemini Recommendations:")
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred while fetching Gemini recommendations: {str(e)}")
            st.write("Here are some general financial tips instead:")
            fallback_recommendations = [
                "Create and stick to a budget to track your income and expenses.",
                "Set up an emergency fund to cover 3-6 months of expenses.",
                "Pay off high-interest debt as quickly as possible.",
                "Invest in a diversified portfolio of low-cost index funds.",
                "Maximize contributions to tax-advantaged retirement accounts.",
                "Regularly review and adjust your investment strategy.",
                "Consider dollar-cost averaging for long-term investments.",
                "Stay informed about market trends but avoid making emotional decisions.",
                "Diversify your investments across different asset classes and sectors.",
                "Regularly review and update your financial goals and plans."
            ]
            for tip in fallback_recommendations:
                st.write(f"- {tip}")