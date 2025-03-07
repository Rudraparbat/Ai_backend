import os
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from threading import Thread
from .scrap import *
import ast
load_dotenv()

key = os.getenv('API_KEY')

class Model :
    def model() :
        try :
            model = ChatGroq(temperature=0, groq_api_key=key, model_name="llama-3.3-70b-versatile")
            if model :
                return model
        except :
            return None
        


class QueryProccesor :
    def __init__ (self) :
        self.model = Model.model()
    

    def getquery(self , query) :
        prompt = PromptTemplate.from_template(
            """
            You are a helpful assistant tasked with generating search queries for a multi-platform search system. Given a user input, create relevant queries for three platforms: Google, YouTube, and LinkedIn. The user’s input is: {query}. Follow these instructions:

            1. For Google: Generate 1 queries to find articles, or resources on the web. Make them broad yet specific, targeting different angles of the input (e.g., beginner-friendly, general learning, current resources).
            2. For YouTube: Generate 1 queries to find video content like tutorials or explanations. Focus on visual or step-by-step learning relevant to the input.
            3. For LinkedIn: Generate 1 query to find professionals or experts related to the input (e.g., people with skills or teaching experience).

            Output the queries in list format(list Format):
            [google_query , youtube_query , linkedin_query]

            (NO PREAMBLE)
            """
        )
        chain = prompt | self.model
        result = chain.invoke({
            "query" : query
        })

        return result.content



class Founder :
    def __init__(self , query) :
        self.query_obj = QueryProccesor()
        self.scrapper = Scrapper()
        self.query = query

    def get_seperated_query(self) :
        query_data = self.query_obj.getquery(self.query)
        cleaned_str = query_data.strip("[]")  # Removes [ and ]
        result = [item.strip() for item in cleaned_str.split(",")]
        print(result)
        self.google_query = str(result[0])
        self.yt_query = str(result[1])
        self.linkedin_data = str(result[2])

    def Processdata(self) :
        self.get_seperated_query()
        t1 =Thread(target=self.scrapper.GoogleScrap, args=(self.google_query,))
        t2 = Thread(target=self.scrapper.YtScrap, args=(self.yt_query,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        return self.scrapper.result
        

    


    



