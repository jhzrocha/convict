from plotCandles import GraficPlotter
from convict import Convict
from controller import Controller
from dataPumper import CompanyDataPumper
from model import mySQLconnection
import pandas as pd

companyCode = 'ALSO3'


Controller().createSharesTables()

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
