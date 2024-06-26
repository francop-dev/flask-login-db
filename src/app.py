from flask import Flask, render_template, url_for, redirect, request,flash
from flask_mysqldb import MySQL
from flask_wtf import CSRFProtect
from config import config
from flask_login import LoginManager,login_user,logout_user,login_required
#models
from models.ModelUser import ModelUser

#entities:
from models.entities.User import User

app =Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
       # print(request.form['email'])
       # print(request.form['password'])
       user= User(0,request.form['email'],request.form['password'])
       logged_user=ModelUser.login(db,user)
       if logged_user!=None:
           if logged_user.password:
               login_user(logged_user)
               return redirect(url_for('home'))
           else:
               flash('invalid password...')   
               return render_template('auth/login.html')
       else:
           flash('user not found...')   
           return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/protected')
@login_required
def protected():
    return "<h1>esta es una vista protegida, solo para usuarios logueados.</h1>"

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Pagina no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()
    

    