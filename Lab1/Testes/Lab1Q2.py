import socket
import requests

sites = ['netflix.com','facebook.com','google.com','live.com','lesc.ufc.br','globoesporte.com','stackoverflow.com','narutoproject.com','gti.ufc.br','thepiratebay.org']


base = 'http://freegeoip.net/json/'

#'google.com'/'web.telegram.com'/'live.com'/'facebook.com'/'youtube.com'
#'netflix.com'/'lua.creative.com'/'nytimes.com'/'g1.globo.com'/'filmow.com'
x = 1
for i in range (len(sites)):
	response = requests.get(base + sites[i] )
	dados = response.json()
	print(x,")", "Site:",sites[i], " Lugar: ", dados['country_name'])
	x = x +1
