from app import User, Business
from app.session import Session


def create_user(first_name, last_name, email, business_name, country):
    global session

    try:
        session = Session()
        user = User(first_name, last_name, email)
        business = Business(business_name, email, country)

        session.add(user)
        session.add(business)
        session.commit()

    except Exception as e:
        print(e)
    finally:
        session.close()


def read():
    pass
