# Lucas Noleto Paiva 390192		
# Vitoria Holanda Gonçalves 385227

# Importando Bibliotecas que serão utilizadas.
import socket 
import requests

# Recebendo o hostname e o IP da máquina que estamos utilizando.
r = socket.gethostname()
ip = socket.gethostbyname(r)


print ("---Questão 1---")
print ("Nome do computador: ", r)
print ("IP do computador: ", ip)

# Percorrendo ports de 0 a 9999 e verificando se existem os protocolos TCP e UDP.
for  p in range(10000):
# Tratamento dos erros.
	try:
		tcp = socket.getservbyport(p, 'tcp')
	except OSError:
		tcp = None
	try:
		udp = socket.getservbyport(p, 'udp')
	except OSError:
		udp = None
	
# Exibição dos resultados dos protocolos.

	# if tcp and udp is not None: 
	# 	print(p, "Porta UDP e TCP")
	# if tcp is None:
	# 	print(p, "Porta não possui TCP")
	# if tcp is None:
	# 	print(p, "Porta não possui UDP")
	if tcp or udp is None:
	 		print (p, "Não possui TCP/UDP")
	if tcp is not None:	
			print(p,tcp, "TCP")		
	if udp is not None:
	 		print (p,udp,"UDP")

print ("\n")
print ("---Questão 2---")

# Criação de um vetor contendo os sites que terão seus IPs avaliados.

sites = ['netflix.com','facebook.com','lua.creactive.com.br','live.com','lesc.ufc.br','g1.globo.com','stackoverflow.com','nytimes.com','gti.ufc.br','thepiratebay.org']

base = 'http://freegeoip.net/json/'

# Percorrendo o vetor sites e exibindo o IP e local.
x = 1
for i in range (len(sites)):
	ip_do_site = socket.gethostbyname(sites[i])
	response = requests.get(base + sites[i] )
	dados = response.json()
	print(x,")", "Site:",sites[i],"-IP: ",ip_do_site,"-Lugar: ", dados['country_name'])
	x = x +1


		




