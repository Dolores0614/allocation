import streamlit as st
import function

def main():
    st.title("Portfolio Optimization")

    tickers = st.text_input("Enter stock tickers (comma separated):")
    investment_amount = st.number_input("Enter investment amount:", min_value=0.0, format="%f")
    
    risk_preference_input = st.selectbox("Select risk preference:", ["Risk Averse", "Risk Neutral", "Risk Seeking"])

    risk_preference = 'neutral'
    if risk_preference_input == "Risk Averse":
        risk_preference = 'averse'
    elif risk_preference_input == "Risk Seeking":
        risk_preference = 'like'

    if st.button("Run Optimization"):
        if tickers:
            tickers = tickers.split(',')
            tickers = [ticker.strip() for ticker in tickers]  # Remove any extra whitespace
            try:
                weights, allocation, leftover, performance = function.optimize_portfolio(tickers, investment_amount, risk_preference)

                st.write("\nOptimal Weights:")
                for ticker, weight in weights.items():
                    st.write(f"The cleaned weight for {ticker} is: {weight:.4f}")

                st.write("\nInvestment Allocation:")
                if allocation:
                    for ticker, amount in allocation.items():
                        st.write(f"The allocation for {ticker} is: {amount:.0f} stocks")
                else:
                    st.write("No allocation was made.")

                st.write(f"\nFunds Remaining: ${leftover:.2f}")

                st.write("\nPortfolio Performance:")
                st.write(f"Expected annual return: {performance[0]:.2f}")
                st.write(f"Annual volatility: {performance[1]:.2f}")
                st.write(f"Sharpe ratio: {performance[2]:.2f}")
            except ValueError as e:
                st.error(f"Error: {e}")
        else:
            st.error("Please enter valid stock tickers.")

if __name__ == "__main__":
    main()
