# -*- coding: utf-8 -*-
"""
Created on Wed May 17 07:41:21 2023

@author: João Victor Barbosa
"""

import psycopg2 as psy

class AppBD:
    
    def abrirConexao(self):
        try:
            self.connection = psy.connect(user="postgres",
                                          password="123321#Sobre2.",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="projectPyhtonGUI")
        except (Exception, psy.Error) as error:
            if(self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)
        return self.connection


