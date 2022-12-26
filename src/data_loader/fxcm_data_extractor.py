import pandas as pd
import fxcmpy


class FXCMDataExtractor:
    def __init__(self):
        pass

        api = fxcmpy.fxcmpy(config_file='fxcm.cfg')
        ############################
        # Atributes
        ############################
        self.history_df=self.get_history_data(api=api,
                                              instrument='EUR/USD',
                                              numb_of_quates=500)
        ############################
        # End Atributes
        ############################
        api.close()

        @staticmethod
        def info_account(api):

            df_account_info= api.get_accounts()
            return df_account_info

        @staticmethod
        def get_scope_instrument(api):
            instruments=api.get_instruments()
            for instrument in instruments:
                print(instrument)

    def  get_history_data(self,api,instrument,numb_of_quates=1000):
            history_df=api.get_candles(instrument,number=numb_of_quates)
            return history_df







if __name__=='__main__':
    data_ext=DataExtractor()
    print('THE END')







