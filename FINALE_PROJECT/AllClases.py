

class Event:
    """ constructor """
    def __init__(self,event_id,event_type,description,address,dangerous_level,user_id):
        self.event_id = event_id
        self.event_type = event_type
        self.description = description
        self.address = address
        self.dangerous_level = dangerous_level
        self.user_id = user_id

    def __repr__(self):
        return "event_id= " + str(self.event_id) + ", event_type= " + str(self.event_type) + \
               ", description= " + str(self.description) + ", address= " + str(self.address) + \
               ", dangerous_level= " + str(self.dangerous_level) + ", user_id= " + str(self.user_id) + \
               ", comments= " + str(self.comments)

class Comment:
    """comment constructor"""
    def __init__(self,user_id,event_id,comment):
        self.user_id = user_id
        self.event_id = event_id
        self.comment = comment

    def _repr_(self):
        return "event_id= " + str(self.event_id) + ", user_id= " + str(self.user_id) + ", comment= " + str(self.comment)

class User:
    def __init__(self,user_id,name,email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __repr__(self):
        return "user_id= " + str(self.user_id) + ", name= " + str(self.name) + ", email= " + str(self.email)

class Approve_Event:
    def __init__(self,event_id, user_id):
        self.event_id = event_id
        self.user_id = user_id

    def __repr__(self):
        return "event_id= " + str(self.event_id) + ", user id= " + str(self.user_id)





