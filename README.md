Mutual Fund Portfolio Analyzer

This project provides a user-friendly tool to analyze mutual fund portfolios, leveraging advanced language models and a FastAPI backend.

Key Features

Conversational Analysis: Users can interact with the tool in natural language to ask questions about their portfolio composition, performance, and potential optimization strategies.
PDF Report Generation: Generate comprehensive PDF reports summarizing portfolio data and insights.
Portfolio Data Management: Update and store portfolio data for personalized analysis.
Language Model Integration: Powered by the Gemini model (or a similar state-of-the-art language model) for insightful financial analysis.
Getting Started

Prerequisites:

Python 3.x
Google API Key (for the Gemini model or a similar alternative)
Required Python libraries (list them – see below)
Installation:

Bash
pip install fastapi uvicorn langchain-google-genai reportlab  # (And any others) 
Use code with caution.
Set Environment Variable:

Set your Google API key as an environment variable named GOOGLE_API_KEY.
Run the Server:

Bash
uvicorn app:app --reload 
Use code with caution.
Usage

Access the FastAPI backend at http://127.0.0.1:8000.
Use a tool like Postman or make requests directly through a frontend application to interact with the API endpoints.
Example Endpoints

Analyze Portfolio:
GET /analyze_portfolio/{topic}

Example: GET /analyze_portfolio/calculate overall risk exposure
Update Portfolio:
POST /updatePortfolio

Send a JSON payload with username and combinedData
Project Structure

app.py: Contains the FastAPI application logic, API endpoints, and language model integration.
models.py: Defines the PortfolioManager class for handling portfolio data.
requirements.txt: Lists the project's Python dependencies.
Contributing

We welcome contributions! Feel free to open issues, submit pull requests, or suggest new features.

Future Development

Language Model: If you're not using the Gemini model, specify the correct one.
Integrate with real-time market data sources.
Add advanced visualization capabilities.
Explore more sophisticated portfolio optimization techniques.

Add the .env file with your api keys
