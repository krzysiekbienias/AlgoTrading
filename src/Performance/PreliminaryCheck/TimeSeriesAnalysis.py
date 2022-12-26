import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from data_loader.yahoo_data_extractor import YahooDataExtractor

class FinancialTimeSeriesAnalysis:
    def __init__(self,tickers,
                 start_date,
                 end_date):
        """
        Description
        ----------
        The class extract prices for chosen set of tickers
        Parameters
        ----------

        tickers
        start_date begining of time window to extract
        end_date
        """

        yahoo_extractor=YahooDataExtractor(tickers=tickers)

        close_prices_df=yahoo_extractor.extract_data(tickers=yahoo_extractor._tickers,
                                                    start_period=start_date,
                                                    end_period=end_date,
                                                    column_name='Close')
        yahoo_extractor.df_info(close_prices_df)

        # ----------------
        # Region Atributes
        # ----------------
        self._tickers=tickers
        self._start_date = start_date
        self._end_date=end_date
        self.close_prices_df = close_prices_df
        self.rate_of_returns=self.calulate_rates_of_returns(df=close_prices_df,
                                                            type='daily')

        #------------------
        # End Region Atributes
        # ------------------

    def __repr__(self):
        return "FinancialTimeSeriesAnalysis(ticker={0}, start_date={1}, end_date={2})".format(self._tickers,self._start_date,self._end_date)


    def normalisePrices(self, df):
        """

        Parameters
        ----------
        df data frame with close price

        Returns
        -------

        """
        norm = df.div(df.iloc[0]).mul(100)
        return norm

    def calulate_rates_of_returns(self,df,type='daily'):

        """


        Parameters
        ----------
        df - data frame of close prices for given set of tickers
        type string

        Returns
        -------
        data frame of returns

        """


        rate_of_returns=None
        if type =='daily':
            rate_of_returns=df.pct_change().dropna()
        elif type=='monthly':
            rate_of_returns=df.resample("BM").last().pct_change(periods=1).mul(100)
        elif type=='quarterly':
            rate_of_returns = df.resample("Q").last().pct_change(periods=1).mul(100)
        return rate_of_returns

    def get_close_price(self,arr_dfs):
        for df in  arr_dfs:
            pass


    def statistic_of_rates(self,df_rates,period='daily'):
        if period=='daily':
            mean_returns=df_rates.mean()
            var_returns=df_rates.var()
            st_dev_returns=np.sqrt(var_returns)
            return (mean_returns,var_returns,st_dev_returns)
        elif period=='annually':
            mean_returns=df_rates.mean()*252
            var_returns=df_rates.var()*252
            st_dev_returns=np.sqrt(var_returns)
            return (mean_returns, var_returns, st_dev_returns)


if __name__=="__main__":
     time_series=FinancialTimeSeriesAnalysis(tickers=['AAPL', "BA", "KO", "IBM", "DIS", "MSFT"],
                                               start_date='2010-01-01',
                                               end_date='2022-10-30')
     print(time_series)
     print("The End")
