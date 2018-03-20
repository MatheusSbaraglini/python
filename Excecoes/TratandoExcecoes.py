def divisao(divisor):

    try:
        return 10 / divisor
    except ZeroDivisionError:
        return 'divisão por zero'
    except TypeError:
        return 'tipo de numero invalido'
    except Exception:
        return 'erro inesperado'

print(divisao(20))