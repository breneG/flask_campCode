from estudo import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    usuario = 'Camp Code'
    idade = 37
    
    context = {
        'usuario': usuario,
        'idade': idade
    }
    return render_template('index.html', context=context)

@app.route('/contatos/')
def newpage():
    return 'outra view'