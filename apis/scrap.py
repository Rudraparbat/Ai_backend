from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_community.tools import YouTubeSearchTool
import os
from dotenv import load_dotenv
load_dotenv()


class Scrapper :
    def __init__(self) :
        self.google_model = GoogleSearchAPIWrapper(
            google_api_key= os.getenv('GOOGLE_API_KEY'),
            google_cse_id=os.getenv('CSE_ID')
        )
        self.yt_model = YouTubeSearchTool(
            api_key=os.getenv('GOOGLE_API_KEY')
        )
        self.result = {}


    def GoogleScrap(self , query) :
        try:
            results = self.google_model.results(query, num_results=5)
            formatted_results = [
                {
                    "source": "Google",
                    "title": result["title"],
                    "url": result["link"],
                    "snippet": result.get("snippet", "")
                }
                for result in results
                ]
            self.result["Google"]=formatted_results
        except Exception as e:
            print(f"Error searching Google for '{query}': {e}")
            self.result["Google"]= []


    def YtScrap(self , query) :
        try:
            results = self.yt_model.run(f"{query},5")
           
            urls = eval(results) if results.startswith("[") else [results]

            formatted_results = [
                {
                    "source": "YouTube",
                    "title": f"Video {i + 1}",  
                    "url": url
                }
                for i, url in enumerate(urls[:5])
            ]
            self.result["Youtube"] = formatted_results
        except Exception as e:
            # Log the error (use logging in production)
            print(f"Error searching YouTube for '{query}': {e}")
            self.result["Youtube"] = []

    