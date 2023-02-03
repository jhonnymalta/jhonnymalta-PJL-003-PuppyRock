from data.db_session import create_session
from services.PassHashing import check_pass


from models.User import User
from typing import List

def insert_tutor(new_tutor) -> User:
    print("Cadastrando um novo tutor")

    tutor: User = User(
        username = new_tutor.username,
        city = new_tutor.city,
        email = new_tutor.email,
        password = new_tutor.password
    ) 

    with create_session() as session:
        session.add(tutor)
        session.commit()
    return tutor


def get_all_tutors() -> List[User]:
    with create_session() as session:
        tutor_list: List[User] = session.query(User)
    return tutor_list

def get_tutor_by_id(id: int) -> User:
    with create_session() as session:
        tutor: User = session.query(User).filter(User.id == id).first()
    return tutor

def authentication_user(name: str,password:str):
    with create_session() as session:
        tutor: User = session.query(User).filter(User.username == name).first()
        if tutor is not None:
            check = check_pass(tutor.password,password)
            if check:
                return tutor
            else:
                return False   
