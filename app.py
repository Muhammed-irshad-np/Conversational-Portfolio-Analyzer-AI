import os
from fastapi import FastAPI, Query,Request,HTTPException
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
import uvicorn
from langchain_core.output_parsers import StrOutputParser
import logging
import google.generativeai as genai

from models import PortfolioManager
import json
from langchain.memory import ConversationBufferMemory

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY,)



# data ="Some error occured in the portfolio api , please tell the user the data is not available currently"
# username ="friend"
# genai.GenerativeModel(tools=)

app = FastAPI()


portfolioObj = PortfolioManager()
memmory = ConversationBufferMemory()


finance_prompt = PromptTemplate.from_template(
    """
        
    Act as a mutual fund financial analyst based in india. I'll provide a portfolio description in JSON format.the data include asset allocation, top 10 underlying hodling list,top holding list,cyclical stocklist,defensive stocklist,sensitive stock list,equity sector stock list,fixed income sector stock lsit,stock sector style list,bondstyelist . Analyze the data and answer questions about the portfolio. 
      give accurate financial answers from this if user ask about suggestions give it , only give answers about financial topic. Greet the user by hello {name} 

    Portfolio Data: {data} 

    Username : {name}

    Question: {topic} 
    """
)

outputpaser = StrOutputParser()
tweet_chain = LLMChain(llm=llm, prompt=finance_prompt,output_parser=outputpaser,)

# if __name__ == "__main__":
#     topic = "how much is the total percentage of returns"
#     resp = tweet_chain.run(topic=topic, data=data)  # Pass 'data' here
#     print(resp)


@app.get("/analyze_portfolio/{topic}")
async def analyze_portfolio(topic: str):
 logging.info('The server request is hitting')
 print("Received topic:", topic)  # Debugging statement
 try:  
        data = portfolioObj.data
        username = portfolioObj.username

        response = tweet_chain.run(topic=topic, data=data,name=username,)
        print(response)
        return {"response": response}
 except Exception as e:  
        return {"error": f"An error occurred: {str(e)}"}
 


@app.post("/updatePortfolio")
async def update_portfolio(request:Request):
   try: 
    # username = request_data.username
    # combined_data = request_data.combinedData
    req =await  request.json()
    username = req.get("username")
    combineddata= req.get('combinedData')

    
    if username is None or username == "" or combineddata is None or combineddata == "":
       raise HTTPException(status_code=400, detail="Bad Request: Username or combinedData is missing or empty")
    portfolioObj.username=username
    portfolioObj.data = combineddata
    

    
     
    # combined_data_string = json.loads(combined_data)
    
    # Process the combined data here, such as updating it in a database
    

    return {"message": f"Portfolio updated for username {username} combineddata is {combineddata}"}
   except Exception as e:
      #  print(request_data.model_dump())
       print(await request.body())
       return {"error":f"an error occured:{str(e)}"}
 

if __name__ == "__main__":

    uvicorn.run(app, host="192.168.34.196", port=8000)
    # uvicorn.run(app, host="192.168.39.171", port=6305)


