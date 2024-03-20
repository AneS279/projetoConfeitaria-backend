from flask import Flask
from flask import request

# flask --app endpoints run
app = Flask(__name__)
app.run(debug=True)


@app.route('/')
def home():
    return str(app.url_map)

#GET/POST Ingredientes
@app.route('/ingredientes', methods = ['GET', 'POST'])
def ingredientes():
    if(request.method == 'POST'):
        return 'Post Ingredientes',102
    else:
        return 'Ingredientes', 200

#GET/POST Fichas Técnicas
@app.route('/fichas_tecnicas', methods = ['GET', 'POST'])
def fichasTecnicas():
    if(request.method == 'POST'):
        return 'Post Ingredientes',102
    else:
        return 'Fichas Técnicas'

#GET/POST Produtos
@app.route('/produtos', methods = ['GET', 'POST'])
def produtos():
    if(request.method == 'POST'):
        return 'Post Produtos',102
    else:
        return 'Produtos'

#GET/POST Pedidos
@app.route('/pedidos', methods = ['GET', 'POST'])
def pedidos():
    if(request.method == 'POST'):
        return 'Post Pedidos',102
    else:
        return 'Pedidos'

#GET/POST Clientes
@app.route('/clientes', methods = ['GET', 'POST'])
def clientes():
    if(request.method == 'POST'):
        return 'Post Clientes',102
    else:
        return 'Clientes'
    
#TODO: Implement Put and Delete
# Add Mocks for gets
# (pedidos já feitos deveriam ser editados?)


if __name__ == '__main__':  
   app.run()