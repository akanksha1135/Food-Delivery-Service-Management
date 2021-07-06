import tkinter as tk
from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from PIL import ImageTk, Image
import csv
import os
import pyodbc
from GeminiFoodPlaza import order

class karl(Frame):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Login")
        self.master.geometry("1000x1000")
        myFont = font.Font(size=15)

        self.button1 = Button( self, text = "Customer Login", width = 25,height=2,bg='Orange',
                               command = self.customer_window )
        self.button1['font'] = myFont
        self.button1.grid( row = 25, column = 0, columnspan = 20, padx=20,pady=20,sticky = W+E+N+S )

        self.button2 = Button(self, text="Restaurant Login", width=25,height=2,bg='Orange',
                              command=self.Restaurant_window)
        self.button2['font'] = myFont
        self.button2.grid(row=26 ,column=1, columnspan=20,padx=20,pady=20, sticky=W + E + N + S)

        self.button3 = Button(self, text="Delivery Agent Login", width=25,height=2,bg='Orange',
                              command=self.DeliveryAgent_window)
        self.button3['font'] = myFont
        self.button3.grid(row=27, column=1, columnspan=20,padx=20,pady=20, sticky=W + E + N + S)

        self.button4 = Button(self, text="Management Login", width=25, height=2,bg='Orange',
                              command=self.Management_window)
        self.button4['font'] = myFont
        self.button4.grid(row=28, column=1, columnspan=20,padx=20,pady=20, sticky=W + E + N + S)
        self.button5 = Button(self, text="Exit", width=25, height=2, bg='Orange',
                              command=self.master.destroy)
        self.button5['font'] = myFont
        self.button5.grid(row=29, column=1, columnspan=20, padx=20, pady=20, sticky=W + E + N + S)
    def customer_window(self):
        self.newWindow = Login_customer()
    def Restaurant_window(self):
        self.newWindow=Login_Restaurant()
    def DeliveryAgent_window(self):
        self.newWindow = Login_DeliveryAgent()
    def Management_window(self):
        self.newWindow = Login_Management()

#Customer Login page
class Login_customer(Frame):
    def __init__(self):
        new =tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("Customer_Login_Page")
        new.geometry("1000x1000")
        #new.resizable(False, False)
        # Login_Frame
        Frame_Login = Frame(new, bg="white")
        Frame_Login.place(x=150, y=150, height=340, width=500)

        title = Label(Frame_Login, text="Login Here", font=("Impact", 35, "bold"), fg="#d77337", bg="white").place(x=90,
                                                                                                                   y=30)
        desc = Label(Frame_Login, text="Customer Login Area", font=("Goudy old style", 15, "bold"), fg="#d25d17",
                     bg="white").place(x=90, y=100)
        lbl_user = Label(Frame_Login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=90, y=140)
        self.txt_user = Entry(Frame_Login, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=90, y=170, width=350, height=35)

        lbl_user = Label(Frame_Login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_Login, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_pass.place(x=90, y=250, width=350, height=35)

        exit_btn = Button(Frame_Login,command=new.destroy ,text="Exit", bg="white", fg="#d77337", bd=0,
                            font=("times new roman", 12)).place(x=90, y=290)
        login_btn = Button(new, command=self.xyz, text="Login", fg="white", bg="#d77337", bd=0,
                           font=("times new roman", 12)).place(x=300, y=470, width=180, height=40)

    def xyz(self):
        with open("user.txt", "r") as file:
            file_reader = csv.reader(file)
            self.login_function(file_reader)
            file.close()

    def login_function(self, file):
        user = self.txt_user.get()
        passw = self.txt_pass.get()
        count = 0
        if passw == "" or user == "":
            messagebox.showerror("Error", "All feilds are required", parent=self)
            count = 1
        for row in file:
            if row[0] == user and row[1] == passw:
                print(f"The name entered by you is {user} {passw}")
                self.window = Tk()
                self.window.title(user)
                self.window.geometry("1000x1000")
                logout_btn = Button(self.window, command=self.window.destroy, text="Logout", fg="white", bg="#d77337",
                                    bd=0,
                                    font=("times new roman", 12)).place(x=0, y=120, width=180, height=40)
                history_btn = Button(self.window, command="none", text="History", fg="white", bg="#d77337", bd=0,
                                     font=("times new roman", 12)).place(x=0, y=80, width=180, height=40)
                feedback_btn = Button(self.window, command=self.Feedback, text="Feedback", fg="white", bg="#d77337", bd=0,
                                      font=("times new roman", 12)).place(x=0, y=40, width=180, height=40)
                restaurant_btn = Button(self.window, command=self.All_Restaurants, text="Restaurant", fg="white", bg="#d77337", bd=0,
                                        font=("times new roman", 12)).place(x=0, y=0, width=180, height=40)
                count = 1
        if count != 1:
            messagebox.showerror("Error", "Username/Password is incorrect", parent=self)
    def All_Restaurants(self):
        username=self.txt_user.get()
        self.newWindow=Display_All_Restaurants(username)
    def Feedback(self):
        self.newWindow= Display_Feedback()

class Display_Feedback(Frame):
    def __init__(self):
        n1 = tk.Frame.__init__(self)
        n1 = Toplevel(self)
        n1.title("feedaback for.........")
        n1.resizable(True, True)
        n1.geometry("500x500")
        #n.bg = ImageTk.PhotoImage(Image.open("feedbackbg.jpg"))
        #n.bg_image = Label(n, image=n.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.button_restaurant_feedback = Button(n1,text='Feedback for restaurants',width=25,height=2,bg='Orange',fg='White',command=self.RestaurantFeedback)
        self.button_restaurant_feedback.grid(row=1,column=1,columnspan=2,sticky=N+E+W+S)

        self.button_delivery_agents_feedback = Button(n1, text='Feedback for delivery agents', width=25, height=2, bg='Orange',
                                                 fg='White',command=self.DeliveryAgentsFeedback)
        self.button_delivery_agents_feedback.grid(row=2, column=1, columnspan=2, sticky=N + E + W + S)

        self.button6 = Button(n1, text='Exit', width=25, height=2, command=self.master.destroy, bg='red')
        self.button6.grid(row=3, column=1, columnspan=2, sticky=W + E + N + S)

    def RestaurantFeedback(self):
        self.newWindow = Feedback_Restaurant()
    def DeliveryAgentsFeedback(self):
        self.newWindow = Feedback_DeliveryAgents()

class Feedback_Restaurant(Frame):
    def __init__(self):
        n2=tk.Frame.__init__(self)
        n2 = Toplevel(self)
        n2.title("Rating n Feedback")
        n2.resizable(True, True)
        n2.geometry("500x700")

        self.entry = Entry(n2, width=50)
        self.label = Label(n2, text='Rating', width=25, height=2, bg='Orange', fg='White', relief=GROOVE)
        self.label1 = Label(n2, text='Feedback', width=25, height=2, bg='Orange', fg='White', relief=GROOVE)
        self.button1 = Button(n2, text='1', width=10, height=3, bg='Yellow')
        self.button2 = Button(n2, text='2', width=10, height=3, bg='Yellow')
        self.button3 = Button(n2, text='3', width=10, height=3, bg='Yellow')
        self.button4 = Button(n2, text='4', width=10, height=3, bg='Yellow')
        self.button5 = Button(n2, text='5', width=10, height=3, bg='Yellow')
        self.button6 = Button(n2, text='Exit', width=25, height=2, command=self.master.destroy, bg='red')
        self.button7 = Button(n2, text='Submit', width=10, height=3, bg='Blue', fg='White',
                              command=self.DisplayMessage)

        self.label.grid(row=0, column=1, padx=5, pady=5)
        self.label1.grid(row=7, column=1, padx=10, pady=10)
        self.button1.grid(row=1, column=1, columnspan=2, sticky=W + E + N + S)
        self.button2.grid(row=2, column=1, columnspan=2, sticky=W + E + N + S)
        self.button3.grid(row=3, column=1, columnspan=2, sticky=W + E + N + S)
        self.button4.grid(row=4, column=1, columnspan=2, sticky=W + E + N + S)
        self.button5.grid(row=5, column=1, columnspan=2, sticky=W + E + N + S)
        self.button6.grid(row=10, column=1, columnspan=2, sticky=W + E + N + S)
        self.entry.grid(row=8, column=1, padx=20, pady=20)
        self.button7.grid(row=9, column=1, columnspan=2, sticky=N + E + W + S)

    def DisplayMessage(self):
        msg = self.entry.get()
        self.f1 = open("Restaurants_Feedback.txt", "w")
        self.f1.write(msg)
        self.f1.close()

class Feedback_DeliveryAgents(Frame):
    def __init__(self):
        n3 = tk.Frame.__init__(self)
        n3 = Toplevel(self)
        n3.title("fRating n Feedback")
        n3.resizable(True, True)
        n3.geometry("500x700")

        self.entry1 = Entry(n3, width=50)
        self.label = Label(n3, text='Rating', width=25, height=2, bg='Orange', fg='White', relief=GROOVE)
        self.label1 = Label(n3, text='Feedback', width=25, height=2, bg='Orange', fg='White', relief=GROOVE)
        self.button1 = Button(n3, text='1', width=10, height=3, bg='Yellow')
        self.button2 = Button(n3, text='2', width=10, height=3, bg='Yellow')
        self.button3 = Button(n3, text='3', width=10, height=3, bg='Yellow')
        self.button4 = Button(n3, text='4', width=10, height=3, bg='Yellow')
        self.button5 = Button(n3, text='5', width=10, height=3, bg='Yellow')
        self.button6 = Button(n3, text='Exit', width=25, height=2, command=self.master.destroy, bg='red')
        self.button7 = Button(n3, text='Submit', width=10, height=3, bg='Blue', fg='White',
                              command=self.DisplayMessage)

        self.label.grid(row=0, column=1, padx=5, pady=5)
        self.label1.grid(row=7, column=1, padx=10, pady=10)
        self.button1.grid(row=1, column=1, columnspan=2, sticky=W + E + N + S)
        self.button2.grid(row=2, column=1, columnspan=2, sticky=W + E + N + S)
        self.button3.grid(row=3, column=1, columnspan=2, sticky=W + E + N + S)
        self.button4.grid(row=4, column=1, columnspan=2, sticky=W + E + N + S)
        self.button5.grid(row=5, column=1, columnspan=2, sticky=W + E + N + S)
        self.button6.grid(row=10, column=1, columnspan=2, sticky=W + E + N + S)
        self.entry1.grid(row=8, column=1, padx=20, pady=20)
        self.button7.grid(row=9, column=1, columnspan=2, sticky=N + E + W + S)

    def DisplayMessage(self):
        msg = self.entry1.get()
        self.f = open("DeliveryAgents_Feedback.txt","w")
        self.f.write(msg)
        self.f.close()


class Display_All_Restaurants(Frame):
    def __init__(self,u):
        n =tk.Frame.__init__(self)
        n = Toplevel(self)
        n.title("List of all Restaurants")
        n.resizable(True, True)
        n.bg = ImageTk.PhotoImage(Image.open("login.jpg"))
        n.bg_image = Label(n, image=n.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.username=u

        title = Label(n,text="Restaurant Names", font=("Impact", 20, "bold"), fg="#d77337", bg="white").place(x=520, y=5)
        f=open("All_Restaurants.txt","r")
        i=50
        for row in f:
          x = Label(n,text=row,width=20,bg="orange").place(x=550, y=i)
          i = i + 20

        my_button = Button(n,command=self.abc,text="Near_by_Restaurants", width=20,bg="green").place(x=550, y=i+75)
    def abc(self):
        user = self.username
        self.newWindow=Display_Nearby_Restaurants(user)
class Display_Nearby_Restaurants(Frame):
    def __init__(self,us):
        new =tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("Nearby Restaurants")
        new.resizable(True, True)
        new.bg = ImageTk.PhotoImage(Image.open("login.jpg"))
        new.bg_image = Label(new, image=new.bg).place(x=0, y=0, relwidth=1, relheight=1)
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-4KBB762;'
                              'Database=Userdb;'
                              'Trusted_connection==yes;')
        title = Label(new, text="Nearby Restaurants", font=("Impact", 20, "bold"), fg="#d77337", bg="white").place(x=520,
                                                                                                               y=5)

        self.user=us

        cursor = conn.cursor()
        # user = self.txt_user.get()
        cursor.execute('SELECT ' +us+ ' FROM usertb')
        a=50
        for i in cursor:
            my_button=Button(new,text=i,width=20,bg="orange").place(x=550,y=a)
            a=a+35
        self.text = Entry(new, font=("times new roman", 15), bg="lightgray")
        self.text.place(x=550, y=a + 50, width=150, height=35)
        my_button = Button(new, command=self.Open, text="send", width=5).place(x=600, y=a + 90)
    def Open(self):
        name=self.text.get()
        os.system('python ' + name + '.py')
        print(name)

#Restaurant Login page
class Login_Restaurant(Frame):
    def __init__(self):
        new =tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("Restaurant_Login_Page")
        new.geometry("1000x1000")
        new.resizable(False, False)
        # Login_Frame
        Frame_Login = Frame(new, bg="white")
        Frame_Login.place(x=150, y=150, height=340, width=500)

        title = Label(Frame_Login, text="Login Here", font=("Impact", 35, "bold"), fg="#d77337", bg="white").place(x=90,
                                                                                                                   y=30)
        desc = Label(Frame_Login, text="Restaurant Login Area", font=("Goudy old style", 15, "bold"), fg="#d25d17",
                     bg="white").place(x=90, y=100)
        lbl_user = Label(Frame_Login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=90, y=140)
        self.txt_user = Entry(Frame_Login, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=90, y=170, width=350, height=35)

        lbl_user = Label(Frame_Login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_Login, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_pass.place(x=90, y=250, width=350, height=35)

        forget_btn = Button(Frame_Login, text="Exit",command=new.destroy, bg="white", fg="#d77337", bd=0,
                            font=("times new roman", 12)).place(x=90, y=290)
        login_btn = Button(new, command=self.xyz, text="Login", fg="white", bg="#d77337", bd=0,
                           font=("times new roman", 12)).place(x=300, y=470, width=180, height=40)

    def xyz(self):
        with open("Restaurant.txt", "r") as file:
            file_reader = csv.reader(file)
            self.login_function(file_reader)
            file.close()

    def login_function(self, file):
        user = self.txt_user.get()
        passw = self.txt_pass.get()
        count = 0
        if passw == "" or user == "":
            messagebox.showerror("Error", "All feilds are required", parent=self)
            count = 1
        for row in file:
            if row[0] == user and row[1] == passw:
                print(f"The name entered by you is {user} {passw}")
                self.window = Tk()
                self.window.title(user)
                self.window.geometry("1000x1000")
                logout_btn = Button(self.window, command=self.window.destroy, text="Logout", fg="white", bg="#d77337",
                                    bd=0,
                                    font=("times new roman", 12)).place(x=0, y=320, width=180, height=40)
                history_btn = Button(self.window, command="none", text="History", fg="white", bg="#d77337", bd=0,
                                     font=("times new roman", 12)).place(x=0, y=160, width=180, height=40)
                feedback_btn = Button(self.window, command="none", text="Feedback", fg="white", bg="#d77337", bd=0,
                                      font=("times new roman", 12)).place(x=0, y=120, width=180, height=40)
                menu_btn = Button(self.window, command="none", text="View Menu", fg="white", bg="#d77337", bd=0,
                                        font=("times new roman", 12)).place(x=0, y=0, width=180, height=40)
                menuedit_btn = Button(self.window, command=self.view_menu, text="Edit Menu", fg="white", bg="#d77337", bd=0,
                                  font=("times new roman", 12)).place(x=0, y=40, width=180, height=40)
                menucreate_btn = Button(self.window, command="none", text="Create Menu", fg="white", bg="#d77337", bd=0,
                                  font=("times new roman", 12)).place(x=0, y=80, width=180, height=40)
                order_button=Button(self.window, command=self.viewOrder, text="Orders", fg="white", bg="#d77337", bd=0,
                                  font=("times new roman", 12)).place(x=0, y=200, width=180, height=40)
                Delivery_btn=Button(self.window, command=self.View_DeliveryAgents, text="Delivery Agent", fg="white", bg="#d77337", bd=0,
                                  font=("times new roman", 12)).place(x=0, y=240, width=180, height=40)
                Rating_btn=Button(self.window, command="none", text="Rating", fg="white", bg="#d77337", bd=0,
                                  font=("times new roman", 12)).place(x=0, y=280, width=180, height=40)
                count = 1

        if count != 1:
            messagebox.showerror("Error", "Username/Password is incorrect", parent=self)
    def view_menu(self):
        name = self.txt_user.get()
        os.system('python '+name+'.py')
    def View_DeliveryAgents(self):
        username = self.txt_user.get()
        self.newWindow = Display_Agents(username)
    def viewOrder(self):
        self.Cart=order()

class Display_Agents(Frame):
    def __init__(self,user_name):
        New=tk.Frame.__init__(self)
        New=Toplevel(self)
        New.title("List of delivery agents")
        New.resizable(True, True)
        self.bg = ImageTk.PhotoImage(Image.open("DeliveryAg.jpg"))
        self.bg_image = Label(New, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        New.resizable(True, True)
        New.bg = ImageTk.PhotoImage(Image.open("DeliveryAg.jpg"))
        New.bg_image = Label(New, image=New.bg).place(x=0, y=0, relwidth=1, relheight=1)
        title = Label(New, text="Delivery Agents", font=("Impact", 20, "bold"), fg="#d77337", bg="white").place(x=520,
                                                                                                         y=5)
        self.Restaurant=user_name
        f = open("List_of_DeliveryAgents.txt", "r")
        i = 50
        for row in f:
            x = Label(New, text=row, width=20).place(x=800, y=i)
            i = i + 45
        self.text = Entry(New, font=("times new roman", 15), bg="lightgray")
        self.text.place(x=800, y=i+50, width=150, height=35)

        my_button=Button(New,command=self.Request,text="send",width=5).place(x=800,y=i+90)
    def Request(self):
        name=self.text.get()
        print(name)
        r=self.Restaurant
        self.newWindow=send_requests(r,name)
class send_requests(Frame):
    def __init__(self,rstrnt,name):
       # New = tk.Frame.init(self)
       # New = Toplevel(self)
       self.rstrnt=rstrnt
       self.db_name=name
       file = open(self.db_name+".txt", "a+")
       file.write("Order request from "+self.rstrnt+"\n")
       file1=open(self.db_name+"_History.txt","a+")
       file1.write(self.rstrnt+"\n")
       file.close()
       file1.close()


# DeliveryAgent login page
class Login_DeliveryAgent(Frame):
    def __init__(self):
        new =tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("DeliveryAgent_Login_Page")
        new.geometry("1000x1000")
        new.resizable(False, False)
        # Login_Frame
        Frame_Login = Frame(new, bg="white")
        Frame_Login.place(x=150, y=150, height=340, width=500)

        title = Label(Frame_Login, text="Login Here", font=("Impact", 35, "bold"), fg="#d77337", bg="white").place(x=90,
                                                                                                                   y=30)
        desc = Label(Frame_Login, text="Delivery Agent Login Area", font=("Goudy old style", 15, "bold"), fg="#d25d17",
                     bg="white").place(x=90, y=100)
        lbl_user = Label(Frame_Login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=90, y=140)
        self.txt_user = Entry(Frame_Login, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=90, y=170, width=350, height=35)

        lbl_user = Label(Frame_Login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_Login, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_pass.place(x=90, y=250, width=350, height=35)

        forget_btn = Button(Frame_Login, text="Exit",command=new.destroy, bg="white", fg="#d77337", bd=0,
                            font=("times new roman", 12)).place(x=90, y=290)
        login_btn = Button(new, command=self.xyz, text="Login", fg="white", bg="#d77337", bd=0,
                           font=("times new roman", 12)).place(x=300, y=470, width=180, height=40)

    def xyz(self):
        with open("DeliveryAgent.txt", "r") as file:
            file_reader = csv.reader(file)
            self.login_function(file_reader)
            file.close()

    def login_function(self, file):
        user = self.txt_user.get()
        passw = self.txt_pass.get()
        count = 0
        if passw == "" or user == "":
            messagebox.showerror("Error", "All feilds are required", parent=self)
            count = 1
        for row in file:
            if row[0] == user and row[1] == passw:
                print(f"The name entered by you is {user} {passw}")
                self.window2 = Tk()
                self.window2.title(user)
                self.window2.geometry("1000x1000")
                logout_btn = Button(self.window2, command=self.window2.destroy, text="Logout", fg="white", bg="#d77337",
                                    bd=0,
                                    font=("times new roman", 12)).place(x=0, y=160, width=180, height=40)
                Request_btn = Button(self.window2, command=self.oreq, text="Order Requests", fg="white", bg="#d77337",
                                     bd=0,
                                     font=("times new roman", 12)).place(x=0, y=40, width=180, height=40)
                feedback_btn = Button(self.window2, command=self.feedb, text="Feedback", fg="white", bg="#d77337", bd=0,
                                      font=("times new roman", 12)).place(x=0, y=120, width=180, height=40)
                pending_btn = Button(self.window2, command="none", text="Pending Orders", fg="white", bg="#d77337",
                                     bd=0,
                                     font=("times new roman", 12)).place(x=0, y=0, width=180, height=40)
                History_btn = Button(self.window2, command=self.hist, text="History", fg="white", bg="#d77337", bd=0,
                                     font=("times new roman", 12)).place(x=0, y=80, width=180, height=40)
                count = 1
        if count != 1:
            messagebox.showerror("Error", "Username/Password is incorrect", parent=self)
    def hist(self):
        usern=self.txt_user.get()
        self.newWindow=Historydb(usern)
    def oreq(self):
        usernm=self.txt_user.get()
        self.newWindow=ordereqs(usernm)
    def feedb(self):
        self.newWindow = Feedb()

class Feedb(Frame):
    def __init__(self):
        m = tk.Frame.__init__(self)
        m=Toplevel(self)
        m.title("Feedback page")
        m.resizable(True, True)
        m.geometry("500x500")

        self.button_customers_feedback = Button(m, text='Feedback from customers', width=25, height=2, bg='Orange',
                                                 fg='White', command=self.Feedback_customers)
        self.button_customers_feedback.grid(row=1, column=1, columnspan=2, sticky=N + E + W + S)

        self.button_restaurants_feedback = Button(m, text='Feedback for restaurants', width=25, height=2,
                                                      bg='Orange',
                                                      fg='White', command="none")
        self.button_restaurants_feedback.grid(row=2, column=1, columnspan=2, sticky=N + E + W + S)

        self.button6 = Button(m, text='Exit', width=25, height=2, command=self.master.destroy, bg='red')
        self.button6.grid(row=3, column=1, columnspan=2, sticky=W + E + N + S)

    def Feedback_customers(self):
        self.newWindow=FbC()

class FbC(Frame):
    def __init__(self):
        m1 = tk.Frame.__init__(self)
        m1=Toplevel(self)
        m1.title("Feedback page")
        m1.resizable(True, True)
        m1.geometry("500x500")

        self.f1 = open("DeliveryAgents_Feedback.txt","r")
        self.label = Label(m1,text=print(self.f1.read()))
        self.label.pack()

class ordereqs(Frame):
    def __init__(self,usrn):
        new = tk.Frame.__init__(self)
        new = Toplevel(self)
        self.user = usrn
        new.title("Order requests of " + self.user)
        new.resizable(True, True)
        self.bg = ImageTk.PhotoImage(Image.open("feedbackbg.jpg"))
        self.bg_image = Label(new, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        Frame_DM = Frame(new, bg="white")
        Frame_DM.place(x=700, y=150, height=340, width=500)
        file = open(self.user + ".txt", "r")
        mylabel = Label(new, text=file.read()).place(x=800, y=200)


class Historydb(Frame):
    def __init__(self,usern):
        N = tk.Frame.__init__(self)
        N= Toplevel(self)
        self.user=usern
        N.title("History of "+self.user)
        N.resizable(True, True)
        self.bg = ImageTk.PhotoImage(Image.open("feedbackbg.jpg"))
        self.bg_image = Label(N, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        Frame_DM = Frame(N, bg="white")
        Frame_DM.place(x=700, y=150, height=340, width=500)
        file=open(self.user+"_History.txt","r")
        mylabel = Label(N, text=file.read()).place(x=800, y=200)


#Login page for Management
class Login_Management(Frame):
    def __init__(self):
        new =tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("Management_Login_Page")
        new.geometry("1000x1000")
        new.resizable(False, False)
        # Login_Frame
        Frame_Login = Frame(new, bg="white")
        Frame_Login.place(x=150, y=150, height=340, width=500)

        title = Label(Frame_Login, text="Login Here", font=("Impact", 35, "bold"), fg="#d77337", bg="white").place(x=90,
                                                                                                                   y=30)
        desc = Label(Frame_Login, text="Management Login Area", font=("Goudy old style", 15, "bold"), fg="#d25d17",
                     bg="white").place(x=90, y=100)
        lbl_user = Label(Frame_Login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=90, y=140)
        self.txt_user = Entry(Frame_Login, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=90, y=170, width=350, height=35)

        lbl_user = Label(Frame_Login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_Login, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_pass.place(x=90, y=250, width=350, height=35)

        forget_btn = Button(Frame_Login, text="Exit",command=new.destroy, bg="white", fg="#d77337", bd=0,
                            font=("times new roman", 12)).place(x=90, y=290)
        login_btn = Button(new, command=self.xyz, text="Login", fg="white", bg="#d77337", bd=0,
                           font=("times new roman", 12)).place(x=300, y=470, width=180, height=40)

    def xyz(self):
        with open("Management.txt", "r") as file:
            file_reader = csv.reader(file)
            self.login_function(file_reader)
            file.close()

    def login_function(self, file):
        user = self.txt_user.get()
        passw = self.txt_pass.get()
        count = 0
        if passw == "" or user == "":
            messagebox.showerror("Error", "All feilds are required", parent=self)
            count = 1
        for row in file:
            if row[0] == user and row[1] == passw:
                print(f"The name entered by you is {user} {passw}")
                self.window3 = Tk()
                self.window3.title(user)
                self.window3.geometry("1000x1000")
                logout_btn = Button(self.window3, command=self.window3.destroy, text="Logout", fg="white", bg="#d77337",
                                    bd=0,
                                    font=("times new roman", 12)).place(x=0, y=160, width=180, height=40)
                Restaurant_btn = Button(self.window3, command=self.view_restaurant, text="Restaurant", fg="white", bg="#d77337",
                                     bd=0,
                                     font=("times new roman", 12)).place(x=0, y=40, width=180, height=40)
                feedback_btn = Button(self.window3, command="none", text="Feedback", fg="white", bg="#d77337", bd=0,
                                      font=("times new roman", 12)).place(x=0, y=120, width=180, height=40)
                Customer_btn = Button(self.window3, command=self.view_customer, text="Customer", fg="white", bg="#d77337",
                                     bd=0,
                                     font=("times new roman", 12)).place(x=0, y=0, width=180, height=40)
                Delivery_btn = Button(self.window3, command=self.view_DeliveryAgent, text="Delivery Agent", fg="white", bg="#d77337", bd=0,
                                     font=("times new roman", 12)).place(x=0, y=80, width=180, height=40)
                count = 1
        if count != 1:
            messagebox.showerror("Error", "Username/Password is incorrect", parent=self)
    def view_customer(self):
        self.window4=Tk()
        self.window4.title("Customer")
        self.window4.geometry("1000x1000")
        delete_btn = Button(self.window4, command=self.delete, text="Delete Customer", fg="white", bg="#d77337", bd=0,
                            font=("times new roman", 12)).place(x=0, y=0, width=180, height=40)
        view_btn = Button(self.window4, command=self.view, text="View Customers", fg="white", bg="#d77337", bd=0,
                          font=("times new roman", 12)).place(x=350, y=0, width=180, height=40)
        exit_btn = Button(self.window4, command=self.window4.destroy, text="Back", fg="white", bg="#d77337", bd=0,
                          font=("times new roman", 12)).place(x=700, y=0, width=180, height=40)
    def view(self):
        f1=open("user.txt","r")
        file_reader1 = csv.reader(f1)
        i=0
        for row in file_reader1:
            view_user = Label(self.window4, text=row[0], font=("Goudy old style", 15, "bold"), fg="red",
                              bg="yellow").place(x=350, y=i+40,width=180,height=40)
            i=i+40
        f1.close()
    def delete(self):
        delete_user = Label(self.window4, text="Enter User name to remove", font=("Goudy old style", 10, "bold"), fg="red",
                            bg="yellow").place(x=0, y= 40, width=180, height=40)
        self.dlt_user = Entry(self.window4, font=("times new roman", 15), bg="lightgray")
        self.dlt_user.place(x=0, y=100, width=180, height=50)
        enter_btn = Button(self.window4, command=self.enter, text="Delete", fg="white", bg="#d77337", bd=0,
                           font=("times new roman", 12)).place(x=0, y=150, width=180, height=40)
    def enter(self):
        user=self.dlt_user.get()
        f2 = open("user.txt", "r")
        output = []
        for line in f2:
            if not line.startswith(user):
                 output.append(line)
        f2.close()
        print(output)
        f2 = open("user.txt", 'w')
        f2.writelines(output)
        f2.close()
    def view_restaurant(self):
        self.window5 = Tk()
        self.window5.title("Restaurant")
        self.window5.geometry("1000x1000")
        delete_btn = Button(self.window5, command=self.delete2, text="Delete Restaurant", fg="white", bg="#d77337", bd=0,
                            font=("times new roman", 12)).place(x=0, y=0, width=180, height=40)
        view_btn = Button(self.window5, command=self.view2, text="View Restaurants", fg="white", bg="#d77337", bd=0,
                          font=("times new roman", 12)).place(x=350, y=0, width=180, height=40)
        add_btn = Button(self.window5, command=self.Add, text="Add Restaurants", fg="white", bg="#d77337", bd=0,
                         font=("times new roman", 12)).place(x=550, y=0, width=180, height=40)
        exit_btn = Button(self.window5, command=self.window5.destroy, text="Back", fg="white", bg="#d77337", bd=0,
                          font=("times new roman", 12)).place(x=750, y=0, width=180, height=40)
    def view2(self):
        f1 = open("All_Restaurants.txt", "r")
        file_reader1 = csv.reader(f1)
        i = 0
        for row in file_reader1:
            view_restaurant = Label(self.window5, text=row[0], font=("Goudy old style", 15, "bold"), fg="red",
                                     bg="yellow").place(x=350, y=i + 40, width=180, height=40)
            i = i + 40
        f1.close()
    def delete2(self):
        delete_user = Label(self.window5, text="Enter Restaurant name to remove", font=("Goudy old style", 10, "bold"), fg="red",
                            bg="yellow").place(x=0, y= 40, width=180, height=40)
        self.dlt_user = Entry(self.window5, font=("times new roman", 15), bg="lightgray")
        self.dlt_user.place(x=0, y=100, width=180, height=50)
        enter_btn = Button(self.window5, command=self.enter2, text="Delete", fg="white", bg="#d77337", bd=0,
                           font=("times new roman", 12)).place(x=0, y=150, width=180, height=40)
    def enter2(self):
        user=self.dlt_user.get()
        f2 = open("All_Restaurants.txt", "r")
        output = []
        for line in f2:
            if not line.startswith(user):
                output.append(line)
        f2.close()
        f2 = open("All_Restaurants.txt", 'w')
        f2.writelines(output)
        f2.close()
    def Add(self):
        add_user = Label(self.window5, text="Enter Restaurant name to Add", font=("Goudy old style", 10, "bold"),
                         fg="red",bg="yellow").place(x=550, y=40, width=180, height=40)
        self.add_user = Entry(self.window5, font=("times new roman", 15), bg="lightgray")
        self.add_user.place(x=550, y=100, width=180, height=50)
        enter_btn = Button(self.window5, command=self.enter3, text="Add", fg="white", bg="#d77337", bd=0,
                           font=("times new roman", 12)).place(x=550, y=150, width=180, height=40)

    def enter3(self):
        user = self.add_user.get()
        f2 = open("All_Restaurants.txt", "a")
        f2.writelines(user+"\n")
        f2.close()

    def view_DeliveryAgent(self):
        self.window7 = Tk()
        self.window7.title("Delivery Agent")
        self.window7.geometry("1000x1000")
        delete_btn = Button(self.window7, command=self.delete1, text="Delete Delivery Agent", fg="white", bg="#d77337", bd=0,
                            font=("times new roman", 12)).place(x=0, y=0, width=180, height=40)
        view_btn = Button(self.window7, command=self.view1, text="View Delivery Agents", fg="white", bg="#d77337", bd=0,
                          font=("times new roman", 12)).place(x=350, y=0, width=180, height=40)
        exit_btn = Button(self.window7, command=self.window7.destroy, text="Back", fg="white", bg="#d77337", bd=0,
                          font=("times new roman", 12)).place(x=700, y=0, width=180, height=40)

    def view1(self):
        f1 = open("DeliveryAgent.txt", "r")
        file_reader1 = csv.reader(f1)
        i = 0
        for row in file_reader1:
            view_user = Label(self.window7, text=row[0], font=("Goudy old style", 15, "bold"), fg="red",
                              bg="yellow").place(x=350, y=i + 40, width=180, height=40)
            i = i + 40
        f1.close()
    def delete1(self):
        delete_user = Label(self.window7, text="Enter Delivery Agent's name to remove", font=("Goudy old style", 10, "bold"),
                            fg="red",bg="yellow").place(x=0, y=40, width=180, height=40)
        self.dlt_user = Entry(self.window7, font=("times new roman", 15), bg="lightgray")
        self.dlt_user.place(x=0, y=100, width=180, height=50)
        enter_btn = Button(self.window7, command=self.enter1, text="Delete", fg="white", bg="#d77337", bd=0,
                           font=("times new roman", 12)).place(x=0, y=150, width=180, height=40)

    def enter1(self):
        user = self.dlt_user.get()
        f2 = open("DeliveryAgent.txt", "r")
        output = []
        for line in f2:
              if not line.startswith(user):
                  output.append(line)
        f2.close()
        print(output)
        f2 = open("DeliveryAgent.txt", 'w')
        f2.writelines(output)
        f2.close()

def main():
    karl().mainloop()
if __name__ == '__main__':
    main()