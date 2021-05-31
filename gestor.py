import mysql.connector
from objects import user
from objects import ware_book
from objects import libro
from datetime import date
import socket

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
				return True, user(i.id ,i.user ,i.passwd, i.level)
		return False, user()


class wares:
	def __init__(self):
		hostname = socket.gethostname()
		self.localIP = str(socket.gethostbyname(hostname))
		self.dict_ = {'id': 0 ,'abrev': "NO SE ENCUENTRA UBICACION",'direccion': "",'telefono': "",'ip': ""}

	def connect_db(self):
		self.mydb = mysql.connector.connect(host = "mysql-28407-0.cloudclusters.net", user="admin01", passwd="alayza2213", port="28416")
		self.cursor = self.mydb.cursor()

	def disconnect_db(self):
		self.cursor.close()
		self.mydb.close()

	def get_Abrev(self):
		self.connect_db()
		try:
			query = ("select * from genesisDB.wares where ip = '" + self.localIP + "';")
			self.cursor.execute(query)
			for (id, abrev, direccion, telefono, ip) in self.cursor:
				self.dict_['id'] = int(id)
				self.dict_['abrev'] = str(abrev)
				self.dict_['direccion'] = str(direccion)
				self.dict_['telefono'] = str(telefono)
				self.dict_['ip'] = str(ip)
			return self.dict_['abrev']
		except:
			return self.dict_['abrev']
			print("No se puede conectar a la base de datos")



class dayly_sales:
	def __init__(self):
		self.currentDay = str(date.today())

	def connect_db(self):
		self.mydb = mysql.connector.connect(host = "mysql-28407-0.cloudclusters.net", user="admin01", passwd="alayza2213", port="28416")
		self.cursor = self.mydb.cursor()

	def disconnect_db(self):
		self.cursor.close()
		self.mydb.close()

	def verify_day(self):
		self.connect_db()
		id_ = 0
		try:
			query = ("select id from genesisDB.dayly_sales where date_ = '" + str(date.today()) + " 00:00:00';")
			self.cursor.execute(query)
			for (id) in self.cursor:
				if type(id) is tuple:
					id_ = int(id[0])
				else:
					id_ = int(id)
			if id_ > 0:
				return True 
			else:
				return False
		except:
			return False
			print("No se puede conectar a la base de datos")

	def insert_currentDay(self):
		self.connect_db()
		try:
			query = ("insert into genesisDB.dayly_sales (date_) values ('" + str(date.today()) + " 00:00:00');")
			self.cursor.execute(query)
			self.mydb.commit()
			self.disconnect_db()
			return True
		except:
			print("No se puede conectar a la base de datos")
			return False
			

	def changeNumber2Day(self, val = 7, day = "", active_ = "INACTIVO"):
		if val == 0:
			return "Lunes" + day + " - ["+ active_ + "]"
		elif val == 1:
			return "Martes " + day + " - ["+ active_ + "]"
		elif val == 2:
			return "Miercoles " + day + " - ["+ active_ + "]"
		elif val == 3:
			return "Jueves " + day + " - ["+ active_ + "]"
		elif val == 4:
			return "Viernes " + day + " - ["+ active_ + "]"
		elif val == 5:
			return "Sabado " + day + " - ["+ active_ + "]"
		elif val == 6:
			return "Domingo " + day + " - ["+ active_ + "]"
		else:
			return "Error"

	def get_lastThreedays(self):
		List_ = []
		self.connect_db()
		try:
			query = ("select date_, condition_ from genesisDB.dayly_sales order by id desc limit 3;")
			self.cursor.execute(query)
			for (date_,condition_) in self.cursor:
				dict_ = {"tab": self.changeNumber2Day(int(date_.weekday()),date_.strftime("%d"),condition_), 'condition': str(condition_)}
				List_.append(dict_)
			self.disconnect_db()
			return List_
		except:
			print("No se puede conectar a la base de datos")
			return List_
			



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
				if(i.book.cod == str.upper(patron)):
					self.temp_list.append(i)
			return len(self.temp_list)		
		elif criterio == "isbn":
			for i in self.ware_list:
				if(i.book.isbn == patron):
					self.temp_list.append(i)
			return len(self.temp_list)
		elif criterio == "nombre":
			for i in self.ware_list:
				if(i.book.name.find(str.upper(patron)) >= 0):
					self.temp_list.append(i)
			return len(self.temp_list)
		
		elif criterio == "autor":
			for i in self.ware_list:
				if(i.book.autor.find(str.upper(patron)) >= 0):
					self.temp_list.append(i)
			return len(self.temp_list)

		return 0


	def update_quantity(self, list_, criterio):
		len_ = len(list_)  
		if len_ > 1:
			self.connect_db()
			try:
				join_line = "update "
				for i in range(len_):
					join_line = join_line + "genesisDB.ware_books " + "t" + str(i+1) + " join "
				size = len(join_line)
				join_line = join_line[:size-5]
				join_line = join_line + "on "
				for j in range(len_):
					join_line = join_line + "t" + str(j+1) + ".cod_book= " + "'" + list_[j]["cod"] + "'" + " and " 
				size = len(join_line)
				join_line = join_line[:size-4]
				
				join_line = join_line + "set "
				for k in range(len_):
					#join_line = join_line + "t" + str(k+1) + ".cant_SNTG= " + "t" + str(k+1) + ".cant_SNTG" + criterio + str(list_[k]["cantidad"]) + ", " + "t" + str(k+1) + ".ubic_STNG= 'LITERATURA - HISTORIA', "
					#join_line = join_line + "t" + str(k+1) + ".cant_SNTG= " + "t" + str(k+1) + ".cant_SNTG" + criterio + str(list_[k]["cantidad"]) + ", "
					join_line = join_line + "t" + str(k+1) + ".cant_STC= " + "t" + str(k+1) + ".cant_STC" + criterio + str(list_[k]["cantidad"]) + ", "
				size = len(join_line)
				join_line = join_line[:size-2]
				join_line = (join_line + ";")
				print(join_line)
				self.cursor.execute(join_line)
				self.mydb.commit()
				self.disconnect_db()
				return True
			except:
				print("No se pudo conectar a la DB")
				self.disconnect_db()		
				return False
		elif len_ == 1:
			self.connect_db()
			try:
				#query = ("update genesisDB.ware_books set cant_SNTG = cant_SNTG" + criterio + str(list_[0]["cantidad"]) + ", ubic_STNG= 'LITERATURA - HISTORIA' where cod_book = '" + list_[0]["cod"] + "';")
				#query = ("update genesisDB.ware_books set cant_SNTG = cant_SNTG" + criterio + str(list_[0]["cantidad"]) + " where cod_book = '" + list_[0]["cod"] + "';")
				query = ("update genesisDB.ware_books set cant_STC = cant_STC" + criterio + str(list_[0]["cantidad"]) + " where cod_book = '" + list_[0]["cod"] + "';")	
				self.cursor.execute(query)
				self.mydb.commit()
				self.disconnect_db()
				return True
			except:
				print("No se pudo conectar a la DB")
				self.disconnect_db()		
				return False
		else:
			print("la tabla se encuentra vacia")

				

	def load_mainlist(self):
		bookList = []
		wareList = []
		self.ware_list.clear()
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
			for (id, cod_book, cant_STC, cant_SNTG, ubic_STC, ubic_STNG,consig_STATE) in self.cursor:
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





