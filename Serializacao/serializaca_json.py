import json
import pickle


class Contato:

    def __init__(self, primeiro_nome, sobrenome, endereco):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.endereco = endereco

    @property
    def nome_completo(self):
        return ('{} {}'.format(self.primeiro_nome, self.sobrenome))

# c = Contato('Matheus', 'Sbaraglini', 'rua sp')
# print(json.dumps(c.__dict__))

contato = Contato('Matheus', 'Sbaraglini', 'rua floripa')
# s_json = json.dumps(contato.__dict__)
s_json = "{'teste': 'valor_teste', 'teste1': 'valor_teste1'}"
contato.__dict__ = dict(eval(s_json))
print(contato.teste)
