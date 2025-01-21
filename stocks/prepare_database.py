"""This file generates an in-memory database."""
from typing import List
from datetime import date, timedelta

import pandas as pd
from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, Table, Date, Float
from sqlalchemy import create_engine
from sqlalchemy import insert
import yfinance as yf


def generate_and_populate_database(ticker_list: List, last_n_days: int):
    data = yf.download(
        tickers=ticker_list,
        start=date.today()-timedelta(days=last_n_days),
        end=date.today()
    )["Close"].reset_index()

    data = pd.melt(
        data,
        id_vars=['Date'],
        value_vars=ticker_list,
        var_name="stock_ticker",
        value_name="price",
        ignore_index=False
    )

    metadata_obj = MetaData()
    stocks = Table(
        "stocks",
        metadata_obj,
        Column("Date", Date, nullable=False),
        Column("stock_ticker", String(4), nullable=False),
        Column("price", Float, nullable=False),
    )
    engine = create_engine("sqlite:///:memory:")
    metadata_obj.create_all(engine)

    def insert_obs(obs):
        stmt = insert(stocks).values(
            stock_ticker=obs[1],
            price=obs[2],
            Date=obs[0]
        )

        with engine.begin() as conn:
            conn.execute(stmt)

    for obs in data.to_numpy():
        insert_obs(obs)


if __name__ == '__main__':
    generate_and_populate_database(['MSFT', 'CRM'], 10)