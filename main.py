from plotCandles import GraficPlotter
from convict import Convict
from controller import Controller
from dataPumper import CompanyDataPumper


companyCode = 'ALSO3'

# CompanyDataPumper('ALSO3').createTableAndAddData()
# Convict().getDailyOscilation(companyCode)
peaksAndValleys = Convict().getValleyAndPeaks(companyCode)


# hammers = Controller().getAllCompanyDatas(companyCode)

# GraficPlotter().plotCandles(hammers['open'],hammers['close'],hammers['high'], hammers['low'])
# Controller().getAverageDayPrices('also3')
GraficPlotter().lineGraficPeaksAndValleys(Controller().getAverageDayPrices('also3'),peaksAndValleys)




# GraficPlotter().lineGrafic(Controller().getIndexes(companyCode),hammers['close'],companyCode)
