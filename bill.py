import tkinter
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox


window = tkinter.Tk()
window.title("Pledge form details")
frame = tkinter.Frame(window)
frame.pack()


#for getting today date
def getdate(event):
    todaydate = datetime.now().strftime("%d/%m/%Y")
    billdate_Entry.delete(0,tkinter.END)
    billdate_Entry.insert(0,todaydate)

def intgetdate(event):
    todaydate = datetime.now().strftime("%d/%m/%Y")
    billdateint_Entry.delete(0,tkinter.END)
    billdateint_Entry.insert(0,todaydate)


#for getting the data
def enter_data():
    billno = billno_Entry.get()
    if billno:
        billdate = billdate_Entry.get()
        intdate = billdateint_Entry.get()
        name = name_Entry.get()
        address = address_Entry.get()
        loan = loantype_Entry.get()
        type = loantype1_Entry.get()
        particulars = details_entry.get()
        grossweight = gwt_Entry.get()
        netweight = nwt_Entry.get()
        pieces  = pieces_Entry.get()
        value = value_Entry.get()
        roi = roi_Entry.get()

        print(billno)
        print(billdate)
        print(intdate)
        print(name)
        print(address)
        print(loan,type)
        print(particulars)
        print(grossweight," ",netweight)
        print(pieces)
        print(value)
        print(roi)
        print("----------------------------------------")
    else:
        tkinter.messagebox.showwarning(title="error",message="Bill no required")

#First layout
bill_no_frame = tkinter.LabelFrame(frame)
bill_no_frame.grid(row=0,column=0,padx=20,pady=20)

#billno
billno_label = tkinter.Label(bill_no_frame,text="BILL NO : ")
billno_label.grid(row=0,column=0)
billno_Entry = tkinter.Entry(bill_no_frame)
billno_Entry.grid(row=0,column=1)

#bill date
billdate_label = tkinter.Label(bill_no_frame,text="BILL DATE : ")
billdate_label.grid(row=0,column=2)
billdate_Entry = tkinter.Entry(bill_no_frame)
billdate_Entry.grid(row=0,column=3)

#interest date
billdateint_label = tkinter.Label(bill_no_frame,text='INTEREST DATE : ')
billdateint_label.grid(row=0,column=4)
billdateint_Entry = tkinter.Entry(bill_no_frame)
billdateint_Entry.grid(row=0,column=5)

#name
name_label = tkinter.Label(bill_no_frame,text='NAME : ')
name_label.grid(row=3,column=0)
name_Entry = tkinter.Entry(bill_no_frame)
name_Entry.grid(row=3,column=1)

#address
address_label = tkinter.Label(bill_no_frame,text='ADDRESS : ')
address_label.grid(row=4,column=0)
address_Entry = tkinter.Entry(bill_no_frame)
address_Entry.grid(row=4,column=1)


#loan type
loantype_label = tkinter.Label(bill_no_frame,text='LOAN TYPE :')
loantype_label.grid(row=5,column=0)
loantype_Entry = ttk.Combobox(bill_no_frame,values=['Gold','Silver','Other'])
loantype_Entry.current(0)
loantype_Entry.grid(row=5,column=1)

loantype1_Entry = ttk.Combobox(bill_no_frame,values=['Daily','Weekly','Monthly','Yearly'])
loantype1_Entry.current(2)
loantype1_Entry.grid(row=5,column=3)

#1 for space and view layout
for widget in bill_no_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)

#second layout
particulars_frame = tkinter.LabelFrame(frame)
particulars_frame.grid(row=1,column=0,sticky="news",padx=20,pady=20)

#particulars
details_label = tkinter.Label(particulars_frame,text='PARTICULARS')
details_label.grid(row=0,column=0)
details_entry = tkinter.Entry(particulars_frame)
details_entry.grid(row=0,column=1)

#2 for space and view layout
for widget in particulars_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)

#third layout
weight_frame = tkinter.LabelFrame(frame)
weight_frame.grid(row=2,column=0,sticky='news',padx=20,pady=20)

#gross weight
gwt_label = tkinter.Label(weight_frame,text='GROSS WEIGHT :')
gwt_label.grid(row=0,column=0)
gwt_Entry = tkinter.Entry(weight_frame)
gwt_Entry.grid(row=0,column=1)

#net weight
nwt_label = tkinter.Label(weight_frame,text='NET WEIGHT :')
nwt_label.grid(row=0,column=5)
nwt_Entry = tkinter.Entry(weight_frame)
nwt_Entry.grid(row=0,column=6)

#purity
purity_label = tkinter.Label(weight_frame,text='PURITY :')
purity_label.grid(row=1,column=0)
purity_Entry = tkinter.Entry(weight_frame)
purity_Entry.grid(row=1,column=1)

#pieces
pieces_label = tkinter.Label(weight_frame,text='PIECES :')
pieces_label.grid(row=1,column=2)
pieces_Entry = tkinter.Entry(weight_frame)
pieces_Entry.grid(row=1,column=3)

#value
value_label = tkinter.Label(weight_frame,text='VALUE :')
value_label.grid(row=1,column=5)
value_Entry = tkinter.Entry(weight_frame,state='disabled')
value_Entry.grid(row=1,column=6)

#principle amount
amt_label = tkinter.Label(weight_frame,text='PRINCIPLE AMOUNT :')
amt_label.grid(row=2,column=0)
amt_Entry = tkinter.Entry(weight_frame)
amt_Entry.grid(row=2,column=1)

#rate of interest
roi_label = tkinter.Label(weight_frame,text='RATE OF INTEREST :')
roi_label.grid(row=3,column=0)
roi_Entry = tkinter.Entry(weight_frame)
roi_Entry.grid(row=3,column=1)

#interest
int_label = tkinter.Label(weight_frame,text='INTEREST :')
int_label.grid(row=3,column=5)
int_Entry = tkinter.Entry(weight_frame,state='disabled')
int_Entry.grid(row=3,column=6)

#interest collected
intc_label = tkinter.Label(weight_frame,text='INTEREST COLLECTED :')
intc_label.grid(row=4,column=0)
intc_Entry = tkinter.Entry(weight_frame)
intc_Entry.grid(row=4,column=1)

#3 for space and view layout
for widget in weight_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)

#fourth layout
options = tkinter.LabelFrame(frame)
options.grid(row=3,column=0,sticky='news',padx=20,pady=20)

#save
save = tkinter.Button(options,text='Save',command=enter_data)
save.grid(row=0,column=0)

#modify
modify = tkinter.Button(options,text='modify')
modify.grid(row=0,column=1)

#check
check = tkinter.Button(options,text='check')
check.grid(row=0,column=2)

#delete
delete = tkinter.Button(options,text='delete')
delete.grid(row=0,column=3)

#exit
exit = tkinter.Button(options,text='exit')
exit.grid(row=0,column=4)

#4 for space and view layout
for widget in options.winfo_children():
    widget.grid_configure(padx=10,pady=10)


getdate(None)
intgetdate(None)

window.mainloop()