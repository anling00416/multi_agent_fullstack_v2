
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base,sessionmaker
engine=create_engine("sqlite:///todos.db",connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()

class Todo(Base):
    __tablename__="todos"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,index=True)
Base.metadata.create_all(bind=engine)
