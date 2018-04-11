from app import app
from app.routes import index
from app.models import endereco
from app.models import cliente


if __name__ == '__main__':
    app.run(port=8080, debug=True)