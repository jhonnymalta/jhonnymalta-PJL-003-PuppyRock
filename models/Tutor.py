import sqlalchemy as sa

from datetime import datetime

from models.model_base import ModelBase

class Tutor(ModelBase):
    _tablename__ :str = 'tutors'

    id: int = sa.Column(sa.integer,primary_key=True,autoincrement=True)
    name: str = sa.Column(sa.String(100),nullable=False)
    city: str = sa.Column(sa.String(100))
    email:str = sa.column(sa.String(100),nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)

    def __repr__(self) -> str:
        return f"<Tutor: {self.name} from {self.city}>"
