import random
import tkinter
import tkinter.ttk as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time

random.seed()
root = tkinter.Tk() 
root.title("Mining Game")
root.configure(bg="lightgray") 

style = ttk.Style()
style.theme_use('classic')
root.title("Mining Game")
state=ACTIVE
timer_id = None


#Digging Site #1:
#------------------------------------------------------------------

# Global Variables

valueadd=0

count =0
basement=-8
luck =100
start = 0
stop = 5
total=0
playerx=80
playery=40
stoney=190
allblocks=0
allblocksbrek=0

# Frame
frame = tk.Frame(root, width=400, height=400, borderwidth=2, relief="groove")
frame.pack_propagate(False)
frame.grid(column=0, row=0)
frame.lower()
root.configure(bg="lightgray")

# Window Configurations
root.geometry("400x400")
root.resizable(True,True)

# Photos
player = PhotoImage(file="minerrr.png")
player = player.subsample(3, 3)

player_what = PhotoImage(file="minerrrwhat.png")
player_what = player_what.subsample(12, 12)

stone_image = PhotoImage(file="stone.png")
stone_image = stone_image.subsample(3, 3)

stone_breaking = PhotoImage(file="stonebreaking.png")
stone_breaking = stone_breaking.subsample(4, 4)

# Functions
def up():
    global count,playery
    if count <0:
        count+=1
        playery-=20
        person.place(x=playerx,y=playery)
        print(count)
        person.lower()
    else:
        print("You are already at the top!")

def down():
    global count,basement,playery
    if count > basement:
        count-=1
        playery+=20
        person.place(x=playerx,y=playery)
        print(count)
        person.lower()
    else:
        print("You can't go any further down!")
    

def dig():
    global start, stop, count, luck, total, timer_id, allblocksbrek,valueadd
    start=0+valueadd
    stop=5+valueadd
    if count < -3:
        luck = random.randrange(start, stop)
        print(luck)
        total += luck
        update_total_label()

        destroyblock(0)
        if allblocksbrek >= 16:
            dig_button.config(state=DISABLED)
            bonus_text = Label(frame, text="Bonus +50", font=("Monocraft", 19), fg="green",bg="lightgray")
            bonus_text.place(x=250, y=250)
            root.after(2000, lambda: bonus_text.destroy())
            total += 50
            update_total_label()

            if timer_id is None:
                timer_id = root.after(5000, reset_blocks)

def buy1():
    global total
    if total >=1000:  
        total-=1000
        update_total_label()
        buy1_button.destroy()
        frame1.place(x=0,y=400)

    else:
        print("You don't have enough money for this yet!")

# Buttons
up= Button(frame, text="Up",font=("Monocraft",12),
          command=up, bg=root.cget("bg"))
up.place(x=5,y=35)

dig_button= Button(frame, text="Dig",font=("Monocraft",12),
          command=dig,
          state=state, bg=root.cget("bg"))
dig_button.place(x=5,y=95)

down= Button(frame, text="Down",font=("Monocraft",12),
          command=down, bg=root.cget("bg"))
down.place(x=5,y=65)


buy1_button= Button(frame, text="Digsite #2: $1,000",
          command=buy1,
          font=("Monocraft", 10))
buy1_button.configure(fg="red",
               activebackground="red",activeforeground="red", bg=root.cget("bg"))
buy1_button.lift()
buy1_button.place(x=5,y=350)

# Labels
digsite= Label(frame, text="Digsite #1:",fg="black",
         font=("Monocraft", 14), bg=root.cget("bg"))
digsite.place(x=5,y=0)

total_lable= Label(frame, text="Total $: "+str(total),fg="black",
         font=("Monocraft", 14), bg=root.cget("bg"))
total_lable.place(x=130,y=0)

Go_Down= Label(frame, text="Go Down to start Digging!",
         font=("Monocraft", 12),
         fg="red", bg=root.cget("bg"))
Go_Down.place(x=180,y=80)

resize= Label(frame, text="Maximize the Screen",
         font=("Monocraft", 12),
         fg="red", bg=root.cget("bg"))
resize.place(x=5,y=310)

# Assets
person= Label(frame, image=player, bg="lightgray")
person.place(x=playerx,y=playery)

stone_labels = [] # list for all stone

stonex=175

def reset_blocks():
    global allblocks, allblocksbrek, total, timer_id, state

    # Cancel any scheduled timer
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None
    stonex = 175
    allblocks = 0
    state=ACTIVE
    dig_button.config(state=ACTIVE)
    allblocksbrek = 0
    for i in range(4):
        stoney = 175
        for j in range(4):
            stone_label = Label(frame, image=stone_image)
            stone_label.place(x=stonex, y=stoney)
            stone_labels.append(stone_label)
            stoney += 56
        stonex += 56

    
    


#https://stackoverflow.com/questions/49854724/cant-background-color-in-tkinter?rq=3

# LIST IS IN ORDER FROM 
# +1|+5|+3|+4
# +2|+6|+7|+8
# +3|-7|-6|-5
# +4|-3|-2|-1
    

stone_brek_labels = []

def destroyblock(block):
    global allblocks,total,allblocksbrek
    if allblocks < 16:
        x = stone_labels[block].place_info().get('x', 0)
        y = stone_labels[block].place_info().get('y', 0)
        stone_labels[block].destroy()
        stone_brek = Label(frame, image=stone_breaking)
        stone_brek.place(x=x, y=y)
        stone_brek_labels.append(stone_brek)  
        stone_labels.pop(block)
        allblocks += 1
    else:
        stone_brek_labels[block].destroy()
        stone_brek_labels.pop(block)
        total+=5
        allblocksbrek+=1
        state=DISABLED

reset_blocks()


# DIGGING SITE #2
#------------------------------------------------------------------
state1=ACTIVE
timer_id1 = None


# Global Variables
count1 =0
basement1=-8
luck1 =0
start1 = 10
stop1 = 35
playerx1=80
playery1=40
stoney1=175
allblocks1=0
allblocksbrek1=0

# Frame
frame1 = tk.Frame(root, width=400, height=400, borderwidth=2, relief="groove")
frame1.pack_propagate(False)
frame1.lower()
frame1.pack_forget()

# Photos
player_what = PhotoImage(file="minerrrwhat.png")
player_what = player_what.subsample(3, 3)

stone_image1 = PhotoImage(file="deepslate1.png")
stone_image1 = stone_image1.subsample(6, 6)

stone_breaking1 = PhotoImage(file="deepslatebrek.png")
stone_breaking1 = stone_breaking1.subsample(13, 13)

# Functions
def up1():
    global count1,playery1
    if count1 <0:
        count1+=1
        playery1-=20
        person1.place(x=playerx1,y=playery1)
        print(count1)
        person1.lower()

    else:
        print("You are already at the top!")

def down1():
    global count1,basement1,playery1
    if count1 > basement1:
        count1-=1
        playery1+=20
        person1.place(x=playerx1,y=playery1)
        print(count1)
        person1.lower()
    else:
        print("You can't go any further down!")
    

def dig1():
    global start1, stop1, count1, luck1, timer_id1, allblocksbrek1,total,valueadd
    start1=10+valueadd
    stop1=35+valueadd
    if count1 < -3:
        luck1 = random.randrange(start1, stop1)
        print(luck1)
        total += luck1
        update_total_label()
        destroyblock1(0)
        if allblocksbrek1 >= 16:
            dig_button1.config(state=DISABLED)
            bonus_text1 = Label(frame1, text="Bonus +150", font=("Monocraft", 19), fg="green",bg="lightgray")
            bonus_text1.place(x=250, y=250)
            root.after(2000, lambda: bonus_text1.destroy())
            total += 150
            update_total_label()


            if timer_id1 is None:
                timer_id1 = root.after(8000, reset_blocks1)

def buy11():
    global total
    if total >=5000:  
        total-=5000
        update_total_label()
        buy11_button.destroy()
        frame2.place(x=400,y=0)

    else:
        print("You don't have enough money for this yet!")

# Buttons
up1= Button(frame1, text="Up",font=("Monocraft",12),
          command=up1, bg=root.cget("bg"))
up1.place(x=5,y=135)

dig_button1= Button(frame1, text="Dig",font=("Monocraft",12),
          command=dig1,
          state=state1, bg=root.cget("bg"))
dig_button1.place(x=5,y=195)

down1= Button(frame1, text="Down",font=("Monocraft",12),
          command=down1, bg=root.cget("bg"))
down1.place(x=5,y=165)


buy11_button= Button(frame1, text="Digsite #3: $5,000",
          command=buy11,
          font=("Monocraft", 10))
buy11_button.configure(fg="red",
               activebackground="red",activeforeground="red", bg=root.cget("bg"))
buy11_button.lift()
buy11_button.place(x=5,y=350)

# Labels
digsite1= Label(frame1, text="Digsite #2:",fg="black",
         font=("Monocraft", 14), bg=root.cget("bg"))
digsite1.place(x=5,y=0)

total_lable1= Label(frame1, text="Total $: "+str(total),fg="black",
         font=("Monocraft", 14), bg=root.cget("bg"))
total_lable1.place(x=130,y=0)

Go_Down1= Label(frame1, text="Go Down to start Digging!",
         font=("Monocraft", 12),
         fg="red", bg=root.cget("bg"))
Go_Down1.place(x=180,y=80)


# Assets
person1= Label(frame1, image=player, bg="lightgray")
person1.place(x=playerx1,y=playery1)

stone_labels1 = [] # list for all stone

stonex1=175

def reset_blocks1():
    global allblocks1, allblocksbrek1,total, timer_id1, state1,stonex1,stoney1

    # Cancel any scheduled timer
    if timer_id1 is not None:
        root.after_cancel(timer_id1)
        timer_id1 = None
    stonex1 = 175
    allblocks1 = 0
    state1=ACTIVE
    dig_button1.config(state=ACTIVE)
    allblocksbrek1 = 0
    for i in range(4):
        stoney1 = 175
        for j in range(4):
            stone_label1 = Label(frame1, image=stone_image1)
            stone_label1.place(x=stonex1, y=stoney1)
            stone_labels1.append(stone_label1)
            stoney1 += 56
        stonex1 += 56

stone_brek_labels1 = []

def destroyblock1(block):
    global allblocks1,total,allblocksbrek1,state1
    if allblocks1 < 16:
        x = stone_labels1[block].place_info().get('x', 0)
        y = stone_labels1[block].place_info().get('y', 0)
        stone_labels1[block].destroy()
        stone_brek1 = Label(frame1, image=stone_breaking1)
        stone_brek1.place(x=x, y=y)
        stone_brek_labels1.append(stone_brek1)  
        stone_labels1.pop(block)
        allblocks1 += 1
    else:
        stone_brek_labels1[block].destroy()
        stone_brek_labels1.pop(block)
        total+=5
        allblocksbrek1+=1
        state1=DISABLED

reset_blocks1()















# DIGGING SITE #3
#------------------------------------------------------------------


state2 = ACTIVE
timer_id2 = None

# Global Variables
count2 = 0
basement2 = -8
luck2 = 0
start2 = 60+valueadd
stop2 = 90+valueadd
playerx2 = 80
playery2 = 40
stoney2 = 175
allblocks2 = 0
allblocksbrek2 = 0

# Frame
frame2 = tk.Frame(root, width=400, height=400, borderwidth=2, relief="groove")
frame2.pack_propagate(False)
frame2.lower()
frame2.pack_forget()

# Photos
player2 = PhotoImage(file="Minerrr.png")
player2 = player2.subsample(3, 3)

stone_image2 = PhotoImage(file="netherrack.png")
stone_image2 = stone_image2.subsample(32, 32)

stone_breaking2 = PhotoImage(file="netherrackbrek.png")
stone_breaking2 = stone_breaking2.subsample(34, 34)

# Functions
def up2():
    global count2, playery2
    if count2 < 0:
        count2 += 1
        playery2 -= 20
        person2.place(x=playerx2, y=playery2)
        print(count2)
        person2.lower()
    else:
        print("You are already at the top!")

def down2():
    global count2, basement2, playery2
    if count2 > basement2:
        count2 -= 1
        playery2 += 20
        person2.place(x=playerx2, y=playery2)
        print(count2)
        person2.lower()
    else:
        print("You can't go any further down!")

def dig2():
    global start2, stop2, count2, luck2, timer_id2, allblocksbrek2, total,valueadd
    start2=60+valueadd
    stop2=90+valueadd
    if count2 < -3:
        luck2 = random.randrange(start2, stop2)
        print(luck2)
        total += luck2
        update_total_label()
        destroyblock2(0)
        if allblocksbrek2 >= 16:
            dig_button2.config(state=DISABLED)
            bonus_text2 = Label(frame2, text="Bonus +350", font=("Monocraft", 19), fg="green", bg="lightgray")
            bonus_text2.place(x=250, y=250)
            root.after(2000, lambda: bonus_text2.destroy())
            total += 350
            update_total_label()

            if timer_id2 is None:
                timer_id2 = root.after(10000, reset_blocks2)

def buy12():
    global total
    if total >=25000:  
        total-=25000
        update_total_label()
        buy12_button.destroy()
        frame3.place(x=400,y=400)

    else:
        print("You don't have enough money for this yet!")
def update_total_label():
    global total
    total_text = "Total $: " + str(total)
    total_lable.config(text="Total $: " + str(total))
    total_lable1.config(text="Total $: " + str(total))
    total_lable2.config(text="Total $: " + str(total))
    total_lable3.config(text="Total $: " + str(total))
    total_lable4.config(text="Total $: " + str(total))

# Buttons
up2 = Button(frame2, text="Up", font=("Monocraft", 12), command=up2, bg=root.cget("bg"))
up2.place(x=5, y=135)

dig_button2 = Button(frame2, text="Dig", font=("Monocraft", 12), command=dig2, state=state2, bg=root.cget("bg"))
dig_button2.place(x=5, y=195)

down2 = Button(frame2, text="Down", font=("Monocraft", 12), command=down2, bg=root.cget("bg"))
down2.place(x=5, y=165)

buy12_button = Button(frame2, text="Digsite #4: $25,000", command=buy12, font=("Monocraft", 10))
buy12_button.configure(fg="red", activebackground="red", activeforeground="red", bg=root.cget("bg"))
buy12_button.lift()
buy12_button.place(x=5, y=350)

# Labels
digsite2 = Label(frame2, text="Digsite #3:", fg="black", font=("Monocraft", 14), bg=root.cget("bg"))
digsite2.place(x=5, y=0)

total_lable2 = Label(frame2, text="Total $: " + str(total), fg="black", font=("Monocraft", 14), bg=root.cget("bg"))
total_lable2.place(x=130, y=0)

Go_Down2 = Label(frame2, text="Go Down to start Digging!", font=("Monocraft", 12), fg="red", bg=root.cget("bg"))
Go_Down2.place(x=180, y=80)

# Assets
person2 = Label(frame2, image=player, bg="lightgray")
person2.place(x=playerx2, y=playery2)

stone_labels2 = []  # list for all stone

stonex2 = 175

def reset_blocks2():
    global allblocks2, allblocksbrek2, total, timer_id2, state2, stonex2, stoney2

    # Cancel any scheduled timer
    if timer_id2 is not None:
        root.after_cancel(timer_id2)
        timer_id2 = None
    stonex2 = 175
    allblocks2 = 0
    state2 = ACTIVE
    dig_button2.config(state=ACTIVE)
    allblocksbrek2 = 0
    for i in range(4):
        stoney2 = 175
        for j in range(4):
            stone_label2 = Label(frame2, image=stone_image2)
            stone_label2.place(x=stonex2, y=stoney2)
            stone_labels2.append(stone_label2)
            stoney2 += 56
        stonex2 += 56

stone_brek_labels2 = []

def destroyblock2(block):
    global allblocks2, total, allblocksbrek2, state2
    if allblocks2 < 16:
        x = stone_labels2[block].place_info().get('x', 0)
        y = stone_labels2[block].place_info().get('y', 0)
        stone_labels2[block].destroy()
        stone_brek2 = Label(frame2, image=stone_breaking2)
        stone_brek2.place(x=x, y=y)
        stone_brek_labels2.append(stone_brek2)
        stone_labels2.pop(block)
        allblocks2 += 1
    else:
        stone_brek_labels2[block].destroy()
        stone_brek_labels2.pop(block)
        total += 5
        allblocksbrek2 += 1
        state2 = DISABLED

reset_blocks2()

# Digsite #4:
#----------------------------------------------------------------------

state3 = ACTIVE
timer_id3 = None

# Global Variables
count3 = 0
basement3 = -8
luck3 = 0
start3 = 120+valueadd
stop3 = 200+valueadd
playerx3 = 80
playery3 = 40
stoney3 = 175
allblocks3 = 0
allblocksbrek3 = 0

# Frame
frame3 = tk.Frame(root, width=400, height=400, borderwidth=3, relief="groove")
frame3.pack_propagate(False)
frame3.lower()
frame3.pack_forget()

# Photos
player3 = PhotoImage(file="Minerrr.png")
player3 = player3.subsample(3, 3)

stone_image3 = PhotoImage(file="end brick.png")
stone_image3 = stone_image3.subsample(3, 3)

stone_breaking3 = PhotoImage(file="end stone.png")
stone_breaking3 = stone_breaking3.subsample(3, 3)

# Functions
def up3():
    global count3, playery3
    if count3 < 0:
        count3 += 1
        playery3 -= 20
        person3.place(x=playerx3, y=playery3)
        print(count3)
    else:
        print("You are already at the top!")

def down3():
    global count3, basement3, playery3
    if count3 > basement3:
        count3 -= 1
        playery3 += 20
        person3.place(x=playerx3, y=playery3)
        print(count3)
        person3.lower()
    else:
        print("You can't go any further down!")

def dig3():
    global start3, stop3, count3, luck3, timer_id3, allblocksbrek3, total,valueadd
    start3=120+valueadd
    stop3=200+valueadd
    if count3 < -3:
        luck3 = random.randrange(start3, stop3)
        print(luck3)
        total += luck3
        update_total_label()
        destroyblock3(0)
        if allblocksbrek3 >= 16:
            dig_button3.config(state=DISABLED)
            bonus_text3 = Label(frame3, text="Bonus +550", font=("Monocraft", 19), fg="green", bg="lightgray")
            bonus_text3.place(x=250, y=250)
            root.after(2000, lambda: bonus_text3.destroy())
            total += 550
            update_total_label()

            if timer_id3 is None:
                timer_id3 = root.after(12000, reset_blocks3)

def buy13():
    global total
    if total >=50000:  
        total-=50000
        update_total_label()
        buy13_button.destroy()
        frame4.place(x=800,y=0)

    else:
        print("You don't have enough money for this yet!")

# Buttons
up3 = Button(frame3, text="Up", font=("Monocraft", 12), command=up3, bg=root.cget("bg"))
up3.place(x=5, y=135)

dig_button3 = Button(frame3, text="Dig", font=("Monocraft", 12), command=dig3, state=state3, bg=root.cget("bg"))
dig_button3.place(x=5, y=195)

down3 = Button(frame3, text="Down", font=("Monocraft", 12), command=down3, bg=root.cget("bg"))
down3.place(x=5, y=165)

buy13_button = Button(frame3, text="Upgrade Shop: $50,000", command=buy13, font=("Monocraft", 9))
buy13_button.configure(fg="red", activebackground="red", activeforeground="red", bg=root.cget("bg"))
buy13_button.lift()
buy13_button.place(x=5, y=350)

# Labels
digsite3 = Label(frame3, text="Digsite #4:", fg="black", font=("Monocraft", 14), bg=root.cget("bg"))
digsite3.place(x=5, y=0)

total_lable3 = Label(frame3, text="Total $: " + str(total), fg="black", font=("Monocraft", 14), bg=root.cget("bg"))
total_lable3.place(x=130, y=0)

Go_Down3 = Label(frame3, text="Go Down to start Digging!", font=("Monocraft", 12), fg="red", bg=root.cget("bg"))
Go_Down3.place(x=180, y=80)

# Assets
person3 = Label(frame3, image=player, bg="lightgray")
person3.place(x=playerx3, y=playery3)

stone_labels3 = []  # list for all stone

stonex3 = 175

def reset_blocks3():
    global allblocks3, allblocksbrek3, total, timer_id3, state3, stonex3, stoney3

    # Cancel any scheduled timer
    if timer_id3 is not None:
        root.after_cancel(timer_id3)
        timer_id3 = None
    stonex3 = 175
    allblocks3 = 0
    state3 = ACTIVE
    dig_button3.config(state=ACTIVE)
    allblocksbrek3 = 0
    for i in range(4):
        stoney3 = 175
        for j in range(4):
            stone_label3 = Label(frame3, image=stone_image3)
            stone_label3.place(x=stonex3, y=stoney3)
            stone_labels3.append(stone_label3)
            stoney3 += 56
        stonex3 += 56

stone_brek_labels3 = []

def destroyblock3(block):
    global allblocks3, total, allblocksbrek3, state3
    if allblocks3 < 16:
        x = stone_labels3[block].place_info().get('x', 0)
        y = stone_labels3[block].place_info().get('y', 0)
        stone_labels3[block].destroy()
        stone_brek3 = Label(frame3, image=stone_breaking3)
        stone_brek3.place(x=x, y=y)
        stone_brek_labels3.append(stone_brek3)
        stone_labels3.pop(block)
        allblocks3 += 1
    else:
        stone_brek_labels3[block].destroy()
        stone_brek_labels3.pop(block)
        total += 5
        allblocksbrek3 += 1
        state3 = DISABLED

reset_blocks3()


# Upgrade Shop:
#--------------------------------------------------------------------------

# Frame 
frame4 = tk.Frame(root, width=400, height=400, borderwidth=3, relief="groove")
frame4.pack_propagate(False)
frame4.lower()
frame4.pack_forget()

# Global Variables

shop0c=50000
shop1c=15000
shop2c=40000
shop3c=60000
# Photos

# Labels
shopl = Label(frame4, text="Upgrade Shop:", fg="black", font=("Monocraft", 14), bg=root.cget("bg"))
shopl.place(x=5, y=0)
total_lable4 = Label(frame4, text="Total $: " + str(total), fg="black", font=("Monocraft", 14), bg=root.cget("bg"))
total_lable4.place(x=130, y=0)

# Functions

def shop1():
    global total,shop1c
    if total >=shop1c:  
        total-=shop1c
        update_total_label()
        shop1c+=5000
        shop1c=shop1c*1.5
        int(shop1c)
        shop_button1.config(text="+1 Minors: $" + str(shop1c))

    else:
        print("You don't have enough money for this yet!")

def shop2():
    global total,shop2c
    if total >=shop2c:  
        total-=shop2c
        update_total_label()
        shop2c=shop2c*1.5
        int(shop2c)
        shop_button2.config(text="Faster Mine Regen: $" + str(shop2c))
    else:
        print("You don't have enough money for this yet!")


def shop3():
    global total,shop3c,valueadd
    if total >=shop3c:  
        total-=shop3c
        update_total_label()
        shop3c=shop3c*1.5
        int(shop3c)
        shop_button3.config(text="More Valuable Ores: $" + str(shop3c))
        valueadd+=30
    else:
        print("You don't have enough money for this yet!")

def shop0():
    global total,shop0c,valueadd
    if total >=shop0c:  
        total-=shop0c
        update_total_label()
        shop0c=shop0c*1.5
        int(shop0c)
        shop_button0.config(text="WIN: $" + str(shop0c))
        
    else:
        print("You don't have enough money for this yet!")


# Buttons

shop_button0 = Button(frame4, text="WIN: $"+str(shop0c), command=shop0, font=("Monocraft", 12))
shop_button0.configure(fg="red", activebackground="red", activeforeground="red", bg=root.cget("bg"))
shop_button0.lift()
shop_button0.place(x=5, y=200)

shop_button1 = Button(frame4, text="+1 Minors: $"+str(shop1c), command=shop1, font=("Monocraft", 12))
shop_button1.configure(fg="red", activebackground="red", activeforeground="red", bg=root.cget("bg"))
shop_button1.lift()
shop_button1.place(x=5, y=250)

shop_button2 = Button(frame4, text="Faster Mine Regen: $"+str(shop2c), command=shop2, font=("Monocraft", 12))
shop_button2.configure(fg="red", activebackground="red", activeforeground="red", bg=root.cget("bg"))
shop_button2.lift()
shop_button2.place(x=5, y=290)

shop_button3 = Button(frame4, text="More Valuable Ores: $"+str(shop3c), command=shop3, font=("Monocraft", 12))
shop_button3.configure(fg="red", activebackground="red", activeforeground="red", bg=root.cget("bg"))
shop_button3.lift()
shop_button3.place(x=5, y=330)



root.mainloop()