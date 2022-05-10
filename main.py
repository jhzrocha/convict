from plotCandles import GraficPlotter
from convict import Convict
from controller import Controller
from dataPumper import CompanyDataPumper


companyCode = 'ALSO3'

# CompanyDataPumper('ALSO3').createTableAndAddData()
# Convict().getDailyOscilation(companyCode)
print(Convict().getPeaksPositonAndValues(companyCode))


# hammers = Controller().getAllCompanyDatas(companyCode)

# GraficPlotter().plotCandles(hammers['open'],hammers['close'],hammers['high'], hammers['low'])
# Controller().getAverageDayPrices('also3')
GraficPlotter().lineGrafic(Controller().getAverageDayPrices('also3'))




# GraficPlotter().lineGrafic(Controller().getIndexes(companyCode),hammers['close'],companyCode)
