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
def exp1():
    ##########################

    # IN SAMPLE

    ##########################
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
    cr_strat = compute_portvals(df_strat, 100000, 9.95, 0.005)
    crsl= (cr_strat.iloc[-1] / cr_strat.iloc[0]) - 1
    daily_returns_sl = cr_strat/cr_strat.shift(1)-1

    #Benchmark 
    prices = get_data([symbol], dates)
    prices = prices.iloc[: ,1:]
    benchmark = pd.DataFrame(0, index=prices.index, columns=["Symbol", 'Order', 'Shares'])
    first = benchmark.index[0]
    benchmark['Symbol'] = 'JPM'
    benchmark.loc[first, 'Order'] = "BUY"
    benchmark.loc[first, 'Shares'] = 1000

    crb = compute_portvals(benchmark, 100000, 9.95, 0.005)
    cr = (crb.iloc[-1] / crb.iloc[0]) - 1
    daily_returns_benchmark = crb/crb.shift(1)-1


    man =ms.ManualStrategy()		  	   		 	   			  		 			 	 	 		 		 	
    mantrades = man.testPolicy(symbol="JPM",  sd=dt.datetime(2008, 1, 1),  ed=dt.datetime(2009, 12, 31), sv=100000)

    crm = compute_portvals(mantrades, 100000, 9.95, 0.005)
    crmf = (crm.iloc[-1] / crm.iloc[0]) - 1
    daily_returns_manual = crm/crm.shift(1)-1
    print(crmf)
    print(crsl)
    #crmf = (crm.iloc[-1] / crm.iloc[0]) - 1
    #daily_returns_manual = crm/crm.shift(1)-1
    plot_df = pd.DataFrame(0,index=benchmark.index, columns=["Benchmark", "Manual","SL"])
    plot_df["Benchmark"] = crb
    plot_df["Manual"] =crm
    plot_df["SL"] = cr_strat
    plot_df["Benchmark"] = plot_df["Benchmark"]/plot_df["Benchmark"].iloc[0]
    plot_df["Manual"] =  plot_df["Manual"] /  plot_df["Manual"].iloc[0]
    plot_df["SL"] =  plot_df["SL"] /  plot_df["SL"].iloc[0]
    plt.figure(1)
    plt.plot(plot_df["Benchmark"], color = 'Purple', label = 'Benchmark')
    plt.plot( plot_df["Manual"], color = 'Red', label = 'Manual Strategy')
    plt.plot( plot_df["SL"], color = 'black', label = 'Strategy Learner')
    plt.title("Experiment 1")
    plt.xlabel("Dates")
    plt.ylabel("Normalized Returns ")
    plt.legend(loc = 'upper left')
    plt.xticks(rotation = 45)
    plt.savefig("Experiment1InSample.png")
    plt.close()



    ##########################

    # OUT OF  SAMPLE

    ###########################

    symbol = 'JPM'
    sd=dt.datetime(2010, 1, 1)
    ed=dt.datetime(2011, 12, 31)
    sv=100000
    dates = pd.date_range(sd,ed)
    #Strategy Learner
    stratLearn = sl.StrategyLearner()		  	   		 	   			  		 			 	 	 		 		 	
    mantrades = stratLearn.add_evidence(symbol="JPM",  sd=dt.datetime(2010, 1, 1),  ed=dt.datetime(2011, 12, 31), sv=100000)
    strat_trades = stratLearn.testPolicy(symbol="JPM",  sd=dt.datetime(2010, 1, 1),  ed=dt.datetime(2011, 12, 31), sv=100000)
    strat_trades['Order'] = strat_trades['Shares'].apply(lambda x: 'BUY' if x >= 1000 else ('SELL' if x <= -1000 else 'Hold'))
    strat_trades["Symbol"] = symbol
    cols = strat_trades.columns.tolist()
    cols = [cols[2]] + [cols[1]] + [cols[0]]
    df_strat= strat_trades[cols]
    cr_strat = compute_portvals(df_strat, 100000, 9.95, 0.005)
    crsl= (cr_strat.iloc[-1] / cr_strat.iloc[0]) - 1
    daily_returns_sl = cr_strat/cr_strat.shift(1)-1

    #Benchmark 
    prices = get_data([symbol], dates)
    prices = prices.iloc[: ,1:]
    benchmark = pd.DataFrame(0, index=prices.index, columns=["Symbol", 'Order', 'Shares'])
    first = benchmark.index[0]
    benchmark['Symbol'] = 'JPM'
    benchmark.loc[first, 'Order'] = "BUY"
    benchmark.loc[first, 'Shares'] = 1000

    crb = compute_portvals(benchmark, 100000, 9.95, 0.005)
    cr = (crb.iloc[-1] / crb.iloc[0]) - 1
    daily_returns_benchmark = crb/crb.shift(1)-1


    man =ms.ManualStrategy()		  	   		 	   			  		 			 	 	 		 		 	
    mantrades = man.testPolicy(symbol="JPM",  sd=dt.datetime(2010, 1, 1),  ed=dt.datetime(2011, 12, 31), sv=100000)

    crm = compute_portvals(mantrades, 100000, 9.95, 0.005)
    crmf = (crm.iloc[-1] / crm.iloc[0]) - 1
    daily_returns_manual = crm/crm.shift(1)-1
    plot_df = pd.DataFrame(0,index=benchmark.index, columns=["Benchmark", "Manual","SL"])
    plot_df["Benchmark"] = crb
    plot_df["Manual"] =crm
    plot_df["SL"] = cr_strat
    plot_df["Benchmark"] = plot_df["Benchmark"]/plot_df["Benchmark"].iloc[0]
    plot_df["Manual"] =  plot_df["Manual"] /  plot_df["Manual"].iloc[0]
    plot_df["SL"] =  plot_df["SL"] /  plot_df["SL"].iloc[0]
    plt.figure(2)
    plt.plot(plot_df["Benchmark"], color = 'Purple', label = 'Benchmark')
    plt.plot( plot_df["Manual"], color = 'Red', label = 'Manual Strategy')
    plt.plot( plot_df["SL"], color = 'black', label = 'Strategy Learner')
    plt.title("Experiment 1 Out of Sample")
    plt.xlabel("Dates")
    plt.ylabel("Normalized Returns ")
    plt.legend(loc = 'upper left')
    plt.xticks(rotation = 45)
    plt.savefig("Experiment1outofSample.png")
    plt.close()
    