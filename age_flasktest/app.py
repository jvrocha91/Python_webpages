from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/dados", methods=['POST'])
def dados():
    nome= request.form['nome']
    idade= int(request.form['idade'])
    
    if idade >= 18 :
        faixa="e maior de idade"
        
    else:
        faixa="nao e maior de idade"    
    

    return render_template('results.html', nome=nome , faixa=faixa)
 

#colocar o site no ar
if __name__=="__main__":
    app.run(debug=True)
