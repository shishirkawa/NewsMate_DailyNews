import pandas as pd
from newsmate.components.get_news import NewsScraper
from newsmate.components.generate_pdf import GeneratePDF

def run_pipeline(date):
    news_scraper = NewsScraper()
    news = news_scraper.extract(date)
    news_df = pd.DataFrame(news)

    pdf = GeneratePDF(date)
    pdf.coverpage()
    for index, row in news_df.iterrows():
        pdf.innerpage(row["title"], row["summary"])
    pdf.save_pdf()