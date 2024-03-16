from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PASSPASS'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():

    user = request.form.get('user')
    senha = request.form.get('senha')
    print(user)
    print(senha)

    return redirect('/')

if __name__ == '__main__':
    app.run(host="localhost", port="5000", debug=True)