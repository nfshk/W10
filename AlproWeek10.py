#helloworld

from flask import Flask
from flask import render_template
import csv
import json

apphello = Flask(__name__)

@apphello.route("/")
def hello_world():
    return render_template('welcome.html')

@apphello.route("/alpro/")
def helloalpro():
    return "<h2>Agoritma Pemrograman</h2>"

@apphello.route('/templ/')
@apphello.route('/templ/<name>')
def templaterun(name=None):
    return render_template('templ.html', name=name)

@apphello.route('/CV')
def CV():
    return render_template('CV.html')

@apphello.route('/portofolio')
def portofolio():
    return render_template('portofolio.html')

@apphello.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    if request.method == 'POST':
        length = int(request.form['length'])
        fibonacci_sequence = generate_fibonacci(length)
        return render_template('fibonacci.html', length=length, sequence=fibonacci_sequence)
    return render_template('fiboInput.html')

def generate_fibonacci(length):
    # Fungsi untuk menghasilkan deret Fibonacci
    sequence = [1, 1]
    while len(sequence) < length:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence


@apphello.route('/csv_to_json')
def csv_to_json():
    csv_data = []
    with open('smartphones.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_data.append(row)
    return json.dumps(csv_data)

from flask import request

@apphello.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        submitted_data = {
            'nama': request.form['nama'],
            'nim': request.form['nim'],
            'fakultas': request.form['fakultas'],
            'prodi': request.form['prodi'],
            'angkatan': request.form['angkatan']
        }
        return render_template('submitted.html', data=submitted_data)
    return render_template('form.html')

@apphello.route('/biodata')
def biodata():
    return render_template('biodata.html')

@apphello.route('/movie')
def movie():
    return render_template('movie.html')

@apphello.route('/music')
def music():
    return render_template('music.html')