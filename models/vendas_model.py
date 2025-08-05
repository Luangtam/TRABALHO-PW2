from sqlalchemy import Column, Integer, String, Float

from models.Conexao import Base ,engine

class Venda(Base):
    __tablename__ = 'vendas'
    id = Column(Integer, primary_key=True, index=True)
    cliente_nome = Column(String)
    total = Column(Float)
