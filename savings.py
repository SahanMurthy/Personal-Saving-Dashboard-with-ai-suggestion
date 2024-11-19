import streamlit as st
import pandas as pd
import requests

# Function to fetch live exchange rate
def get_live_exchange_rate():
    # Example API endpoint (use your preferred service and API key if required)
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data["rates"]["INR"]  # Get the INR exchange rate
        else:
            st.error("Error fetching exchange rates. Using default rate.")
            return 82.5  # Fallback default conversion rate
    except Exception as e:
        st.error(f"Error: {e}")
        return 82.5  # Fallback default conversion rate

def display_savings_overview():
    st.header("Savings Overview")

    # Fetch the live exchange rate for USD to INR
    conversion_rate = get_live_exchange_rate()
    st.write(f"Current Exchange Rate (1 USD to INR): ₹{conversion_rate:.2f}")

    # Currency selection
    currency = st.radio("Select Currency:", ["₹ (INR)", "$ (USD)"])

    # User input for savings
    savings_amount = st.number_input(f"Enter your total savings ({currency}):", min_value=0.0, format="%.2f")
    monthly_contribution = st.number_input(f"Enter your monthly contribution ({currency}):", min_value=0.0, format="%.2f")
    duration_years = st.number_input("Enter the duration (in years):", min_value=1, max_value=30, value=5)

    if st.button("Calculate Future Savings"):
        # Calculate future savings
        future_savings = savings_amount + (monthly_contribution * 12 * duration_years)
        average_savings = future_savings / (duration_years * 12)

        # Convert to selected currency
        if currency == "₹ (INR)":
            future_savings_inr = future_savings if currency == "₹ (INR)" else future_savings * conversion_rate
            average_savings_inr = average_savings if currency == "₹ (INR)" else average_savings * conversion_rate
            st.write(f"Your estimated savings after {duration_years} years will be: ₹{future_savings_inr:.2f}")
            st.write(f"Your average savings contribution per month will be: ₹{average_savings_inr:.2f}")
        else:
            st.write(f"Your estimated savings after {duration_years} years will be: ${future_savings:.2f}")
            st.write(f"Your average savings contribution per month will be: ${average_savings:.2f}")

        # Recommendations based on average savings
        if currency == "₹ (INR)":
            threshold_low = 100 * conversion_rate  # Convert USD thresholds to INR
            threshold_high = 500 * conversion_rate
        else:
            threshold_low = 100
            threshold_high = 500

        st.write("### Recommendation:")
        if average_savings < threshold_low:
            st.write("Consider increasing your monthly contributions to reach your savings goals.")
        elif threshold_low <= average_savings < threshold_high:
            st.write("You're on the right track! Maintain your contributions and explore high-yield savings options.")
        else:
            st.write("Excellent job! Your savings strategy is strong. Consider investing some of your savings for greater returns.")

        # Display savings projection chart
        months = list(range(0, duration_years * 12 + 1))
        savings_projection = [savings_amount + (monthly_contribution * month) for month in months]

        # Adjust savings projection based on currency
        if currency == "₹ (INR)":
            savings_projection = [amount * conversion_rate for amount in savings_projection]
        df = pd.DataFrame({'Month': months, 'Savings': savings_projection})
        st.line_chart(df.set_index('Month'))

# Call the function to display the Savings Overview page
if __name__ == "__main__":
    display_savings_overview()
