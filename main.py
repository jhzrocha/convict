
from dataPumper import DataPumper
from plotCandles import GraficPlotter
from controller import controller
from analyzer import Analyzer
from model import mySQLconnection
companyCode = 'petr4'

hammers = Analyzer().candleIdentifier(companyCode)

print(hammers)
# [highHammer,lowHammer,openHammer,closeHammer]
GraficPlotter().plotCandles(hammers[2],hammers[3],hammers[0],hammers[1])