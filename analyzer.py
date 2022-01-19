from controller import controller

class Analyzer():

    def candleIdentifier(self,companyCode):
        companyData = controller().getAllCompanyDatas(companyCode)
        
        highHammer = []
        lowHammer = []
        openHammer = []
        closeHammer = []

        for index in range(0,companyData['numberRegister']):
            high = companyData['high'][index]
            low = companyData['low'][index]
            openValue = companyData['open'][index]
            close = companyData['close'][index]
            variation = companyData['variation'][index]

            if(variation > 0):
                head = close - openValue
                tail = openValue - low
                if (head > 0):
                        # Adicionar a proporção de head do candle
                        if((tail/head > 2.5)  and (((high-close)/head)< 2) and (tail/3 < head)):
                            highHammer.append(high)
                            lowHammer.append(low)
                            openHammer.append(openValue)
                            closeHammer.append(close)
        
        hammerDatas = {'high':highHammer,
                        'low': lowHammer,
                        'open':openHammer,
                        'close':closeHammer}        
        return hammerDatas
