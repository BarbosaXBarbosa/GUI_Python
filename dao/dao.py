# -*- coding: utf-8 -*-
"""
Created on Mon May 15 10:54:44 2023

@author: João Victor Barbosa
"""

import psycopg2 as psy

from acessobd import AppBD

class DAO:
    def __init__(self):
        app_bd = AppBD()  # Criar uma instância da classe AppBD
        self.connection = app_bd.abrirConexao()  # Abrir a conexão e atribuir à variável

    def recuperarProdutos(self):
        try:
            cursor = self.connection.cursor()
            
            print("Selecionando todos os produtos")
            
            sql = """SELECT * FROM public."PRODUTO" """
            
            cursor.execute(sql)
            registros = cursor.fetchall()
            print(registros)
            
        except (Exception, psy.Error) as  error:
            print("Erro na recuperação de dados", error)
            
        finally:   
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão foi encerrada")
                
        return registros
    
    
    def inserirProduto(self, codigo, nome, preco):
        try:
            cursor = self.connection.cursor()
            
            sql="""INSERT INTO public."PRODUTO"("CODIGO", "NOME", "PRECO")
                   VALUES (%s,%s,%s)"""
                   
            registro =(codigo, nome, preco)
            
            cursor.execute(sql, registro)
            self.connection.commit()
            
            count = cursor.rowcount
            print(count, "Registro Inserido com sucesso na tabela PRODUTO")
        except (Exception, psy.Error) as error:
            print("Falha ao inserir o registro na tabela", error)
        
        finally:   
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão foi encerrada")
        
    
    def atualizarProduto(self, codigo, nome, preco):
        try:
            cursor = self.connection.cursor()
            
            sql="""UPDATE public."PRODUTO"
                   SET    "NOME" = %s,
                          "PRECO" = %s
                   WHERE  "CODIGO" =%s""" 
                   
            registro =(nome, preco, codigo)
            
            cursor.execute(sql, registro)
            self.connection.commit()
            
            count = cursor.rowcount
            print(count, "Registro Atualizado com sucesso na tabela PRODUTO")
        except (Exception, psy.Error) as error:
            print("Falha ao atualizar o registro na tabela", error)
        
        finally:   
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão foi encerrada")
            
                
    
    
dao = DAO()  # Criar uma instância da classe DAO
# dao.recuperarProdutos()  # Chamar o método recuperarDados() na instância criada
# dao.inserirProduto(2, "Morango", 8.90)
dao.atualizarProduto(2, "Beterraba", 7.90)
