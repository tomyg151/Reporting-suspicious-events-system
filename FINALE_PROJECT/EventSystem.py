import AllClases
from AllClases import *
from DB_connection import *


class EventSystem:

    def __init__(self):
        self.myDataBase = DataBaseClass()

    def add_User(self, user_id, name, email):
        self.myDataBase.add_User(user_id, name, email)

    def add_event(self,event_id,user_id,event_type,description,address,dangerous_level):
        self.myDataBase.add_event(event_id,user_id,event_type,description,address,dangerous_level)


    def delete_event(self,event_id):
        self.myDataBase.delete_event(event_id)

    def update_event(self, event_id, event_type, description, address, dangerous_level):
        self.myDataBase.update_event(event_id, event_type, description, address, dangerous_level)

    def show_all_events(self):
        self.myDataBase.show_all_events()

    def show_Report_events(self, user_id):
        self.myDataBase.show_Report_events(user_id)

    def show_report(self, user_id):
        self.myDataBase.show_report(user_id)

    def show_report2(self,user_id):
        self.myDataBase.show_report2(user_id)

    def add_comment(self, event_id, user_id, comment):
        self.myDataBase.add_comment(event_id ,user_id, comment)

    def show_all_users(self):
        self.myDataBase.show_all_users()

    def add_approve_event(self, event_id, user_id):
        self.myDataBase.add_approve_event(event_id, user_id)

    def show_approved_users(self, event_id):
        """  הצגת המשתמשים אשר "אשרו" אירוע כלשהו """
        self.myDataBase.show_aprove_user(event_id)

    def add_comment(self, event_id, user_id, comment):
        self.myDataBase.add_comment(event_id, user_id, comment)

    def edit_comment(self, event_id, user_id, comment2):
        self.myDataBase.edit_comment(event_id, user_id, comment2)

    def delete_comment(self, user_id,event_id):
        self.myDataBase.delete_comment(user_id,event_id)

    def types_count(self):
        self.myDataBase.types_count()

    def max_reports(self):
        self.myDataBase.max_reports()

    def show_evenue(self):
        self.myDataBase.show_evenue()


