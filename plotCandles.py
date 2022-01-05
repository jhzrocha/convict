import matplotlib.pyplot as plt
import pandas as pd

from controller import ClasseConexao

class GraficPlotter:

    def plotAllCandles(self, companyCode):
        conexao = ClasseConexao('localhost' ,'root', '','convict')
        
        prices = pd.DataFrame({'open': conexao.getAllOpenValues(companyCode),
                       'close': conexao.getAllCloseValues(companyCode),
                       'high': conexao.getAllHighValues(companyCode),
                       'low': conexao.getAllLowValues(companyCode)},
                       index=pd.date_range("2021-01-01", periods=len(conexao.getAllLowValues(companyCode)), freq="d"))
        #create figure
        conexao.desconectar();
        plt.figure()

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

        #display candlestick chart
        plt.show()

