import requests
import pandas as pd
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class FetchNewsOperator(BaseOperator):
    @apply_defaults
    def __init__(self, api_url: str, output_path: str, **kwargs):
        super().__init__(**kwargs)
        self.api_url = api_url
        self.output_path = output_path

    def execute(self, context):
        response = requests.get(self.api_url)
        articles = response.json().get("articles", [])
        df = pd.DataFrame(articles)[["title", "url", "publishedAt"]]
        df.to_parquet(self.output_path)