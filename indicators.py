import datetime as dt  		  	   		 	   			  		 			 	 	 		 		 	
import os  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
import numpy as np  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
import pandas as pd  	
from marketsimcode import compute_portvals	  
import matplotlib.pyplot as plt	   		 	   			  		 			 	 	 		 		 	
from util import get_data, plot_data 

def author(): 
  return "radjei3"
def SMA( data , window_size ,  symbol, plot = False):
    sma_df = pd.DataFrame(0, index=data.index, columns=["SMA"])
    sma_df["SMA"] = data.rolling(window = window_size, min_periods =window_size).mean()
    #sma_df["SMA"] = sma_df["SMA"].fillna(method = 'bfill')
    sma_df[symbol] = data[symbol]
    sma_df['Price/SMA'] = sma_df[symbol]/sma_df['SMA'] 
    sma_df['singal'] = np.where(sma_df["Price/SMA"] < 0.9,-1, np.where(sma_df["Price/SMA"] > 1.1,1,0))
    
    return sma_df['singal'].values

def BB(data , window_size ,  symbol, plot = False):
    bb_df = pd.DataFrame(0, index=data.index, columns=["BB +","BB -"])
    bb_df["BB"] = data.rolling(window = window_size, min_periods =window_size).std()
    bb_df["SMA"] = data.rolling(window = window_size, min_periods =window_size).mean()
    bb_df["SMA"] = bb_df["SMA"].fillna(method = 'bfill')
    bb_df["BB"] = bb_df["BB"].fillna(method = 'bfill')
    bb_df["BB +"] = bb_df["SMA"] + (bb_df["BB"]* 2)
    bb_df["BB -"] = bb_df["SMA"] - (bb_df["BB"]* 2)
    bb_df["Answer"] = (data[symbol] - bb_df["BB -"]) / (bb_df["BB +"] - bb_df["BB -"])
    bb_df['singal'] = np.where(bb_df["Answer"] < 0,1, np.where(bb_df["Answer"] > 1,-1,0))

    return   bb_df["singal"].values

def GDC ( data , symbol,window_long = 50, window_short = 20, plot = False):
    gdc = pd.DataFrame(0, index=data.index, columns=["SMA Long"])
    gdc["SMA Long"] = data.rolling(window = window_long).mean()
    gdc["SMA Short"] = data.rolling(window = window_short).mean()  
    gdc["SMA Short"] = gdc["SMA Short"].fillna(method = 'bfill')
    gdc["SMA Long"] = gdc["SMA Long"].fillna(method = 'bfill')
    gdc[symbol] = data[symbol]




    if plot:
        plt.plot(gdc, label = gdc.columns)
        plt.xticks(rotation = 30)
        plt.title("Golden Death Cross")
        plt.ylabel("Normalized Price")
        plt.xlabel("Dates")
        plt.legend(loc="upper left")
        plt.savefig("GCD.png")
        plt.close()
    gdc['signal'] = 0
    
    
    # Find crossover points
    for i in range(1, len(gdc)):
        if  gdc["SMA Short"].iloc[i] >  gdc["SMA Long"].iloc[i] and   gdc["SMA Short"].iloc[i - 1] <=   gdc["SMA Long"].iloc[i-1] :
            gdc.at[gdc.index[i], 'signal'] = 1
        elif  gdc["SMA Short"].iloc[i] < gdc["SMA Long"].iloc[i] and  gdc["SMA Short"].iloc[i - 1] >= gdc["SMA Long"].iloc[i-1]  :
            gdc.at[gdc.index[i], 'signal'] = -1



    

    return gdc['signal'].values



def MACD ( data , symbol,window_long = 26, window_short = 12, plot = False):
    MACD = pd.DataFrame(0, index=data.index, columns=["MACD Long"])
    MACD["MACD Long"] = data.ewm(span = window_long, adjust = False).mean()
    MACD["MACD Short"] = data.ewm(span =  window_short, adjust = False).mean()
    MACD["JPM Price"] = data[symbol]
    MACD2 = pd.DataFrame(0, index=data.index, columns=["MACD"])
    MACD2["MACD"] = MACD["MACD Short"] - MACD["MACD Long"]
    MACD2["Signal"] = MACD2["MACD"].ewm(span =9,adjust=False).mean()
    MACD3 = pd.DataFrame(0, index=data.index, columns=["Final"])
    for i in range (1,len(MACD2)):
        if  MACD2["MACD"].iloc[i-1] >  MACD2["Signal"].iloc[i-1] and   MACD2["MACD"].iloc[i] <  MACD2["Signal"].iloc[i]:
             MACD3["Final"].iloc[i] = 1
        elif  MACD2["MACD"].iloc[i-1] <  MACD2["Signal"].iloc[i-1] and  MACD2["MACD"].iloc[i] >  MACD2["Signal"].iloc[i] :
             MACD3["Final"].iloc[i] = -1
    return  MACD3["Final"].values


def momentum(data , symbol , days, plot = True):
    momentum = pd.DataFrame(0, index=data.index, columns=["Momentum"])
    momentum["Momentum"] = data[symbol] - data[symbol].shift(days)
    momentum['Signal'] =0
    momentum['Signal'][momentum['Momentum']> 0] = 1
    momentum['Signal'][momentum['Momentum']< 0] = -1



    


    return  momentum['Signal'].values