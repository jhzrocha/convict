import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as web
import seaborn as sns
import yfinance as yf
import warnings

from controller import ClasseConexao

conexao = ClasseConexao('localhost' ,'root', '','convict')

warnings.filterwarnings('ignore')
yf.pdr_override()

companyCode = "PETR4"
companyCodeyfBR = companyCode + ".SA"

closeValue= web.get_data_yahoo(companyCodeyfBR, start='1980-01-01')["Close"]
openValue= web.get_data_yahoo(companyCodeyfBR, start='1980-01-01')["Open"]
lowerValue = web.get_data_yahoo(companyCodeyfBR, start='1980-01-01')["Low"]
HigherValue = web.get_data_yahoo(companyCodeyfBR, start='1980-01-01')["High"]
volume = web.get_data_yahoo(companyCodeyfBR, start='1980-01-01')["Volume"]
adjCloseValue = web.get_data_yahoo(companyCodeyfBR, start='1980-01-01')["Adj Close"]

conexao.createTable(companyCode)

for x in range(len(closeValue + 1)):
    variation = ((closeValue[x] - closeValue[x - 1])/closeValue[x-1])*100
    conexao.insertData(companyCode, openValue[x], closeValue[x], HigherValue[x], lowerValue[x], volume[x], variation,adjCloseValue[x])

# # Preço de fechamento
closeValue.plot(figsize=(20, 5), label=companyCode)
# # Média móvel 21 dias
# df_ibov["Close"].rolling(21).mean().plot(label="mm-21")
# # Média móvel 200 dias
# df_ibov["Close"].rolling(200).mean().plot(label="mm-200")
# # Legendas
plt.legend()
plt.show()
