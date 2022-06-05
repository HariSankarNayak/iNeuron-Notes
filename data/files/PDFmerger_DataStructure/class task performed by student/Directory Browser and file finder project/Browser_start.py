from tkinter import *
from Browser_path import getpath
from Browser_file import fetchfile
from Browser_logger import *

#lst_dir=[]
def start1():
    '''
    This function will start with creating the menu for Browser and File finder

    :return:
    '''
    writelogs('start1', 'info', 'started with browser menu building')
    root=Tk()
    root.title("Directory Browser and File Finder")
    try:

        label1=Label(root,text="Please enter the directory path",
                     background='pink',foreground='blue')
        label1.grid(row=0,column=0)
        e1=Entry(root,width=100,border=5,fg='green',bg='yellow')
        e1.grid(row=0,column=1)
        button1 = Button(root, text='Click here', command=lambda:getlist(e2),
                         background='green',foreground='orange')
        button1.grid(row=0, column=2)


        label=Label(root,text="List of files and Folders inside the given directory are: ",
                    background='orange',foreground='brown')
        label.grid(row=1,column=0)
        sb = Scrollbar(root,orient=VERTICAL)
        sb.grid(row=2,column=2,sticky=NS)
        e2=Text(root,height=10,width=60,fg='blue',bg='orange')
        e2.grid(row=2, column=1)
        e2.config(yscrollcommand=sb.set)
        sb.config(command=e2.yview)


        label2=Label(root,text="Enter the directory path to fetch .pdf files in it:  ",
                     background='blue',foreground='yellow')
        label2.grid(row=3,column=0)
        e3=Entry(root,width=100,border=5,bg='green',fg='yellow')
        e3.grid(row=3,column=1)
        button2 = Button(root, text="Click here", command=lambda: getfile(e4,e5),
                         background='red',foreground='blue')
        button2.grid(row=3, column=2)

        e4=Text(root,height=5,width=60,background='red',foreground='blue')
        e4.grid(row=4,column=1)
        label3=Label(root,text="List of pdf files in the given directory are:",
                     background='white',foreground='brown')
        label3.grid(row=4,column=0)
        label4=Label(root,text="The final Merged pdf file created is ",
                     background='pink',foreground='green')
        label4.grid(row=5,column=1)
        e5=Text(root,height=5,width=40,background='yellow',foreground='red')
        e5.grid(row=6,column=1)

    except Exception as e:
        writelogs('start1','error','Errorred occurred in module start1')
        writelogs('start1','exception',e)


    def getlist(e2):
        '''
        This Function calls the getpath function to get the list of directories in
        the given path '''
        writelogs('getlist','info','Entered to getlist')
        try:

            lst_dir=getpath(e1.get())
            e2.insert(END, str(lst_dir))
        except Exception as e:
            writelogs('getlist','error','Error occurred during listing files and directories')
            writelogs('getlist','exception',e)


    def getfile(e4,e5):
        '''
        This function will call the fetchfile to get the list of pdf files in the given
        path '''
        writelogs('getfile','info','entered into getfile')
        try:

            l,filename=fetchfile(e3.get())
            e4.insert(END, str(l))
            e5.insert(END, filename)
        except Exception as e:
            writelogs('getfile', 'error', 'Error occurred during listing .pdf files')
            writelogs('getfile', 'exception', e)

    root.mainloop()