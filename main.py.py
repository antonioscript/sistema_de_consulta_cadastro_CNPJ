import PySimpleGUI as sg
import requests
import mysql.connector

mydb = mysql.connector.connect (
	host = "localhost", 
	user = "root",
	password = "sua_senha",
	database = "seu_banco"
)

sg.theme("DarkTeal12")

#==================Página de Remoção===============================
def remover_empresas():
	layout = [
		[sg.Text("")],
		[sg.Text("")],
		[sg.Text("")],
		[sg.Text("")],
		[sg.Text("")],
		[sg.Text("")],
		[sg.Text("")],
		[sg.Text("")],
		[sg.Text("")],
		[sg.Text("")],
		[sg.Text("")],
		[sg.Text("Digite o ID da Empresa que Será Removida ", font=" Helvetica 20")],
		[sg.Input(size=(30), font=" Any 16", key="-IDREV-")],
		[sg.Button("Remover", key="rer", font=16), sg.Button("Voltar", key="voltar", font=16)],
		[sg.Text("", key="-MSG-", font=" Helvetica 16")]
]
	
	window = sg.Window('Sistema de Consultar CNPJ', layout, size=(900,700), element_justification='center'  )
	
	while True:
		event, values = window.read()
		if event == sg.WINDOW_CLOSED or event == 'Sair':
			break
		elif event == "voltar":
			window.close()
			empresas_cadastradas()
		elif event == "rer":
			identificador = values['-IDREV-']
			mycursor = mydb.cursor()
			sql = "DELETE FROM empresas3 WHERE id = %s"
			mycursor.execute(sql,(identificador,))
			mydb.commit()
			window['-IDREV-'].update("")
			window['-MSG-'].update('Dados Removidos com Sucesso!')
#===================Página de Produtos Cadastrados============
def empresas_cadastradas():
	layout = [
		[sg.Text("Empresas Cadastradas ", font=" Helvetica 20")],
		[sg.Output(size=(200,20), key="-OUTPUT-", font='Courier 18' )],
		[sg.Button("Visualizar", key="vis", font=16), sg.Button("Remover Alguma Empresa", key="remover", font=16), sg.Button("Voltar", key="voltar", font=16)]
]
	
	window = sg.Window('Sistema de Consultar CNPJ', layout, size=(900,700), element_justification='center'  )
	
	while True:
		event, values = window.read()
		if event == sg.WINDOW_CLOSED or event == 'Sair':
			break
		elif event == "voltar":
			window.close()
			index()
		elif event == "vis":
			mycursor = mydb.cursor()
			mycursor.execute("SELECT * FROM empresas3")
			myresult = mycursor.fetchall()
			print("ID / Nome / Tipo / Situação / Natureza / Município / Estado / Telefone / Email")
			print()
			for row in myresult:
				print(row)
				print()
		elif event == "remover":
			window.close()
			remover_empresas()
#=============================Página Principal========================
def index():	
	layout = [
		[sg.Text("Digite um CNPJ: ", font=" Helvetica 20")],
		[sg.Push(), sg.Input(key = '-CNPJ-', size=20, font=" Any 16"), sg.Push()],
		[sg.Button("Consultar", font="16"), sg.Button("Nova Consulta", font="16"), sg.Button("Sair", font="16")],
		[sg.Text("")],
		[sg.Push(), sg.Text("Nome da Empresa", font="16"), sg.Input(size=(60), font=" Any 16", key="-OUT1-")],
		[sg.Text("")],
		[sg.Push(), sg.Text("Tipo", font="16"), sg.Input(size=(60), font=" Any 16", key="-OUT3-")],
		[sg.Text("")],
		[sg.Push(), sg.Text("Situação", font="16"), sg.Input(size=(60), font=" Any 16", key="-OUT4-")],
		[sg.Text("")],
		[sg.Push(), sg.Text("Natureza Jurídica", font="16"), sg.Input(size=(60), font=" Any 16", key="-OUT5-")],
		[sg.Text("")],
		[sg.Push(), sg.Text("Município", font="16"), sg.Input(size=(60), font=" Any 16", key="-OUT6-")],
		[sg.Text("")],
		[sg.Push(), sg.Text("Estado", font="16"), sg.Input(size=(60), font=" Any 16", key="-OUT7-")],
		[sg.Text("")],
		[sg.Push(), sg.Text("Telefone", font="16"), sg.Input(size=(60), font=" Any 16", key="-OUT8-")],
		[sg.Text("")],
		[sg.Push(), sg.Text("Email", font="16"), sg.Input(size=(60), font=" Any 16", key="-OUT9-")],
		[sg.Text("")],
		[sg.Push(), sg.Button("Cadastrar Empresa", key="cadastrar", font=16), sg.Button("Visuzalizar Empresas Cadastradas", key="visualizar", font=16), sg.Push()],
		[sg.Text("", font="18",  key="saida")]
		
]
	window = sg.Window('Sistema de Consultar CNPJ', layout, size=(900,700), element_justification='center'  )

	while True:
		event, values = window.read()
		if event == sg.WINDOW_CLOSED or event == 'Sair':
			break
		elif event == 'Consultar':
			cnpj = values['-CNPJ-']
			r = requests.get("https://receitaws.com.br/v1/cnpj/{}".format(cnpj))
			empresa = r.json()
			
			nome = empresa["nome"]
			tipo = empresa["tipo"]
			situacao = empresa["situacao"]
			natureza = empresa["natureza_juridica"]
			municipio = empresa["municipio"]
			uf = empresa["uf"]
			telefone = empresa["telefone"]
			email = empresa["email"]
			
			window['-OUT1-'].update(nome)
			window['-OUT3-'].update(tipo)
			window['-OUT4-'].update(situacao)
			window['-OUT5-'].update(natureza)
			window['-OUT6-'].update(municipio)
			window['-OUT7-'].update(uf)
			window['-OUT8-'].update(telefone)
			window['-OUT9-'].update(email)
		elif event == "cadastrar":
			mycursor = mydb.cursor()
			sql = "INSERT INTO empresas3 (nome, tipo, situacao, natureza, municipio, uf, telefone, email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (nome, tipo, situacao, natureza, municipio, uf, telefone, email)
			mycursor.execute(sql, val)
			mydb.commit()
			window["saida"].update("Dados Cadastrados!")
		elif event == "Nova Consulta":
			window['-CNPJ-'].update("")
			window['-OUT1-'].update("")
			window['-OUT3-'].update("")
			window['-OUT4-'].update("")
			window['-OUT5-'].update("")
			window['-OUT6-'].update("")
			window['-OUT7-'].update("")
			window['-OUT8-'].update("")
			window['-OUT9-'].update("")
		elif event == "visualizar":
			window.close()
			empresas_cadastradas()	
index()

