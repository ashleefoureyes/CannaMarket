import pandas as pd
import numpy as np
from pandas_datareader import data, wb

start_date = '2014-08-01'
end_date = '2017-10-13'

#convert csv files to pandas dataframes
acb_df = pd.DataFrame.from_csv('stock_data/ACBFF.csv', header=0, sep=',',index_col=0)
aph_df = pd.DataFrame.from_csv('stock_data/APH.TO.csv', header=0, sep=',',index_col=0)
weed_df = pd.DataFrame.from_csv('stock_data/WEED.TO.csv', header=0, sep=',',index_col=0)

#parse wanted dates
acb_df = acb_df.ix[start_date:end_date]
aph_df = aph_df.ix[start_date:end_date]
weed_df = weed_df.ix[start_date:end_date]

# create dataframe from the 3 close prices

close_prices = pd.DataFrame({
    "ACBFF": acb_df['Close'],
    "APH.TO": aph_df['Close'],
    "WEED.TO": weed_df['Close']
})



close_prices.head()
close_prices.reset_index(inplace=True)

acb_list = close_prices['ACBFF'].tolist()
aph_list = close_prices['APH.TO'].tolist()
weed_list = close_prices['WEED.TO'].tolist()

close_matrix = np.matrix([acb_list, aph_list, weed_list])
close_dataframe = pd.DataFrame(data=close_matrix)

close_dataframe.head()
close_dataframe.reset_index(inplace=True)

print(close_dataframe)
#print(close_prices)
