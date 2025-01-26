from textblob import TextBlob
import pandas as pd
from airflow.models import BaseOperator

class SentimentAnalysisOperator(BaseOperator):
    def __init__(self, input_path: str, output_path: str, **kwargs):
        super().__init__(**kwargs)
        self.input_path = input_path
        self.output_path = output_path

    def execute(self, context):
        df = pd.read_parquet(self.input_path)
        df["sentiment"] = df["content"].apply(
            lambda x: TextBlob(str(x)).sentiment.polarity if x else None
        )
        df.to_parquet(self.output_path)