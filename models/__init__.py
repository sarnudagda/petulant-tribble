from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import (
    Column,
    BIGINT,
    String,
    Float
)


class Base(object):
    index = Column(BIGINT)
    charm = Column(Float)
    color = Column(Float)
    dag = Column(Float)
    delta = Column(Float)
    expiration = Column(String)
    gamma = Column(Float)
    iv = Column(Float)
    kind = Column(String)
    mid = Column(String)
    occured = Column(Float)
    omega = Column(Float)
    owner = Column(String)
    price = Column(String)
    rho = Column(Float)
    size = Column(String)
    speed = Column(Float)
    strike = Column(Float)
    symbol = Column(String)
    t = Column(Float)
    theta = Column(Float)
    ticker = Column(String)
    ultima = Column(Float)
    underlying = Column(Float)
    value = Column(Float)
    vanna = Column(Float)
    vega = Column(Float)
    vera = Column(Float)
    veta = Column(Float)
    vomma = Column(Float)
    zomma = Column(Float)


Base = declarative_base(cls=Base)