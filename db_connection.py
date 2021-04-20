import mysql.connector

mydb = mysql.connector.connect(host = "mysql-28407-0.cloudclusters.net", user="admin02", passwd="alayza2213", port="28416")
cursor = mydb.cursor()

query = ("select * from users;")
query_1 = ("use genesisDB;")

try:
	cursor.execute(query_1)
	cursor.execute(query)

	for (param1, param2, param3, param4) in cursor:
		print("codigo:{}, nombre:{}, contraseña:{}, level:{}.".format(type(param1), type(param2), type(param3), type(param4)))

	cursor.close()
	mydb.close()
except:
	print("An exception ocurred")
	cursor.close(
	mydb.close()