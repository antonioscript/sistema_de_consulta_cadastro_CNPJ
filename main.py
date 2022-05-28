import PySimpleGUI as sg
import requests
sg.theme("DarkTeal12")

def index():	
	layout = [
		[sg.Text("Digite um CNPJ: ", font=" Helvetica 20")],
		[sg.Input(key = '-CNPJ-', size=20, font=" Any 16")],
		[sg.Button("Consultar", font="16"), sg.Button("Nova Consulta", font="16"), sg.Button("Sair", font="16")],
		[sg.Text("")],
		[sg.Text("Nome da Empresa", font="16"), sg.Input(size=(50), font=" Any 16", key="-OUT1-")],
		[sg.Text("")],
		[sg.Text("Nome Fantasia      ", font="16"), sg.Input(size=(50), font=" Any 16", key="-OUT2-")],
		[sg.Text("")],
		[sg.Text("Tipo                         ", font="16"), sg.Input(size=(50), font=" Any 16", key="-OUT3-")],
		[sg.Text("")],
		[sg.Text("Situação                 ", font="16"), sg.Input(size=(50), font=" Any 16", key="-OUT4-")],
		[sg.Text("")],
		[sg.Text("Natureza Jurídica  ", font="16"), sg.Input(size=(50), font=" Any 16", key="-OUT5-")],
		[sg.Text("")],
		[sg.Text("Município                ", font="16"), sg.Input(size=(50), font=" Any 16", key="-OUT6-")],
		[sg.Text("")],
		[sg.Text("Estado                    ", font="16"), sg.Input(size=(50), font=" Any 16", key="-OUT7-")],
		[sg.Text("")],
		[sg.Text("Telefone                 ", font="16"), sg.Input(size=(50), font=" Any 16", key="-OUT8-")],
		[sg.Text("")],
		[sg.Text("Email                      ", font="16"), sg.Input(size=(50), font=" Any 16", key="-OUT9-")]
]
	window = sg.Window('Sistema de Consultar CNPJ', layout, size=(800,700), element_justification='center'  )

	while True:
		event, values = window.read()
		if event == sg.WINDOW_CLOSED or event == 'Sair':
			break
		elif event == 'Consultar':
			cnpj = values['-CNPJ-']
			r = requests.get("https://receitaws.com.br/v1/cnpj/{}".format(cnpj))
			empresa = r.json()
			window['-OUT1-'].update(empresa["nome"])
			window['-OUT2-'].update(empresa["fantasia"])
			window['-OUT3-'].update(empresa["tipo"])
			window['-OUT4-'].update(empresa["situacao"])
			window['-OUT5-'].update(empresa["natureza_juridica"])
			window['-OUT6-'].update(empresa["municipio"])
			window['-OUT7-'].update(empresa["uf"])
			window['-OUT8-'].update(empresa["telefone"])
			window['-OUT9-'].update(empresa["email"])
		elif event == "Nova Consulta":
			window['-CNPJ-'].update("")
			window['-OUT1-'].update("")
			window['-OUT2-'].update("")
			window['-OUT3-'].update("")
			window['-OUT4-'].update("")
			window['-OUT5-'].update("")
			window['-OUT6-'].update("")
			window['-OUT7-'].update("")
			window['-OUT8-'].update("")
			window['-OUT9-'].update("")
index()

