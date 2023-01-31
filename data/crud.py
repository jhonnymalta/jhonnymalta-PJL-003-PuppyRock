from data.db_session import create_session
from models.Tutor import Tutor

def insert_tutor(new_tutor) -> None:
    print("Cadastrando um novo tutor")

    tutor: Tutor = Tutor(
        name = new_tutor.name,
        city = new_tutor.city,
        email = new_tutor.email
    ) 

    with create_session() as session:
        session.add(tutor)
        session.commit()
    
    print('Tutor Created!')