import pandas_datareader as web
import yfinance as yf
import warnings
from model import mySQLconnection


class DataPumper():

    def __init__(self,companyCode):
        self.companyCode = companyCode
        self.companyCodeyfBR = companyCode + '.SA'
        self.conexao = mySQLconnection()
        self.closeValue= web.get_data_yahoo(self.companyCodeyfBR, start='1980-01-01')["Close"]
        self.openValue= web.get_data_yahoo(self.companyCodeyfBR, start='1980-01-01')["Open"]
        self.lowerValue = web.get_data_yahoo(self.companyCodeyfBR, start='1980-01-01')["Low"]
        self.HigherValue = web.get_data_yahoo(self.companyCodeyfBR, start='1980-01-01')["High"]
        self.volume = web.get_data_yahoo(self.companyCodeyfBR, start='1980-01-01')["Volume"]
        self.adjCloseValue = web.get_data_yahoo(self.companyCodeyfBR, start='1980-01-01')["Adj Close"]    
        warnings.filterwarnings('ignore')
        yf.pdr_override()

    def createTable(self):
        self.conexao.createTable(self.companyCode)

        for x in range(len(self.closeValue + 1)):
            variation = ((self.closeValue[x] - self.closeValue[x - 1])/self.closeValue[x-1])*100
            self.conexao.insertData(self.companyCode, self.openValue[x], self.closeValue[x], self.HigherValue[x], self.lowerValue[x], self.volume[x], variation,self.adjCloseValue[x])





