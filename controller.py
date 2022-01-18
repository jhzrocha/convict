from model import mySQLconnection

class controller():

    def getAllCompanyDatas(self,companyCode):
        

        allData = { 'high': mySQLconnection().getAllHighValues(companyCode),
                    'low' : mySQLconnection().getAllLowValues(companyCode),
                    'open':mySQLconnection().getAllOpenValues(companyCode),
                    'close': mySQLconnection().getAllCloseValues(companyCode), 
                    'volume': mySQLconnection().getAllVolumeValues(companyCode), 
                    'variation': mySQLconnection().getAllVariationValues(companyCode),
                    'numberRegister': mySQLconnection().getNumberOfRegisters(companyCode)[0]
                    }
        return allData
    
  