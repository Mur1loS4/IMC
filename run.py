from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calcular_imc():
    imc = None
    classificacao = None
    obesidade = None

    if request.method == 'POST':
        altura = float(request.form['altura'])
        peso = float(request.form['peso'])
        imc = round(peso / (altura * altura), 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
            obesidade = "0"
        elif imc < 24.9:
            classificacao = "Normal"
            obesidade = "0"
        elif imc < 29.9:
            classificacao = "Sobrepeso"
            obesidade = "1"
        elif imc < 39.9:
            classificacao = "Obesidade"
            obesidade = "2"
        else:
            classificacao = "Obesidade grave"
            obesidade = "3"

    return render_template('index.html', imc=imc, classificacao=classificacao, obesidade=obesidade)

app.run(host='127.0.0.1', port=80, debug=True)