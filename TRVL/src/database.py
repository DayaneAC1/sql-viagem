import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("trvl.db")
    return conexao 

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''create table if not exists usuarios
                   (email text primary key,nome text,senha text)''')
    
    cursor.execute('''create table if not exists projetos_de_viagem
                   (id integer primary key,id_usuario text,destino text,data_prevista text,
                   status text,imagem text,gastos real,dinheiro_guardado real)''')
    
    conexao.commit()

def criar_usuario(email, nome, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute('insert into usuarios (email,nome,senha) VALUES (?,?,?) ',(email,nome,senha))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()

def criar_projeto(id_usuario,destino,data_prevista,status,imagem,gastos,dinheiro_guardado):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('''INSERT INTO projetos_de_viagem(id_usuario,destino,data_prevista,
                       status,imagem,gastos,dinheiro_guardado) values (?, ?, ? , ?, ?, ?, ?)'''
                       ,(id_usuario,destino,data_prevista,status,imagem,gastos,dinheiro_guardado))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()  

def buscar_viagens(id_usuario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    # PREENCHA AQUI, BUSCAR TODAS AS VIAGENS ordem: destino, data prevista, status, imagem
    cursor.execute("SELECT destino, data_prevista,status,imagem FROM projetos_de_viagem WHERE id_usuario=?",(id_usuario,))
    viagens = cursor.fetchall()
    conexao.close()

    return viagens

def deletar_viagens(email):
    
    
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # DELETA A VIAGEM CONFORME O EMAIL
        cursor.execute('DELETE FROM projetos_de_viagem WHERE id=?',(email,))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close() 
        
        
def mostrar_id_viagem(id_email):
    
    
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM projetos_de_viagem where id_usuario=?',(id_email,))
        conexao.commit()
        viagens= cursor.fetchall()
        return viagens
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close() 
        
def deletar_usuario(deletar_usuario):
    
    
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        #DELETA O USUARIO CONFORME O EMAIL INFORMADO
        cursor.execute('DELETE FROM usuarios WHERE email=?',(deletar_usuario,))
        conexao.commit()
        #CHAMA FUNÇÃO DE DELETAR VIAGENS
        deletar_viagens(deletar_usuario)
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close() 
        
        
def mudar_nome(nome,email):
    
    
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        #ATUALIZA O NOME COM BASE NO NOME INFORMADO
        cursor.execute("UPDATE usuarios SET nome='paulo' WHERE nome=? AND email=?",(nome,email,))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close() 
        
        
def mudar_senha():
    
    
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        #ATUALIZA A SENHA CONFORME O NOME E A SENHA INFORMADA.
        cursor.execute("UPDATE usuarios SET senha='5' WHERE senha='123' and nome='123'")
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close() 
        

def editar_viagem(email):
    
    
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        #ATUALIZA VIAGEM CONFORME O NOME E A SENHA INFORMADA.
        cursor.execute("UPDATE projetos_de_viagem SET destino ='brasil',data_prevista='27012004',status='pendente',imagem='',gastos='1500',dinheiro_guardado='0' WHERE id_usuario=? ",(email,))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close() 
        
        
if __name__ == '__main__': 
    conexao = conectar_banco()
    criar_tabelas()
   # deletar_usuario("leetobr2@gmail.com")
    mudar_nome("leeto","leetobr@gmail.com")
    editar_viagem("leetobr@gmail.com")
    mudar_senha()