import urllib.parse
import os
from langchain.llms.openai import OpenAI

from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import AgentExecutor

from langchain.sql_database import SQLDatabase

from dotenv import load_dotenv # pip install load-dotenv
load_dotenv()

import psycopg2 # pip install psycopg-binary
os.environ['OPENAI_API_KEY'] = "............."
# Your details
username = 'postgres'
password = 'Test@1234'
hostname = 'localhost'
dbname = 'TestDB1'

# Encode the password
encoded_password = urllib.parse.quote_plus(password)

# Connection URI
uri = f"postgresql://{username}:{encoded_password}@{hostname}:5432/{dbname}"
db = SQLDatabase.from_uri(uri)

# password = "Test@1234";
# db = SQLDatabase.from_uri('postgresql+psycopg2://postgres:Test@1234@localhost:5432/TestDB1')
print(db)

from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

     

toolkit = SQLDatabaseToolkit(db=db,llm=llm)

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)


agent_executor.run("what is the member id of Naveen")


