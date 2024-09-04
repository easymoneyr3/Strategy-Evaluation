
import datetime as dt  		  	   		 	   			  		 			 	 	 		 		 	
import os  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
import numpy as np  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
import pandas as pd  		  	   		 	   			  		 			 	 	 		 		 	
from util import get_data, plot_data  	

def compute_portvals(  		  	   		 	   			  		 			 	 	 		 		 	
    order,  		  	   		 	   			  		 			 	 	 		 		 	
    start_val=1000000,  		  	   		 	   			  		 			 	 	 		 		 	
    commission=0,  		  	   		 	   			  		 			 	 	 		 		 	
    impact=0,  
    symbol = "JPM"		  	   		 	   			  		 			 	 	 		 		 	
):  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    Computes the portfolio values.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    :param orders_file: Path of the order file or the file object  		  	   		 	   			  		 			 	 	 		 		 	
    :type orders_file: str or file object  		  	   		 	   			  		 			 	 	 		 		 	
    :param start_val: The starting value of the portfolio  		  	   		 	   			  		 			 	 	 		 		 	
    :type start_val: int  		  	   		 	   			  		 			 	 	 		 		 	
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)  		  	   		 	   			  		 			 	 	 		 		 	
    :type commission: float  		  	   		 	   			  		 			 	 	 		 		 	
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction  		  	   		 	   			  		 			 	 	 		 		 	
    :type impact: float  		  	   		 	   			  		 			 	 	 		 		 	
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.  		  	   		 	   			  		 			 	 	 		 		 	
    :rtype: pandas.DataFrame  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    # this is the function the autograder will call to test your code  		  	   		 	   			  		 			 	 	 		 		 	
    # NOTE: orders_file may be a string, or it may be a file object. Your  		  	   		 	   			  		 			 	 	 		 		 	
    # code should work correctly with either input  		  	   		 	   			  		 			 	 	 		 		 	
    # TODO: Your code here  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # In the template, instead of computing the value of the portfolio, we just  		  	   		 	   			  		 			 	 	 		 		 	
    # read in the value of IBM over 6 months
    #
    #read data in 
    #order = pd.read_csv(orders,index_col= 'Date')	
    
      	   		 	   			  		 			 	 	 		 		 	
    start_date = order.index.min()  		  	   		 	   			  		 			 	 	 		 		 	
    end_date =  order.index.max()  	
    #https://www.listendata.com/2023/11/find-unique-values-in-column-pandas.html#:~:text=Incase%20you%20want%20the%20unique,use%20the%20tolist()%20function.&text=The%20drop_duplicates()%20method%20is,DataFrame%20and%20return%20unique%20values.&text=The%20drop_duplicates()%20method%20returns%20a%20Series%20or%20DataFrame.
    order["Symbol"] = symbol
    choice = [ order["Shares"] < 0, order["Shares"] > 0 ]
    choices = ["SELL", "BUY"]
    order["Order"] =np.select(choice,choices)
    order = order[order['Order'] != "0"]


    # get the stock data which filters out days spy is not traded	   		 	   			  		 			 	 	 		 		 	
    portvals = get_data([symbol], pd.date_range(start_date, end_date)) 
    portvals['CASH'] = 1
		 	   			  		 			 	 	 		 		 	
    portvals = portvals.iloc[:,1:]  # remove SPY  	 		
    trades = pd.DataFrame(0, index=portvals.index.values,columns=portvals.columns.values )
    for index, row in order.iterrows():
        symbol = row[0]
        orders = row[1]
        shares  = abs(row[2])
        price = portvals.loc[index,symbol]
        total = price * shares
        fee = abs(total)*impact
        if orders == 'BUY':
            total = total *-1
            trades.loc[index,symbol] += shares
            trades.loc[index,'CASH'] += total - commission - fee
        else:
            trades.loc[index,symbol] += shares*-1
            trades.loc[index,'CASH'] += total - commission - fee
    first = trades.index[0]
    
    
    holdings = pd.DataFrame(0,index=portvals.index, columns=portvals.columns)	
    holdings.loc[first,'CASH'] = start_val
    for i in range(0, holdings.shape[0]):
        if i == 0:
            holdings.iloc[[i]] = holdings.iloc[[i]].values + trades.iloc[[i]]
        else:
            holdings.iloc[[i]] = holdings.iloc[[i-1]].values + trades.iloc[[i]]
    
    values = portvals * holdings
    portvals2 = values.sum(axis=1)
 	   			  		 			 	 	 		 		 	
    return portvals2 
	  	   		 	   			  		 			 	 	 		 		 	
def author():
    return 'radjei3' 

def test_code():  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    Helper function to test code  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    # this is a helper function you can use to test your code  		  	   		 	   			  		 			 	 	 		 		 	
    # note that during autograding his function will not be called.  		  	   		 	   			  		 			 	 	 		 		 	
    # Define input parameters  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    		  	   		 	   			  		 			 	 	 		 		 	
    sv = 1000000  		  	   		 	   			  		 			 	 	 		 		 	
'''	   		 	   			  		 			 	 	 		 		 	
    # Process orders  		  	   		 	   			  		 			 	 	 		 		 	
    portvals = compute_portvals(orders_file=of, start_val=sv)  		  	   		 	   			  		 			 	 	 		 		 	
    if isinstance(portvals, pd.DataFrame):  		  	   		 	   			  		 			 	 	 		 		 	
        portvals = portvals[portvals.columns[0]]  # just get the first column  		  	   		 	   			  		 			 	 	 		 		 	
    else:  		  	   		 	   			  		 			 	 	 		 		 	
        "warning, code did not return a DataFrame"  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # Get portfolio stats  		  	   		 	   			  		 			 	 	 		 		 	
    # Here we just fake the data. you should use your code from previous assignments.  	
    # 
    	  	   		 	   			  		 			 	 	 		 		 	
    start_date = dt.datetime(2008, 1, 1)  		  	   		 	   			  		 			 	 	 		 		 	
    end_date = dt.datetime(2008, 6, 1)  		  	   		 	   			  		 			 	 	 		 		 	
    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = [  		  	   		 	   			  		 			 	 	 		 		 	
        0.2,  		  	   		 	   			  		 			 	 	 		 		 	
        0.01,  		  	   		 	   			  		 			 	 	 		 		 	
        0.02,  		  	   		 	   			  		 			 	 	 		 		 	
        1.5,  		  	   		 	   			  		 			 	 	 		 		 	
    ]  		  	   		 	   			  		 			 	 	 		 		 	
    cum_ret_SPY, avg_daily_ret_SPY, std_daily_ret_SPY, sharpe_ratio_SPY = [  		  	   		 	   			  		 			 	 	 		 		 	
        0.2,  		  	   		 	   			  		 			 	 	 		 		 	
        0.01,  		  	   		 	   			  		 			 	 	 		 		 	
        0.02,  		  	   		 	   			  		 			 	 	 		 		 	
        1.5,  		  	   		 	   			  		 			 	 	 		 		 	
    ]  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # Compare portfolio against $SPX  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Date Range: {start_date} to {end_date}")  		  	   		 	   			  		 			 	 	 		 		 	
    print()  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Sharpe Ratio of Fund: {sharpe_ratio}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Sharpe Ratio of SPY : {sharpe_ratio_SPY}")  		  	   		 	   			  		 			 	 	 		 		 	
    print()  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Cumulative Return of Fund: {cum_ret}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Cumulative Return of SPY : {cum_ret_SPY}")  		  	   		 	   			  		 			 	 	 		 		 	
    print()  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Standard Deviation of Fund: {std_daily_ret}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Standard Deviation of SPY : {std_daily_ret_SPY}")  		  	   		 	   			  		 			 	 	 		 		 	
    print()  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Average Daily Return of Fund: {avg_daily_ret}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Average Daily Return of SPY : {avg_daily_ret_SPY}")  		  	   		 	   			  		 			 	 	 		 		 	
    print()  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Final Portfolio Value: {portvals[-1]}")  		  	   		 	   			  		 			 	 	 		 		 	
  	'''	  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
if __name__ == "__main__":  		  	   		 	   			  		 			 	 	 		 		 	
    test_code()  		  	   		 	   			  		 			 	 	 		 		 	
