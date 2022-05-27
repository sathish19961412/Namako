from college import Session,engine,User

local_session=Session(bind=engine)

user_to_update=local_session.query(User).filter(User.username=='sathishmathew').first()

user_to_update.username="sathish"
user_to_update.email="sathishfreelanc5@gmail.com"

local_session.commit()