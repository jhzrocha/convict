from controller import Controller

class Convict():

    def hammerIdentifier(self,companyCode):
        companyData = Controller().getAllCompanyDatas(companyCode)
        
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

    def priceTrendByAveragePrice(self, companyCode):
        
        averageDayPrices = Controller().getAverageDayPrice(companyCode)
        dayPriceDifference = []
        for price in range(len(averageDayPrices) - 1):
            dayPriceDifference.append((averageDayPrices[price] - averageDayPrices[price + 1])/averageDayPrices[price])

        print(dayPriceDifference)    
        return dayPriceDifference
