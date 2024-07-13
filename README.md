
```markdown
# Portfolio Optimization Web Application

## Project Overview

This project is a web application built using Flask and Streamlit that helps users optimize their investment portfolios. Users can input stock tickers, investment amounts, and risk preferences. The application will use historical data, news sentiment analysis, and financial models to optimize the portfolio, providing optimal investment weights and portfolio performance metrics.

## Features

1. **Stock Data Fetching**:
   - Uses the `yfinance` library to fetch historical data for specified stocks.
   
2. **News Sentiment Analysis**:
   - Analyzes news sentiment related to stocks using NLTK's VADER sentiment analyzer.
   
3. **Portfolio Optimization**:
   - Calculates historical mean returns and covariance matrices for stocks.
   - Adjusts expected returns based on user risk preferences.
   - Optimizes the portfolio using the Pypfopt library to maximize the Sharpe ratio.

4. **Risk and Performance Metrics**:
   - Calculates and displays expected annual return, annual volatility, and Sharpe ratio for the portfolio.
   - Provides discrete allocation based on the user's investment amount.


## Project Structure

- `app.py`: The main application file containing the Streamlit user interface and logic for calling the optimization functions.
- `function.py`: Contains functions for data fetching, sentiment analysis, and portfolio optimization.
- `requirements.txt`: Lists all the required Python libraries.
- `Procfile`: Heroku deployment file defining how to start the application.
- `nltk.txt`: Lists the NLTK datasets needed for the application.
```

## Example

In the application, try the following example stock tickers:

AAPL, GOOGL, MSFT, AMZN, FB

Enter an investment amount (e.g., 10000), select a risk preference (e.g., Risk Neutral), and click the "Run Optimization" button to see the results.

## Contribution

Feel free to submit pull requests and issues to help improve this project.

## License

This project is open-source and available under the MIT License.
```

Save this README file as `README.md` and place it in the root directory of your project. This will help others understand your project and its features, and guide them on how to install and use the application. If you need any further adjustments, please let me know!
