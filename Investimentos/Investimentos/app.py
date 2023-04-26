from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/calcular_poupanca", methods=['POST'])
def calcular_poupanca():
    escolha = int(request.form.get('escolha'))
    if escolha == 1:
        valor = float(request.form.get('valor'))
        polpansa = float(request.form.get('polpansa'))
        tempo = int(request.form.get('tempo'))
        resultado = []
        for x in range(tempo):
            valor += polpansa
            resultado.append(f"Mês {x + 1} - {valor:.2f} R$")
        return render_template('resultado.html', resultado=resultado)
    else:
        return "Escolha inválida"
    
    
@app.route("/calcular_juros", methods=['POST'])
def calcular_juros():
    escolha = int(request.form.get('escolha'))
    if escolha == 1:
        valor = float(request.form.get('valor'))
        juros = float(request.form.get('juros'))
        tempo = int(request.form.get('tempo'))
        resultado2 = []
        for x in range(tempo):
            valor+=valor*(juros/100)
            resultado2.append(f"Mês {x + 1} - {valor:.2f} R$")
        return render_template('resultado2.html', resultado2=resultado2)
    else:
        return "Escolha inválida"   
       
    

if __name__ == "__main__":
    app.run(debug=True)