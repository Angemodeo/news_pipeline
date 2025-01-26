from bs4 import BeautifulSoup
import pandas as pd
import requests
from airflow.models import BaseOperator

class ScrapeContentOperator(BaseOperator):
    def __init__(self, input_path: str, output_path: str, **kwargs):
        super().__init__(**kwargs)
        self.input_path = input_path
        self.output_path = output_path

    def execute(self, context):
        df = pd.read_parquet(self.input_path)
        
        def scrape(url):
            try:
                page = requests.get(url, timeout=10)
                soup = BeautifulSoup(page.content, "html.parser")
                return " ".join(p.text for p in soup.find_all("p"))
            except:
                return None

        df["content"] = df["url"].apply(scrape)
        df.to_parquet(self.output_path)