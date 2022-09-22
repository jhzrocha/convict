from plotCandles import GraficPlotter
from convict import Convict
from controller import Controller
from dataPumper import CompanyDataPumper
from model import mySQLconnection
import pandas_datareader as web
import pandas as pd
import yfinance as yf
from enums import sectors

# companyCode = 'PETR4.SA'

mySQLconnection().addAndInsertSectorTypesData()
# data = yf.Ticker(companyCode)
# for i in sectors.sectorTypes:
#     for j in i:
#         for x in i.get(j):
#             mySQLconnection().insertSubSectorType(x,j)
#print(data.history(period="max")['Open'])
#print(web.get_data_yahoo(companyCode, start='1980-01-01'))

#print(mySQLconnection().getAllCompanyCodes())
#Controller().createSharesTables()


#CompanyDataPumper('PETR4').createTableAndAddData()
#Convict().getDailyOscilation(companyCode)
# peaksAndValleys = Convict().getValleyAndPeaks(companyCode)

# hammers = Controller().getAllCompanyDatas(companyCode)

# GraficPlotter().plotCandles(hammers['open'],hammers['close'],hammers['high'], hammers['low'])
# Controller().getAverageDayPrices('also3')
# GraficPlotter().lineGraficPeaksAndValleys(Controller().getAverageDayPrices('also3'),peaksAndValleys)

# ativosData = pd.read_excel('B3_Ativos.xlsx', sheet_name='B3_Ativos', usecols="B,AV,AY")
# for i in range(len(ativosData)):
#             print(str(ativosData.get('TckrSymb')[i]) +
#                                               str(ativosData.get('CrpnNm')[i]) +
#                                               str(ativosData.get('MktCptlstn')[i]))
#Controller().createAndInsertAtivos()
print()


# GraficPlotter().lineGrafic(Controller().getIndexes(companyCode),hammers['close'],companyCode)
