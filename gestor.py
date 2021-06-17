import mysql.connector
from objects import user
from objects import ware_book
from objects import libro
from datetime import date
from datetime import datetime
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

	"""def get_Abrev(self):
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
			print("No se puede conectar a la base de datos")"""



class dayly_sales:
	def __init__(self):
		self.List1 = []
		self.List2 = []
		self.List3 = []

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
			self.disconnect_db()
			if id_ > 0:
				return (True,id_) 
			else:
				return (False,0)
		except:
			print("No se puede conectar a la base de datos")
			self.disconnect_db()
			return (False,0)
			
	def update_sales(self, cod_, cantidad):
		print(cod_)
		print(cantidad)
		self.connect_db()
		try:
			query = ("update genesisDB.ware_books set genesisDB.ware_books.cant_STC = genesisDB.ware_books.cant_STC - " + str(cantidad) + " where genesisDB.ware_books.cod_book = '" + str(cod_) + "';")
			self.cursor.execute(query)
			self.mydb.commit()
			self.disconnect_db()
			return True
		except:
			print("No se puede conectar a la base de datos")
			self.disconnect_db()
			return False


	def insert_currentDay(self):
		self.connect_db()
		try:
			query = ("insert into genesisDB.dayly_sales (date_) values ('" + str(date.today()) + " 00:00:00');")
			query1 = ("set @ID := (select genesisDB.dayly_sales.id from genesisDB.dayly_sales order by genesisDB.dayly_sales.id desc limit 1);")
			query2 = ("insert into genesisDB.salesDetails (id, id_sales, codBook, total) values (0, @ID, 'PST_1', 0.0);")
			self.cursor.execute(query)
			self.cursor.execute(query1)
			self.cursor.execute(query2)
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
			query = ("select date_, condition_, id from genesisDB.dayly_sales order by id desc limit 3;")
			self.cursor.execute(query)
			for (date_,condition_,id_) in self.cursor:
				dict_ = {"tab": self.changeNumber2Day(int(date_.weekday()),date_.strftime("%d"),condition_), "condition": str(condition_), "id": int(id_)}
				List_.append(dict_)
			self.disconnect_db()
			return List_
		except:
			print("No se puede conectar a la base de datos")
			return List_

	def change_state(self, id_, id_user = 0):
		self.connect_db()
		try:
			query = ("update genesisDB.dayly_sales set genesisDB.dayly_sales.condition_ = 'INACTIVO', genesisDB.dayly_sales.employeeID = " + str(id_user) + " where genesisDB.dayly_sales.id = " + str(id_) + ";")
			self.cursor.execute(query)
			self.mydb.commit()
			self.disconnect_db()
			return True
		except:
			print("No se puede conectar a la base de datos")
			self.disconnect_db()
			return False


	def getlastdaylyID(self, dayID): ## falta corejir esta parte
		id_ = 0
		self.connect_db()
		try:
			query = ("select id from genesisDB.salesDetails where genesisDB.salesDetails.id_sales = " + str(dayID) + " order by genesisDB.salesDetails.id asc limit 1")
			self.cursor.execute(query)
			for (param1) in self.cursor:
				if type(param1) is tuple:
					id_ = int(param1[0])
				else:
					id_ = int(param1)
			self.disconnect_db()
			if id_ >= 0:
				return (id_ + 1)
			else:
				return 1
		except:
			print("No se puede conectar a la base de datos")
			return 1
		


	def actualizarCajaChica(self, CajaChica, currentID_day):
		self.connect_db()
		try:
			query = ("update genesisDB.salesDetails set genesisDB.salesDetails.total = " + str(CajaChica) + " where genesisDB.salesDetails.id = 0 and genesisDB.salesDetails.id_sales = " + str(currentID_day) + ";")
			self.cursor.execute(query)
			self.mydb.commit()
			self.disconnect_db()
			return True
		except:
			print("No se puede conectar a la base de datos")
			self.disconnect_db()
			return False
			


	def registrarVenta(self, dayID, userID, bookCOD, cant, credit_, receipt_, PU, title_):
		total = float(PU) * cant
		if credit_ == True:
			credit__ = 1
		else:
			credit__ = 0

		if receipt_ == True:
			receipt__ = 1
		else:
			receipt__ = 0

		self.connect_db()
		try:
			query = ("set @IV := (select genesisDB.salesDetails.id from genesisDB.salesDetails where genesisDB.salesDetails.id_sales = " + str(dayID) + " order by genesisDB.salesDetails.id desc limit 1) + 1;")
			query1 = ("insert into genesisDB.salesDetails (id,id_sales,time_,userID,codBook,cant,credit_,receipt,total) values (@IV," + str(dayID) + ",'" + datetime.now().strftime("%H:%M:%S") + "'," + str(userID) + ",'" + str(bookCOD)+ "'," + str(cant) + "," + str(credit_) + "," + str(receipt_) + "," + str(total) +");")
			self.cursor.execute(query)
			self.cursor.execute(query1)
			self.mydb.commit()
			self.disconnect_db()
			return True
		except:
			print("No se puede conectar a la base de datos")
			return False


	def currentSales_(self, id):
		self.List1.clear()
		self.connect_db()
		query = ("select genesisDB.salesDetails.*, genesisDB.books.name from genesisDB.salesDetails inner join genesisDB.books on genesisDB.salesDetails.codBook = genesisDB.books.cod where genesisDB.salesDetails.id_sales = " + str(id) + ";")
		try:
			self.cursor.execute(query)
			for (param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11) in self.cursor:
				if int(param2) != 0:
					pu = float(param10) / float(param7)
					dict_ = {'id': int(param2),'hora': str(param4),'user': str(param5),'codBook': str(param6),'metodo': bool(param8),'recibo': bool(param9),'titulo':str(param11),'cant':str(param7),'pu': str(pu), 'pv': str(param10)}
					self.List1.append(dict_)
				else:
					dict_ = {'id': int(param2),'hora': '00:00:00','user': '0','codBook': 'no tiene','metodo': False,'recibo': False,'titulo':'no tiene','cant': '0','pu': '0', 'pv': str(param10)}
					self.List1.append(dict_)
			self.disconnect_db()
		except:
			print("No se puede conectar a genesisDB")
			self.disconnect_db()


	def getLastThree(self):
		self.List1.clear()
		self.List2.clear()
		self.List3.clear()
		indexList = []
		self.connect_db()
		try:
			query = ("select id from genesisDB.dayly_sales order by genesisDB.dayly_sales.id desc limit 3;")
			self.cursor.execute(query)
			for (id) in self.cursor:
				if type(id) is tuple:
					indexList.append(int(id[0]))
				else:
					indexList.append(int(id))
			self.disconnect_db()
		except:
			print("No se puede conectar a la base de datos")
			self.disconnect_db()

		if len(indexList) > 0:
			self.currentSales(self.List1,indexList[0])
			self.currentSales(self.List2,indexList[1])
			self.currentSales(self.List3,indexList[2])
		else:
			print("No se puede cargar index´s")

	def getLastTwo(self):
		self.List1.clear()
		self.List2.clear()
		self.List3.clear()
		indexList = []
		self.connect_db()
		try:
			query = ("select id from genesisDB.dayly_sales order by genesisDB.dayly_sales.id desc limit 3;")
			self.cursor.execute(query)
			for (id) in self.cursor:
				if type(id) is tuple:
					indexList.append(int(id[0]))
				else:
					indexList.append(int(id))
			self.disconnect_db()
		except:
			print("No se puede conectar a la base de datos")
			self.disconnect_db()

		if len(indexList) > 0:
			self.currentSales(self.List2,indexList[1])
			self.currentSales(self.List3,indexList[2])
		else:
			print("No se puede cargar index´s")



	def currentSales(self, List_, id):
		self.connect_db()
		query = ("select genesisDB.salesDetails.*, genesisDB.books.name from genesisDB.salesDetails inner join genesisDB.books on genesisDB.salesDetails.codBook = genesisDB.books.cod where id_sales = " + str(id) + ";")
		try:
			self.cursor.execute(query)
			for (param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11) in self.cursor:
				if int(param2) != 0:
					pu = float(param10) / float(param7)
					dict_ = {'id': int(param2),'hora': str(param4),'user': str(param5),'codBook': str(param6),'metodo': bool(param8),'recibo': bool(param9),'titulo':str(param11),'cant':str(param7),'pu': str(pu), 'pv': str(param10)}
					List_.append(dict_)
				elif int(param2) == 0:
					dict_ = {'id': int(param2),'hora': '00:00:00','user': '0','codBook': 'no tiene','metodo': False,'recibo': False,'titulo':'no tiene','cant': '0','pu': '0', 'pv': str(param10)}
					List_.append(dict_)
			self.disconnect_db()
		except:
			print("No se puede conectar a genesisDB")
			self.disconnect_db()


		
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
				#print(join_line)
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





