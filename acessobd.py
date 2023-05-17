# -*- coding: utf-8 -*-
"""
Created on Wed May 17 07:41:21 2023

@author: João Victor Barbosa
"""


class ConexaoBanco:
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.string_conexao = f"host={self.host} port={self.port} user={self.username} password={self.password} dbname={self.database}"

# Exemplo de utilização
dadosConexao = ConexaoBanco("127.0.0.1", "5432", "postgres", "123321#Sobre2.", "projectPyhtonGUI")

dadosConexao = dadosConexao.string_conexao
