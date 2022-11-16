import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# create DB in interactive mode from root dir
# from workshop.tables import Base
# from workshop.database import engine
# Base.metadata.create_all(engine)


class Operation(Base):
    __tablename__ = 'opertions'

    id = sq.Column(sq.Integer, primary_key=True)
    date = sq.Column(sq.Date)
    kind = sq.Column(sq.String)
    amount = sq.Column(sq.Integer)
    description = sq.Column(sq.String, nullable=True)

