from tkinter import *
from tkinter import messagebox
import os

def submit():
	global screen3
	screen3 = Toplevel(screen)
	screen3.geometry("700x400")
	screen3.title("user List")
	username_info1 = username_verify.get()
	password_info1 = password_verify.get()
	Label(text="",height= '3',width='30').pack()
	# Label(screen3,text="Wellcome "+username_info1,font ="green",bg="light salmon",height= '2',width='30').pack()
	Label(screen3,text="Wellcome !  "+username_info1,bg="#c0ecc0", fg="black",
          width="300", height="2",font=("Calibri", 13)).pack(padx=20, pady=23 )
	Label(screen3,text="",height= '10',width='30').pack()
	Label(screen3,text="UserName :"+username_info1,font ="green",height= '2',width='30').pack()
	Label(screen3,text="Password :"+password_info1,font ="green",height= '2',width='30').pack()
	



def register_user():
	username_info = username.get()
	password_info = password.get()
	file = open(username_info,"w")
	file.write(username_info+"\n")
	file.write(password_info)
	file.close()
	Label(screen1,text= "Account Created Successfully...!",font ="green",height= '2',width='30').pack()


def register():
	global screen1
	screen1 = Toplevel(screen)
	screen1.geometry("700x400")
	screen1.title("register")
	global username 
	global password
	global username_entry
	global password_entry
	username = StringVar()
	password = StringVar()
	Label(screen1,text="Enter Details Below to Sign Up!",bg="#c0ecc0", fg="black",
          width="300", height="2",font=("Calibri", 13)).pack(padx=20, pady=23 )
	# Label(screen1,text="  Please Enter The Given Information  ",height ="2", width="30")
	Label(screen1,text="",height= '2',width='30').pack()
	Label(screen1,text="Username * ",height= '2',width='30').pack()
	username_entry= Entry(screen1,textvariable = username)
	username_entry.pack()
	Label(screen1,text="Password * ",height= '2',width='30').pack()
	password_entry = Entry(screen1,textvariable = password)
	password_entry.pack()
	Label(screen1,text="",height= '2',width='30').pack()
	Button(screen1,text="Submit",height= '2',width='30',bg="light salmon", command = register_user).pack()

def login_verify():
	username1 = username_verify.get()
	password1 = password_verify.get()
	list_of_dir = os.listdir()
	if username1 in list_of_dir:
		file = open (username1,"r")
		verify = file.read().splitlines()
		if password1 in verify:
			print ("Success")
			submit()
		else:
			messagebox.showerror("error","wrong password")
			print ("Wrong Password ")

	else :
		messagebox.showerror("error","User not found")
		print ("User not found ")


def login():
	global screnn2
	global username_verify
	global password_verify
	username_verify = StringVar()
	password_verify = StringVar()

	screen2 = Toplevel(screen)
	screen2.geometry("700x400")
	screen2.title("login")
	Label(screen2,text="Please enter the information for login!",bg="#f2d0d7", fg="black",
          width="300", height="2",font=("Calibri", 13)).pack(padx=20, pady=23 )
	# Label(screen2,text="Please enter the information for login ",height= '2',width='30').pack()
	Label(screen2,text="",height= '2',width='30').pack()
	Label(screen2,text="Username : ",height= '2',width='30').pack()
	username_entry1 = Entry(screen2,textvariable = username_verify)
	username_entry1.pack()
	Label(screen2,text="password : ",height= '2',width='30').pack()
	password_entry1 = Entry (screen2,textvariable = password_verify)
	password_entry1.pack()
	Label(screen2,text="",height= '2',width='30').pack()
	Button(screen2, text="login", height= "2",width="30",bg="spring green", command =login_verify).pack()


def main_screen():
	global screen
	screen = Tk()
	screen.geometry("700x400")
	Label(text="",height= '2',width='30').pack()
	Label(text="Login GUI Interface",font=SOLID).pack()
	Label(text="",height= '5',width='30').pack()
	Button(text="Login ",height= '2',width='30',bg="spring green",command = login).pack()
	Label(text="",height= '2',width='30').pack()
	Button(text="Register",height= '2',width='30',bg="light salmon", command= register).pack()
	screen.mainloop()

	


main_screen()


# screen.mainloop()
