from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contrato(Base):
    __tablename__ = 'contratos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)