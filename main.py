#!/usr/bin/python3
#coding: utf-8
# main.py
# Criado por William Pscheidt
# 09/06/2017 as 16:38

import sys
import os

os.system('cls')

import sqlite3

db = sqlite3.connect("Database/Database.db")
cursor = db.cursor()

print("Opções: ")
print("  inserirdados: Insere musicas na tabela")
print("  criardb: Criar o banco de dados")
print("  musicas: Listar suas musicas")
print("")
opcao = input("Qual opção você quer? ")

if opcao == "criardb":
	try:
		cursor.execute("""
		CREATE TABLE IF NOT EXISTS musicas (
				id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
				titulo TEXT NOT NULL,
				url TEXT NOT NULL
		);
		""")
	except:
		print("[!] Erro de conexão ao banco de dados ou na criação do banco de dados")	
		
elif opcao == "inserirdados":
	url = input("Insira a url(Preferencialmente do youtube): ")
	titulo = input("Insira o titulo da musica: ")
	musicas = ("INSERT INTO musicas (titulo, url) VALUES ('"+url+"', '"+titulo+"')")
	try:
		cursor.execute(musicas)
		db.commit()
	except:
		db.rollback()
	arq = open('musicas.txt', 'w')
	texto = ("Titulo: "+titulo+", Url: "+url)
	arq.write(texto)
	arq.close
		
elif opcao == "musicas":
	try:
		cursor.execute("SELECT * FROM musicas;")
		for linha in cursor.fetchall():
			print(linha)
	except:
		print("[!] Não foi possivel encontrar suas musicas, volte no menu e use 'criardb'")
		
elif opcao == "apagartudo":
	sql = "DROP TABLE musicas;"
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
else:
	print("[!] Opção inexistente!")
	





	