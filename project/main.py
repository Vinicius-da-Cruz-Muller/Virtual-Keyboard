from flask import Flask, render_template, redirect, request, flash
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PASSPASS'

pool = mysql.connector.pooling.MySQLConnectionPool(
    host="localhost",
    user="root",
    password="Semestre202301",
    database="users",
    pool_size=32,
)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    cont = 0
    user = request.form.get('user')
    senha = request.form.get('senha')
    
    mydb = pool.get_connection()

    if mydb.is_connected():
        print('conectado')
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM usuario;')
        usuariosBD = cursor.fetchall()

        for usuario in usuariosBD:
            cont += 1
            usuarioUser = str(usuario[1])
            usuarioSenha = str(usuario[2])

            if usuarioUser == user and usuarioSenha == senha:
                return redirect('/usuarios')
            
            if cont >= len(usuariosBD):
                return redirect('/')
            
        cursor.close()
        mydb.close()
    
    return redirect('/')

@app.route('/usuarios')
def usuarios():
    return render_template("usuarios.html")

@app.route('/path')
def path():
    return render_template("cadastrar.html")

@app.route('/show_login_form')
def show_login_form():
    return render_template('login.html')


@app.route('/cadastrarUsuario', methods = ['POST'])
def cadastrarUsuario():
    mydb = pool.get_connection()
    user = request.form.get('user')
    senha = request.form.get('senha')
    cursor = mydb.cursor()
    cursor.execute(f"INSERT INTO usuario VALUES (default, '{user}', '{senha}');")
    mydb.commit()

    if cursor.rowcount > 0:
        flash("Usuário cadastrado com sucesso!")
        if mydb.is_connected():
            mydb.close()
        return redirect('/show_login_form')
    else:
        flash("Erro ao cadastrar usuário")
        return redirect('/path')

    

if __name__ == '__main__':
    app.run(host="localhost", port="5000", debug=True, use_reloader = "False")