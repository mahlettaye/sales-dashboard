import sys
import os
#sys.path.insert(0, '/home/mahlet/sales-dashboard/data/')
#sys.path.append(os.path.abspath(os.path.join('..')))
import pandas as pd
import numpy as np
import random
import sys
print(sys.path)


class DataProcessor:

    """
        The class contains all data preprocessing functions  
        
    """

    def __init__(self):
        pass
      
        
    
    def read_csv (self, filename):

        try:
            self.data = pd.read_csv(filename)
            
        
        except FileNotFoundError as e:
            print (e)
        return self.data
       
    def identify_unique_value (df):
        """
        The Function accept datafrme and  aimes to report unique values in each columns  

        Parameters
        ----------
        df: pd.Dataframe :
        B

        Returns
        -------
        None

        """
        for col in df:
            unique=df[col].nunique()
            print(col,"......",unique)
    
    def Find_null_(df):
        """
        The Function accepts datafrme and  aimes to report null values in each columns  

        Parameters
        ----------
        df: pd.Dataframe :
        

        Returns
        -------
        df: pd.Dataframe :

        """

        df = df.isnull().sum()

        return df
    
    def  change_date(df1,df2):
        """
        The Function accepts set of datafrme and aimes to process date column.
        Convert object type to datatime.
        Extract date, month, year and return dataframe that have each data  

        Parameters
        ----------
        df: pd.Dataframe :
        

        Returns
        -------
        df: pd.Dataframe :

        """


        for df in (df1, df2):
            df['Date'] = df['Date'].astype('datetime64[ns]')
            df['Month'] = df.Date.dt.month
            df['Day'] = df.Date.dt.day
            df['Year'] = df.Date.dt.year.astype(str)+ '-01-01'
            df['Week']= (((df['Date'] - df['Year'].astype('datetime64[ns]')).dt.days)/7).astype('int16') +1
            df['Week']=  df.Week.where(df['Week']!=53, 52)
            df['Year'] = df.Date.dt.year

        return df1,df2
    
    def drop_cols(gdf):
        """
       This function will be used to drop redundant or unwanted columns generated via join operations. 

        Parameters
        ----------
        gdf: pd.Dataframe :
        

        Returns
        -------
        gdf: pd.Dataframe :

        """

        for c in gdf.columns:
            if c.endswith('_y'):
                if c in gdf.columns: gdf.drop(c, inplace=True, axis=1)
        return gdf


  
    def merge(df, right, left_on, right_on=None, suffix=None):
        """
       We will use the function below to perform left outer join operation. 
       The suffixes argument describes the naming convention for duplicate fields

        Parameters
        ----------
        df: pd.Dataframe :
        

        Returns
        -------
        df: pd.Dataframe :

        """
        df = df.merge(right, how='left', left_on=left_on, right_on=right_on or left_on, suffixes=('', suffix or '_y'))
        return df

    def handdle_missing_values(self, df):
        """
        Next we’ll fill in missing values to avoid complications with NA’s.
        Here, we are picking arbitrary signal values and filling the missing values with them.

        Parameters
        ----------
        df: pd.Dataframe :
        

        Returns
        -------
        df: pd.Dataframe :

        """
        
        df['CompetitionOpenSinceYear'] = df.CompetitionOpenSinceYear.fillna(1900).astype('int32')
        df['CompetitionOpenSinceMonth'] = df.CompetitionOpenSinceMonth.fillna(1).astype('int32')
       
        df['Promo2SinceWeek'] = df.Promo2SinceWeek.fillna(1).astype('int32')
      
        df["CompetitionDistance"].fillna(lambda x: random.choice(df[df["CompetitionDistance"] != np.nan]["CompetitionDistance"]), inplace =True)
        
        return df
    def data_to_send (slef):
        data = slef.read_csv("../training.csv")
        processed_data = slef.handdle_missing_values(data)
        
        print  (processed_data.head())
        return processed_data

    

if __name__=="__main__":
    processor=DataProcessor()
    processor.data_to_send()
    #print(train_data.head())
    #processor.identify_unique_value(train_data)
