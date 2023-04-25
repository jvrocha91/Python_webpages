from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#criar a 1 pagina do site 
#route-> link
#funcao -> O que voce que exibir na pagina

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/menu", methods=['POST'])
def menu():
    choice = int(request.form.get('option', 0))

    if choice == 1:
        return redirect(url_for('option1'))
    elif choice == 2:
        return redirect(url_for('option2'))
    else:
        return redirect(url_for('index'))
    
@app.route('/option1')
def option1():
    return "Você escolheu a opção 1"

@app.route('/option2')
def option2():
    return "Você escolheu a opção 2"   
    
 

#colocar o site no ar
if __name__=="__main__":
    app.run(debug=True)