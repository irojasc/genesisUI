import mysql.connector
from objects import user
from objects import ware_book
from objects import libro

class users_gestor:
	def __init__(self):
		self.users = []
		try:
			self.mydb = mysql.connector.connect(host = "mysql-28407-0.cloudclusters.net", user="admin01", passwd="alayza2213", port="28416")
			self.cursor = self.mydb.cursor()
		except:
			print("No se puede conectar a genesisDB")
			self.cursor.close()
			self.mydb.close()

	def disconnectDB(self):
		self.cursor.close()
		self.mydb.close()

	def fill_users(self):
		query = ("use genesisDB;")
		query1 = ("select * from users;")
		try:
			self.cursor.execute(query)
			self.cursor.execute(query1)

			for (param1, param2, param3, param4) in self.cursor:
				objUser = user(param1,param2,param3,param4)
				self.users.append(objUser)

			self.disconnectDB()
		
		except:
			print("No se puede conectar a genesisDB")
			self.disconnectDB()

	def check_login(self, name, passwd):
		for i in self.users:
			if i.user == name and i.passwd == passwd:
				return True, user(i.id ,i.user)
		return False, user()



class ware_gestor:
	
	def connect_db(self):
		self.mydb = mysql.connector.connect(host = "mysql-28407-0.cloudclusters.net", user="admin01", passwd="alayza2213", port="28416")
		self.cursor = self.mydb.cursor()

	def disconnect_db(self):
		self.cursor.close()
		self.mydb.close()

	def None_Type(self, val):
		myList = []
		for i in range(len(val)):
			if val[i] is None:
				myList.append("")
			else:
				myList.append(val[i])
		if len(val) == 10:
			tup = (myList[0],myList[1],myList[2],myList[3],myList[4],myList[5],myList[6],myList[7],myList[8],myList[9])
		else:
			tup = () 
		return tup

	
	def buscar(self, criterio, patron):
		self.temp_list.clear()
		if criterio == "cod":
			for i in self.ware_list:
				if(i.book.cod == patron):
					self.temp_list.append(i)
			return len(self.temp_list)		
		elif criterio == "isbn":
			for i in self.ware_list:
				if(i.book.isbn == patron):
					self.temp_list.append(i)
			return len(self.temp_list)
		elif criterio == "nombre":
			return len(self.temp_list)
		return 0


	def load_mainlist(self):
		bookList = []
		wareList = []
		self.connect_db()
		try:
			query = ("select * from genesisDB.books;")
			query1 = ("select * from genesisDB.ware_books;")

			# -----------  carga data de libros  -----------
			self.cursor.execute(query)
			for (cod, isbn, name, autor, editorial, supplierID, genderID, pc, pv, dsct) in self.cursor:
				values = self.None_Type((cod, isbn, name, autor, editorial, supplierID, genderID, pc, pv, dsct))
				## 0 = cod, 1 = isbn, 2 = name, 3 = autor, 4 = editorial, 5 = supplierID, 6 = genderID, 7 = pc, 8 = pv , 9 = dsct
				objLibro = libro(str(values[0]),str(values[1]),str(values[2]),str(values[3]),str(values[4]),
					str(values[5]),str(values[6]),str(values[7]),float(values[8]))
				bookList.append(objLibro)

			# -----------  carga data de almacen  -----------
			self.cursor.execute(query1)
			for (id, cod_book, cant_STC, cant_SNTG, ubic_STC, ubic_STNG) in self.cursor:
				objWare = ware_book(str(cod_book),[int(cant_STC),int(cant_SNTG)],[str(ubic_STC),str(ubic_STNG)])
				wareList.append(objWare)

			# -----------  cerrar conexion db  -----------
			self.disconnect_db()	
			
			# -----------  match libro with ware  -----------
			for i in range(len(wareList)):
				for j in range(len(bookList)):
					if wareList[i].book == bookList[j].cod:
						wareList[i].book = bookList[j]

			# -----------  eliminar los codigos de almacen que no tienen objeto libro  -----------
			for i in wareList:
				if(type(i.book) != str):
					self.ware_list.append(i)
		except:
			print("No se pudo conectar a la DB")
			self.disconnect_db()


	def __init__(self):
		self.ware_list = []
		self.temp_list = []





