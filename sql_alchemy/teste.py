from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)


class Endereco(Base):
    __tablename__ = 'endereco'
    id = Column(Integer, primary_key=True)
    nome_rua = Column(String(100))
    bairro = Column(String(100))
    cep = Column(String(20))
    id_pessoa = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship(Pessoa)

engine = create_engine('sqlite:///banco.db')

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    pessoa = Pessoa(id=1, nome='Matheus')
    pessoa2 = Pessoa(id=2, nome='Marina')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(pessoa)
    session.add(pessoa2)
    session.commit()
    """
       http://docs.sqlalchemy.org/en/latest/orm/tutorial.html
       quando alterar o nome, o session, ja vai "saber" que o objeto foi alterado(edit)
    pessoa.nome = 'Matheus1'
    session.dirty
    """
