from util  import get_data, plot_data   		  	   		 	   			  		 			 	 	 		 		 	
import datetime as dt 
import numpy as np 		  	   		 	   			  		 			 	 	 		 		 	
import random  		  	   		 	   			  		 			 	 	 		 		 	 		  	   		 	   			  		 			 	 	 		 		 	
import pandas as pd  		  	   		 	   			  		 			 	 	 		 		 	
from indicators  	import GDC, SMA, BB, MACD , momentum
from marketsimcode import compute_portvals	 
import RTLearner as rl
import BagLearner as bl 
import matplotlib.pyplot as plt	   
import StrategyLearner as sl
import ManualStrategy as ms

def author(): 
  return "radjei3"

def exp2():
    symbol = 'JPM'
    sd=dt.datetime(2008, 1, 1)
    ed=dt.datetime(2009, 12, 31)
    sv=100000
    dates = pd.date_range(sd,ed)
    #Strategy Learner
    stratLearn = sl.StrategyLearner()		  	   		 	   			  		 			 	 	 		 		 	
    mantrades = stratLearn.add_evidence(symbol="JPM",  sd=dt.datetime(2008, 1, 1),  ed=dt.datetime(2009, 12, 31), sv=100000)
    strat_trades = stratLearn.testPolicy(symbol="JPM",  sd=dt.datetime(2008, 1, 1),  ed=dt.datetime(2009, 12, 31), sv=100000)
    strat_trades['Order'] = strat_trades['Shares'].apply(lambda x: 'BUY' if x >= 1000 else ('SELL' if x <= -1000 else 'Hold'))
    strat_trades["Symbol"] = symbol
    cols = strat_trades.columns.tolist()
    cols = [cols[2]] + [cols[1]] + [cols[0]]
    df_strat= strat_trades[cols]
    cr_strat = compute_portvals(df_strat, 100000, 0, 0)
    cr_strats = (cr_strat.values/  cr_strat.iloc[0]) -1

    crsl= (cr_strat.iloc[-1] / cr_strat.iloc[0])
    daily_returns_sl = cr_strat/cr_strat.shift(1)-1




    symbol = 'JPM'
    sd=dt.datetime(2008, 1, 1)
    ed=dt.datetime(2009, 12, 31)
    sv=100000
    dates = pd.date_range(sd,ed)
    #Strategy Learner
    stratLearn2 = sl.StrategyLearner(impact =  0.05)		  	   		 	   			  		 			 	 	 		 		 	
    mantrades2 = stratLearn2.add_evidence(symbol="JPM",  sd=dt.datetime(2008, 1, 1),  ed=dt.datetime(2009, 12, 31), sv=100000)
    strat_trades2 = stratLearn2.testPolicy(symbol="JPM",  sd=dt.datetime(2008, 1, 1),  ed=dt.datetime(2009, 12, 31), sv=100000)
    strat_trades2['Order'] = strat_trades2['Shares'].apply(lambda x: 'BUY' if x >= 1000 else ('SELL' if x <= -1000 else 'Hold'))
    strat_trades2["Symbol"] = symbol
    cols2 = strat_trades2.columns.tolist()
    cols2 = [cols2[2]] + [cols2[1]] + [cols2[0]]
    df_strat2= strat_trades2[cols]
    cr_strat2  = compute_portvals(df_strat2, 100000, 0, 0.05)
    cr_strat2s = (cr_strat2.values/  cr_strat2.iloc[0]) -1
    crsl2= (cr_strat2.iloc[-1] / cr_strat2.iloc[0]) 
    daily_returns_sl2 = cr_strat2/cr_strat2.shift(1)-1









    symbol = 'JPM'
    sd=dt.datetime(2008, 1, 1)
    ed=dt.datetime(2009, 12, 31)
    sv=100000
    dates = pd.date_range(sd,ed)
    #Strategy Learner
    stratLearn3 = sl.StrategyLearner( impact = 0.1)		  	   		 	   			  		 			 	 	 		 		 	
    mantrades3 = stratLearn3.add_evidence(symbol="JPM",  sd=dt.datetime(2008, 1, 1),  ed=dt.datetime(2009, 12, 31), sv=100000)
    strat_trades3 = stratLearn3.testPolicy(symbol="JPM",  sd=dt.datetime(2008, 1, 1),  ed=dt.datetime(2009, 12, 31), sv=100000)
    strat_trades3['Order'] = strat_trades3['Shares'].apply(lambda x: 'BUY' if x >= 1000 else ('SELL' if x <= -1000 else 'Hold'))
    strat_trades3["Symbol"] = symbol
    cols3 = strat_trades3.columns.tolist()
    cols3 = [cols3[2]] + [cols3[1]] + [cols3[0]]
    df_strat3= strat_trades3[cols]
    cr_strat3 = compute_portvals(df_strat3, 100000, 0, 0.1)
    cr_strat3s = (cr_strat3.values/  cr_strat.iloc[0]) -1
    crsl3= (cr_strat3.iloc[-1] / cr_strat3.iloc[0]) 
    daily_returns_sl3 = cr_strat3/cr_strat3.shift(1)-1

    plt.figure(1)
    plt.plot(cr_strats, color = 'Purple', label = '0 impact')
    plt.plot( cr_strat2s, color = 'Red', label = '0.05 impact ')
    plt.plot( cr_strat3s, color = 'black', label = '0.1 impact')
    plt.title("Experiment 2")
    plt.xlabel("Dates")
    plt.ylabel("Normalized Returns ")
    plt.legend(loc = 'upper left')
    plt.xticks(rotation = 45)
    plt.savefig("Experiment2impact.png")
    plt.close()

    cum_ret = [cr_strats.mean(),cr_strat2s.mean(),cr_strat3s.mean()]
    impactx =[0, 0.05, 0.1]

    plt.plot(impactx, cum_ret)
    plt.title("Experiment 2 Impact vs Average Returns")
    plt.xlabel("Impact")
    plt.ylabel("Normalized Returns")
    plt.xticks(rotation = 45)
    plt.savefig("Experiment2avg.png")
    plt.close()