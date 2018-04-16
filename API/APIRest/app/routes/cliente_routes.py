from app import app, db
from app.models import Cliente
from flask import jsonify

@app.route('/api/clientes/')
def clientes():
    all_clientes = Cliente.query.all()
    cliente_output = all_clientes.name
    return jsonify(cliente_output.data)
