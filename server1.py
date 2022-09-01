from flask import Flask
app = Flask(__name__)

#1
@app.route('/')          
def hola_mundo():
    return '¡Hola Mundo!'


#2
@app.route('/dojo')
def dojo():
    return "Dojo!"

#3
@app.route('/say/<name>')
def say(name):
    print(name)
    return "Hola, " + name

#4
@app.route('/repeat/<int:num>/<string:text>')
def repeat(num, text):
    return f"{text * num}"











# Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos (PISTA: int() puede ser útil Por ejemplo, int("35") devuelve 35):
#localhost:5000/repeat/35/hello: haz que diga "hola" 35 veces
#localhost:5000/repeat/80/bye: haz que diga "adiós" 80 veces
#localhost:5000/repeat/99/dogs: haz que diga "perros" 99 veces






if __name__=="__main__":
    app.run(debug=True)
