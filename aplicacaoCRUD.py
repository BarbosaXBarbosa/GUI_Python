# -*- coding: utf-8 -*-
"""
Created on Thu May 18 07:57:01 2023

@author: João Victor Barbosa
"""

import tkinter as tk
from tkinter import ttk
import dao as Dao

class Principal:
    def __init__(self, win):
        self.win = win
        self.objBD = Dao.DAO()

        # componentes
        self.lblCodigo = tk.Label(win, text='Código do Produto:')
        self.lblNome = tk.Label(win, text='Nome do Produto')
        self.lblPreco = tk.Label(win, text='Preco')

        self.txtCodigo = tk.Entry(win, bd=3)
        self.txtNome = tk.Entry(win)
        self.txtPreco = tk.Entry(win)
        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)
        self.btnAtualizar = tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)
        self.btnExcluir = tk.Button(win, text='Excluir', command=self.fExcluirProduto)
        self.btnLimpar = tk.Button(win, text='Limpar', command=self.fLimparTela)

        # --------------------Componentes TreeView--------------------------------------
        self.dadosColunas = ("Código", "Nome", "Preço")
        self.treeProdutos = ttk.Treeview(win, column=self.dadosColunas, selectmode='browse')

        self.verscrlbar = ttk.Scrollbar(win, orient="vertical", command=self.treeProdutos.yview)

        self.verscrlbar.pack(side='right', fill='y')

        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)

        self.treeProdutos.heading("Código", text="Código")
        self.treeProdutos.heading("Nome", text="Nome")
        self.treeProdutos.heading("Preço", text="Preço")

        self.treeProdutos.column("Código", minwidth=0, width=100)
        self.treeProdutos.column("Nome", minwidth=0, width=100)
        self.treeProdutos.column("Preço", minwidth=0, width=100)

        self.treeProdutos.pack(padx=100, pady=10)

        self.treeProdutos.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)

        # --------------------------------------------------------------
        # Posicionamento dos Componentes na Janela
        # ---------------------------------------------------------------
        self.lblCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)

        self.lblNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)

        self.lblPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y=150)

        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)

        self.treeProdutos.place(x=100, y=300)

        self.carregarDadosIniciais()

    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeProdutos.selection():
            item = self.treeProdutos.item(selection)
            codigo, nome, preco = item["values"][0:3]
            self.txtCodigo.insert(0, codigo)
            self.txtNome.insert(0, nome)
            self.txtPreco.insert(0, preco)

    def carregarDadosIniciais(self):
        try:
            self.id = 0
            self.iid = 0
            registros = self.objBD.recuperarProdutos()
            print("**************** dados disponíveis no BD *******************")

            for item in registros:
                codigo = item[0]
                nome = item[1]
                preco = item[2]

                print("Código =", codigo)
                print("Nome =", nome)
                print("Preço =", preco, "\n")

                self.treeProdutos.insert('', 'end', iid=self.iid, values=(codigo, nome, preco))
                self.iid = self.iid + 1
                self.id = self.id + 1

            print('Dados da Base')
        except Exception as e:
                print("Erro durante a execução:", e)

    def fLerCampos(self):
        try:
            print("********** dados disponíveis ************")
            codigo = int(self.txtCodigo.get())
            print('Código:', codigo)
            nome = self.txtNome.get()
            print('Nome:', nome)
            preco = float(self.txtPreco.get())
            print('Preço:', preco)
            print('Leitura dos Dados com Sucesso!')
        except:
            print('Não foi possível ler os dados.')
        return codigo, nome, preco

    def fCadastrarProduto(self):
        try:
            print('************** dados disponíveis ***************')
            codigo, nome, preco = self.fLerCampos()
            print('Valores lidos:', codigo, nome, preco)  # Adicione esta linha para imprimir os valores lidos
            self.objBD.inserirProduto(codigo, nome, preco)
            self.treeProdutos.insert('', 'end', iid=self.iid, values=(codigo, nome, preco))
    
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.fLimparTela()
            print('Produto Cadastrado com Sucesso!')
        except:
            print('Não foi possível fazer o cadastro.')

    def fAtualizarProduto(self):
        try:
            print("****************** dados disponíveis ***************")
            codigo, nome, preco = self.fLerCampos()
            self.objBD.atualizarProduto(codigo, nome, preco)
            # recarregar dados na tela
            self.recarregarTela()
            print('Produto Atualizado com Sucesso!')
        except:
            print('Não foi possível fazer a atualização.')

    def fExcluirProduto(self):
        try:
            print("******************* dados disponíveis *******************")
            codigo, nome, preco = self.fLerCampos()
            self.objBD.excluirProduto(codigo)
            # recarregar dados na tela
            self.recarregarTela()
            print('Produto Excluído com Sucesso!')
        except:
            print('Não foi possível fazer a exclusão do produto.')

    def fLimparTela(self):
        try:
            print("******************** dados disponíveis *******************")
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            print('Campos Limpos!')
        except:
            print('Não foi possível limpar os campos.')

    def recarregarTela(self):
        self.treeProdutos.delete(*self.treeProdutos.get_children())
        self.carregarDadosIniciais()
        self.fLimparTela()
    
    def fecharAplicacao(self):
        self.objBD.fecharConexao()
        self.win.destroy()
    


# -------------------------------------------------------------------------------------------
# Programa Principal
# -------------------------------------------------------------------------------------------
janela = tk.Tk()
principal = Principal(janela)
janela.title('Bem Vindo a Aplicação de GUI e Banco de Dados Utilizando Python')
janela.geometry("820x600+10+10")

janela.protocol("WM_DELETE_WINDOW", principal.fecharAplicacao)

janela.mainloop()

                