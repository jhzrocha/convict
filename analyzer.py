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
                        if((tail/head > 2.5) and (head > tail/3) and ((high-close)/head)> 0.3):
                            highHammer.append(high)
                            lowHammer.append(low)
                            openHammer.append(openValue)
                            closeHammer.append(close)

        hammerDatas = [highHammer,lowHammer,openHammer,closeHammer]
        
        return hammerDatas
