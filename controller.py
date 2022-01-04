import mysql.connector
 
 
class ClasseConexao:
    def __init__(self, host, usuario, senha, banco):
 
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.banco = banco
        self.conn = mysql.connector.connect(host=self.host,username=self.usuario, password=self.senha, database = self.banco)
        if (self.conn.is_connected):
            print("Conexão com o banco de dados " + self.conn.database + " foi bem sucedida")
            
 
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
    
    