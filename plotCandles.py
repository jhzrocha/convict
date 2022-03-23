import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class GraficPlotter:

    def plotCandles(self, openValues, closeValues, highValues,lowValues):
        prices = pd.DataFrame({'open': openValues,
                       'close': closeValues,
                       'high': highValues,
                       'low': lowValues},
                       index=pd.date_range("2021-01-01", periods=len(lowValues), freq="d"))
        #create figure
      
        fig = plt.figure()       

        #define width of candlestick elements
        width = .4
        width2 = .05

        #define up and down prices
        up = prices[prices.close>=prices.open]
        down = prices[prices.close<prices.open]
        #define colors to use
        upColor = 'green'
        downColor = 'red'

        #plot up prices
        plt.bar(up.index,up.close-up.open,width,bottom=up.open,color=upColor)
        plt.bar(up.index,up.high-up.close,width2,bottom=up.close,color=upColor)
        plt.bar(up.index,up.low-up.open,width2,bottom=up.open,color=upColor)

        #plot down prices
        plt.bar(down.index,down.close-down.open,width,bottom=down.open,color=downColor)
        plt.bar(down.index,down.high-down.open,width2,bottom=down.open,color=downColor)
        plt.bar(down.index,down.low-down.close,width2,bottom=down.close,color=downColor)

        #rotate x-axis tick labels
        plt.xticks(rotation=45, ha='right')
        plt.grid(True)

        #display candlestick chart
        plt.show()

    def lineGrafic(self, dataArray):
        plt.style.use('_mpl-gallery')

# make data
        npDataArray = np.array(dataArray)
        x = np.sort(npDataArray)
        y = npDataArray

        fig, ax = plt.subplots()

        zero = 0

        supper = np.ma.masked_where(y > zero, y)
        slower = np.ma.masked_where(y < zero, y)
        zeroValues = np.ma.masked_where(y == zero, y)
        ax.plot(x, zeroValues, x, slower, x, supper)
  

        # ax.set(xlim=(0, len(dataArray)), xticks=np.arange(1, 8),
        #     ylim=(-0.4, 0.4), yticks=np.arange(-0.4, 0.4))

        plt.show()