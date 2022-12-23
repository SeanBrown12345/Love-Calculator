from tkinter import*
import tkinter.messagebox
from winsound import *
import random



class MyGUI:
    def __init__(self):
        
        self.x = 0
        
        PlaySound("music.wav", SND_LOOP | SND_ASYNC)
        self.mainwindow = Tk()
        self.mainwindow.geometry("500x1000+0+0")
        self.mainwindow.title("Love Compatability Calculator")
        self.frame1=Frame(self.mainwindow, width=500, height=1000, bg="yellow")
        self.frame1.place(x=0,y=0)
        self.frame2=Frame(self.frame1, width=450, height=150, bg="pink", highlightthickness=3, highlightcolor="black", highlightbackground="black")
        self.frame2.place(x=25,y=450)
        self.frame3=Frame(self.frame1, width=230, height=150, bg="lightcyan", highlightthickness=3, highlightcolor="black", highlightbackground="black")
        self.frame3.place(x=10,y=750)
        self.frame4=Frame(self.frame1, width=230, height=150, bg="lightcyan", highlightthickness=3, highlightcolor="black", highlightbackground="black")
        self.frame4.place(x=260,y=750)

        

        label1 = Label(self.frame1, text = "Love Compatability Calculator",bg="yellow", font=("ms serif", 20, 'bold'))
        label1.place(x=50, y=50)
        label10 = Label(self.frame1, text = "Toggle Music",bg="yellow", font=("ms serif", 12, 'bold'))
        label10.place(x=110, y=15)

        


        self.canvas = Canvas(self.frame1, width = 260, height = 257)            
        self.img = PhotoImage(file="heart2.gif")     
        self.canvas.create_image(0,0, anchor=NW, image=self.img)
        self.canvas.place(x=120, y=100)



        self.label2= Label(self.frame1, text="Your Name", bg="yellow", font=("ms serif", 15, 'bold'))
        self.label2.place(x=50, y=380)
        self.label3= Label(self.frame1, text="Partner's Name", bg="yellow", font=("ms serif", 15, 'bold'))
        self.label3.place(x=300, y=380)
        self.entry=Entry(self.frame1, width=10, font=("ms serif", 14, 'bold'), bg="pink")
        self.entry.place(x=50, y=420)
        self.entry1=Entry(self.frame1, width=10, font=("ms serif", 14, 'bold'), bg="pink")
        self.entry1.place(x=320, y=420)

        self.label2= Label(self.frame1, text="Your Genders", bg="pink", font=("ms serif", 15, 'bold'))
        self.label2.place(x=170, y=460)

        self.radio1= StringVar()
        self.radio1.set("Male and Female")
        self.rc1 =Radiobutton(self.frame1, text= "Male and Female", bg="pink", font=("ms serif", 11, 'bold'), variable=self.radio1, value="Male and Female")
        self.rc1.place(x=170, y=490)
        self.rc2 =Radiobutton(self.frame1, text= "Male and Male", bg="pink", font=("ms serif", 11, 'bold'), variable=self.radio1, value="Male and Male")
        self.rc2.place(x=170, y=510)
        self.rc3 =Radiobutton(self.frame1, text= "Female and Female", bg="pink", font=("ms serif", 11, 'bold'), variable=self.radio1, value="Female and Female")
        self.rc3.place(x=170, y=530)
        self.rc3 =Radiobutton(self.frame1, text= "Other", bg="pink", font=("ms serif", 11, 'bold'), variable=self.radio1, value="Other")
        self.rc3.place(x=170, y=550)

        self.label4= Label(self.frame1, text="Your Age", bg="yellow", font=("ms serif", 15, 'bold'))
        self.label4.place(x=50, y=610)
        self.label5= Label(self.frame1, text="Partner's Age", bg="yellow", font=("ms serif", 15, 'bold'))
        self.label5.place(x=300, y=610)

        self.var1=DoubleVar()
        self.var1.set(18)
        self.scale1 = Scale(self.mainwindow, variable=self.var1, bg="yellow", from_=1, to=50)
        self.scale1.place(x=70, y=640)
        self.var2=DoubleVar()
        self.var2.set(18)
        self.scale2 = Scale(self.mainwindow, variable=self.var2, bg="yellow", from_=1, to=50)
        self.scale2.place(x=340, y=640)

        



        self.label9= Label(self.frame1, text="Your Favourite Foods", bg="lightcyan", font=("ms serif", 13, 'bold'))
        self.label9.place(x=35, y=770)
        self.label10= Label(self.frame1, text="Partner's Favourite Foods", bg="lightcyan", font=("ms serif", 13, 'bold'))
        self.label10.place(x=280, y=770)

        self.choice1 = IntVar()
        self.choice2 = IntVar()
        self.choice3 = IntVar()
        self.choice4 = IntVar()
        self.choice1.set(1)
        self.choice2.set(0)
        self.choice3.set(0)
        self.choice4.set(0)

        self.cb1 =Checkbutton(self.mainwindow, text="Asian", variable=self.choice1, font=("ms serif", 11, 'bold'), bg="lightcyan")
        self.cb2 =Checkbutton(self.mainwindow, text="Middle Eastern", variable=self.choice2, font=("ms serif", 11, 'bold'), bg="lightcyan")
        self.cb3 =Checkbutton(self.mainwindow, text="Spanish/Mexican", variable=self.choice3, font=("ms serif", 11, 'bold'), bg="lightcyan")
        self.cb4 =Checkbutton(self.mainwindow, text="Fast Food", variable=self.choice4, font=("ms serif", 11, 'bold'), bg="lightcyan")
        self.cb1.place(x=40, y=800)
        self.cb2.place(x=40, y=820)
        self.cb3.place(x=40, y=840)
        self.cb4.place(x=40, y=860)


        self.choice5 = IntVar()
        self.choice6 = IntVar()
        self.choice7 = IntVar()
        self.choice8 = IntVar()
        self.choice5.set(1)
        self.choice6.set(0)
        self.choice7.set(0)
        self.choice8.set(0)

        self.cb5 =Checkbutton(self.mainwindow, text="Asian", variable=self.choice5, font=("ms serif", 11, 'bold'), bg="lightcyan")
        self.cb6 =Checkbutton(self.mainwindow, text="Middle Eastern", variable=self.choice6, font=("ms serif", 11, 'bold'), bg="lightcyan")
        self.cb7 =Checkbutton(self.mainwindow, text="Spanish/Mexican", variable=self.choice7, font=("ms serif", 11, 'bold'), bg="lightcyan")
        self.cb8 =Checkbutton(self.mainwindow, text="Fast Food", variable=self.choice8, font=("ms serif", 11, 'bold'), bg="lightcyan")
        self.cb5.place(x=290, y=800)
        self.cb6.place(x=290, y=820)
        self.cb7.place(x=290, y=840)
        self.cb8.place(x=290, y=860)


        self.button1 = Button(self.frame1, text="Quit", font=("ms serif", 14, 'bold'), command = self.mainwindow.destroy, bg="pink")
        self.button1.place(x=200, y=940)
        self.button2 = Button(self.frame1, text="Calculate!", font=("ms serif", 14, 'bold'), bg="Red", command = self.dothis)
        self.button2.place(x=255, y=940)

        self.off = Button(self.frame1, text="Off", font=("ms serif", 12, 'bold'), command = self.offmusic, bg="lightcyan")
        self.off.place(x=10, y=10)
        self.off = Button(self.frame1, text="On", font=("ms serif", 12, 'bold'), command = self.onmusic, bg="lightcyan")
        self.off.place(x=60, y=10)

        
        mainloop()



    def offmusic(self):
        PlaySound('*', SND_LOOP | SND_ASYNC)
        self.x = 1

    def onmusic(self):
        PlaySound('music.wav', SND_FILENAME | SND_ASYNC)
        self.x = 0

    def dothis(self):
        counter = 0
        foods = ""
        yesfood = False 
        if abs(self.var1.get() - self.var2.get()) <= 5:
            counter = counter + 35

        if abs(self.var1.get() - self.var2.get()) <= 10 and abs(self.var1.get() - self.var2.get()) > 5 :
            counter = counter + 10

        if self.choice1.get() != 0 and  self.choice5.get() != 0:
            counter = counter + 15
            foods = foods + " Asian"
            yesfood = True

        if self.choice2.get() != 0 and self.choice6.get() != 0:
            counter = counter + 15
    
            if yesfood == True:
                foods = foods + " and Middle Eastern"
            else:
                foods = foods + " Middle Eastern"
                yesfood = True

        if self.choice3.get() != 0 and self.choice7.get() != 0:
            counter = counter + 15
            if yesfood == True:
                foods = foods + " and Spanish/Mexican"
            else:
                foods = foods + " Spanish/Mexican"
                yesfood = True

        if self.choice4.get() != 0 and self.choice8.get() != 0:
            counter = counter + 15
            if yesfood == True:
                foods = foods + " and Fast"
            else:
                foods = foods + " Fast"
                yesfood = True

        total = random.randint(1,11) + counter
        if self.entry1.get() != "" and self.entry.get() != "":
            if counter == 95:
                PlaySound('yay1.wav', SND_FILENAME | SND_ASYNC)
                total = total - 5
                tkinter.messagebox.showinfo("Results! " + self.radio1.get(), "Congratulations! Its a perfect match!" + "\n" + "\n" + self.entry.get() + " and " + self.entry1.get() + " have a "
                                            + str(total) + "% " + "compatability!" + "\n" + "\n" + "You two are quite obviously ment for each other! You both like all foods, and are within 5 years of an age difference!")
            if counter == 70:
                PlaySound('yay1.wav', SND_FILENAME | SND_ASYNC)
                tkinter.messagebox.showinfo("Results!" + self.radio1.get(), "Pretty good!" + "\n" + "\n" + self.entry.get() + " and " + self.entry1.get() + " have a "
                                            + str(total) + "% " + "compatability!" + "\n" + "\n" + "You two are not picky eaters, and seem to like all foods! You have an age difference of more than 10 years, which may be an obstacle to overcome!")
            if counter == 0:
                PlaySound('no1.wav', SND_FILENAME | SND_ASYNC)
                tkinter.messagebox.showinfo("Results!" + self.radio1.get(), "Run as fast as you can!" + "\n" + "\n" + self.entry.get() + " and " + self.entry1.get() + " have a "
                                            + str(total) + "% " + "compatability!" + "\n" + "\n" + "You two have almost nothing in common, and have a big difference in age! Perhaps, not everything was ment to be.")
            if counter == 10:
                PlaySound('no1.wav', SND_FILENAME | SND_ASYNC)
                tkinter.messagebox.showinfo("Results!" + self.radio1.get(), "Not looking good!" + "\n" + "\n" + self.entry.get() + " and " + self.entry1.get() + " have a "
                                            + str(total) + "% " + "compatability!" + "\n" + "\n" + "Where will you guys go eat on date night! It seems you two do not share the same tastes in cuisine, however your age range is winthin 10 years!")
            if counter == 35 and yesfood == False:
                PlaySound('no1.wav', SND_FILENAME | SND_ASYNC)
                tkinter.messagebox.showinfo("Results!" + self.radio1.get(), "Perhaps its time to rethink!" + "\n" + "\n" + self.entry.get() + " and " + self.entry1.get() + " have a "
                                            + str(total) + "% " + "compatability!" + "\n" + "\n" + "Date nights will be miserable, as you two do not share the same tastes. However your age difference could be your saving factor!")
            if counter == 15:
                PlaySound('no1.wav', SND_FILENAME | SND_ASYNC)
                tkinter.messagebox.showinfo("Results!" + self.radio1.get(), "Quite Unfortunate!" + "\n" + "\n" + self.entry.get() + " and " + self.entry1.get() + " have a "
                                            + str(total) + "% " + "compatability!" + "\n" + "\n" + "You two both like" + foods + " food. But you cant keep having" + foods
                                            + " food for every date night! Furthermore your age difference will be an obstacle that you two will have to overcome.")
            if counter == 30 and yesfood == True:
                PlaySound('no1.wav', SND_FILENAME | SND_ASYNC)
                tkinter.messagebox.showinfo("Results!" + self.radio1.get(), "Getting there!" + "\n" + "\n" + self.entry.get() + " and " + self.entry1.get() + " have a "
                                            + str(total) + "% " + "compatability!" + "\n" + "\n" + "You two both like" + foods + " food. At least you two have options! However, you too are a quite far apart in age.")
            if counter == 45 and yesfood == True:
                PlaySound('yay1.wav', SND_FILENAME | SND_ASYNC)
                tkinter.messagebox.showinfo("Results!" + self.radio1.get(), "Your'e Passing!" + "\n" + "\n" + self.entry.get() + " and " + self.entry1.get() + " have a "
                                            + str(total) + "% " + "compatability!" + "\n" + "\n" + "You two both like" + foods + " food. Which means you two have a lot in common! You may stuff your faces but your age difference will hinder your relationship!")
            if counter == 60 and yesfood == True:
                PlaySound('yay1.wav', SND_FILENAME | SND_ASYNC)
                tkinter.messagebox.showinfo("Results!" + self.radio1.get(), "Stuff your faces!" + "\n" + "\n" + self.entry.get() + " and " + self.entry1.get() + " have a "
                                            + str(total) + "% " + "compatability!" + "\n" + "\n" + "You two both like" + foods + " food. Which means date night will be a breeze! However, according to the calculations, you two are quite far apart in age.")
            if counter == 50 and yesfood == True:
                PlaySound('yay1.wav', SND_FILENAME | SND_ASYNC)
                tkinter.messagebox.showinfo("Results!" + self.radio1.get(), "Not Terrible!" + "\n" + "\n" + self.entry.get() + " and " + self.entry1.get() + " have a "
                                            + str(total) + "% " + "compatability!" + "\n" + "\n" + "You two both like" + foods + " food. And your age difference is perfect! Just work on not being so picky.")
            if counter == 65 and yesfood == True:
                PlaySound('yay1.wav', SND_FILENAME | SND_ASYNC)
                tkinter.messagebox.showinfo("Results!" + self.radio1.get(), "Almost there!" + "\n" + "\n" + self.entry.get() + " and " + self.entry1.get() + " have a "
                                            + str(total) + "% " + "compatability!" + "\n" + "\n" + "You two both like" + foods + " food. And your age difference is immaculate! Date night here you go!.")
            if counter == 80 and yesfood == True:
                PlaySound('yay1.wav', SND_FILENAME | SND_ASYNC)
                tkinter.messagebox.showinfo("Results!" + self.radio1.get(), "Almost there!" + "\n" + "\n" + self.entry.get() + " and " + self.entry1.get() + " have a "
                                            + str(total) + "% " + "compatability!" + "\n" + "\n" + "You two both like" + foods + " food. You two will be stuffing your faces, and your parents will be proud of the age difference!")
            if counter == 25 and yesfood == True:
                PlaySound('no1.wav', SND_FILENAME | SND_ASYNC)
                tkinter.messagebox.showinfo("Results!" + self.radio1.get(), "Not the worst I've seen!" + "\n" + "\n" + self.entry.get() + " and " + self.entry1.get() + " have a "
                                            + str(total) + "% " + "compatability!" + "\n" + "\n" + "You two both like" + foods + " food. And your age is not too bad! Perhaps, something can be made of this.")
            if counter == 40 and yesfood == True:
                PlaySound('no1.wav', SND_FILENAME | SND_ASYNC)
                tkinter.messagebox.showinfo("Results!" + self.radio1.get(), "Almost Passing!" + "\n" + "\n" + self.entry.get() + " and " + self.entry1.get() + " have a "
                                            + str(total) + "% " + "compatability!" + "\n" + "\n" + "You two both like" + foods + " food. And your age is not too bad! Keep trying, because something could be potentially made from this.")
            if counter == 55 and yesfood == True:
                PlaySound('yay1.wav', SND_FILENAME | SND_ASYNC)
                tkinter.messagebox.showinfo("Results!" + self.radio1.get(), "Not the worst odds!" + "\n" + "\n" + self.entry.get() + " and " + self.entry1.get() + " have a "
                                            + str(total) + "% " + "compatability!" + "\n" + "\n" + "You two both like" + foods + " food. And your age is not too bad! Date nights should be a breeze!")
        self.entry.delete(0, 'end')
        self.entry1.delete(0, 'end')
        self.choice1.set(1)
        self.choice2.set(0)
        self.choice3.set(0)
        self.choice4.set(0)
        self.choice5.set(1)
        self.choice6.set(0)
        self.choice7.set(0)
        self.choice8.set(0)
        self.radio1.set("Male and Female")

        if self.x == 0:
            PlaySound('music.wav', SND_FILENAME | SND_ASYNC)
                       
        







        
my_gui=MyGUI()
