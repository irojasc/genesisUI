class user:
	def __init__(self, id = 0, user = "", passwd = "", level = ""):
		self.id = id
		self.user = user
		self.passwd = passwd
		self.level = level

class libro:
	def __init__(self, cod, isbn, name, autor, editorial, supplierID, genderID, Pc, Pv):
		self.cod = cod
		self.isbn = isbn
		self.name = name
		self.autor = autor 
		self.editorial = editorial
		self.supplierID = supplierID
		self.genderID = genderID
		self.Pc = Pc
		self.Pv = Pv

class supplier:
	def __init__(self, id, name, admin, phone, direction, mail):
		self.id = id
		self.name = name
		self.register = register
		self.admin = admin
		self.phone = phone
		self.direction = direction
		self.mail = mail

class gender:
	def __init__(self, id, name):
		self.id = id
		self.name = name

class movement_detail:
	def __init__(self, id, userID, books_IDs, depart_ID, depart_date, arrival_ID, arrival_date, cond = [False,False]):
		self.id = id
		self.userID = userID
		self.books_IDs = books_IDs
		self.depart_ID = depart_ID
		self.depart_date = depart_date
		self.arrival_ID = arrival_ID
		self.arrival_date = arrival_date
		self.cond = cond

class daily_sale:
	def __init__(self, id, date, books_IDs = [] , total_ = 0):
		self.id = id
		self.books_IDs = books_IDs
		self.date = date
		self.total_ = total_

class main_stock:
	def __init__(self, book, almacen_quantity = []):
		self.book = book
		self.almacen_quantity = almacen_quantity





