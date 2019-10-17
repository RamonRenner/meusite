from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_) #erro estava com apenas 1 _
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///meusite.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(8), unique=True, nullable=False) # inconsistencia de tabs ou uso de espaco
	email = db.Column(db.String(200), unique=True, nullable=False)
	
	def _repr_(self): #erro estava com apenas 1 _
		return "<User %r>" % self.username

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/cadastro')
def cadastro():
	return render_template('cadastro.html')

@app.route('/denuncia')
def denuncia():
	return render_template('denuncia.html')
if _name_ == 'main': #erro estava com apenas 1 _
	app.run(debug=True)
