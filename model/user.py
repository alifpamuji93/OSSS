from flask.ext.sqlalchemy import SqlAlchemy

db = oss

class user(db.model):
	"""docstring for user"""
	__tablename__ = 'user'

	email = db.Column(db.String., primary_key=True)
	password = db.Column(db.String)
	authecticated = db.Column(db.Boolean, default=False)

	def is_activate(self):
		"""True, untuk semu uset yang telah aktif"""
		return True

	def get_id(self):
		"""gunakan email sebagai idetintas masuk user ke dalam aplikasi"""
		return self.email

	def is_authecticated(self):
		"""Return true jika telah terauthenticasi"""
		return self.authecticated

	def is_anonymous(self):
		""" return false jika user belum terauthenticasi"""
		return False
		