import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime

from models.model_base import ModelBase


class Puppy(ModelBase):
    __tablename__ :str = 'puppies'

    id : int = sa.Column(sa.Integer,primary_key=True,autoincrement=True)
    name: str = sa.Column(sa.String(100),nullable=False)
    age : int = sa.Column(sa.Integer)
    city: str = sa.Column(sa.String(100))
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)





    def __repr__(self) -> str:
        return f"<Puppy: {self.name} from {self.city}>"