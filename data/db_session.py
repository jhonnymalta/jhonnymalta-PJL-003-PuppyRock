import sqlalchemy as sa

from sqlalchemy.orm import sessionmaker
from pathlib import Path # Usado no SQLite
from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine

from models.model_base import ModelBase


__engine: Optional[Engine] = None

def create_engine(sqlite: bool = False) -> Engine:
    global __engine

    if __engine:
        return
    
    if sqlite:
        arquivo_db = 'db/puppy_rock.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents = True,exist_ok=True)

        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url=conn_str,echo=False,connect_args={"check_same_thread":False})

    else:
        conn_str = "postgresql://usuario:senha@localhost_ou_ip:porta/nome_do_banco"
        __engine = sa.create_engine(url=conn_str,echo=False)

    return __engine

def create_session() -> Session:
    global __engine

    if not __engine:
        create_engine(sqlite=True) 

    __session = sessionmaker(__engine,expire_on_commit=False,class_=Session)

    session: Session = __session()

    return session

def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine(sqlite=True)

    import models.__all_models
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)