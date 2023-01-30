from sqlalchemy import sa

from datetime import datetime

from models.model_base import ModelBase

class Puppy(ModelBase):
    __tablename__ :str = 'puppies'

    id = sa.Column(sa.Integer,Primary_Key=True,autoincrement=True)
    name = sa.Column(sa.String(100),nullable=False)
    age = sa.Column(sa.Integer)
    city = sa.Column(sa.Text)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)



    def __repr__(self) -> str:
        return f"<Puppy: {self.name} from {self.city}>"