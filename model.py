from mysql.connector import (connection)
from enums import connectionData
from enums import sectors
import time 
import pandas as pd

class mySQLconnection:
    def __init__(self):
 
        self.host = connectionData.local
        self.usuario = connectionData.user
        self.senha = connectionData.password
        self.banco = connectionData.dataBaseName
        self.conn = connection.MySQLConnection(user=self.usuario, 
                                               password= self.senha,
                                               host=self.host,
                                               database=self.banco)
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
        
        sql = "CREATE OR REPLACE TABLE " + CompanyName+ " (open FLOAT(24), close FLOAT(24), high FLOAT(24), low FLOAT(24), volume FLOAT(24), variation FLOAT(24) ,adjClose FLOAT(24));"
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
    
    def createAtivosTable(self):
        cursor = self.conn.cursor()        
        sql = "CREATE OR REPLACE TABLE ATIVOS (nr_sequencia int primary key AUTO_INCREMENT NOT NULL, cd_ativo VARCHAR(50) NOT NULL, nm_ativo varchar(100), qt_volume_total float(30));"
        cursor.execute(sql)
        self.conn.commit()

    
    def insertAtivoData(self, cd_ativo, ds_tipo , ds_sgt_name , ds_sqt_mk, cd_type ,nm_ativo, qt_volume_total):
        cursor = self.conn.cursor()
        sql = "INSERT INTO ativos (cd_ativo, ds_tipo , ds_sgt_name , ds_sqt_mkt,cd_type, nm_ativo, qt_volume_total) VALUES ('"+ str(cd_ativo) + "','" + str(ds_tipo) + "','" + str(ds_sgt_name) + "','" + str(ds_sqt_mk) + "','" + str(cd_type) +  "','" + str(nm_ativo) + "','"+ str(qt_volume_total) + "');"
        cursor.execute(sql)       
        self.conn.commit()

    def addAndInsertAtivoData(self):
        ativosData = pd.read_excel('B3_Ativos.xlsx', sheet_name='B3_Ativos', usecols="B,D,E,F,G,AV,AY")
        cursor = self.conn.cursor()        
        sql = "CREATE OR REPLACE TABLE ATIVOS (nr_sequencia int primary key AUTO_INCREMENT NOT NULL, cd_ativo VARCHAR(50) NOT NULL, ds_tipo varchar(250), ds_sgt_name varchar(60), ds_sqt_mkt varchar(30), cd_type varchar(60) ,nm_ativo varchar(100), qt_volume_total varchar(30));"
        cursor.execute(sql)
        self.conn.commit()
        
        for i in range(len(ativosData)):
            self.insertAtivoData(str(ativosData.get('TckrSymb')[i]),
                                 str(ativosData.get('AsstDesc')[i]),
                                 str(ativosData.get('SgmtNm')[i]),
                                 str(ativosData.get('MktNm')[i]),
                                 str(ativosData.get('SctyCtgyNm')[i]),
                                 str(ativosData.get('CrpnNm')[i]),
                                 str(ativosData.get('MktCptlstn')[i]))
            print(str(ativosData.get('TckrSymb')[i]) + '- Dado adicionado na tabela Ativos')
        
    def getAllCompanyCodes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT  cd_ativo from ativos where cd_type = 'SHARES';")
        cursorResults = cursor.fetchall() 
        results = []
        for result in cursorResults:
            results.append(result[0])            
        return results  
    
    def insertSectorType(self, ds_sector_type):
        cursor = self.conn.cursor()
        sql = "INSERT INTO Setores (ds_sector_type) VALUES ('"+ str(ds_sector_type) + "');"
        cursor.execute(sql)       
        self.conn.commit()
    
    def insertSubSectorType(self, ds_subsector_type, ds_sector_type):
        cursor = self.conn.cursor()
        sql = "INSERT INTO Subsetores (ds_subsector_type,nr_seq_sector) VALUES ('"+ str(ds_subsector_type) + "', (select nr_sequencia from setores where ds_sector_type = '" + str(ds_sector_type) +"')"");"
        cursor.execute(sql)       
        self.conn.commit()

    def createSubSectorTable(self):
        cursor = self.conn.cursor()        
        sql = "CREATE OR REPLACE TABLE Subsetores (nr_sequencia int primary key AUTO_INCREMENT NOT NULL, ds_subsector_type VARCHAR(150) NOT NULL, nr_seq_sector int);"
        cursor.execute(sql)
        self.conn.commit()
    
    def addAndInsertSectorTypesData(self):
        cursor = self.conn.cursor()        
        sql = "CREATE OR REPLACE TABLE Setores (nr_sequencia int primary key AUTO_INCREMENT NOT NULL, ds_sector_type VARCHAR(150) NOT NULL);"
        cursor.execute(sql)
        self.conn.commit()
        for i in sectors.sectorTypes:
            for j in i:        
                self.insertSectorType(j)
                for x in i.get(j):
                    self.insertSubSectorType(x,j)
        
    
