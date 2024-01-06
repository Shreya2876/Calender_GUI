from tkinter import *
import calendar

def showCalender():
  gui=Tk()
  gui.config(background='yellow')
  gui.title('Calender')
  gui.geometry("700x1000")
  year=int(year_field.get())
  gui_content=calendar.calendar(year)
  calYear=Label(gui,text=gui_content,font="Consolas 10 bold")
  calYear.grid(row=10,column=10,padx=20)
  gui.mainloop()

def quitApplication():
  new.destroy()
  
if __name__=='__main__':
  new=Tk()
  new.config(background='yellow')
  new.title('Calender')
  new.geometry("700x1000")
  cal=Label(new,text="Calender",bg='orange',font=("times",28,"bold"))
  year=Label(new,text="Enter year",bg='dark grey')
  year_field=Entry(new)
  button=Button(new,text='Show Calender',fg='Black',bg='Blue',command=showCalender)
  exit_button = Button(new, text='Quit', fg='black', bg='red', command=quitApplication)
  cal.grid(row=1,column=5)
  year.grid(row=2,column=1)
  year_field.grid(row=3,column=1)
  button.grid(row=4,column=1)
  exit_button.grid(row=6,column=1)
  new.mainloop()
