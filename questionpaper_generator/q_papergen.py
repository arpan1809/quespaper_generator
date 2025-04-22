from tkinter import *
from tkinter import messagebox
import random
from PIL import Image,ImageTk
import mysql.connector


## Main display class showing various options
class windows():
    def __init__(self):
        self.screen=Tk()
        self.screen.title("Question paper generator")
        self.font='Times New Roman'

        #size and initial position of the window
        self.screen.geometry("1100x700+200+50")

        #colour of screen
        self.canva= Canvas(self.screen, width= 1200, height= 800)
        self.canva.pack()
        self.img= ImageTk.PhotoImage(Image.open("bg_main.png"))
        self.canva.create_image(0,0,anchor=NW,image=self.img)

        #self.canva.create_text(550,100,text="\tWELCOME TO \nQUESTION PAPER GENERATOR",font=(self.font,30,'bold'),fill='black')
        #fix window size 
        self.screen.maxsize(1100,700)
        self.screen.minsize(1100,700)

        #creating buttons
        self.add_ques=Button(self.screen,text="ADD QUESTIONS",fg="#02203d",font=(self.font,15,'bold'),bg="#fba75b",activebackground="#6d7a6d",command=lambda:self.add())
        self.add_ques.place(x=420,y=310,height=50,width=300)

        self.generate=Button(self.screen,text="GENERATE PAPER",fg="#02203d",font=(self.font,15,'bold'),bg="#fba75b",activebackground="#6d7a6d",command=lambda:self.generator())
        self.generate.place(x=420,y=430,height=50,width=300)

        self.add_ques=Button(self.screen,text="ADD SUBJECTS",fg="#02203d",font=(self.font,15,'bold'),bg="#fba75b",activebackground="#6d7a6d",command=lambda:self.add_sub())
        self.add_ques.place(x=420,y=540,height=50,width=300)

    ## 
    def add(self):
        self.screen.destroy()
        screen=Tk()

        #destuction function
        def destruction():
            screen.destroy()
            self.__init__()

        #size and initial position of the window
        screen.geometry("1100x700+200+50")


        #Colour of screen
        canva=Canvas(screen,width=1200,height=700)
        canva.pack()
        global img_add
        img_add=ImageTk.PhotoImage(Image.open("bg.png"))
        canva.create_image(0,0,anchor=NW,image=img_add)
        #fix window size 
        screen.maxsize(1100,700)
        screen.minsize(1100,700)

         #creating Labels
        lable=Label(screen,text="ADD YOUR QUESTIONS",bg="#02203d",fg="white",font=(self.font,30,'bold')).place(x=330,y=30)
        label=Label(screen,text="Subject:",bg='#02203d',fg="white",font=(self.font,15)).place(x=150,y=170)
        label=Label(screen,text="Mark:",bg='#02203d',fg="white",font=(self.font,15)).place(x=700,y=170)
        label=Label(screen,text="Enter Question:",font=(self.font,15),bg="#02203d",fg="white").place(x=150,y=320)

        #creating input box
        question=Entry(screen,font=(self.font,20))
        question.place(x=150,y=350,height=50,width=750)

        #creating menu
        marks_options=["1","3","5"]
        marks_value_inside=StringVar(screen)
        marks_value_inside.set("select marks")
        marks=OptionMenu(screen,marks_value_inside,*marks_options)
        marks.place(x=700,y=200,height=50,width=200)

        #creating menu
        cursor.execute("show tables")
        tables=cursor.fetchall()
        sub_options=[]
        if(len(tables) == 1):
            sub_options=["No Subjects"]
        else:
            for i in tables:
                if i[0]!='info':
                    sub_options.append(i[0])
        sub_value_inside=StringVar(screen)
        sub_value_inside.set("select subject")
        subject=OptionMenu(screen,sub_value_inside,*sub_options)
        subject.place(x=150,y=200,height=50,width=500)

         

        #creating buttons
        add_ques=Button(screen,text="ADD",fg="#02203d",font=(self.font,20,'bold'),bg="#fba75b",command=lambda:self.get_values(question,sub_value_inside,marks_value_inside))
        add_ques.place(x=200,y=500,height=70,width=300)
        generate=Button(screen,text="DONE",fg="#02203d",font=(self.font,20,'bold'),bg="#fba75b",command=lambda:destruction())
        generate.place(x=550,y=500,height=70,width=300)

    def get_values(self,question,sub,marks):
        ques=question.get()
        mark=marks.get()
        subject=sub.get()
        cmd="insert into {} values(\"{}\",{})".format(subject,ques,mark)
        cursor.execute(cmd)
        db.commit()

    def generator(self):
        self.screen.destroy()
        screen=Tk()

        #destuction function
        def destruction():
            screen.destroy()
            self.__init__()


        #size and initial position of the window
        screen.geometry("1100x700+200+50")

        #solour of screen
        canva=Canvas(screen,width=1200,height=700)
        canva.pack()
        global img_gen
        img_gen=ImageTk.PhotoImage(Image.open("bg.png"))
        canva.create_image(0,0,anchor=NW,image=img_gen)
        #fix window size 
        screen.maxsize(1100,700)
        screen.minsize(1100,700)

        #LABELS
        Title=Label(screen,text="Paper Title",bg='#02203d',fg="white",font=('bold',12)).place(x=100,y=50)
        Title=Label(screen,text="Maximun Marks",bg='#02203d',fg="white",font=('bold',12)).place(x=100,y=250)
        Title=Label(screen,text="College Name",bg='#02203d',fg="white",font=('bold',12)).place(x=100,y=150)
        Title=Label(screen,text="Subject",bg='#02203d',fg="white",font=('bold',12)).place(x=600,y=50)
        Title=Label(screen,text="1 Mark Questions",bg='#02203d',fg="white",font=('bold',12)).place(x=100,y=350)
        Title=Label(screen,text="3 Mark Questions",bg='#02203d',fg="white",font=('bold',12)).place(x=100,y=450)
        Title=Label(screen,text="5 Mark Questions",bg='#02203d',fg="white",font=('bold',12)).place(x=100,y=550)
        Title=Label(screen,text="Sets",bg='#02203d',fg="white",font=('bold',12)).place(x=600,y=150)

        #Entry
        entry1=Entry(screen)
        entry1.place(x=100,y=80,width=400,height=40)

        entry2=Entry(screen)
        entry2.place(x=100,y=180,width=400,height=40)

        entry3=Entry(screen)
        entry3.place(x=100,y=280,width=400,height=40)

        entry4=Entry(screen)
        entry4.place(x=100,y=380,width=400,height=40)

        entry5=Entry(screen)
        entry5.place(x=100,y=480,width=400,height=40)

        entry6=Entry(screen)
        entry6.place(x=100,y=580,width=400,height=40)

        entry7=Entry(screen)
        entry7.place(x=600,y=180,width=400,height=40)

        #Menu
        cursor.execute("show tables")
        tables=cursor.fetchall()
        sub_options=[]
        if(len(tables) == 1):
            sub_options=["No Subjects"]
        else:
            for i in tables:
                if i[0]!='info':
                    sub_options.append(i[0])
        sub_value_inside=StringVar(screen)
        sub_value_inside.set("select subject")
        subject=OptionMenu(screen,sub_value_inside,*sub_options)
        subject.place(x=600,y=80,height=40,width=400)
        #Buttons
        button1=Button(screen,text="Done",fg="#02203d",font=(self.font,20,'bold'),bg="#fba75b",command=lambda:self.get_data(sub_value_inside,entry1,entry2,entry3,entry4,entry5,entry6,entry7))
        button1.place(x=600,y=430,height=40,width=400)

        button2=Button(screen,text="Back",fg="#02203d",font=(self.font,15),bg="#fba75b",command=lambda:destruction())
        button2.place(x=10,y=10,height=40,width=70)


    def get_data(self,sub,e1,e2,e3,e4,e5,e6,e7):
        sub=sub.get()
        entry1=e1.get()
        entry2=e2.get()
        entry3=e3.get()
        entry4=e4.get()
        entry5=e5.get()
        entry6=e6.get()
        entry7=e7.get()
        values="insert into info values(\"{}\",\"{}\",\"{}\",{},{},{},{},{})".format(sub,entry1,entry2,int(entry3),int(entry4),int(entry5),int(entry6),int(entry7))

        if((sub=="select subject") or (entry4==''or entry4.isalpha()) or (entry5==''or entry5.isalpha()) or (entry6=='' or entry6.isalpha())):
            messagebox.showerror("error","ENTER VALID VALUES")
        else:

            command="delete from info"
            cursor.execute(command)
            db.commit()
            cursor.execute(values)
            db.commit()
            done()
        
    def sub_create(self,entry):
        val=entry.get()
        l=val.split(',')
        for i in l:
            try:
                cursor.execute("create table {}(ques varchar(200), mark int)".format(i))
            except mysql.connector.Error:
                messagebox.showwarning("Dudeeeeee!","{} already exists!".format(i))

    def add_sub(self):
        def destruction():
            screen.destroy()
            self.__init__()

        self.screen.destroy()
        screen=Tk()
        canva=Canvas(screen,width=1200,height=700)
        canva.pack()
        global img_gen
        img_gen=ImageTk.PhotoImage(Image.open("bg.png"))
        canva.create_image(0,0,anchor=NW,image=img_gen)

        screen.geometry("600x400+360+140")
        screen.maxsize(600,400)
        screen.minsize(600,400)

        canva.create_text(320,50,text="Add Subject",fill="white",font=(self.font,25,'bold'))

        canva.create_text(300,150,text="SUBJECT(s)",fill="white",font=(self.font,15,'bold'))
        canva.create_text(310,250,text="(use  \',\' if adding multiple sujects)",font=(self.font,10,"bold"),fill='red')

        entry=Entry(screen)
        entry.place(x=120,y=170,height=50,width=400)

        button=Button(screen,text="ADD",font=(self.font,20),bg="#fba75b",command=lambda:self.sub_create(entry))
        button.place(x=200,y=330,width=200,height=50) 
        
        button=Button(screen,text="back",font=(self.font,10),bg="#fba75b",command=lambda:destruction())
        button.place(x=20,y=20,width=40,height=30) 
        
class question_paper():
    def __init__(self):

        cursor.execute("select * from info")
        data=cursor.fetchone()
        self.subject=data[0]
        self.title=data[1]
        self.clg=data[2]
        self.max_mark=data[3]
        self.mark1=data[4]
        self.mark3=data[5]
        self.mark5=data[6]
        self.set=data[7]


    def extract(self):
        for i in range(self.set):    
            file=self.subject+"paper{}.txt".format(i+1)

            paper=open(file,'w')
            paper.close()

            paper=open(file,'a')
            paper.write("             \t\t\t\t "+self.title+'\n')
            paper.write("             \t\t\t\t "+self.clg+'\n')
            paper.write("Subject:"+self.subject+" \t\t\t\t\t\t\t\t\t\t\t\tMM:"+str(self.max_mark)+'\n')
            
            cursor.execute("select ques from {} where mark=1".format(self.subject))
            data_mark1=cursor.fetchall()
            cursor.execute("select ques from {} where mark=3".format(self.subject))
            data_mark3=cursor.fetchall()
            cursor.execute("select ques from {} where mark=5".format(self.subject))
            data_mark5=cursor.fetchall()

            paper.write("A.Answer the following for 1 marks.\n")

            for i in range(self.mark1):
                ques=random.choice(data_mark1)
                paper.write('\t'+str(i+1)+"."+ques[0]+'\n')
                data_mark1.remove(ques)

            paper.write("\nB.Answer the following for 3 marks.\n")

            for i in range(self.mark3):
                ques=random.choice(data_mark3)
                paper.write('\t'+str(i+1)+"."+ques[0]+'\n')
                data_mark3.remove(ques)

            paper.write("\nC.Answer the following for 5 marks.\n")

            for i in range(self.mark5):
                ques=random.choice(data_mark5)
                paper.write('\t'+str(i+1)+"."+ques[0]+'\n')
                data_mark5.remove(ques)

            paper.close()
  

class preview():
    def __init__(self):
        self.font="Times New Roman"
        self.screen=Tk()
        self.screen.geometry("700x750+200+10")
        self.screen.minsize(700,750)
        self.screen.maxsize(700,750)
        cursor.execute("select * from info")
        data=cursor.fetchone()
        self.subject=data[0]
        self.title=data[1]
        self.clg=data[2]
        self.max_mark=data[3]
        self.mark1=data[4]
        self.mark3=data[5]
        self.mark5=data[6]
        self.set=data[7]
        self.x=50
        self.y=100


    def pre(self):
        label=Label(self.screen,text=(self.title).upper()).pack(anchor=CENTER)
        label=Label(self.screen,text=(self.clg).upper()).pack(anchor=CENTER)
        label=Label(self.screen,text="Subject:"+(self.subject).upper()).pack(anchor=W)
        label=Label(self.screen,text="MM:"+str(self.max_mark)).pack(anchor=E)
        label=Label(self.screen,text="Q1.Answer the following for 1 mark.",font=(self.font,12)).place(x=10,y=70)
        for i in range(self.mark1):
            label=Label(self.screen,text="Q{}.question.".format(i+1),font=(self.font,12)).place(x=self.x,y=self.y)
            self.y+=30
        label=Label(self.screen,text="Q1.Answer the following for 1 mark.",font=(self.font,12)).place(x=10,y=self.y)
        self.y+=30
        for i in range(self.mark3):
            label=Label(self.screen,text="Q{}.question.".format(i+1),font=(self.font,12)).place(x=self.x,y=self.y)
            self.y+=30
        label=Label(self.screen,text="Q1.Answer the following for 1 mark.",font=(self.font,12)).place(x=10,y=self.y)
        self.y+=30
        for i in range(self.mark5):
            label=Label(self.screen,text="Q{}.question.".format(i+1),font=(self.font,12)).place(x=self.x,y=self.y)
            self.y+=30


def done():
    screen=Tk()
    screen.geometry("500x300+460+240")
    screen.minsize(500,300)
    screen.maxsize(500,300)
    canva=Canvas(screen,bg="#02203d")
    canva.place(x=0,y=0,width=700,height=600)
    button1=Button(screen,text="generate",bg='#333333',fg='#ffffff',command=lambda:generate())
    button1.place(x=100,y=50,height=75,width=300)
    button2=Button(screen,text="preview",bg='#333333',fg='#ffffff',command=lambda:func_preview())
    button2.place(x=100,y=175,height=75,width=300)



def func_preview():
    pre=preview()
    pre.pre()

def generate():
    paper=question_paper()
    paper.extract() 

def get(entry):
    global password
    password=entry.get()
    login(password)

def start():
    global screen
    screen=Tk()
    screen.geometry("200x200+400+200")
    screen.minsize(200,200)
    screen.maxsize(200,200)

    label=Label(screen,text="Password:").place(x=50,y=20)
    entry=Entry(screen)
    entry.place(x=50,y=50)
    button=Button(screen,text="connect",command=lambda:get(entry)).place(x=50,y=100)
    mainloop()


def login(p):
    try:
        global cursor,db
        db=mysql.connector.connect(host="localhost",user="root",password=p)
        screen.destroy()
        cursor=db.cursor()

        try:
            cursor.execute("use question_bank")
        except mysql.connector.Error as no_database:
            messagebox.showinfo("No Database","No current Database Exist\n Created one!!")
            cursor.execute("create database question_bank")
            cursor.execute("use question_bank")
            db.commit()
            cursor.execute("create table info(subject varchar(50) , paper_title varchar(50) , clg_name varchar(50) , MM int, ques_1 int , ques_3 int, ques_5 int, sets int)")
        windows() 
    except mysql.connector.Error as ex:
        messagebox.showerror("error","wrong password")

start()