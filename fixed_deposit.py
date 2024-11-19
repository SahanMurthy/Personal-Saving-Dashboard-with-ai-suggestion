import streamlit as st
import pandas as pd
import requests

# Function to fetch live exchange rate
def get_live_exchange_rate():
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

def display_fixed_deposit_calculator():
    st.header("Fixed Deposit Calculator")
    
    # Fetch the live exchange rate for USD to INR
    conversion_rate = get_live_exchange_rate()
    st.write(f"Current Exchange Rate (1 USD to INR): ₹{conversion_rate:.2f}")

    # Currency selection
    currency = st.radio("Select Currency:", ["₹ (INR)", "$ (USD)"])
    
    # User input for fixed deposit
    deposit_amount = st.number_input(f"Enter your fixed deposit amount ({currency}):", min_value=0.0, format="%.2f")
    interest_rate = st.number_input("Enter the annual interest rate (in %):", min_value=0.0, format="%.2f")
    years = st.number_input("Enter the duration (in years):", min_value=1, max_value=30, value=5)

    if st.button("Calculate Maturity Amount"):
        # Calculate maturity amount
        maturity_amount = deposit_amount * (1 + (interest_rate / 100)) ** years

        if currency == "₹ (INR)":
            st.write(f"The maturity amount after {years} years will be: ₹{maturity_amount:.2f}")
        else:
            st.write(f"The maturity amount after {years} years will be: ${maturity_amount:.2f}")
        
        # Maturity projection chart
        years_range = list(range(1, years + 1))
        maturity_projection = [deposit_amount * (1 + (interest_rate / 100)) ** year for year in years_range]

        # Adjust projection to selected currency
        if currency == "₹ (INR)":
            maturity_projection = [amount * conversion_rate for amount in maturity_projection]
        
        # Create and display chart
        df = pd.DataFrame({'Year': years_range, 'Maturity Amount': maturity_projection})
        st.line_chart(df.set_index('Year'))

# Call the function to display the Fixed Deposit Calculator page
if __name__ == "__main__":
    display_fixed_deposit_calculator()
