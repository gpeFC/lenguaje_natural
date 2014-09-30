import re

entrada_correos = ["aclopez@estudiants.urv.cat", 
				  "user.25(at)ccg.unam.mx", 
				  "soy_spam at upemor  dot edu", 
				  """<script type="text/javascript">obfuscate('gmail.com','aclopez')</script>"""]

entrada_telefonos = ["+52-777-563-1295", "(777) 563-1295", "(+52)777-563-1295", """<a href="contact.html">TEL</a> +52&thinsp;777&thinsp;563&thinsp;1295"""]

patron = r"[a-zA-Z0-9(\<script)]+[\.{1}[a-zA-Z0-9]+]*[@(\(at\))at]*"

salida_correos = []
salida_telefonos = []

print
print "Correos/Entrada:"
for correo in entrada_correos: print "\t", correo
print
for cadena in entrada_correos:
	if re.match(patron, cadena):
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
print 
