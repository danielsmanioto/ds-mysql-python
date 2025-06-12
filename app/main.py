import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Contrato
from datetime import date

DB_USER = "user" # os.getenv("DB_USER")
DB_PASSWORD = "password" # os.getenv("DB_PASSWORD")
DB_HOST = "localhost" # os.getenv("DB_HOST")
DB_NAME = "contratacao" # os.getenv("DB_NAME")

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Cria as tabelas
Base.metadata.create_all(engine)

class ContratoRepository:
    def __init__(self, session):
        self.session = session

    def cadastrar(self, nome, data_inicio, data_fim):
        contrato = Contrato(nome=nome, data_inicio=data_inicio, data_fim=data_fim)
        self.session.add(contrato)
        self.session.commit()
        print(f"Contrato cadastrado: {contrato.nome}")

    def consultar(self):
        contratos = self.session.query(Contrato).all()
        for c in contratos:
            print(f"{c.id}: {c.nome} ({c.data_inicio} - {c.data_fim})")

if __name__ == "__main__":
    session = Session()
    repo = ContratoRepository(session)

    # Exemplo de cadastro
    repo.cadastrar("Contrato Exemplo", date(2024, 6, 1), date(2025, 6, 1))

    # Exemplo de consulta
    repo.consultar()