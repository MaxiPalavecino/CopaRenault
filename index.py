from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/deportes')
def deportes():
    return render_template('deportes.html')

@app.route('/tablon')
def tablon():
    return render_template('tablon.html')

@app.route('/calendario')
def calendario():
    return render_template('calendario.html')

@app.route('/precios')
def precios():
    return render_template('precios.html')

@app.route('/galeria')
def galeria():
    images = [ "images/copa.jpg", "images/copa1.jpg", "images/copa2.jpg", "images/copa3.jpg", "images/copa4.jpg" ]

    return render_template('galeria.html', images=images)

@app.route('/sponsors')
def sponsors():
    sponsors = [
        {"name": "Arcor", "logo": "images/arcor.png"},
        {"name": "Bancor", "logo": "images/bancor.png"},
        {"name": "Cadena 3", "logo": "images/cadena3.png"},
        {"name": "CocaCola", "logo": "images/cocacola.png"},
        {"name": "Grido", "logo": "images/grido.png"},
        {"name": "Nike", "logo": "images/nike.jpg"},
        {"name": "Personal", "logo": "images/personal.jpg"},
        {"name": "Sect. Ambiente", "logo": "images/Secretariaambiente.jpg"},
        {"name": "UNC", "logo": "images/unc.png"},
        {"name": "Vitnik", "logo": "images/vitnik.png"},
    ]
    return render_template('sponsors.html', sponsors=sponsors)

if __name__ == '__main__':
    app.run(debug=True)


