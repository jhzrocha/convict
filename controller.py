from model import mySQLconnection

class Controller():

    def getAllCompanyDatas(self,companyCode):        

        allData = { 'high': mySQLconnection().getAllHighValues(companyCode),
                    'low' : mySQLconnection().getAllLowValues(companyCode),
                    'open':mySQLconnection().getAllOpenValues(companyCode),
                    'close': mySQLconnection().getAllCloseValues(companyCode), 
                    'volume': mySQLconnection().getAllVolumeValues(companyCode), 
                    'variation': mySQLconnection().getAllVariationValues(companyCode),
                    'numberOfRegisters': mySQLconnection().getNumberOfRegisters(companyCode)[0]
                    }
        return allData
    
    def getIndexes(self, companyCode):
        indexes = []
        for index in range(0,mySQLconnection().getNumberOfRegisters(companyCode)[0]):
            indexes.append(index)
        return indexes
    
    def getAverageDayPrices(self, companyCode):
        lowPrices = mySQLconnection().getAllLowValues(companyCode)
        highPrices = mySQLconnection().getAllHighValues(companyCode)

        averageDayPrice = []

        for day in range(len(lowPrices)):
            averageDayPrice.append((highPrices[day] + lowPrices[day])/2)
        
        return averageDayPrice
