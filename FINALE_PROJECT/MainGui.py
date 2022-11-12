from tkinter.ttk import Style
import mysql.connector
from tkinter import *
import EventSystem
from AllClases import *
from DB_connection import *
import DB_connection
from tkinter import ttk
import tkinter.messagebox as mb


# create a tkinter window
root = Tk()
root.title('Welcome To Our Final Project! Ido Goldshmid And Tom Groundland')
# Open window having dimension 100x100
root.geometry('610x350')
root['background'] = '#e4e7ed'
Copyright_label = Label(root, bg='#e4e7ed', text="Ⓒ Copyright Ido Goldshmid")
# Copyright_label.grid(row=8, column=2)

Copyright_label.place(bordermode=OUTSIDE, height=660, width=630)

# DataBase

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='tom9151',
    database='db_finaleprojectCoursePython'
)

# Create cursor
c = connection.cursor()

"""Add a new user to the DB"""


def add_user():
    def user_clear():
        user_id.delete(0, END)
        name.delete(0, END)
        email.delete(0, END)

    def user_submit():
        user = EventSystem.EventSystem()
        user.add_User(int(user_id.get()), name.get(), email.get())
        root2 = Tk()
        root2.title('Good Job!')
        root2.geometry('350x100')
        btn2 = Button(root2, width=20, text='User added successfully', command=None)
        btn2.grid(row=1, column=3, pady=30, padx=100)

    root1 = Tk()
    root1.title('Add User Gui')
    root1['background'] = '#e4e7ed'
    root1.geometry('420x180')
    # Create User Text Box
    user_id = Entry(root1, width=40)
    user_id.grid(row=0, column=1, pady=10)
    name = Entry(root1, width=40)
    name.grid(row=1, column=1, pady=10)
    email = Entry(root1, width=40)
    email.grid(row=2, column=1, pady=10)

    # Create Text Box Lables
    user_id_label = Label(root1, bg='#e4e7ed', text="User Id: ")
    user_id_label.grid(row=0, column=0)
    name_label = Label(root1, bg='#e4e7ed', text="Name: ")
    name_label.grid(row=1, column=0)
    email_label = Label(root1, bg='#e4e7ed', text="Email: ")
    email_label.grid(row=2, column=0)

    # Create Submit And Clear Buttons
    submit_btn = Button(root1, width=12, text="Add User", bg='#8ff86f', command=user_submit)
    submit_btn.grid(row=3, column=0, padx=10, pady=10)
    clear_btn = Button(root1, width=12, text="Clear", bg="#f8af6f", command=user_clear)
    clear_btn.grid(row=3, column=1, padx=190, columnspan=3, pady=10)


"""Add a new Event to the DB"""


def add_event():
    def event_clear():
        event_id.delete(0, END)
        user_id.delete(0, END)
        event_type.delete(0, END)
        description.delete(0, END)
        address.delete(0, END)
        dangerous.delete(0, END)

    def event_submit():
        event = EventSystem.EventSystem()
        event.add_event(int(event_id.get()), int(user_id.get()), event_type.get(), description.get(), address.get(),
                        dangerous.get())
        root2 = Tk()
        root2.title('Good Job!')
        root2.geometry('350x100')
        btn2 = Button(root2, width=20, text='Event added successfully', command=None)
        btn2.grid(row=1, column=3, pady=30, padx=100)

    root2 = Tk()
    root2.title('Add Event Gui')
    root2['background'] = '#e4e7ed'
    root2.geometry('340x290')
    # Create User Text Box
    event_id = Entry(root2, width=30)
    event_id.grid(row=0, column=1, pady=10)
    user_id = Entry(root2, width=30)
    user_id.grid(row=1, column=1, pady=10)
    event_type = Entry(root2, width=30)
    event_type.grid(row=2, column=1, pady=10)
    description = Entry(root2, width=30)
    description.grid(row=3, column=1, pady=10)
    address = Entry(root2, width=30)
    address.grid(row=4, column=1, pady=10)
    dangerous = Entry(root2, width=30)
    dangerous.grid(row=5, column=1, pady=10)

    # Create Text Box Lables
    event_id_label = Label(root2, bg='#e4e7ed', text="Event Id: ")
    event_id_label.grid(row=0, column=0)
    user_id_label = Label(root2, bg='#e4e7ed', text="User Id: ")
    user_id_label.grid(row=1, column=0)
    event_type_label = Label(root2, bg='#e4e7ed', text="Event Type: ")
    event_type_label.grid(row=2, column=0)
    description_label = Label(root2, bg='#e4e7ed', text="Description: ")
    description_label.grid(row=3, column=0)
    address_label = Label(root2, bg='#e4e7ed', text="Address: ")
    address_label.grid(row=4, column=0)
    dangerous_level_label = Label(root2, bg='#e4e7ed', text="Dangerous Level: ")
    dangerous_level_label.grid(row=5, column=0)

    # Create Submit And Clear Buttons
    submit_btn = Button(root2, width=12, text="Add Event", bg='#8ff86f', command=event_submit)
    submit_btn.grid(row=6, column=0, padx=10, pady=10)
    clear_btn = Button(root2, width=12, text="Clear", bg="#f8af6f", command=event_clear)
    clear_btn.grid(row=6, column=1, padx=110, columnspan=3, pady=10)


"""Add Approve Event by input Event ID and user ID"""


def add_approve_event():
    def approve_clear():
        event_id.delete(0, END)
        user_id.delete(0, END)

    def approve_submit():
        approve = EventSystem.EventSystem()
        approve.add_approve_event(int(event_id.get()), int(user_id.get()))
        root2 = Tk()
        root2.title('Good Job!')
        root2.geometry('350x100')
        btn2 = Button(root2, width=20, text='Approve added successfully', command=None)
        btn2.grid(row=1, column=3, pady=30, padx=100)

    root4 = Tk()
    root4.title('Approve Event Gui')
    root4['background'] = '#e4e7ed'
    root4.geometry('330x130')
    # Create User Text Box
    event_id = Entry(root4, width=30)
    event_id.grid(row=0, column=1, pady=10)
    user_id = Entry(root4, width=30)
    user_id.grid(row=1, column=1, pady=10)

    # Create Text Box Lables
    event_id_label = Label(root4, bg='#e4e7ed', text="Event Id: ")
    event_id_label.grid(row=0, column=00)
    user_id_label = Label(root4, bg='#e4e7ed', text="User Id: ")
    user_id_label.grid(row=1, column=0)

    # Create Submit And Clear Buttons
    submit_btn = Button(root4, width=12, text="Approve Event", bg='#8ff86f', command=approve_submit)
    submit_btn.grid(row=2, column=0, padx=10, pady=10)
    clear_btn = Button(root4, width=12, text="Clear", bg="#f8af6f", command=approve_clear)
    clear_btn.grid(row=2, column=1, columnspan=3, padx=110, pady=10)


"""Add a new comment to the DB"""


def add_comment():
    def comment_clear():
        event_id.delete(0, END)
        user_id.delete(0, END)
        comment.delete(0, END)

    def comment_submit():
        comment1 = EventSystem.EventSystem()
        comment1.add_comment(int(event_id.get()), int(user_id.get()), comment.get())
        root2 = Tk()
        root2.title('Good Job!')
        root2.geometry('350x100')
        btn2 = Button(root2, width=20, text='Comment added successfully', command=None)
        btn2.grid(row=1, column=3, pady=30, padx=100)

    root5 = Tk()
    root5.title('Add Comment Gui')
    root5['background'] = '#e4e7ed'
    root5.geometry('350x180')
    # Create User Text Box
    event_id = Entry(root5, width=30)
    event_id.grid(row=0, column=1, pady=10)
    user_id = Entry(root5, width=30)
    user_id.grid(row=1, column=1, pady=10)
    comment = Entry(root5, width=30)
    comment.grid(row=2, column=1, pady=10)

    # Create Text Box Lables
    event_id_label = Label(root5, bg='#e4e7ed', text="Event Id: ")
    event_id_label.grid(row=0, column=0)
    user_id_label = Label(root5, bg='#e4e7ed', text="User Id: ")
    user_id_label.grid(row=1, column=0)
    comment_label = Label(root5, bg='#e4e7ed', text="Your Comment: ")
    comment_label.grid(row=2, column=0)

    # Create Submit And Clear Buttons
    submit_btn = Button(root5, width=12, text="Add Comment", bg='#8ff86f', command=comment_submit)
    submit_btn.grid(row=3, column=0, padx=10, pady=10)
    clear_btn = Button(root5, width=12, text="Clear", bg="#f8af6f", command=comment_clear)
    clear_btn.grid(row=3, column=1, columnspan=2, padx=130, pady=10)


"""Show the number of events that user report, and the number of events that he approved"""


def show_report1_event():
    def report1_clear():
        user_id.delete(0, END)

    def report1_submit():
        report1 = EventSystem.EventSystem()
        report1.show_report(int(user_id.get()))

    root6 = Tk()
    root6.title('Show Report 1')
    root6['background'] = '#e4e7ed'
    root6.geometry('350x110')
    # Create User Text Box
    user_id = Entry(root6, width=30)
    user_id.grid(row=0, column=1)

    # Create Text Box Lables
    user_id_label = Label(root6, bg='#e4e7ed', text="User Id: ")
    user_id_label.grid(row=0, column=0, padx=20, pady=10)

    # Create Submit And Clear Buttons
    submit_btn = Button(root6, width=12, text="Show Report 1", bg='#8ff86f', command=report1_submit)
    submit_btn.grid(row=1, column=0, padx=10, pady=10)
    clear_btn = Button(root6, width=12, text="Clear", bg="#f8af6f", command=report1_clear)
    clear_btn.grid(row=1, column=1, columnspan=2, padx=130, pady=10)


"""Show Report 2: Money that user make from Likes, Money That user make from is Event"""


def show_report2_event():
    def report2_clear():
        user_id.delete(0, END)

    def report2_submit():
        report2 = EventSystem.EventSystem()
        report2.show_report2(int(user_id.get()))

    root7 = Tk()
    root7.title('Show Report 2')
    root7['background'] = '#e4e7ed'
    root7.geometry('350x110')

    # Create User Text Box
    user_id = Entry(root7, width=30)
    user_id.grid(row=0, column=1, pady=10)

    # Create Text Box Lables
    user_id_label = Label(root7, bg='#e4e7ed', text="User Id: ")
    user_id_label.grid(row=0, column=0)

    # Create Submit And Clear Buttons
    submit_btn = Button(root7, text="Show Report 2", width=12, bg='#8ff86f', command=report2_submit)
    submit_btn.grid(row=1, column=0, padx=10, pady=10)
    clear_btn = Button(root7, text="Clear", width=12, bg="#f8af6f", command=report2_clear)
    clear_btn.grid(row=1, column=1, columnspan=2, padx=130, pady=10)


"""Delete Event by Event ID, but first of all you need to delete all comments and approved event that connect to this event"""


def delete_event():
    def delete_clear():
        event_id.delete(0, END)

    def delete_submit():
        delete = EventSystem.EventSystem()
        delete.delete_event(int(event_id.get()))
        root2 = Tk()
        root2.title('Good Job!')
        root2.geometry('400x100')
        btn2 = Button(root2, width=30, text='Event Deleted successfully', command=None)
        btn2.grid(row=1, column=3, pady=30, padx=100)

    root8 = Tk()
    root8.title('Delete Event Gui')
    root8['background'] = '#e4e7ed'
    root8.geometry('330x110')
    # Create User Text Box
    event_id = Entry(root8, width=30)
    event_id.grid(row=0, column=1, pady=10)

    # Create Text Box Lables
    event_id_label = Label(root8, bg='#e4e7ed', text="Event Id: ")
    event_id_label.grid(row=0, column=00)

    # Create Submit And Clear Buttons
    submit_btn = Button(root8, width=12, text="Delete Event", bg='#8ff86f', command=delete_submit)
    submit_btn.grid(row=2, column=0, padx=10, pady=10)
    clear_btn = Button(root8, width=12, text="Clear", bg="#f8af6f", command=delete_clear)
    clear_btn.grid(row=2, column=1, columnspan=3, padx=110, pady=10)


"""Delete comment by event ID and user ID"""

def delete_comment():
    def delete_comment_clear():
        event_id.delete(0, END)
        user_id.delete(0, END)

    def delete_comment_submit():
        delete_comment1 = EventSystem.EventSystem()
        delete_comment1.delete_comment(int(user_id.get()), int(event_id.get()))
        root2 = Tk()
        root2.title('Good Job!')
        root2.geometry('400x100')
        btn2 = Button(root2, width=30, text='Comment Deleted successfully', command=None)
        btn2.grid(row=1, column=3, pady=30, padx=100)

    root9 = Tk()
    root9.title('Delete Comment Gui')
    root9['background'] = '#e4e7ed'
    root9.geometry('350x130')
    # Create User Text Box
    user_id = Entry(root9, width=30)
    user_id.grid(row=0, column=1, pady=10)
    event_id = Entry(root9, width=30)
    event_id.grid(row=1, column=1, pady=10)

    # Create Text Box Lables
    user_id_label = Label(root9, bg='#e4e7ed', text="User Id: ")
    user_id_label.grid(row=0, column=0)
    event_id_label = Label(root9, bg='#e4e7ed', text="Event Id: ")
    event_id_label.grid(row=1, column=0)

    # Create Submit And Clear Buttons
    submit_btn = Button(root9, width=12, text="Delete Comment", bg='#8ff86f', command=delete_comment_submit)
    submit_btn.grid(row=3, column=0, padx=10, pady=10)
    clear_btn = Button(root9, width=12, text="Clear", bg="#f8af6f", command=delete_comment_clear)
    clear_btn.grid(row=3, column=1, columnspan=2, padx=130, pady=10)


"""Update a comment by Event ID , User ID and input a new Commemt"""


def edit_comment():
    def edit_comment_clear():
        event_id.delete(0, END)
        user_id.delete(0, END)
        comment.delete(0, END)

    def edit_comment_submit():
        edit_comment1 = EventSystem.EventSystem()
        edit_comment1.edit_comment(int(event_id.get()), int(user_id.get()) , comment.get())
        root2 = Tk()
        root2.title('Good Job!')
        root2.geometry('350x80')
        btn2 = Button(root2, width=20, text='Update Comment successfully', command=None)
        btn2.grid(row=1, column=3, pady=30, padx=100)

    root12 = Tk()
    root12.title('Edit Comment Gui')
    root12['background'] = '#e4e7ed'
    root12.geometry('350x180')
    # Create User Text Box
    user_id = Entry(root12, width=30)
    user_id.grid(row=0, column=1, pady=10)
    event_id = Entry(root12, width=30)
    event_id.grid(row=1, column=1, pady=10)
    comment = Entry(root12, width=30)
    comment.grid(row=2, column=1, pady=10)

    # Create Text Box Lables
    user_id_label = Label(root12, bg='#e4e7ed', text="User Id: ")
    user_id_label.grid(row=0, column=0)
    event_id_label = Label(root12, bg='#e4e7ed', text="Event Id: ")
    event_id_label.grid(row=1, column=0)
    comment_label = Label(root12, bg='#e4e7ed', text="New Comment: ")
    comment_label.grid(row=2, column=0)

    # Create Submit And Clear Buttons
    submit_btn = Button(root12, width=12, text="Edit Comment", bg='#8ff86f', command=edit_comment_submit)
    submit_btn.grid(row=3, column=0, padx=10, pady=10)
    clear_btn = Button(root12, width=12, text="Clear", bg="#f8af6f", command=edit_comment_clear)
    clear_btn.grid(row=3, column=1, columnspan=2, padx=130, pady=10)


"""Total number of each dangerous level of event by Types: easy/medium/hard"""


def types_count():
    types_count = EventSystem.EventSystem()
    types_count.types_count()

"""Show Report Evenue"""
def show_report_evenue():
    evenue = EventSystem.EventSystem()
    evenue.show_evenue()


"""Show the user with the max reports, show is ID, Name and Email"""


def max_report():
    max_report = EventSystem.EventSystem()
    max_report.max_reports()


"""Show the users that apprved Event by Event ID"""
def show_approved_user():
    def user_comment_clear():
        event_id.delete(0, END)

    def approved_users_submit():
        approved_users = EventSystem.EventSystem()
        approved_users.show_approved_users(int(event_id.get()))

    root13 = Tk()
    root13.title('Approved Users Report')
    root13['background'] = '#e4e7ed'
    root13.geometry('350x100')

    event_id = Entry(root13, width=30)
    event_id.grid(row=0, column=1, pady=10)

    # Create Text Box Lables
    event_id_label = Label(root13, bg='#e4e7ed', text="Event Id: ")
    event_id_label.grid(row=0, column=0)

    # Create Submit And Clear Buttons
    submit_btn = Button(root13, text="Approved Users", width=12, bg='#8ff86f', command=approved_users_submit)
    submit_btn.grid(row=1, column=0, padx=10, pady=10)
    clear_btn = Button(root13, width=12, text="Clear", bg="#f8af6f", command=user_comment_clear)
    clear_btn.grid(row=1, column=1, columnspan=2, padx=130, pady=10)


"""Show all users in the DB"""


def show_all_users():

    show_all = EventSystem.EventSystem()
    show_all.show_all_users()

    # root14 = Tk()
    # root14.title('Show All Users Report')
    # root14['background'] = '#e4e7ed'
    # root14.geometry('350x110')

    # # Create Submit And Clear Buttons
    # submit_btn = Button(root14, text="Show All Users", width=12, bg='#8ff86f', command=show_all_users_submit)
    # submit_btn.grid(row=1, column=0, padx=10, pady=10)


"""Update event"""


def upadte_event():
    def update_event_clear():
        event_id.delete(0, END)
        event_type.delete(0, END)
        description.delete(0, END)
        address.delete(0, END)
        dangerous.delete(0, END)

    def event_submit():
        event2 = EventSystem.EventSystem()
        event2.update_event(int(event_id.get()), event_type.get(), description.get(), address.get(), dangerous.get())
        root2 = Tk()
        root2.title('Good Job!')
        root2.geometry('350x100')
        btn2 = Button(root2, width=20, text='Update Event successfully', command=None)
        btn2.grid(row=1, column=3, pady=30, padx=100)

    root15 = Tk()
    root15.title('Update Event Gui')
    root15['background'] = '#e4e7ed'
    root15.geometry('340x270')
    # Create User Text Box
    event_id = Entry(root15, width=30)
    event_id.grid(row=0, column=1, pady=10)
    event_type = Entry(root15, width=30)
    event_type.grid(row=2, column=1, pady=10)
    description = Entry(root15, width=30)
    description.grid(row=3, column=1, pady=10)
    address = Entry(root15, width=30)
    address.grid(row=4, column=1, pady=10)
    dangerous = Entry(root15, width=30)
    dangerous.grid(row=5, column=1, pady=10)

    # Create Text Box Lables
    event_id_label = Label(root15, bg='#e4e7ed', text="Event Id: ")
    event_id_label.grid(row=0, column=0)
    event_type_label = Label(root15, bg='#e4e7ed', text="Event Type: ")
    event_type_label.grid(row=2, column=0)
    description_label = Label(root15, bg='#e4e7ed', text="Description: ")
    description_label.grid(row=3, column=0)
    address_label = Label(root15, bg='#e4e7ed', text="Address: ")
    address_label.grid(row=4, column=0)
    dangerous_level_label = Label(root15, bg='#e4e7ed', text="Dangerous Level: ")
    dangerous_level_label.grid(row=5, column=0)

    # Create Submit And Clear Buttons
    submit_btn = Button(root15, width=12, text="Update Event", bg='#8ff86f', command=event_submit)
    submit_btn.grid(row=6, column=0, padx=10, pady=10)
    clear_btn = Button(root15, width=12, text="Clear", bg="#f8af6f", command=update_event_clear)
    clear_btn.grid(row=6, column=1, padx=110, columnspan=3, pady=10)


"""Show All The Events That Users Added"""


def show_all_events():
    show_all = EventSystem.EventSystem()
    show_all.show_all_events()

    # root16 = Tk()
    # root16.title('Show All Events')
    # root16['background'] = '#e4e7ed'
    # root16.geometry('350x110')
    #
    # # Create Submit And Clear Buttons
    # submit_btn = Button(root16, text="Show All Events", width=12, bg='#8ff86f', command=show_all_events_submit)
    # submit_btn.grid(row=1, column=0, padx=10, pady=10)


"""Show Report Event By User ID"""


def show_report_event():
    def report_event_clear():
        user_id.delete(0, END)

    def show_report_event_submit():
        report_event = EventSystem.EventSystem()
        report_event.show_Report_events(int(user_id.get()))

    root18 = Tk()
    root18.title('Show Report event Gui')
    root18['background'] = '#e4e7ed'
    root18.geometry('400x100')
    # Create User Text Box
    user_id = Entry(root18, width=30)
    user_id.grid(row=0, column=1, pady=10)

    # Create Text Box Lables
    user_id_label = Label(root18, bg='#e4e7ed', text="User Id: ")
    user_id_label.grid(row=0, column=0)

    # Create Submit And Clear Buttons
    submit_btn = Button(root18, text="Show Report Event", width=15, bg='#8ff86f', command=show_report_event_submit)
    submit_btn.grid(row=1, column=0, padx=10, pady=10)
    clear_btn = Button(root18, width=15, text="Clear", bg="#f8af6f", command=report_event_clear)
    clear_btn.grid(row=1, column=1, columnspan=2, padx=130, pady=10)


# Create Buttons
"""Add a new user to the DB"""
Add_User_btn = Button(root, text="Add User", border=5, bg='#8ff86f', width=16, fg='black', bd='2', command=add_user)
Add_User_btn.grid(row=3, column=1, columnspan=1, padx=15, pady=15)

"""Add a new Event to the DB"""
Add_Event_btn = Button(root, text="Add Event", border=5, bg='#8ff86f', width=16, fg='black', bd='2', command=add_event)
Add_Event_btn.grid(row=3, column=2, columnspan=1, padx=15, pady=15)

"""Add a new comment to the DB"""
Add_Comment_btn = Button(root, text="Add Comment", border=5, bg='#8ff86f', width=16, fg='black', bd='2',command=add_comment)
Add_Comment_btn.grid(row=3, column=3, columnspan=1, padx=15, pady=15)
#
"""Add Approve Event by input Event ID and user ID"""
Add_Approve_Event_btn = Button(root, text="Add Approve Event", border=5, bg='#8ff86f', width=16, fg='black', bd='2',command=add_approve_event)
Add_Approve_Event_btn.grid(row=3, column=4, columnspan=1, padx=15, pady=15)
#
"""Delete Event by Event ID, but first of all you need to delete all comments and approved event that connect to this event"""
Delete_Event_btn = Button(root, text="Delete Event", border=5, bg='#8ff86f', width=16, fg='black', bd='2',command=delete_event)
Delete_Event_btn.grid(row=4, column=1, columnspan=1, padx=15, pady=15)

"""Update a comment by Event ID ,User ID and input a new Commemt"""
Edit_Comment_btn = Button(root, text="Update Comment", border=5, bg='#8ff86f', width=16, fg='black', bd='2',command=edit_comment)
Edit_Comment_btn.grid(row=4, column=2, columnspan=1, padx=15, pady=15)
#
"""Update event"""
Edit_Event_btn = Button(root, text="Update Event", border=5, bg='#8ff86f', width=16, fg='black', bd='2',command=upadte_event)
Edit_Event_btn.grid(row=4, column=3, columnspan=1, padx=15, pady=15)

"""Delete comment by event ID and user ID"""
Delete_Comment_btn = Button(root, text="Delete Comment", border=5, bg='#8ff86f', width=16, fg='black', bd='2',command=delete_comment)
Delete_Comment_btn.grid(row=4, column=4, columnspan=1, padx=15, pady=15)

"""Total number of each dangerous level of event by Types: easy/medium/hard"""
Types_count_btn = Button(root, text="Types Count", border=5, bg='#8ff86f', width=16, fg='black', bd='2',command=types_count)
Types_count_btn.grid(row=5, column=1, columnspan=1, padx=15, pady=15)

"""Show the user with the max reports, show is ID, Name and Email"""
Max_report_btn = Button(root, text="Max Report", border=5, bg='#8ff86f', width=16, fg='black', bd='2',command=max_report)
Max_report_btn.grid(row=5, column=2, columnspan=1, padx=15, pady=15)

"""Show the users that apprved Event by Event ID"""
Show_approved_users_btn = Button(root, text="Show Approved Users", border=5, bg='#8ff86f', width=16, fg='black', bd='2',command=show_approved_user)
Show_approved_users_btn.grid(row=5, column=3, columnspan=1, padx=15, pady=15)

"""Show all users in the DB"""
Show_all_users_btn = Button(root, text="Show All Users", border=5, bg='#8ff86f', width=16, fg='black', bd='2',command=show_all_users)
Show_all_users_btn.grid(row=5, column=4, columnspan=1, padx=15, pady=15)

"""Show the number of events that user report, and the number of events that he approved"""
Show_Report1_btn = Button(root, text="Show Report 1", border=5, bg='#8ff86f', width=16, fg='black', bd='2',command=show_report1_event)
Show_Report1_btn.grid(row=6, column=1, columnspan=1, padx=15, pady=15)

"""Show Report 2: Money that user make from Likes, Money That user make from is Event"""
Show_Report2_btn = Button(root, text="Show Report 2", border=5, bg='#8ff86f', width=16, fg='black', bd='2',command=show_report2_event)
Show_Report2_btn.grid(row=6, column=2, columnspan=1, padx=15, pady=15)

"""Show All The Events That Users Added"""
show_all_events_btn = Button(root, text="Show All Events", border=5, bg='#8ff86f', width=16, fg='black', bd='2',command=show_all_events)
show_all_events_btn.grid(row=6, column=3, columnspan=1, padx=15, pady=15)

"""Show Report Event By User ID"""
show_report_event_btn = Button(root, text="Show Report Event", border=5, bg='#8ff86f', width=16, fg='black', bd='2',command=show_report_event)
show_report_event_btn.grid(row=6, column=4, columnspan=1, padx=15, pady=15)

"""Show Report Evenue"""
show_report_event_btn = Button(root, text="Show Evenue", border=5, bg='#8ff86f', width=16, fg='black', bd='2',command=show_report_evenue)
show_report_event_btn.grid(row=7, column=1, columnspan=1, padx=15, pady=15)

# commit changes
connection.commit()

# close the connection
connection.close()

root.mainloop()