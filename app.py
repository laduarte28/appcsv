from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

CSV_FILE = "users.csv"

#Função pra ler usuários .CSV

def read_users ():
    if not os.path.exists (CSV_FILE):
        return []
    with open (CSV_FILE, newline = "", encoding = 'UTF-8') as csvfile:
        reader = csv.reader(csvfile)
        return list (reader)

#Função pra add novo usuário
def add_user(name, email):
    with open (CSV_FILE, mode = "a", newline = '', encoding = 'UTF-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email])

#rota de inicio
@app.route('/')
def home():
    users = read_users()
    return render_template('home.html', users=users)

@app.route('/about')
def about():
    return render_template('about.html')


#Rota para formulário de registro

@app.route('/register', methods = ['GET', 'POST'])
def register ():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        add_user(name, email)
        return redirect(url_for('home'))
    return render_template ('form.html')

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
