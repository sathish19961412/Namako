from college import User,Session,engine

local_session=Session(bind=engine)

"""
Returns All Objects
"""
# users=local_session.query(User).all()[0:6]
#
# for user in users:
#     print(user.username,user.email,user.date_created)

json=local_session.query(User).filter(User.username=="sathish").first()
print(json)