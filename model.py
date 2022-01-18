import mysql.connector
from enums import connectionData
 
class mySQLconnection:
    def __init__(self):
 
        self.host = connectionData.local
        self.usuario = connectionData.user
        self.senha = connectionData.password
        self.banco = connectionData.dataBaseName
        self.conn = mysql.connector.connect(host=self.host,username=self.usuario, password=self.senha, database = self.banco)
        if (self.conn.is_connected):
            print("Conexão com o banco de dados " + self.conn.database + " foi bem sucedida")
            
    def desconnect(self):
        self.conn.close()
 
        if (self.conn.is_closed):
            print("Conexão encerrada")

    def insertData(self,table, open, close, high, low, volume, variation,adjClose):
        cursor = self.conn.cursor()
        sql = "INSERT INTO " + table +" (open, close, high, low , volume, variation, adjClose) VALUES ("+ str(open) +"," + str(close) + ","+ str(high) +","+ str(low) + "," + str(volume) +"," + str(variation) +","+ str(adjClose) + ");"
        cursor.execute(sql)
        self.conn.commit()

    def createTable(self,CompanyName):
        cursor = self.conn.cursor()
        
        sql = "CREATE TABLE " + CompanyName+ " (open FLOAT(24), close FLOAT(24), high FLOAT(24), low FLOAT(24), volume FLOAT(24), variation FLOAT(24) ,adjClose FLOAT(24));"
        cursor.execute(sql)
        self.conn.commit()

    def getAllOpenValues(self, companyCode):
        cursor = self.conn.cursor()
        cursor.execute("SELECT open from "+ companyCode + " ;")
        cursorResults = cursor.fetchall() 
        results = []
        for result in cursorResults:
            results.append(result[0])            
        return results


    def getAllCloseValues(self, companyCode):
        cursor = self.conn.cursor()
        cursor.execute("SELECT close from "+ companyCode + " ;")
        cursorResults = cursor.fetchall() 
        results = []
        for result in cursorResults:
            results.append(result[0])            
        return results  

    def getAllHighValues(self, companyCode):
        cursor = self.conn.cursor()
        cursor.execute("SELECT high from "+ companyCode + " ;")
        cursorResults = cursor.fetchall() 
        results = []
        for result in cursorResults:
            results.append(result[0])            
        return results    

    def getAllLowValues(self, companyCode):
        cursor = self.conn.cursor()
        cursor.execute("SELECT low from "+ companyCode + " ;")
        cursorResults = cursor.fetchall() 
        results = []
        for result in cursorResults:
            results.append(result[0])            
        return results       

    def getAllVolumeValues(self, companyCode):
        cursor = self.conn.cursor()
        cursor.execute("SELECT volume from "+ companyCode + " ;")
        cursorResults = cursor.fetchall() 
        results = []
        for result in cursorResults:
            results.append(result[0])            
        return results  
        
    def getAllVariationValues(self, companyCode):
        cursor = self.conn.cursor()
        cursor.execute("SELECT variation from "+ companyCode + " ;")
        cursorResults = cursor.fetchall() 
        results = []
        for result in cursorResults:
            results.append(result[0])            
        return results  
    
    def getAllAdjCloseValues(self, companyCode):
        cursor = self.conn.cursor()
        cursor.execute("SELECT adjClose from "+ companyCode + " ;")
        cursorResults = cursor.fetchall() 
        results = []
        for result in cursorResults:
            results.append(result[0])            
        return results
        
    def getNumberOfRegisters(self, companyCode):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(volume) from "+ companyCode + " ;")
        cursorResult = cursor.fetchone()
        return cursorResult

        
                    