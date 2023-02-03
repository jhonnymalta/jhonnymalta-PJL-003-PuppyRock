import sqlalchemy as sa
import sqlalchemy.orm as orm
from flask_login import UserMixin


from datetime import datetime

from models.model_base import ModelBase

class User(UserMixin,ModelBase):
    __tablename__ :str = 'tutors'

    id: int = sa.Column(sa.Integer,primary_key=True,autoincrement=True)
    username: str = sa.Column(sa.String(100), nullable=False,unique=True)
    city: str = sa.Column(sa.String(100))
    email:str = sa.Column(sa.String(100), nullable=False)
    password: str = sa.Column(sa.String(250),nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    # is_authenticated: bool = sa.Column(sa.Boolean)
    # is_active: bool = sa.Column(sa.Boolean,default=True)
    # is_anonymous: bool = sa.Column(sa.Boolean)
    


    # def get_id():
    #     return str(id)

   

    def __repr__(self) -> str:
        return f"<Tutor: {self.username} from {self.city}>"
