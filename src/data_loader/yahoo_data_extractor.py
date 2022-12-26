import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


class YahooDataExtractor:
    def __init__(self,tickers):
        """

        Args:
            tickers:
        """
        self._tickers=tickers

        data_extracted=self.extract_data(tickers=self._tickers,
                                         start_period='2010-01-01',
                                         end_period='2022-10-30')



    def extract_data(self,tickers,
                     start_period,
                     end_period,
                     column_name="Close"):
        df_equities=yf.download(tickers=tickers,
                    start=start_period,
                    end=end_period)
        df_equities.swaplevel(axis=1).sort_index(axis=1)
        one_column_ts=df_equities.loc[:,column_name].copy()
        return one_column_ts

    def df_info(self,_df):
        _df.describe()
        _df.info()

    def normalise_prices(self,df):
        norm=df.div(df.iloc[0]).mul(100)
        return norm

    def basic_statistics(self,df):
        print(df.info())








if __name__=='__main__':
    yahoo_data_extractor=YahooDataExtractor(tickers=['AAPL',
                                                     "BA",
                                                     "KO",
                                                     "IBM",
                                                     "DIS",
                                                     "MSFT"])
