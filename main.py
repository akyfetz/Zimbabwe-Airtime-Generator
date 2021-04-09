#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:16:21 2020

@author: akylwnnfetzmede
"""

#=============================[LIBRARIES]=====================================
from tkinter import*
import random
from tkinter import Menu, messagebox
import sqlite3
import tkinter.ttk as ttk

#=============================[GLOBAL VARS]=====================================
author = 'Akylwnn Fetzmede'
title = 'Zimbabwe Airtime Generator'
contact = "hyltechsys@gmail.com"
version = '1.0'

#==============================[APP WINDOW]====================================
app=Tk()
app.title(title + " v" + version)
app.geometry("470x360")
app.resizable(0, 0)
app.config(bg="#E4D4EC")

#=============================[VARIABLES]===================================
Rech =StringVar()
Rech.set(" ____ ____ ____ ____ ")
cd =StringVar()
cd.set(" * ___ *")
info="\tGenerated Numbers"

#===========================[FUNCTIONS]=====================================
def abt():
	abtinfo=messagebox.showinfo("About", title + "\nVersion " +version)

def database():
	global conn, cursor
	conn = sqlite3.connect('airtime.db')
	cursor = conn.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS `result` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, ntwrk_nm TEXT, rec_nmbr TEXT)")

def read():
	global tree
	scrollbary = Scrollbar(dbfr,orient=VERTICAL)
	scrollbarx = Scrollbar(dbfr,orient=HORIZONTAL)
	style=ttk.Style()
	tree = ttk.Treeview(dbfr, columns=("id", "ntwrk_nm", "rec_nmbr"),style="mystyle.Treeview", height=10, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
	style.configure("mystyle.Treeview", background="#E4D4EC", foreground="#7D497D", fieldbackground="#E4D4EC")
	tree.heading('id', text="ID", anchor=W)
	tree.heading('ntwrk_nm', text="Network Name", anchor=W)
	tree.heading('rec_nmbr', text="Recharge Number", anchor=W)
	tree.column('#0', stretch=NO, minwidth=0, width=0)
	tree.column('#1', stretch=NO, minwidth=0, width=100)
	tree.column('#2', stretch=NO, minwidth=0, width=60)
	tree.grid(row=1,column=0, padx=20,sticky='e')
	tree.delete(*tree.get_children())

	database()
	cursor.execute("SELECT * FROM `result` ORDER BY `id` ASC")
	fetch = cursor.fetchall()
	for data in fetch:
		tree.insert('', 'end', values=(data[0], data[1], data[2]))
	cursor.close()
	conn.close()

def frame_raise(frame):
    frame.tkraise()

def close():
    frame_raise(appfr)
	
def Reset():
    Rech.set(" ____ ____ ____ ____ ")
    cd.set(" * ___ *")

def NumGen():
	global rec_pin
	fst=str(random.randint(0000,9999))
	snd=str(random.randint(0000,9999))
	trd=str(random.randint(0000,9999))
	rec_pin=(" "+"0"*(4-len(fst))+fst+" "+"0"*(4-len(snd))+snd+" "+"0"*(4-len(trd))+trd)
	if (rec_pin.count('0') or rec_pin.count('1') or rec_pin.count('2') or rec_pin.count('3') or rec_pin.count('4') or
		rec_pin.count('5') or rec_pin.count('6') or rec_pin.count('7') or rec_pin.count('8') or rec_pin.count('9')) <3:
		NumGen()
	else:
		pass
		
def Econet():
	global rec_pin
	Rech.set("")
	cd.set(" * 121 *")
	eco=str(random.randint(00000,99999))
	NumGen()
	ecnt=(" "+"0"*(5-len(eco))+eco+" "+rec_pin+"")
	Rech.set(ecnt)
	database()
	cursor.execute("INSERT INTO 'result' (ntwrk_nm, rec_nmbr) VALUES(?, ?)",(  "Econet", ecnt))
	conn.commit()
	read()

def Net1():
	global rec_pin
	cd.set(" * 133 *")
	Rech.set("")
	net=str(random.randint(0,4))
	NumGen()
	#net1_$500
	net1=(" 204"+"0"*(1-len(net))+net+" "+rec_pin+"")
	Rech.set(net1)
	database()
	cursor.execute("INSERT INTO 'result' (ntwrk_nm, rec_nmbr) VALUES(?, ?)",(  "NetOne", net1))
	conn.commit()
	read()

def Telecel():
	global rec_pin
	Rech.set("")
	cd.set(" * 123 *")
	tel=str(random.randint(0000,9999))
	NumGen()
	tcl=(" "+"0"*(4-len(tel))+tel+" "+rec_pin+"")
	Rech.set(tcl)
	database()
	cursor.execute("INSERT INTO 'result' (ntwrk_nm, rec_nmbr) VALUES(?, ?)",( "Telecel", tcl))
	conn.commit()
	read()

#=============================[MENUBAR]=====================================
menubar = Menu(app)
file= Menu(menubar, tearoff = 0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="Database",command=lambda:frame_raise(dbfr))
file.add_command(label="Exit", command =app.destroy)
help=Menu(menubar, tearoff=0)
help.add_command(label="About", command=abt)
menubar.add_cascade(label="Help", menu=help)

#=============================[FRAMES]======================================
appfr=Frame(app, height=80, width=480, bg="#E4D4EC")
dbfr=Frame(app, height=80, width=480, bg="#E4D4EC")

for frame in (appfr,dbfr):
    frame.grid(row=1,column=0, sticky='news')
 
#app_frames
topfrm=Frame(app, height=70, width=480, bg="#d8b8e0", relief=RAISED)    
topfrm.grid(row=0,column=0,sticky='news')
frm1=Frame(appfr,height=80, width=480, bg="#E4D4EC")
frm1.grid(row=1,column=0,sticky='news')
frm2=Frame(appfr,height=80, width=480, bg="#E4D4EC")
frm2.grid(row=2,column=0,sticky='news')

#==============================[LABELS]====================================
appttle=Label(topfrm,font=('michroma',16,'bold'),fg="purple",text="Zimbabwe Airtime Generator",bg="#d8b8e0",bd=20,anchor='w')
appttle.grid(row=0,column=0,sticky='e')
apptt2=Label(appfr,font=('purisa',11,'bold'),fg="purple",text="Supported Networks",bg="#E4D4EC",bd=8,anchor='w')
apptt2.grid(row=0,column=0)
abt=Label(dbfr,font=('purisa',11,'bold'),fg="#7D497D",text=info,bg="#E4D4EC",bd=5,anchor='w')
abt.grid(row=0,column=0)
blnk=Label(frm1,font=('michroma',17,'bold'),fg="purple",text="   ",bg="#E4D4EC",bd=15,anchor='w')
blnk.grid(row=0,column=0)
outlf=LabelFrame(frm2, text="Output", font=('purisa',9),bg="#E4D4EC",height=90, fg="purple",width=480, highlightbackground="purple")
outlf.grid(row=0,column=0,padx=12, pady=5, sticky='se', columnspan="2")

#==============================[BUTTONS]====================================
Ntn=Button(frm1,bd=20,font=('chilanka',12,'bold'),fg="silver", text="NetOne",bg="purple",cursor="heart", command=Net1).grid(row=0,column=1)
Ecnt=Button(frm1,bd=20,font=('chilanka',12,'bold'),fg="silver", text="Econet",bg="purple",cursor="heart", command=Econet).grid(row=0,column=2)
Tlcl=Button(frm1,bd=20,font=('chilanka',12,'bold'),fg="silver", text="Telecel",bg="purple",cursor="heart", command=Telecel).grid(row=0,column=3)
Rst=Button(frm2,bd=8,font=('chilanka',11,'bold'),fg="silver", text="Reset",bg="purple", command=Reset).grid(row=1,column=0, sticky='e')
cls=Button(dbfr,bd=0,font=('nice',9,'bold'),fg="#7D497D", text="Close",bg="#E2E2E2",cursor="heart", command=close).grid(row=2,column=1, sticky="se")

#===============================[OUTPUT]====================================
lblRech=Label(outlf,font=('gentium',16,'bold'),fg="#a04cbc",bd=20, bg="#E4D4EC",textvariable=cd,anchor='w')
lblRech.grid(row=0,column=0)
txtRech=Label(outlf,font=('gentium',16,'bold'), bg="#E4D4EC",highlightcolor="purple",relief=RAISED,bd=1, fg="#a04cbc",width=20, textvariable=Rech)
txtRech.grid(row=0,column=1, padx=15)
Output2=Label(outlf,font=('gentium',16,'bold'),fg="#a04cbc", bg="#E4D4EC",text="#",bd=20,anchor='sw')
Output2.grid(row=0,column=2)

#==============================[APP LOOP]=====================================
read()
frame_raise(appfr)
app.config(menu=menubar)
app.mainloop()
