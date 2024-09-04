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
from util  import get_data, plot_data   		  	   		 	   			  		 			 	 	 		 		 	
import datetime  
import numpy as np 		  	   		 	   			  		 			 	 	 		 		 	
import random  		  	   		 	   			  		 			 	 	 		 		 	 		  	   		 	   			  		 			 	 	 		 		 	
import pandas as pd  		  	   		 	   			  		 			 	 	 		 		 	
from indicators  	import GDC, SMA, BB, MACD , momentum
from marketsimcode import compute_portvals	 
import RTLearner as rl
import BagLearner as bl 
import matplotlib.pyplot as plt	   
	  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
class StrategyLearner(object):  		  	   		 	   			  		 			 	 	 		 		 	
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
        self.learner = bl.BagLearner(learner = rl.RTLearner, kwargs = {"leaf_size":5}, bags = 20) 		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # this method should create a QLearner, and train it for trading  		  	   		 	   			  		 			 	 	 		 		 	
    def add_evidence( self, symbol='IBM', sd=datetime.datetime(2008, 1, 1, 0, 0), ed=datetime.datetime(2009, 1, 1, 0, 0), sv=100000 ):  		  	   		 	   			  		 			 	 	 		 		 	
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
       		  	   		 	   			  		 			 	 	 		 		 	
        prices = prices_all[syms] 
         # only portfolio symbols  		  	   		 	   			  		 			 	 	 		 		 	
        #prices_SPY = prices_all["SPY"]  # only SPY, for comparison later 
        
        gdc = GDC(prices,symbol)	
        macd = (MACD(prices,symbol= symbol)) 
        

       
       #Bollinger Bands < 0 buy >1 sell 
        bb =(BB(prices,20,symbol))  
        x = np.column_stack(( macd , gdc, bb  ))
        x_train = x[:-5]
        end= prices.shape[0]- 5
       
        y = np.zeros(end)
        for i in range (end):
            prof =  (prices[symbol].loc[prices.index[i + 5]])/ prices[symbol].loc[prices.index[i]] -1
            if prof < -0.029 + self.impact:
                y[i] = -1
            elif prof >  0.029 + self.impact:
                 y[i] = 1
            else:
                y[i] = 0
        y = np.round(y)
       
        
        self.learner.add_evidence(x_train,y)



       # only SPY, for comparison later  		  	   		 	   			  		 			 	 	 		 		 	
        	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # this method should use the existing policy and test it against new data  		  	   		 	   			  		 			 	 	 		 		 	
    def testPolicy( self, symbol='IBM', sd=datetime.datetime(2008, 1, 1, 0, 0), ed=datetime.datetime(2009, 1, 1, 0, 0), sv=100000 ):  		  	   		 	   			  		 			 	 	 		 		 	
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
  		  	   		 	   			  		 			 	 	 		 		 	
      	  	   		 	   			  		 			 	 	 		 		 	
        dates = pd.date_range(sd, ed)  		  	   		 	   			  		 			 	 	 		 		 	
        prices_all = get_data([symbol], dates)  # automatically adds SPY  		  	   		 	   			  		 			 	 	 		 		 	
        trades = prices_all[[symbol,]]  # only portfolio symbols  
        gdc = GDC(trades,symbol)	
        macd = (MACD(trades,symbol= symbol))  
        bb =(BB(trades,10,symbol))  
        x_test = np.column_stack(( macd , gdc, bb  ))
        y_test = self.learner.query(x_test)
        rounded_y = np.where(y_test > 0, 1, np.where(y_test < 0, -1, 0))
       
        df = pd.DataFrame({'Signal': rounded_y}, index= trades.index, columns= ["Signal"])
        
        position = 0
        trades = pd.DataFrame(0, index= trades.index,columns=['Shares']) 
        for index, row in df.iterrows():
            signal = row['Signal']
            if signal > 0:
               
                    action= 1000 - position 
            elif signal < 0:
                
                   action = -1000 - position 
            else:
                action= 0 
    
            trades.at[index, 'Shares'] = action
            position += action
            	   			  		 			 	 	 		 		 	
        return  trades	 	
    
    
def author():
    return 'radjei3'

       			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
if __name__ == "__main__":  		  	   		 	   			  		 			 	 	 		 		 	
    print("One does not simply think up a strategy")  		  	   		 	   			  		 			 	 	 		 		 	
    