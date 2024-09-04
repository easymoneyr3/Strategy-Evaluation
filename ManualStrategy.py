""""""  		  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	   			  		 			 	 	 		 		 	
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	   			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		 	   			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Template code for CS 4646/7646  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	   			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			 	 	 		 		 	
and other users of this template code are advised not to share it with others  		  	   		 	   			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			 	 	 		 		 	
or edited.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			 	 	 		 		 	
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	   			  		 			 	 	 		 		 	
GT honor code violation.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
-----do not edit anything above this line---  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Student Name: Renny Adjei (replace with your name)  		  	   		 	   			  		 			 	 	 		 		 	
GT User ID: radjei3 (replace with your User ID)  		  	   		 	   			  		 			 	 	 		 		 	
GT ID: 903948765 (replace with your GT ID)  		  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	  	   		 	   			  		 			 	 	 		 		 	
import random  		  	   		 	   			  		 			 	 	 		 		 		  	   		 	   			  		 			 	 	 		 		 	 		  	   		 	   			  		 			 	 	 		 		 	 		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
import datetime  		  	   		 	   			  		 			 	 	 		 		 	
import os  		  	   		 	   			  		 			 	 	 		 		 			  	   		 	   			  		 			 	 	 		 		 	
import numpy as np  		  	   		 	   			  		 			 	 	 		 		 		   		 	   			  		 			 	 	 		 		 	
import pandas as pd
from indicators  	import GDC, SMA, BB, MACD
from marketsimcode import compute_portvals	  
import matplotlib.pyplot as plt	   
from util  import get_data, plot_data   	   		 	   			  		 			 	 	 		 		 	
class ManualStrategy(object):  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    A strategy learner that can learn a trading policy using the same indicators used in ManualStrategy.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		 	   			  		 			 	 	 		 		 	
        If verbose = False your code should not generate ANY output.  		  	   		 	   			  		 			 	 	 		 		 	
    :type verbose: bool  		  	   		 	   			  		 			 	 	 		 		 	
    :param impact: The market impact of each transaction, defaults to 0.0  		  	   		 	   			  		 			 	 	 		 		 	
    :type impact: float  		  	   		 	   			  		 			 	 	 		 		 	
    :param commission: The commission amount charged, defaults to 0.0  		  	   		 	   			  		 			 	 	 		 		 	
    :type commission: float  		  	   		 	   			  		 			 	 	 		 		 	
    """  
    def author(): 
        return "radjei3"	  	   		 	   			  		 			 	 	 		 		 	
    # constructor  		  	   		 	   			  		 			 	 	 		 		 	
    def __init__(self, verbose=False, impact=0.0, commission=0.0):  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        Constructor method  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        self.verbose = verbose  		  	   		 	   			  		 			 	 	 		 		 	
        self.impact = impact  		  	   		 	   			  		 			 	 	 		 		 	
        self.commission = commission  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # this method should create a QLearner, and train it for trading  		  	   		 	   			  		 			 	 	 		 		 	
    def add_evidence(self, symbol='IBM', sd=datetime.datetime(2009, 1, 1, 0, 0), ed=datetime.datetime(2010, 1, 1, 0, 0), sv=100000):  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        Trains your strategy learner over a given time frame.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
        :param symbol: The stock symbol to train on  		  	   		 	   			  		 			 	 	 		 		 	
        :type symbol: str  		  	   		 	   			  		 			 	 	 		 		 	
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	   			  		 			 	 	 		 		 	
        :type sd: datetime  		  	   		 	   			  		 			 	 	 		 		 	
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	   			  		 			 	 	 		 		 	
        :type ed: datetime  		  	   		 	   			  		 			 	 	 		 		 	
        :param sv: The starting value of the portfolio  		  	   		 	   			  		 			 	 	 		 		 	
        :type sv: int  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
        # add your code to do learning here  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
        # example usage of the old backward compatible util function  		  	   		 	   			  		 			 	 	 		 		 	
        syms = [symbol]  		  	   		 	   			  		 			 	 	 		 		 	
        dates = pd.date_range(sd, ed)  		  	   		 	   			  		 			 	 	 		 		 	
        prices_all = get_data(syms, dates)  # automatically adds SPY  		  	   		 	   			  		 			 	 	 		 		 	
        prices = prices_all[syms]  # only portfolio symbols  		  	   		 	   			  		 			 	 	 		 		 	
        prices_SPY = prices_all["SPY"]  # only SPY, for comparison later  	
        
        '''  	   		 	   			  		 			 	 	 		 		 	
        if self.verbose:  		  	   		 	   			  		 			 	 	 		 		 	
            print(prices)  		

        '''  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
        # example use with new colname  		  	   		 	   			  		 			 	 	 		 		 	
        volume_all = get_data(  		  	   		 	   			  		 			 	 	 		 		 	
            syms, dates, colname="Volume"  		  	   		 	   			  		 			 	 	 		 		 	
        )  # automatically adds SPY  		  	   		 	   			  		 			 	 	 		 		 	
        volume = volume_all[syms]  # only portfolio symbols  		  	   		 	   			  		 			 	 	 		 		 	
        volume_SPY = volume_all["SPY"]  # only SPY, for comparison later  		  	   		 	   			  		 			 	 	 		 		 	
       # if self.verbose:  		  	   		 	   			  		 			 	 	 		 		 	
           # print(volume)  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # this method should use the existing policy and test it against new data  		  	   		 	   			  		 			 	 	 		 		 	
    def testPolicy( self, symbol='IBM', sd=datetime.datetime(2009, 1, 1, 0, 0), ed=datetime.datetime(2010, 1, 1, 0, 0), sv=100000):  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        Tests your learner using data outside of the training data  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
        :param symbol: The stock symbol that you trained on on  		  	   		 	   			  		 			 	 	 		 		 	
        :type symbol: str  		  	   		 	   			  		 			 	 	 		 		 	
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	   			  		 			 	 	 		 		 	
        :type sd: datetime  		  	   		 	   			  		 			 	 	 		 		 	
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	   			  		 			 	 	 		 		 	
        :type ed: datetime  		  	   		 	   			  		 			 	 	 		 		 	
        :param sv: The starting value of the portfolio  		  	   		 	   			  		 			 	 	 		 		 	
        :type sv: int  		  	   		 	   			  		 			 	 	 		 		 	
        :return: A DataFrame with values representing trades for each day. Legal values are +1000.0 indicating  		  	   		 	   			  		 			 	 	 		 		 	
            a BUY of 1000 shares, -1000.0 indicating a SELL of 1000 shares, and 0.0 indicating NOTHING.  		  	   		 	   			  		 			 	 	 		 		 	
            Values of +2000 and -2000 for trades are also legal when switching from long to short or short to  		  	   		 	   			  		 			 	 	 		 		 	
            long so long as net holdings are constrained to -1000, 0, and 1000.  		  	   		 	   			  		 			 	 	 		 		 	
        :rtype: pandas.DataFrame  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
        # here we build a fake set of trades  		  	   		 	   			  		 			 	 	 		 		 	
        # your code should return the same sort of data  		  	   		 	   			  		 			 	 	 		 		 	
        dates = pd.date_range(sd, ed)  		  	   		 	   			  		 			 	 	 		 		 	
        prices_all = get_data([symbol], dates)  # automatically adds SPY  		  	   		 	   			  		 			 	 	 		 		 	
        trades = prices_all[[symbol,]]  # only portfolio symbols  		  	   		 	   			  		 			 	 	 		 		 	
        trades_SPY = prices_all["SPY"]  # only SPY, for comparison later  	
        gdc = GDC(trades,symbol)	
        macd = (MACD(trades,symbol= symbol)) 
        bb =(BB(trades,20,symbol))  
         
        signal = macd  + bb + gdc 

        df = pd.DataFrame({'Signal': signal}, index= trades.index, columns= ["Signal","Symbol", "Order", "Shares"])
        #https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
        df['Order'] = df['Signal'].apply(lambda x: 'BUY' if x >= 1 else ('SELL' if x <= -1 else 'Hold'))
        df["Symbol"] = symbol
        position = 0
        for index, row in df.iterrows():
            signal = row['Signal']
            #long
            if signal == 1:
                    action= 1000 - position    
            #short   
            elif signal == -1:
                
                   action = -1000 - position 
            #hold
            else:
                action= 0  
            df.at[index, 'Shares'] = action
            position += action
            ans= df.iloc[:, 1:]
            
        return ans
       
    
   	

  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
if __name__ == "__main__":  

    print("One does not simply think up a strategy")
    '''
    # -------------------------
    ###########################
    # IN SAMPLE
    ###########################
    # -------------------------
    man = ManualStrategy()		  	   		 	   			  		 			 	 	 		 		 	
    mantrades = man.testPolicy(symbol="JPM",  sd=datetime.datetime(2008, 1, 1),  ed=datetime.datetime(2009, 12, 31), sv=100000)

    crm = compute_portvals(mantrades, 100000, 9.95, 0.005)
    crmf = (crm.iloc[-1] / crm.iloc[0]) - 1
    daily_returns_manual = crm/crm.shift(1)-1
    
    symbol="JPM",  
    sd=datetime.datetime(2008, 1, 1)
    ed=datetime.datetime(2009, 12, 31)
    sv=100000

    dates = pd.date_range(sd,ed)
    prices = get_data(symbol, dates)
    prices = prices.iloc[: ,1:]
    benchmark = pd.DataFrame(0, index=prices.index, columns=["Symbol", 'Order', 'Shares'])
    first = benchmark.index[0]
    benchmark['Symbol'] = 'JPM'
    benchmark.loc[first, 'Order'] = "BUY"
    benchmark.loc[first, 'Shares'] = 1000
  
    
    crb = compute_portvals(benchmark, 100000, 9.95, 0.005)
    cr = (crb.iloc[-1] / crb.iloc[0]) - 1
    daily_returns_benchmark = crb/crb.shift(1)-1
    
    dict = {"Metrics": ["Cumalitive Return", "Mean", "Standard Deviation"], "Manual": [crmf,daily_returns_manual.mean(),daily_returns_manual.std()],"Benchmark": [cr,daily_returns_benchmark.mean(),daily_returns_benchmark.std()]}
    table = pd.DataFrame(dict)
    table.to_csv('InSampleManualvsBenchMark.csv', index=False)
    plot_df = pd.DataFrame(0,index=benchmark.index, columns=["Benchmark", "Manual"])
    plot_df["Benchmark"] = crb
    plot_df["Manual"] =crm
    plot_df["Benchmark"] = plot_df["Benchmark"]/plot_df["Benchmark"].iloc[0]
    plot_df["Manual"] =  plot_df["Manual"] /  plot_df["Manual"].iloc[0]
    plt.figure(1)
    plt.plot(plot_df["Benchmark"], color = 'Purple', label = 'Benchmark')
    plt.plot( plot_df["Manual"], color = 'Red', label = 'Manual Strategy')
    plt.title("Benchmark vs Manual In Sample")
    plt.xlabel("Dates")
    plt.ylabel("Normalized Returns ")

    trades_l = mantrades[mantrades['Shares'] > 0]
    trades_s = mantrades[mantrades['Shares'] < 0]

    trades_l = trades_l.index
    trades_s = trades_s.index
    for date in trades_s:
        plt.axvline(x=date, color='black', linestyle='--')

    for date in trades_l:
        plt.axvline(x=date, color='blue', linestyle='--')
    plt.axvline(x=date, color='blue', linestyle='--', label = 'Long Stock')
    plt.axvline(x=date, color='black', linestyle='--', label = 'Short Stock')
    plt.legend(loc = 'upper left')
    plt.xticks(rotation = 45)
    plt.savefig("InSample.png")
    plt.close()


    # -------------------------
    ###########################
    # OUT OF SAMPLE
    ###########################
    #--------------------------
    man = ManualStrategy()		  	   		 	   			  		 			 	 	 		 		 	
    mantrades = man.testPolicy(symbol="JPM",  sd=datetime.datetime(2010, 1, 1),  ed=datetime.datetime(2011, 12, 31), sv=100000)
    crm = compute_portvals(mantrades, 100000, 9.95, 0.005)
    crmf = (crm.iloc[-1] / crm.iloc[0]) - 1
    daily_returns_manual2 = crm/crm.shift(1)-1
    symbol="JPM",  
    sd=datetime.datetime(2010, 1, 1)
    ed=datetime.datetime(2011, 12, 31)
    sv=100000

    dates = pd.date_range(sd,ed)
    prices = get_data(symbol, dates)
    prices = prices.iloc[: ,1:]
    benchmark = pd.DataFrame(0, index=prices.index, columns=["Symbol", 'Order', 'Shares'])
    first = benchmark.index[0]
    benchmark['Symbol'] = 'JPM'
    benchmark.loc[first, 'Order'] = "BUY"
    benchmark.loc[first, 'Shares'] = 1000
  
    
    crb = compute_portvals(benchmark, 100000, 9.95, 0.005)
    cr = (crb.iloc[-1] / crb.iloc[0]) - 1
    daily_returns_benchmark2 = crb/crb.shift(1)-1
    dict2 = {"Metrics": ["Cumalitive Return", "Mean", "Standard Deviation"], "Manual": [crmf,daily_returns_manual2.mean(),daily_returns_manual2.std()],"Benchmark": [cr,daily_returns_benchmark2.mean(),daily_returns_benchmark2.std()]}
    table2 = pd.DataFrame(dict2)
    table2.to_csv('OutofSampleManualvsBenchMark.csv', index=False)
    cr = (crb.iloc[-1] / crb.iloc[0]) - 1
    plot_df = pd.DataFrame(0,index=benchmark.index, columns=["Benchmark", "Manual"])
    plot_df["Benchmark"] = crb
    plot_df["Manual"] =crm
    plot_df["Benchmark"] = plot_df["Benchmark"]/plot_df["Benchmark"].iloc[0]
    plot_df["Manual"] =  plot_df["Manual"] /  plot_df["Manual"].iloc[0]
    plt.figure(2)
    plt.plot(plot_df["Benchmark"], color = 'Purple', label = 'Benchmark')
    plt.plot( plot_df["Manual"], color = 'Red', label = 'Manual Strategy')
    plt.title("Benchmark vs Manual Out of Sample ")
    plt.xlabel("Dates")
    plt.ylabel("Normalized Returns ")

    trades_l = mantrades[mantrades['Shares'] > 0]
    trades_s = mantrades[mantrades['Shares'] < 0]

    trades_l = trades_l.index
    trades_s = trades_s.index
    for date in trades_s:
        plt.axvline(x=date, color='black', linestyle='--')

    for date in trades_l:
        plt.axvline(x=date, color='blue', linestyle='--')
    plt.axvline(x=date, color='blue', linestyle='--', label = 'Long Stock')
    plt.axvline(x=date, color='black', linestyle='--', label = 'Short Stock')
    plt.legend(loc = 'upper left')
    plt.xticks(rotation = 45)
    plt.savefig("OutofSample.png")
    plt.close()


    '''
    
