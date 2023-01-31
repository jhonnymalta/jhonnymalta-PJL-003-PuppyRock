from data.db_session import create_session
from models.Tutor import Tutor
from typing import List

def insert_tutor(new_tutor) -> Tutor:
    print("Cadastrando um novo tutor")

    tutor: Tutor = Tutor(
        name = new_tutor.name,
        city = new_tutor.city,
        email = new_tutor.email
    ) 

    with create_session() as session:
        session.add(tutor)
        session.commit()
    return tutor


def get_all_tutors() -> List[Tutor]:
    with create_session() as session:
        tutor_list: List[Tutor] = session.query(Tutor)
    return tutor_list

def get_tutor_by_id(id: int) -> Tutor:
    with create_session() as session:
        tutor: Tutor = session.query(Tutor).filter(Tutor.id == id).first()
    return tutor