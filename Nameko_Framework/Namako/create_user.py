from college import User,Session,engine


users=[
    {
        "username":"raj",
        "email":"raj@gmail.com"
    },
    {
        "username": "rajkumar" ,
        "email": "rajkumar@gmail.com"
    } , {
        "username":"permakumar",
        "email":"permakumar@gmail.com"
    }, {
        "username":"Prasath",
        "email":"Prasath@gmail.com"
    }, {
        "username":"sriram",
        "email":"sriram@gmail.com"
    }, {
        "username":"saravanakumar",
        "email":"saravanakumar@gmail.com"
    },{
        "username":"sriharish",
        "email":"sriharish@gmail.com"
    },

]
local_session=Session(bind = engine)

new_user=User(username = "nithya1",email="nithya1freelanc5@gmail.com")

local_session.add(new_user)
local_session.commit()

# for multipleuser in users:
#     new_user = User (username=multipleuser["username"], email =multipleuser["email"])
#     print(new_user)
#     local_session.add(new_user)
#     local_session.commit()
#     print(f"Added {multipleuser['username']}")