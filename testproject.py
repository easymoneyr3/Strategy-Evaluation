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
import experiment1 as exp1
import experiment2 as exp2   
import StrategyLearner as sl
import ManualStrategy as ms
def author(): 
  return "radjei3"
 # -------------------------
    ###########################
    # IN SAMPLE
    ###########################
    # -------------------------
man = ms.ManualStrategy()		  	   		 	   			  		 			 	 	 		 		 	
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
man = ms.ManualStrategy()		  	   		 	   			  		 			 	 	 		 		 	
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

exp1.exp1()
exp2.exp2()

