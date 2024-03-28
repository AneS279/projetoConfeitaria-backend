from flask import Flask
from flask import request
from flask_restx import Api, Resource

# flask --app endpoints run
app = Flask(__name__)

api = Api(app,
           catch_all_404s=True,
           version='0.1',
           title="REST HTTP API's Gateway",
           descrition="REST API gateway")

ns = api.namespace('helloworld', description='Hello World operations')

@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        """ Hello World!

        Returns:
            _type_: None
        """
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
#[Brendon] Poderia, mas acredito que seja melhor ter versionamento/histórico de alterações.


if __name__ == '__main__':
   app.run(debug=True)