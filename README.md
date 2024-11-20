# Personal-Saving-Dashboard-with-ai-suggestion
Personal Saving Dashboard with gemini-ai suggestion, live-stock market, etc... 

**Authentication Features**  
- **User Login System:**  
  - Users authenticate with a securely stored username and password in a YAML file.  
  - Passwords are hashed using SHA-256 for enhanced security.  

- **Session Management:**  
  - Users remain logged in throughout their session and receive a personalized welcome message.  
  - A sidebar logout button allows for secure session termination.  

- **Access Control:**  
  - Dashboard sections are restricted until the user is authenticated.  

![Screenshot 2024-11-20 182155](https://github.com/user-attachments/assets/4baeb1b6-efb3-4a54-ada7-e9069cdf14fd)


**1. Savings Overview**  
- **Features:**  
  - Input current savings, monthly contributions, and duration to calculate future savings.  
  - Provides personalized recommendations based on average savings.  
  - Includes a projection chart for visualizing savings growth.  
- **Secure Access:** Available only after authentication.
![Screenshot 2024-11-20 182304](https://github.com/user-attachments/assets/cbd29583-347f-4669-b976-969a1921953f)


**2. Fixed Deposit Calculator**  
- **Features:**  
  - Calculate maturity amounts for fixed deposits.  
  - Enter deposit amount, annual interest rate, and duration.  
  - Visualize growth with a line chart of maturity projections.  
- **Secure Access:** Requires successful login.  
![Screenshot 2024-11-20 182321](https://github.com/user-attachments/assets/864a83bb-72ff-42ad-98f9-0b29ea96abc3)


**3. Real-time Stock Market Data**  
- **Features:**  
  - Retrieve live stock data for selected symbols.  
  - View metrics such as closing prices, daily changes, and moving averages.  
  - Includes detailed charts for closing prices and trends.  
- **Secure Access:** Only authenticated users can access real-time data.

![Screenshot 2024-11-20 182506](https://github.com/user-attachments/assets/4a2f0e3c-c079-44be-ba57-92ce37a4e549)
![Screenshot 2024-11-20 182453](https://github.com/user-attachments/assets/5315b57d-c07a-4a39-b87c-1ff3caf732f3)

  
**4. AI Tips & Recommendations**  
- **Features:**  
  - AI-generated savings tips and investment strategies tailored to user input.  
  - Suggestions for stock investments based on real-time data.  
  - Dynamically updated based on user portfolio or savings goals.  
- **Secure Access:** Limited to authenticated users for personalization.  
![Screenshot 2024-11-20 182522](https://github.com/user-attachments/assets/3f604e8d-e14b-4711-b81f-39db27086a02)


**App Workflow**  
1. **Login Page:**  
   - Users enter their credentials to gain access.  
2. **Dashboard Navigation:**  
   - After authentication, users can navigate between:  
     - Savings Overview  
     - Fixed Deposit Calculator  
     - Stock Market Data  
     - AI Recommendations  
3. **Secure Logout:**  
   - A logout button ensures proper session termination.
