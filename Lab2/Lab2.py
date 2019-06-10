#Vitoria Holanda 385227
#Lucas Noleto 390192

import urllib 
import requests
import json
import urllib.request
import urllib.parse

def quest1():
	print("Questão 1:\n")
	sites = ('http://netflix.com',
		'http://facebook.com',
		'http://lua.creactive.com.br',
		'http://live.com',
		'http://lesc.ufc.br',
		'http://g1.globo.com',
		'http://stackoverflow.com',
		'http://nytimes.com',
		'http://gti.ufc.br',
		'https://github.com/')

#.info obtem a resposta do  item a) e o .code o item b)
	for site in sites:
		try:
			html = urllib.request.urlopen(site)
			print("Endereço:",site,"\n","Codigo HTTP do site:",html.code,"\n""Meta-info logo abaixo ","\n",html.info(),"\n")
		except urllib.error.HTTPError as e:
			print('Error code: ', e.code)
		except urllib.error.URLError as e:
			print('Reason: ', e.reason)
#Como exemplo de metainformação, temos "Content-Type", essa informação fala sobre o tipo de conteudo exibido.
#text/html por exemplo, informa que se trata de um html em texto 		
#
#Nesse caso os codigos são iguais.São uma resposta de status do HTTP 
#Codigo 200 - O request da pagina HTTP foi um sucesso

#Questao 2a)
#Acessamos o site vicep e utilizamos o vetor CEPs para pesquisar os respectivos logradouros. Então utilizamos o json para printar as informações desejadas.		
def quest2():
	print("Questão 2:\n")
	CEPs = ('60810025','60831600','60721340','60874230')

	for CEP in CEPs:
		try:
			url = urllib.request.urlopen('http://viacep.com.br/ws/'+CEP+'/json')
			data = json.load(url)
			print('CEP:', CEP,"->", 'Logradouro:',data['logradouro'])
		except urllib.error.HTTPError as e:
			print('Error code: ', e.code)
		except urllib.error.URLError as e:
			print('Reason: ', e.reason)
	

#Questão 2b
#Quando tentamos acessar o site do google pelo python essa informção aparece no header e nosso acesso não é permitido.
def quest2b():		
	print("Questão 2.b:\n")
	try:
		x = urllib.request.urlopen('https://google.com/search?q=PALAVRA')

		print(x.read())
	except Exception as e:
		print(str(e))	
#Ao alterarmos nosso header estamos de certa forma nos camuflando para o site e então conseguimos acessar normalmente.		
	try:
 		url = 'https://www.google.com/search?q=PALAVRA'

	 	headers = {}
	 	headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
	 	req = urllib.request.Request(url, headers = headers)
	 	resp=urllib.request.urlopen(req)
 		respData = resp.info()
 		print(respData)

	except Exception as e:
	 	print(str(e))
	
	 	
#quest1()
#quest2()
quest2b()
	

