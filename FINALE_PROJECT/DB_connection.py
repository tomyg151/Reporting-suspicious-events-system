import mysql
from mysql import connector
import pandas as pd
from tkinter import *
from tkinter import ttk


class DataBaseClass:
    """ open/close connections"""

    def get_connection(self):
        """ connecting to DataBase """
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='tom9151',
            database='db_finaleprojectCoursePython'
        )
        return connection

    def close_connection(self,connection):
        """ closing connection DataBase """
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


    """creat tables"""

    def create_new_table_event(self):
        """ Create a new event table """
        connection = DataBaseClass.get_connection(self)
        cursor = connection.cursor()
        sql_select_query = """CREATE TABLE event (
                              event_id int NOT NULL,
                              user_id int not null,
                              event_type varchar (50) NOT NULL,
                              description varchar(250) NOT NULL,
                              address varchar(50) NOT NULL,
                              dangerous_level ENUM('easy', 'medium', 'hard') NOT NULL,
                              FOREIGN KEY (user_id) REFERENCES user(user_id),
                              PRIMARY KEY (event_id))"""
        cursor.execute(sql_select_query)
        res = cursor.fetchall()
        connection.commit()
        self.close_connection(connection)
        return res

    def create_new_table_User(self):
        """ Create a new user table """
        connection = DataBaseClass.get_connection(self)
        cursor = connection.cursor()
        sql_select_query = """CREATE TABLE User (
                              user_id int NOT NULL,
                              name varchar(20) not null,
                              email varchar(50) not null,
                              PRIMARY KEY (user_id))"""
        cursor.execute(sql_select_query)
        res = cursor.fetchall()
        connection.commit()
        self.close_connection(connection)
        return res

    def create_new_table_Approve_Event(self):
        """ Create a new Approve_Event table """
        connection = DataBaseClass.get_connection(self)
        cursor = connection.cursor()
        sql_select_query = """CREATE TABLE Approve_Event (
                              event_id int NOT NULL,
                              user_id int not null,
                              PRIMARY KEY (event_id, user_id),
                              FOREIGN KEY(event_id) REFERENCES event(event_id),
                              FOREIGN KEY(user_id) REFERENCES user(user_id))"""
        connection.commit()
        cursor.execute(sql_select_query)
        res = cursor.fetchall()
        self.close_connection(connection)
        return res

    def create_new_table_comments(self):
        """ Create a new comments table """
        connection = DataBaseClass.get_connection(self)
        cursor = connection.cursor()
        sql_select_query = """CREATE TABLE Comments (
                              event_id int NOT NULL,
                              user_id int not null,
                              comment varchar(200) not null,
                              PRIMARY KEY (event_id,user_id),
                              FOREIGN KEY(event_id) REFERENCES event(event_id),
                              FOREIGN KEY(user_id) REFERENCES user(user_id)
                              )"""
        connection.commit()
        cursor.execute(sql_select_query)
        res = cursor.fetchall()
        self.close_connection(connection)
        return res

    def create_all_tables(self):
        DataBaseClass.create_new_table_User(self)
        DataBaseClass.create_new_table_event(self)
        DataBaseClass.create_new_table_Approve_Event(self)
        DataBaseClass.create_new_table_comments(self)
        print('All tables are Created!')

    """ all function for users"""

    def add_User(self, user_id, name, email):
        """ insert an user to user table """
        try:
            conection = DataBaseClass().get_connection()
            curser = conection.cursor()
            query = ("INSERT INTO user "
                     "(user_id,name,email) "
                     "VALUES (%s,%s,%s)")
            val = (int(user_id), name, email)
            curser.execute(query, val)
            conection.commit()
            print("inserted successfully into user table")
            self.close_connection(conection)
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))


    """all function for events"""

    def add_event(self, event_id, user_id, type, description, address, dangerous_level):
        """ insert an event to event table """
        try:
            conection = DataBaseClass().get_connection()
            curser = conection.cursor()
            query = """INSERT INTO event(event_id,user_id, event_type, description, address, dangerous_level)
                    VALUES (%s,%s,%s,%s,%s,%s)"""
            val = (int(event_id), int(user_id), type, description, address, dangerous_level)
            curser.execute(query, val)
            conection.commit()
            print("inserted successfully into event table")
            self.close_connection(conection)
        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table: {}".format(error))

    def add_approve_event(self, event_id, user_id):
        """ insert an event to event table """
        try:
            conection = DataBaseClass().get_connection()
            curser = conection.cursor()
            event_id2 = event_id
            user_id2 = user_id
            query = """insert into approve_event (event_id, user_id) select %s,%s WHERE %s <> (SELECT user_id FROM event WHERE event_id = %s);"""
            val = int(event_id), int(user_id), int(user_id2), int(event_id2)
            curser.execute(query, val)
            result = curser.fetchall()
            conection.commit()
            print("inserted successfully into event table")
            self.close_connection(conection)
        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table: {}".format(error))

    def add_comment(self, event_id, user_id, comment):
        """ insert an comment to comment table """
        try:
            conection = self.get_connection()
            curser = conection.cursor()
            event_id2 = event_id
            user_id2 = user_id
            query = """insert into comments(event_id, user_id, comment) select %s,%s,%s WHERE %s <> (SELECT user_id FROM event WHERE event_id = %s);"""
            val = int(event_id),int(user_id), comment, int(user_id2), int(event_id2)
            curser.execute(query, val)
            conection.commit()
            print("inserted successfully into event table")
            self.close_connection(conection)
        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table: {}".format(error))

    def edit_comment(self, event_id, user_id, comment):
        """ update the comment table """
        try:
            connection = self.get_connection()
            curser = connection.cursor()
            event_id2 = event_id
            user_id2 = user_id
            query = """UPDATE comments SET comment = %s WHERE event_id = %s and user_id = %s and %s  <> (SELECT user_id FROM event WHERE event_id = %s);"""
            val = comment, int(event_id), int(user_id), int(user_id2) ,int(event_id2)
            curser.execute(query, val)
            connection.commit()
            print("updated successfully into event table")
            self.close_connection(connection)
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))

    def delete_event(self,event_id):
        """ delete an event from event table """
        try:
            connection = DataBaseClass().get_connection()
            curser = connection.cursor()
            query = """DELETE FROM event WHERE event_id = %s """
            curser.execute(query, (event_id,))
            result = curser.fetchall()
            connection.commit()
            print("Delete succesfully")
            self.close_connection(connection)
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))

    def max_reports(self):
        """ select user with max events """
        try:
            connection = self.get_connection()
            curser = connection.cursor()
            query = """select COUNT(event.event_id) as event_id , user.name,user.email
                        from event inner join user on user.user_id=event.user_id 
                        group by event.user_id
                        ORDER BY COUNT(event.event_id) desc
                        LIMIT 1 """
            curser.execute(query, )
            result = curser.fetchall()
            print_records = ''
            for record in result:
                print_records += str(record) + "\n"
            root = Tk()
            root.title('Max Report records')
            root['background'] = '#e4e7ed'
            root.geometry('300x200')
            i = 2
            query_label = Label(root, text="Number of Event ID, Name, Email")
            query_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
            for record in result:
                query_label = Label(root, text=record)
                query_label.grid(row=(8 + i), column=0, columnspan=2, padx=10, pady=10)
                i += 2
            connection.commit()
            self.close_connection(connection)
        except mysql.connector.Error as error:
            print("Failed to select max user report in MySQL: {}".format(error))

    def update_event(self, event_id, event_type, description, address, dangerous_level):
        """ update the event table """
        try:
            conection = DataBaseClass().get_connection()
            cursor = conection.cursor()
            query = """UPDATE event SET event_type = %s ,description = %s ,address = %s ,dangerous_level = %s WHERE event_id = %s;"""
            val = event_type, description, address, dangerous_level, event_id
            cursor.execute(query, val)
            result = cursor.fetchall()
            conection.commit()
            print("Update succesfully")
            self.close_connection(conection)
        except mysql.connector.Error as error:
            print("Failed to update table in MySQL: {}".format(error))

    def show_evenue(self):
        """" show users number of report and number of aprprove reports """
        list = []
        try:
            connection = DataBaseClass().get_connection()
            cursor = connection.cursor()

            query2 = """select user_id from user"""
            cursor.execute(query2)
            rows = cursor.fetchall()
            for row in rows:
                query = """select user.user_id, (select count(approve_event.user_id) from approve_event where approve_event.user_id = %s)*3 as cash_from_likes,
                                        (select (case when count(approve_event.event_id) = 5 THEN 10 WHEN count(approve_event.event_id) > 5 THEN 10 + (((count(approve_event.event_id)) - 5)* 2) ELSE 0 END)
                                        from approve_event join event on approve_event.event_id = event.event_id join user on event.user_id = user.user_id
                                        where user.user_id = %s) as cash_from_report
                                        from user
                                        where user.user_id = %s"""

                val = row[0], row[0], row[0]
                cursor.execute(query, val)
                results = cursor.fetchall()
                for res in results:
                    sum = res[1] + res[2]
                    t = (row[0], sum)
                    list.append(t)

            max = 0
            max_t2 = (0, 0)
            for el in list:
                if (el[1] > max):
                    max = el[1]
                    max_t2 = el
                    print(max_t2)
            # print_records = ''
            # for record in results:
            #     print_records += str(record) + "\n"
            root = Tk()
            root.title('Max Evenue')
            root['background'] = '#e4e7ed'
            root.geometry('300x200')
            query_label = Label(root, text="Event ID , Cash")
            query_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
            # for record in results:
            query_label = Label(root, text=max_t2)
            query_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10)
            connection.commit()
            self.close_connection(connection)
        except mysql.connector.Error as error:
            print("Failed to show_report2 in MySQL: {}".format(error))

    def delete_comment(self, user_id, event_id):
        """ delete an comment from comment table """
        try:
            connection = DataBaseClass().get_connection()
            curser = connection.cursor()
            query = """delete from db_finaleproject.comments where event_id = %s and user_id = %s"""
            val = event_id, user_id
            curser.execute(query, val)
            res = curser.fetchall()
            connection.commit()
            print("Delete succesfully")
            curser.execute("SELECT * FROM comments")
            for rows in res:
                print(rows)
            self.close_connection(connection)
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))

    def types_count(self):
        """ show the count of every dangerous_level type ('easy','medium','hard') """
        try:
            connection = self.get_connection()
            curser = connection.cursor()
            query = """select count(dangerous_level),
                       case
                            when dangerous_level='hard' then  "hard"
                            when dangerous_level ='medium' then "medium"
                            when dangerous_level ='easy' then "easy"
                        else null
                        end as dangerous_level
                        from event 
                        group by dangerous_level"""
            curser.execute(query, )
            result = curser.fetchall()
            my_data = pd.read_sql(query, connection, params=[])
            print(my_data)
            print_records = ''
            for record in result:
                print_records += str(record) + "\n"
            root = Tk()
            root.title('Types Count Records Gui')
            root['background'] = '#e4e7ed'
            root.geometry('300x200')
            i = 2
            query_label = Label(root, text="Count , Dangerous level")
            query_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
            for record in result:
                query_label = Label(root, text=record)
                query_label.grid(row=(8 + i), column=0 , columnspan=2,padx=10, pady=10)
                i+=2
            connection.commit()
        except mysql.connector.Error as error:
            print("Failed to select max user report in MySQL: {}".format(error))

    def show_all_events(self):
        """" show all events """
        try:
            connection = DataBaseClass().get_connection()
            curser = connection.cursor()
            query = """select * from event"""
            curser.execute(query,)
            result = curser.fetchall()
            my_data = pd.read_sql(query, connection, params=[])
            # print(my_data)
            print_records = ''
            for record in result:
                print_records += str(record) + "\n"
            root = Tk()
            root.title('Show All Events Records Gui')
            root['background'] = '#e4e7ed'
            root.geometry('400x300')
            i = 2
            query_label = Label(root, text="Event ID , User ID, Event type, Description, Address, Dangerous level")
            query_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
            for record in result:
                query_label = Label(root, text=record)
                query_label.grid(row=(8 + i), column=0, columnspan=2, padx=10, pady=10)
                i += 2
            connection.commit()
            self.close_connection(connection)
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))

    def show_all_users(self):
        """" show all users """
        try:
            connection = DataBaseClass().get_connection()
            curser = connection.cursor()
            query = """select * from user"""
            curser.execute(query,)
            result = curser.fetchall()
            # my_data = pd.read_sql(query, connection, params=[])
            # print(my_data)
            print_records = ''
            for record in result:
                print_records += str(record) + "\n"
            root = Tk()
            root.title('Show All Users Records Gui')
            root['background'] = '#e4e7ed'
            root.geometry('700x700')
            i = 2
            query_label = Label(root, text="User ID , Name, Email")
            query_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
            for record in result:
                query_label = Label(root, text=record)
                query_label.grid(row=(8 + i), column=0, columnspan=2, padx=10, pady=10)
                i += 2
            connection.commit()
            self.close_connection(connection)
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))

    def show_Report_events(self, user_id):
        """" show all users report on events """
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            query = """SELECT * FROM event WHERE (user_id = %s);"""
            val = int(user_id)
            cursor.execute(query, (val,))
            result = cursor.fetchall()
            # my_data = pd.read_sql(query, connection, params=[int(user_id)])
            # print(my_data)
            print_records = ''
            for record in result:
                print_records += str(record) + "\n"
            root = Tk()
            root.title('Show Report Events Records Gui')
            root['background'] = '#e4e7ed'
            root.geometry('400x500')
            i = 2
            query_label = Label(root, text="Event ID , User ID, Event type, Description, Address, Dangerous level")
            query_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
            for record in result:
                query_label = Label(root, text=record)
                query_label.grid(row=(8 + i), column=0, columnspan=2, padx=10, pady=10)
                i += 2
            connection.commit()
            self.close_connection(connection)
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))

    def show_report(self, user_id):
        """" show users number of report and number of aprprove reports """
        try:
            connection = DataBaseClass().get_connection()
            curser = connection.cursor()
            query = """SELECT (SELECT COUNT(user_id) FROM db_finaleproject.event WHERE user_id = %s) as num_of_events_reported, (SELECT COUNT(user_id) FROM db_finaleproject.approve_event WHERE user_id = %s) as num_of_user_approve;"""
            val = user_id, user_id
            curser.execute(query, val)
            result = curser.fetchall()
            print_records = ''
            for record in result:
                print_records += str(record) + "\n"
            root = Tk()
            root.title('Show Report 1 Records Gui')
            root['background'] = '#e4e7ed'
            root.geometry('700x700')
            i = 2
            query_label = Label(root, text="Number of events reported , Number of user approve")
            query_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
            for record in result:
                query_label = Label(root, text=record)
                query_label.grid(row=(8 + i), column=0, columnspan=2, padx=10, pady=10)
                i += 2
            connection.commit()
            self.close_connection(connection)
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))

    def show_report2(self, user_id):
        """" show users number of report and number of aprprove reports """
        try:
            connection = DataBaseClass().get_connection()
            cursor = connection.cursor()
            query = """select user.user_id, (select count(approve_event.user_id) from approve_event where approve_event.user_id = %s)*3 as cash_from_likes,
                        (select (case when count(approve_event.event_id) = 5 THEN 10 WHEN count(approve_event.event_id) > 5 THEN 10 + (((count(approve_event.event_id)) - 5)* 2) ELSE 0 END)
                        from approve_event join event on approve_event.event_id = event.event_id join user on event.user_id = user.user_id
                        where user.user_id = %s) as cash_from_report
                        from user
                        where user.user_id = %s"""
            val = user_id ,user_id, user_id
            cursor.execute(query, val)
            result = cursor.fetchall()
            print_records = ''
            for record in result:
                print_records += str(record) + "\n"
            root = Tk()
            root.title('Show Report 2 Records Gui')
            root['background'] = '#e4e7ed'
            root.geometry('700x700')
            i = 2
            query_label = Label(root, text="User ID , Cash from likes, Cash from report")
            query_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
            for record in result:
                query_label = Label(root, text=record)
                query_label.grid(row=(8 + i), column=0, columnspan=2, padx=10, pady=10)
                i += 2
            connection.commit()
            self.close_connection(connection)
        except mysql.connector.Error as error:
            print("Failed to show_report2 in MySQL: {}".format(error))

    def show_aprove_user(self, event_id):
        """" show all approved users """
        try:
            connection = DataBaseClass().get_connection()
            curser = connection.cursor()
            query = """select user.user_id, user.name, user.email
                        from user
                        where user.user_id in (select user_id from approve_event where event_id = %s)"""
            val = int(event_id)
            curser.execute(query, (val,))
            result = curser.fetchall()
            print_records = ''
            for record in result:
                print_records += str(record) + "\n"
            root = Tk()
            root.title('Show Approve Users Report Records Gui')
            root['background'] = '#e4e7ed'
            root.geometry('700x700')
            i = 2
            query_label = Label(root, text="User ID , Name, Email")
            query_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
            for record in result:
                query_label = Label(root, text=record)
                query_label.grid(row=(8 + i), column=0, columnspan=2, padx=10, pady=10)
                i += 2
            connection.commit()
            self.close_connection(connection)
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))




"""Create all Tables"""
# table = DataBaseClass()
# table.create_all_tables()