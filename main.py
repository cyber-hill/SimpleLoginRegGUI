import  db,hashlib,sqlite3,tkinter
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Մուտք")
root.geometry('250x250')
closestate=False
loginbut=Button(root, text="Մուտք գործել", width=15, height=1,font="helvetica 11 italic")
label=Label(root, text="կամ",font="helvetica 11 italic")
regbutton=Button(root, text="Գրանցվել", width=15, height=1,font="helvetica 11 italic")

def on_closing():
    if closestate==False:
        root.destroy()
    elif closestate == True:
        pass
def login():
    conn = sqlite3.connect("main.db", check_same_thread=False)
    cursor = conn.cursor()
    global closestate
    closestate=True
    loginbut.config(state=DISABLED)
    regbutton.config(state=DISABLED)
    loginpage=Tk()

    def on_closings():
        global closestate
        closestate = False
        loginbut.config(state=NORMAL)
        regbutton.config(state=NORMAL)
        loginpage.destroy()
    loginpage.title("Մուտք գործել")
    loginpage.geometry('350x125')
    Label(loginpage, text="Մուտքանուն",font="helvetica 11 italic").place(x=10, y=10)
    Label(loginpage, text="Գաղտնաբառ",font="helvetica 11 italic").place(x=10, y=40)

    e1 = Entry(loginpage,width=30)
    e1.place(x=140, y=10)
    e2 = Entry(loginpage,width=30)
    e2.place(x=140, y=40)
    e2.config(show='*')
    def checklogin():
        username=e1.get()
        password=e2.get()
        if not username and not password:
            messagebox.showerror("Սխալ", "Գաղտնաբառը և մուտքանունը դատարկ է")
        elif not username:
            messagebox.showerror("Սխալ", "Մուտքանունը դատարկ է")
        elif not password:
            messagebox.showerror("Սխալ", "Գաղտնաբառը դատարկ է")
        try:
            hash_object = hashlib.sha256(password.encode('utf-8'))
            password_hash = hash_object.hexdigest()
            user = cursor.execute(f'SELECT * FROM users WHERE Username = "{username}"').fetchall()
            if not user and username and password:
                messagebox.showerror("Սխալ", "Մուտքանունը սխալ է։")
            elif user:
                defuser = user[0]
                if defuser[2]==password_hash:
                    messagebox.showinfo('❗','Դուք հաջողությամբ մուտք եղաք համակարգ')
                elif defuser[2] != password_hash:
                    messagebox.showerror("Սխալ", "Գաղտնաբառը սխալ է։")

        except EXCEPTION as e:
            print(e)
            messagebox.showerror("Սխալ", "Մուտքի ժամանակ տեղի է ունեցել սխալ։Փորձեք նորից։")

    Button(loginpage, text="Մուտք", command=checklogin, height=1, width=13,font="helvetica 11 italic").place(x=120, y=80)
    loginpage.protocol("WM_DELETE_WINDOW", on_closings)

    loginpage.mainloop()
def register():
    conn = sqlite3.connect("main.db", check_same_thread=False)
    cursor = conn.cursor()
    global closestate
    closestate=True
    loginbut.config(state=DISABLED)
    regbutton.config(state=DISABLED)
    registerpage=Tk()
    def reginfo():
        messagebox.showinfo('❗','** Մուտքանունը պետք է լինի ունիկալ\n** Գաղտանաբառը պետք է լինի առնվազն 8 նիշ և \nառավելագույնը 32 նիշ')

    def on_closings():
        global closestate
        closestate = False
        loginbut.config(state=NORMAL)
        regbutton.config(state=NORMAL)
        registerpage.destroy()
    registerpage.title("Գրանցվել")
    registerpage.geometry('400x200')
    # Label(registerpage, text="** Մուտքանունը պետք է լինի ունիկալ\n** Գաղտանաբռը պետք է լինի առնվազն 8 նիշ և \nառավելագույնը 32 նիշ").place(x=10, y=1)
    Label(registerpage, text="Անուն,Ազգանուն",font="helvetica 11 italic").place(x=10, y=10)
    Label(registerpage, text="Մուտքանուն",font="helvetica 11 italic").place(x=10, y=40)
    Label(registerpage, text="Գաղտնաբառ",font="helvetica 11 italic").place(x=10, y=70)
    Label(registerpage, text="Կրկնեք գաղտնաբառը",font="helvetica 11 italic").place(x=10, y=100)
    e1 = Entry(registerpage,width=30)
    e1.place(x=180, y=10)
    e2 = Entry(registerpage,width=30)
    e2.place(x=180, y=40)
    e3 = Entry(registerpage,width=30)
    e3.place(x=180, y=70)
    e4 = Entry(registerpage,width=30)
    e4.place(x=180, y=100)
    e3.config(show='*')
    e4.config(show='*')
    def checkreg():
        fullname=e1.get()
        username=e2.get()
        password=e3.get()
        password1=e4.get()

        if not fullname or not username or not password or not password1:
            messagebox.showerror("Սխալ", "Բոլոր դաշտերը պարտադիր են լրացման համար")
        elif len(password) < 8 or len(password1) < 8:
            messagebox.showerror("Սխալ", "Գաղտնաբառը պետք է լինի առնվազն 8 նիշ")
        elif len(password) > 32 or len(password1) > 32:
            messagebox.showerror("Սխալ", "Գաղտնաբառը պետք է լինի առավելագույնը 32 նիշ")
        elif password != password1:
            messagebox.showerror("Սխալ", "Գաղտնաբառերը չեն համընկնում")
        user = cursor.execute(f'SELECT * FROM users WHERE Username = "{username}"').fetchall()
        if user:
            messagebox.showerror("Սխալ", "Մուտքանունը զբաղված է։")
        elif not user and password and password1 and fullname and (len(password) >= 8 and len(password1) >= 8) and (len(password) <= 32 or len(password1) <= 32) and password==password1:
            try:
                db.adduser(fullname,username,password)
                messagebox.showinfo('❗', 'Դուք հաջողությամբ գրանցվեցիք')
            except EXCEPTION as e:
                print(e)
                messagebox.showerror("Սխալ", "Գրանցման ժամանակ տեղի է ունեցել սխալ։Փորձեք նորից։")
    Button(registerpage, text="Գրանցվել",font="helvetica 11 italic", command=checkreg, height=1, width=9).place(x=90, y=130)
    Button(registerpage, text="❗",font="helvetica 11 italic", command=reginfo, height=1, width=5).place(x=210, y=130)
    registerpage.protocol("WM_DELETE_WINDOW", on_closings)

    registerpage.mainloop()
Label(root, text="").pack(pady=20)
loginbut.config(command=login)
regbutton.config(command=register)
loginbut.pack(pady=5)
label.pack()
regbutton.pack(pady=5)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()