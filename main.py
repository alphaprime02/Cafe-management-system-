from tkinter import *
import random
import time
import datetime
import tkinter.messagebox
import mysql.connector as sql

root = Tk()
root.geometry("1350x750+0+0")
root.title("Cafe Management System")
root.configure(background = 'Cadet Blue')

Tops = Frame(root, bg = 'Cadet Blue',bd = 20, pady = 5, relief=RIDGE)
Tops.pack(side=TOP)
lblTitle = Label(Tops,font=('aerial',60,'bold'), text="Cafe Management System",bd=21,bg='Cadet Blue',fg='Cornsilk', justify = CENTER)
lblTitle.grid(row=0, column = 0)

MenuFrame = Frame(root, bg = 'Cadet Blue',bd = 10, relief=RIDGE)
MenuFrame.pack(side=LEFT)

RecieptCal_F = Frame(root, bg = 'Powder Blue',bd = 10, relief=RIDGE)
RecieptCal_F.pack(side=RIGHT)
Buttons_F = Frame(RecieptCal_F, bg = 'Powder Blue',bd = 3, relief=RIDGE,)
Buttons_F.pack(side=BOTTOM)
Cal_F = Frame(RecieptCal_F, bg = 'Powder Blue',bd = 6, relief=RIDGE,)
Cal_F.pack(side=TOP)
Receipt_F = Frame(RecieptCal_F, bg = 'Powder Blue',bd = 4, relief=RIDGE,)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root, bg = 'Cadet Blue', bd = 10,  relief = RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F = Frame(MenuFrame, bg = 'Powder Blue',bd = 4,)
Cost_F.pack(side=BOTTOM)
Drinks_F = Frame(MenuFrame, bg = 'Cadet Blue',bd = 4,)
Drinks_F.pack(side=TOP)

Drinks_F = Frame(MenuFrame, bg = 'Powder Blue',bd = 10,relief = RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F = Frame(MenuFrame, bg = 'Powder Blue',bd = 10,relief = RIDGE)
Cake_F.pack(side=RIGHT)
 #=================================Variables====================================================================#
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateOfOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostOfCakes = StringVar()
CostOfDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

E_Latta = StringVar()
E_Espresso = StringVar()
E_Iced_Latta = StringVar()
E_Vale_Coffee = StringVar()
E_Cappucino = StringVar()
E_African_Coffee = StringVar()
E_American_Coffee = StringVar()
E_Iced_Cappucino = StringVar()

E_School_Cake = StringVar()
E_Sunny_AO_Cake = StringVar()
E_Jonathan_YO_Cake = StringVar()
E_West_African = StringVar()
E_Lagos_Chcolate_Cake = StringVar()
E_Killburn_Chocolate_Cake = StringVar()
E_Carlton_Hill_Chocolate_Cake = StringVar()
E_Queen_Park_Chocolate_Cake = StringVar()

E_Latta.set("0")
E_Espresso.set("0")
E_Iced_Latta.set("0")
E_Vale_Coffee.set("0")
E_Cappucino.set("0")
E_African_Coffee.set("0")
E_American_Coffee.set("0")
E_Iced_Cappucino.set("0")

E_School_Cake.set("0")
E_Sunny_AO_Cake.set("0")
E_Jonathan_YO_Cake.set("0")
E_West_African.set("0")
E_Lagos_Chcolate_Cake.set("0")
E_Killburn_Chocolate_Cake.set("0")
E_Carlton_Hill_Chocolate_Cake.set("0")
E_Queen_Park_Chocolate_Cake.set("0")

DateOfOrder.set(time.strftime("%d/%m/%Y"))

def CostOfItem():
    Item1 = float(E_Latta.get())
    Item2 = float(E_Espresso.get())
    Item3 = float(E_Iced_Latta.get())
    Item4 = float(E_Vale_Coffee.get())
    Item5 = float(E_Cappucino.get())
    Item6 = float(E_African_Coffee.get())
    Item7 = float(E_American_Coffee.get())
    Item8 = float(E_Iced_Cappucino.get())
    Item9 = float(E_School_Cake.get())
    Item10 = float(E_Sunny_AO_Cake.get())
    Item11 = float(E_Jonathan_YO_Cake.get())
    Item12 = float(E_West_African.get())
    Item13 = float(E_Lagos_Chcolate_Cake.get())
    Item14 = float(E_Killburn_Chocolate_Cake.get())
    Item15 = float(E_Carlton_Hill_Chocolate_Cake.get())
    Item16 = float(E_Queen_Park_Chocolate_Cake.get())

    PriceOfDrinks = (Item1 * 1.2) + (Item2 * 1.99) + (Item3 * 2.05) \
                    + (Item4 * 1.89) + (Item5 * 1.99) + (Item6 * 2.99) + (Item7 * 2.39) + (Item8 * 1.29)
    PriceOfCakes = (Item9 * 1.35) + (Item10 * 2.2) + (Item11 * 1.99)  \
                   + (Item12 * 1.49) + (Item13 * 1.8) + (Item14 * 1.67) + (Item15 * 1.6) + (Item16 * 1.99)

    DrinksPrice = "₹ "+str('%.2f'%(PriceOfDrinks))
    CakesPrice = "₹ "+str("%.2f"%(PriceOfCakes))
    CostOfCakes.set(CakesPrice)
    CostOfDrinks.set(DrinksPrice)
    SC = "₹ "+ str("%.2f"%(1.59))
    ServiceCharge.set(SC)

    SubTotalOfITEMS = "₹ "+ str("%.2f"%(PriceOfDrinks + PriceOfCakes + 1.59))
    SubTotal.set(SubTotalOfITEMS)

    Tax = "₹ "+ str('%.2f'%((PriceOfDrinks + PriceOfCakes + 1.59)))
    PaidTax.set(Tax)
    TT = ((PriceOfDrinks + PriceOfCakes + 1.59)*0.15)
    TC = "₹ "+str("%.2f"%(PriceOfDrinks + PriceOfCakes + 1.59 + TT))
    TotalCost.set(TC)

def chkLatta():
    if(var1.get() == 1):
        txtLatta.configure(state = NORMAL)
        txtLatta.focus()
        txtLatta.delete('0', END)
        E_Latta.set("")
    elif (var1.get()==0):
        txtLatta.configure(state=DISABLED)
        E_Latta.set("0")
def chkEspresso():
    if(var2.get() == 1):
        txtEspresso.configure(state = NORMAL)
        txtEspresso.focus()
        txtEspresso.delete('0', END)
        E_Espresso.set("")
    elif (var2.get()==0):
        txtEspresso.configure(state=DISABLED)
        E_Espresso.set("0")
def chkIced_Latta():
    if(var3.get() == 1):
        txtIced_Latta.configure(state = NORMAL)
        txtIced_Latta.focus()
        txtIced_Latta.delete('0', END)
        E_Iced_Latta.set("")
    elif (var3.get()==0):
        txtIced_Latta.configure(state=DISABLED)
        E_Iced_Latta.set("0")
def chkValle_Coffee():
    if(var4.get() == 1):
        txtValle_Coffee.configure(state = NORMAL)
        txtValle_Coffee.focus()
        txtValle_Coffee.delete('0', END)
        E_Vale_Coffee.set("")
    elif (var4.get()==0):
        txtValle_Coffee.configure(state=DISABLED)
        E_Vale_Coffee.set("0")
def chkCappucino():
    if(var5.get() == 1):
        txtCappuccino.configure(state = NORMAL)
        txtCappuccino.focus()
        txtCappuccino.delete('0', END)
        E_Cappucino.set("")
    elif (var5.get()==0):
        txtCappuccino.configure(state=DISABLED)
        E_Cappucino.set("0")
def chkAfrican_Coffee():
    if(var6.get() == 1):
        txtAfrican_Coffee.configure(state = NORMAL)
        txtAfrican_Coffee.focus()
        txtAfrican_Coffee.delete('0', END)
        E_African_Coffee.set("")
    elif (var6.get()==0):
        txtAfrican_Coffee.configure(state=DISABLED)
        E_African_Coffee.set("0")
def chkAmerican_Coffee():
    if(var7.get() == 1):
        txtAmerican_Coffee.configure(state = NORMAL)
        txtAmerican_Coffee.focus()
        txtAmerican_Coffee.delete('0', END)
        E_American_Coffee.set("")
    elif (var7.get()==0):
        txtAmerican_Coffee.configure(state=DISABLED)
        E_American_Coffee.set("0")
def chkIced_Cappucino():
    if(var8.get() == 1):
        txtIced_Cappucino.configure(state = NORMAL)
        txtIced_Cappucino.focus()
        txtIced_Cappucino.delete('0', END)
        E_Iced_Cappucino.set("")
    elif (var8.get()==0):
        txtIced_Cappucino.configure(state=DISABLED)
        E_Iced_Cappucino.set("0")
def chkSchool_Cake():
    if(var9.get() == 1):
        txtSchool_Cake.configure(state = NORMAL)
        txtSchool_Cake.focus()
        txtSchool_Cake.delete('0', END)
        E_School_Cake.set("")
    elif (var9.get()==0):
        txtSchool_Cake.configure(state=DISABLED)
        E_School_Cake.set("0")
def chkSunny_AO_Cake():
    if(var10.get() == 1):
        txtSunny_AO_Cake.configure(state = NORMAL)
        txtSunny_AO_Cake.focus()
        txtSunny_AO_Cake.delete('0', END)
        E_Sunny_AO_Cake.set("")
    elif (var10.get()==0):
        txtSunny_AO_Cake.configure(state=DISABLED)
        E_Sunny_AO_Cake.set("0")
def chkJonathan_YO_Cake():
    if(var11.get() == 1):
        txtJonathan_YO_Cake.configure(state = NORMAL)
        txtJonathan_YO_Cake.focus()
        txtJonathan_YO_Cake.delete('0', END)
        E_Jonathan_YO_Cake.set("")
    elif (var11.get()==0):
        txtJonathan_YO_Cake.configure(state=DISABLED)
        E_Jonathan_YO_Cake.set("0")
def chkWest_African_Cake():
    if(var12.get() == 1):
        txtWest_African_Cake.configure(state = NORMAL)
        txtWest_African_Cake.focus()
        txtWest_African_Cake.delete('0', END)
        E_West_African.set("")
    elif (var12.get()==0):
        txtWest_African_Cake.configure(state=DISABLED)
        E_West_African.set("0")

def chkLagos_Chocolate_Cake():
    if(var13.get() == 1):
        txtLagos_Chocolate_Cake.configure(state = NORMAL)
        txtLagos_Chocolate_Cake.focus()
        txtLagos_Chocolate_Cake.delete('0', END)
        E_Lagos_Chcolate_Cake.set("")
    elif (var13.get()==0):
        txtLagos_Chocolate_Cake.configure(state=DISABLED)
        E_Lagos_Chcolate_Cake.set("0")

def chkKillburn_Chocolate_Cake():
    if(var14.get() == 1):
        txtKillburn_Chocolate_Cake.configure(state = NORMAL)
        txtKillburn_Chocolate_Cake.focus()
        txtKillburn_Chocolate_Cake.delete('0', END)
        E_Killburn_Chocolate_Cake.set("")
    elif (var14.get()==0):
        txtKillburn_Chocolate_Cake.configure(state=DISABLED)
        E_Killburn_Chocolate_Cake.set("0")
def chkCarlton_Hill_Chocolate_Cake():
    if(var15.get() == 1):
        txtCarlton_Hill_Chocolate_Cake.configure(state = NORMAL)
        txtCarlton_Hill_Chocolate_Cake.focus()
        txtCarlton_Hill_Chocolate_Cake.delete('0', END)
        E_Carlton_Hill_Chocolate_Cake.set("")
    elif (var15.get()==0):
        txtCarlton_Hill_Chocolate_Cake.configure(state=DISABLED)
        E_Carlton_Hill_Chocolate_Cake.set("0")

def chkQueen_Park_Chocolate_Cake():
    if(var16.get() == 1):
        txtQueen_Park_Chocolate_Cake.configure(state = NORMAL)
        txtQueen_Park_Chocolate_Cake.focus()
        txtQueen_Park_Chocolate_Cake.delete('0', END)
        E_Queen_Park_Chocolate_Cake.set("")
    elif (var16.get()==0):
        txtQueen_Park_Chocolate_Cake.configure(state=DISABLED)
        E_Queen_Park_Chocolate_Cake.set("0")
def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10903, 609235)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+Receipt_Ref.get()+'\t'+DateOfOrder.get()+"\n")
    txtReceipt.insert(END, 'Item:\t\t\t' + 'Cost Of Items\n')
    txtReceipt.insert(END,'Latta:  \t\t\t' + E_Latta.get()+'\t'+DateOfOrder.get()+"\n")
    txtReceipt.insert(END, 'Espresso:  \t\t\t' + E_Espresso.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'Iced Latta:  \t\t\t' + E_Iced_Latta.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'Vale Coffee:  \t\t\t' + E_Vale_Coffee.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'Cappucino :  \t\t\t' + E_Cappucino.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'African Coffee:  \t\t\t' + E_African_Coffee.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'American Coffee:  \t\t\t' + E_American_Coffee.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'Iced Cappucino:  \t\t\t' + E_Iced_Cappucino.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'School Cake:  \t\t\t' + E_School_Cake.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'Sunday O Cake:  \t\t\t' + E_Sunny_AO_Cake.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'Jonathan O Cake:  \t\t\t' + E_Jonathan_YO_Cake.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'West African Cake:  \t\t\t' + E_West_African.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'Lagos Chocolate Cake:  \t\t\t' + E_Lagos_Chcolate_Cake.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'Killburn Chocolate Cake:  \t\t\t' + E_Killburn_Chocolate_Cake.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'Carlton Hill Chocolate Cake:  \t\t\t' + E_Carlton_Hill_Chocolate_Cake.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, "Queen's Park Chocolate Cake:  \t\t\t" + E_Queen_Park_Chocolate_Cake.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END,"Cost of Drinks \t\t\t\t" + CostOfDrinks.get() + '\nTax Paid: \t\t\t\t' + PaidTax.get()+"\n")
    txtReceipt.insert(END,"Cost of Cakes \t\t\t\t" + CostOfCakes.get() + '\nSub Total: \t\t\t\t' + SubTotal.get() + "\n")
    txtReceipt.insert(END,"Service Charge \t\t\t\t" + ServiceCharge.get() + '\nTotal Cost: \t\t\t\t' + ServiceCharge.get()+"\n")


#================================DRINKS====================================================#
Latta = Checkbutton(Drinks_F, text= " Latta",variable=var1, onvalue = 1, offvalue = 0, command=chkLatta, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=0, sticky = W)
Espresso = Checkbutton(Drinks_F, text= "Espresso",variable=var2, onvalue = 1, offvalue = 0, command=chkEspresso, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=1, sticky = W)
Iced_Latta = Checkbutton(Drinks_F, text= "Iced Latta",variable=var3, onvalue = 1, offvalue = 0, command=chkIced_Latta, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=2, sticky = W)
Vale_Coffee = Checkbutton(Drinks_F, text= "Vale Coffee",variable=var4, onvalue = 1, offvalue = 0, command=chkValle_Coffee, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=3, sticky = W)
Cappucino = Checkbutton(Drinks_F, text= "Cappucino",variable=var5, onvalue = 1, offvalue = 0, command=chkCappucino, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=4, sticky = W)
African_Coffee = Checkbutton(Drinks_F, text= "African Coffee",variable=var6, onvalue = 1, command=chkAfrican_Coffee, offvalue = 0, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=5, sticky = W)
American_Coffee = Checkbutton(Drinks_F, text= "American Coffee",variable=var7, onvalue = 1, command=chkAmerican_Coffee, offvalue = 0, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=6, sticky = W)
Iced_Cappucino = Checkbutton(Drinks_F, text= "Iced Cappucino",variable=var8, onvalue = 1, command=chkIced_Cappucino, offvalue = 0, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=7, sticky = W)
#===============================Entry Box for Drinks======================================================#
txtLatta = Entry(Drinks_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED, textvariable=E_Latta)
txtLatta.grid(row=0, column=1)
txtEspresso = Entry(Drinks_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED,textvariable=E_Espresso)
txtEspresso.grid(row=1, column=1)
txtIced_Latta = Entry(Drinks_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED, textvariable=E_Iced_Latta)
txtIced_Latta.grid(row=2, column=1)
txtValle_Coffee = Entry(Drinks_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED, textvariable=E_Vale_Coffee)
txtValle_Coffee.grid(row=3, column=1)
txtCappuccino = Entry(Drinks_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED, textvariable=E_Cappucino)
txtCappuccino.grid(row=4, column=1)
txtAfrican_Coffee = Entry(Drinks_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED, textvariable=E_African_Coffee)
txtAfrican_Coffee.grid(row=5, column=1)
txtAmerican_Coffee = Entry(Drinks_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED, textvariable = E_American_Coffee)
txtAmerican_Coffee.grid(row=6, column=1)
txtIced_Cappucino = Entry(Drinks_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED,  textvariable = E_Iced_Cappucino)
txtIced_Cappucino.grid(row=7, column=1)
#===============================Entry Box for Cakes======================================================#
txtSchool_Cake = Entry(Cake_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED, textvariable=E_School_Cake)
txtSchool_Cake.grid(row=0, column=1)
txtSunny_AO_Cake = Entry(Cake_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED, textvariable=E_Sunny_AO_Cake)
txtSunny_AO_Cake.grid(row=1, column=1)
txtJonathan_YO_Cake = Entry(Cake_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED, textvariable=E_Jonathan_YO_Cake)
txtJonathan_YO_Cake.grid(row=2, column=1)
txtWest_African_Cake = Entry(Cake_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED, textvariable=E_West_African)
txtWest_African_Cake.grid(row=3, column=1)
txtLagos_Chocolate_Cake = Entry(Cake_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED, textvariable=E_Lagos_Chcolate_Cake)
txtLagos_Chocolate_Cake.grid(row=4, column=1)
txtKillburn_Chocolate_Cake = Entry(Cake_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED, textvariable=E_Killburn_Chocolate_Cake)
txtKillburn_Chocolate_Cake.grid(row=5, column=1)
txtCarlton_Hill_Chocolate_Cake = Entry(Cake_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED, textvariable=E_Carlton_Hill_Chocolate_Cake)
txtCarlton_Hill_Chocolate_Cake.grid(row=6, column=1)
txtQueen_Park_Chocolate_Cake = Entry(Cake_F,font=('aerial',16,'bold'), bd = 8, width=6, justify=LEFT, state = DISABLED, textvariable=E_Queen_Park_Chocolate_Cake)
txtQueen_Park_Chocolate_Cake.grid(row=7, column=1)
#=======================================Cake======================================#
SchoolCake = Checkbutton(Cake_F, text= "School Cake \t\t\t",variable=var9, onvalue = 1, command=chkSchool_Cake, offvalue = 0, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=0, sticky = W)
Sunny_AO_Cake = Checkbutton(Cake_F, text= "Sunday O Cake",variable=var10, onvalue = 1, command=chkSunny_AO_Cake, offvalue = 0, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=1, sticky = W)
Jonathan_YO_Cake = Checkbutton(Cake_F, text= "Jonathan O Cake",variable=var11, onvalue = 1,command=chkJonathan_YO_Cake, offvalue = 0, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=2, sticky = W)
West_African_Cake = Checkbutton(Cake_F, text= "West African Cake",variable=var12, onvalue = 1, command=chkWest_African_Cake, offvalue = 0, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=3, sticky = W)
Lagos_Chocolate_Cake = Checkbutton(Cake_F, text= "Lagos Chocolate Cake",variable=var13, onvalue = 1, command=chkLagos_Chocolate_Cake, offvalue = 0, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=4, sticky = W)
Killburn_Chocolate_Cake = Checkbutton(Cake_F, text= "Killburn Chocolate Cake",variable=var14, onvalue = 1, command=chkKillburn_Chocolate_Cake, offvalue = 0, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=5, sticky = W)
Carlton_Hill_Cake = Checkbutton(Cake_F, text= "Carlton Hill Chocolate Cake",variable=var15, onvalue = 1, offvalue = 0, command=chkCarlton_Hill_Chocolate_Cake, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=6, sticky = W)
Queen_Park_Cake = Checkbutton(Cake_F, text= "Queen's Park Chocolate Cake",variable=var16, onvalue = 1, offvalue = 0,command=chkQueen_Park_Chocolate_Cake, font = ('aerial',18,'bold'),bg='Powder Blue',).grid(row=7, sticky = W)
#=================================Total Cost====================================================================#
lblCostOfDrinks = Label(Cost_F, font = ('aerial',14,'bold'), text = "Cost of Drink \t",  bg = 'Powder Blue',fg = 'Black', )
lblCostOfDrinks.grid(row=0, column = 0, sticky = W)
txtCostOfDrinks = Entry(Cost_F,bg="white", bd = 7, insertwidth=2, font=("aerial",14,'bold'),textvariable=CostOfDrinks, justify=LEFT)
txtCostOfDrinks.grid(row=0,column=1,)

lblCostOfCakes = Label(Cost_F, font = ('aerial',14,'bold'), text = "Cost of Cakes \t",  bg = 'Powder Blue',fg = 'Black', )
lblCostOfCakes.grid(row=1, column = 0, sticky = W)
txtCostOfCakes = Entry(Cost_F,bg="white", bd = 7, insertwidth=2, font=("aerial",14,'bold'),textvariable=CostOfCakes, justify=LEFT)
txtCostOfCakes.grid(row=1,column=1,)

lblServiceCharge = Label(Cost_F, font = ('aerial',14,'bold'), text = "Service Charge \t",  bg = 'Powder Blue',fg = 'Black', )
lblServiceCharge.grid(row=2, column = 0, sticky = W)
txtServiceCharge = Entry(Cost_F,bg="white", bd = 7, insertwidth=2, font=("aerial",14,'bold'), textvariable=ServiceCharge, justify=LEFT)
txtServiceCharge.grid(row=2,column=1,)
#=================================Payment Information====================================================================#
lblPaidTax = Label(Cost_F, font = ('aerial',14,'bold'), text = "\t Paid Tax \t",  bg = 'Powder Blue',fg = 'Black', )
lblPaidTax.grid(row=0, column = 2, sticky = W)
txtPaidTax = Entry(Cost_F,bg="white", bd = 7, insertwidth=2, font=("aerial",14,'bold'),textvariable=PaidTax, justify=LEFT)
txtPaidTax.grid(row=0,column=3,)

lblSubTotal = Label(Cost_F, font = ('aerial',14,'bold'), text = "\tSub Total",  bg = 'Powder Blue',fg = 'Black', )
lblSubTotal.grid(row=1, column=2, sticky = W)
txtSubTotal = Entry(Cost_F,bg="white", bd = 7, insertwidth=2, font=("aerial",14,'bold'),textvariable=SubTotal, justify=LEFT)
txtSubTotal.grid(row=1,column=3,)

lblTotalCost = Label(Cost_F, font = ('aerial',14,'bold'), text = " \tTotal Cost",  bg = 'Powder Blue',fg = 'Black', )
lblTotalCost.grid(row=2, column=2, sticky = W)
txtTotalCost = Entry(Cost_F,bg="white", bd = 7, insertwidth=2, font=("aerial",14,'bold'),textvariable=TotalCost, justify=LEFT)
txtTotalCost.grid(row=2,column=3,)
#=================================Receipt====================================================================#
txtReceipt = Text(Receipt_F, width=46, height=12,bg = "White", bd = 4, font=('arial',12,'bold'))
txtReceipt.grid(row=0, column=0)
#================================Function Declaration========================================================================#

def iExit():
    iExit = tkinter.messagebox.askyesno("Exit Cafe Management System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return
def Reset():
    E_Latta.set("0")
    E_Espresso.set("0")
    E_Iced_Latta.set("0")
    E_Vale_Coffee.set("0")
    E_Cappucino.set("0")
    E_African_Coffee.set("0")
    E_American_Coffee.set("0")
    E_Iced_Cappucino.set("0")

    E_School_Cake.set("0")
    E_Sunny_AO_Cake.set("0")
    E_Jonathan_YO_Cake.set("0")
    E_West_African.set("0")
    E_Lagos_Chcolate_Cake.set("0")
    E_Killburn_Chocolate_Cake.set("0")
    E_Carlton_Hill_Chocolate_Cake.set("0")
    E_Queen_Park_Chocolate_Cake.set("0")

    CostOfDrinks.set("")
    CostOfCakes.set("")
    ServiceCharge.set("")
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    txtReceipt.delete("1.0", END)

    txtLatta.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtIced_Latta.configure(state=DISABLED)
    txtValle_Coffee.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtAfrican_Coffee.configure(state=DISABLED)
    txtAmerican_Coffee.configure(state=DISABLED)
    txtIced_Cappucino.configure(state=DISABLED)
    txtSchool_Cake.configure(state=DISABLED)
    txtSunny_AO_Cake.configure(state=DISABLED)
    txtJonathan_YO_Cake.configure(state=DISABLED)
    txtWest_African_Cake.configure(state=DISABLED)
    txtLagos_Chocolate_Cake.configure(state=DISABLED)
    txtKillburn_Chocolate_Cake.configure(state=DISABLED)
    txtCarlton_Hill_Chocolate_Cake.configure(state=DISABLED)
    txtQueen_Park_Chocolate_Cake.configure(state=DISABLED)


#=================================Buttons===========================================================================#
btnTotal = Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=CostOfItem, width=4,text="Total",bg="Powder Blue",).grid(row=0,column=0)
btnReceipt = Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=Receipt,width=4,text="Receipt",bg="Powder Blue",).grid(row=0,column=1)
btnReset = Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=Reset, width=4,text="Reset",bg="Powder Blue",).grid(row=0,column=2)
btnExit = Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=iExit,width=4,text="Exit",bg="Powder Blue",).grid(row=0,column=3)
#=================================Calculator Display==========================================================#


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


txtDisplay = Entry(Cal_F,width=45, bg="white", bd = 4, font=("aerial",12,'bold'), justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")
#============================Calculator Buttons===========================================================================#
btn7 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=lambda:btnClick(7),width=4,text="7",bg="Powder Blue",).grid(row=2,column=0)
btn8 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=lambda:btnClick(8),width=4,text="8",bg="Powder Blue",).grid(row=2,column=1)
btn9 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=lambda:btnClick(9),width=4,text="9",bg="Powder Blue",).grid(row=2,column=2)
btnAdd = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=lambda:btnClick("+"),width=4,text="+",bg="Powder Blue",).grid(row=2,column=3)
btn4 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=lambda:btnClick(4),width=4,text="4",).grid(row=3,column=0)
btn5 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=lambda:btnClick(5),width=4,text="5",).grid(row=3,column=1)
btn6 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=lambda:btnClick(6),width=4,text="6",).grid(row=3,column=2)
btnSub = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=lambda:btnClick("-"),width=4,text="-",bg="Powder Blue",).grid(row=3,column=3)
btn3 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=lambda:btnClick(3),width=4,text="3").grid(row=4,column=0)
btn2 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=lambda:btnClick(2),width=4,text="2").grid(row=4,column=1)
btn1 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=lambda:btnClick(1),width=4,text="1").grid(row=4,column=2)
btnMulti = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=lambda:btnClick("*"),width=4,text="*",bg="Powder Blue",).grid(row=4,column=3)
btn0 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=lambda:btnClick(0),width=4,text="0",bg="Powder Blue",).grid(row=5,column=0)
btnClear = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=btnClear,width=4,text="C",bg="Powder Blue",).grid(row=5,column=1)
btnEquals = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=btnEquals,width=4,text="=",bg="Powder Blue",).grid(row=5,column=2)
btnDiv = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font=("aerial",16,'bold'),command=lambda:btnClick("/"),width=4,text="/",bg="Powder Blue",).grid(row=5,column=3)

root.mainloop()