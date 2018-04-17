from app import app
from app.routes import index
from app.models import endereco, cliente
from app.routes.cliente_routes import clientes
from app.routes.endereco_routes import enderecos


if __name__ == '__main__':
    app.run(port=8080, debug=True)