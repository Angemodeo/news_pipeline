from datetime import datetime
from airflow import DAG
from airflow.models import Variable
from plugins.operators.fetch_news import FetchNewsOperator
from plugins.operators.scrape_content import ScrapeContentOperator
from plugins.operators.sentiment_analysis import SentimentAnalysisOperator

default_args = {
    "owner": "data_team",
    "retries": 3,
}

with DAG(
    dag_id="news_analysis",
    default_args=default_args,
    schedule_interval="*/5 * * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    fetch = FetchNewsOperator(
        task_id="fetch_news",
        api_url=Variable.get("NEWS_API_URL"),
        output_path="data/raw/news.parquet"
    )

    scrape = ScrapeContentOperator(
        task_id="scrape_content",
        input_path="data/raw/news.parquet",
        output_path="data/processed/scraped.parquet"
    )

    analyze = SentimentAnalysisOperator(
        task_id="sentiment_analysis",
        input_path="data/processed/scraped.parquet",
        output_path="data/final/results.parquet"
    )

    fetch >> scrape >> analyze