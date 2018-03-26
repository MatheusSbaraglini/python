from database import BancoDeDados


if __name__ == '__main__':
    banco = BancoDeDados()
    banco.conecta()
    banco.criar_tabelas()
    # banco.inserir_cliente('Matheus', '11111111111', 'matheus@hotmail.com')
    banco.buscar_cliente('11111111111')
    banco.desconecta()
