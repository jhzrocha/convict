from plotCandles import GraficPlotter
from analyzer import Analyzer

companyCode = 'petr4'

hammers = Analyzer().candleIdentifier(companyCode)

GraficPlotter().plotCandles(hammers['open'],hammers['close'],hammers['high'], hammers['low'])