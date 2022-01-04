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
            
 
    def efetuaConsulta(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_perfil, nome_perfil from perfis;")
        
        linhas = cursor.fetchall() 
        #Fetchone retorna somente um registro 
        #fetchall retorna todos os registros da tabela
        
        print("Total de registros: " + str(cursor.rowcount))
        for linha in linhas:
            print (str(linha[0]) +"  -  " +  linha[1])
 
    def efetuaConsultaPersonalizada(self, tabela,clausula,):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * from "+ tabela + " where " + clausula+ " ;")
        x = cursor.fetchall() 
        print("Total de Registros: " + str(cursor.rowcount))
 
 
    def desconectar(self):
        self.conn.close()
 
        if (self.conn.is_closed):
            print("Conexão encerrada")
 
    def insertData(self,table, open, close, high, low, volume, variation,adjClose):
        cursor = self.conn.cursor()
        sql = "INSERT INTO " + table +" (open, close, high, low , volume, variation, adjClose) VALUES ("+ str(open) +"," + str(close) + ","+ str(high) +","+ str(low) + "," + str(volume) +"," + str(variation) +","+ str(adjClose) + ");"
        cursor.execute(sql)
        self.conn.commit()
        # print(table)
        # print(open)
        # print(close)
        # print(high)
        # print(low)
        # print(volume)
        # print(variation)
        # print(adjClose)
    def createTable(self,CompanyName):
        cursor = self.conn.cursor()
        
        sql = "CREATE TABLE " + CompanyName+ " (open FLOAT(24), close FLOAT(24), high FLOAT(24), low FLOAT(24), volume FLOAT(24), variation FLOAT(24) ,adjClose FLOAT(24));"
        cursor.execute(sql)
        self.conn.commit()
    
    def fazerLogin (self, login, senha):
        # login = str(input("Login: "))
        # senha = str(input("Senha:" ))
        cursor = self.conn.cursor()
        
        try:
            cursor.execute("SELECT login_acesso  FROM acessos WHERE login_acesso = '" + login + "' ;")
            linha = cursor.fetchone() 
                      
            cursor.execute("SELECT senha_acesso FROM acessos WHERE login_acesso = '" + linha[0] + "';")
            linha2 = cursor.fetchone()
            
            if (linha2[0] == senha):
                print("Seja bem vindo!")
            else:
                print("Senha inválida")        
        
        except:       
            print("Login inválido!")
            
    def excluiCategoria(self, nomeCategoria):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_categoria FROM categorias WHERE nome_categoria = " + nomeCategoria + ";")
        linha = cursor.fetchone()
        
        if  cursor.rowcount == 1:
            qry = cursor.execute("SELECT * FROM cursos WHERE id_categoria =  '" + linha[0] + "';")    
        
        cursor.execute("DELETE FROM categorias WHERE nome_categoria = '" + nomeCategoria+ "';")
        self.conn.commit()
        
    def insereCursos(self, nome_curso, valor_curso, id_modalidade, id_categoria, duracao_curso, status_curso):
        cursor = self.conn.cursor()
        
        cursor.execute("INSERT INTO cursos (nome_curso, valor_curso, id_modalidade, id_categoria, duracao_curso,status_curso) VALUES"
                      " ('" + nome_curso + "','" + str(valor_curso) + "'," + str(id_modalidade) + "," + str(id_categoria) + "," + str(duracao_curso) + ",'" + status_curso + "');")
 
        self.conn.commit()
# conexao = ClasseConexao('localhost' ,'root', '','db_projeto')
# # conexao.efetuaConsulta()
# # print("______ outro método de consulta _______")
# # conexao.efetuaConsultaPersonalizada('categorias','status_categoria ="A" ')
# # conexao.fazerLogin("jhzrocha","1234")
# # conexao.desconectar()
# conexao.insereCursos( "Django", 300.1 , 1, 1, 150, "A")