"""
Emanuel GP
30/10/2014
FC UAEM
"""

import re

entrada_correos = ["aclopez@estudiants.urv.cat", 
				  "user.25(at)ccg.unam.mx", 
				  "soy_spam at upemor  dot edu", 
				  """<script type="text/javascript">obfuscate('gmail.com','aclopez')</script>"""]

entrada_telefonos = ["+52-777-563-1295", 
					"(777) 563-1295", 
					"(+52)777-563-1295", 
					"""<a href="contact.html">TEL</a> +52&thinsp;777&thinsp;563&thinsp;1295"""]

patron_telefono = r".*\d{3}.*\d{3}.*\d{4}"
patron_correo = r"[a-zA-Z0-9(\<script)]+[\.{1}[a-zA-Z0-9]+]*[@(\(at\))at]*"

patron = re.compile(r"\d{3}\d{3}\d{4}", re.I)
salida_correos = []

print "Telefonos/Entrada:"
for telefono in entrada_telefonos: print "\t", telefono
print
print "Telefonos/Salida:"
for cadena in entrada_telefonos:
	lista =  re.findall(r"\d{3,4}", cadena)
	telefono = ""
	for i in range(len(lista)):
		if i < len(lista)-1:
			telefono += lista[i]
			telefono += "-"
		else:
			telefono += lista[i]
	print "\t", telefono

print "\n"
print "Correos/Entrada:"
for correo in entrada_correos: print "\t", correo
for cadena in entrada_correos:
	if re.match(patron_correo, cadena):
		salida_correos.append(cadena)
print 
print "Correos/Salida:"
for cadena in salida_correos:
	if re.match(r"[a-zA-Z0-9]+[\.{1}a-zA-Z0-9]*@{1}([a-zA-Z0-9]+[\.{1}a-zA-Z0-9])+", cadena):
		print "\t", cadena
	elif cadena.find("(at)") != -1:
		print "\t", cadena.replace("(at)", "@")
	elif cadena.find("script") != -1:
		nueva = ""
		for index in range(len(cadena)):
			if cadena[index] == "(":
				while True:
					nueva += cadena[index]
					if cadena[index] == ")":
						break
					index += 1
				break
		cadena = ""
		for letra in nueva:
			if letra!='"' and letra!="'" and letra!="(" and letra!=")":
				cadena += letra
		lista = cadena.split(",")
		cadena = lista[1] + "@" + lista[0]
		print "\t", cadena
	elif cadena.find(" ") != -1:
		nueva = ""
		lista = cadena.split(" ")
		for token in lista:
			if token == "at":
				nueva += "@"
			elif token == "dot":
				nueva += "."
			else:
				nueva += token
		print "\t", nueva

