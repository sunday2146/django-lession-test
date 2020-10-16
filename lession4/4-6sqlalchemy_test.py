#coding:utf-8

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()
engine = create_engine('mysql+pymysql://root:@localhost:3306/sqlalchemy_test')
db_session = sessionmaker(bind=engine)()



def init():
  Base.metadata.create_all(engine)

def drop():
  Base.metadata.drop_all()


class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(20))


if __name__ == '__main__':
  init()