from plotCandles import GraficPlotter
from convict import Convict
from controller import Controller
from dataPumper import CompanyDataPumper


companyCode = 'MGLU3'

# CompanyDataPumper('MGLU3').createTableAndAddData()

# hammers = Controller().getAllCompanyDatas(companyCode)

# GraficPlotter().plotCandles(hammers['open'],hammers['close'],hammers['high'], hammers['low'])
GraficPlotter().lineGrafic(Convict().priceTrendByAveragePrice(companyCode))




# GraficPlotter().lineGrafic(Controller().getIndexes(companyCode),hammers['close'],companyCode)
