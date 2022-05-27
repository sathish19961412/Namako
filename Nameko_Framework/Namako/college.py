from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column , Integer , String , DateTime , create_engine
from datetime import datetime
import os



Base_DIR=os.path.dirname(os.path.realpath (__file__ ))
connection_string="sqlite:///"+os.path.join(Base_DIR,'site.db')
Base = declarative_base ( )
engine=create_engine(connection_string,echo=True)
Session=sessionmaker()


"""
class User
      id Integer
      username String
      email String
      date_created datetime
"""


class User(Base):
    __tablename__ = 'users'
    id=Column(Integer(),primary_key =True)
    username=Column(String(25),unique=True,nullable=False)
    email=Column(String(80),unique=True,nullable=False)
    date_created=Column(DateTime(),default=datetime.utcnow)


def __repr__(self):
    return f"<User username={self.username} email={self.email}"


new_user =User( id = 1 , username = "sathish" , email = "sathishfreelanc5@gmail.com")
print (new_user)
