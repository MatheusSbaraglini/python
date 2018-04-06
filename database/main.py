from database import BancoDeDados


if __name__ == '__main__':
    banco = BancoDeDados()
    banco.conecta()
    banco.criar_tabelas()
    # banco.inserir_cliente('Matheus', 'python', '1111', 'matheus@hotmail.com')
    # banco.inserir_cliente('Marina', 'python1', '2222', 'marina@gmail.com')
    banco.buscar_cliente('2222')
    banco.desconecta()
