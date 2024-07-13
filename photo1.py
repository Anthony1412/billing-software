from tkinter import *
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry('%dx%d+%d+%d' %(1170,400,0,0))
        self.root.title("Biling Software")
        title=Label(self.root,text="Billing software",bd=12,relief=GROOVE,bg="yellow",fg="black",font=("times new roman",30,"bold"),pady=10).pack(fill=X)
        
        #=============Variables-------------
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        #Grocery-------------
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.wheat=IntVar()
        self.daal=IntVar()        
        self.sugar=IntVar()
        self.tea=IntVar()
        #-----------------Cold Drinks
        self.maaza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.limca=IntVar()
        self.thumbsup=IntVar()
        self.sprite=IntVar()
        #------------Total Product Price and tax variable----------------
        self.tax=IntVar()
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #-------------------Customer-----------
        self.c_name=StringVar()
        self.c_phon=StringVar()

        #
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()

        #**************** CUSTOMER DETAIL *************
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),bg="blue",fg="gold")
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg="#cceeff",font=("ariel",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=19,textvariable=self.c_name,font="ariel 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
        
        cphn_lbl=Label(F1,text="Customer ph.No",bg="#cceeff",font=("ariel",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=19,textvariable=self.c_phon,font="ariel 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        c_bill_lbl=Label(F1,text="Bill No",bg="#cceeff",font=("ariel",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=19,textvariable=self.search_bill,font="ariel 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)       

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=7,bd=7,font="ariel 12  bold").grid(row=0,column=7,padx=10,pady=10)


        #cosmetic frame( second frame)

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="COSMETICS",font=("times new roman",15,"bold"),bg="blue",fg="gold")
        F2.place(x=5,y=180,width=325,height=380)
        #PRODUCTS IN COSMETIC GRID 
        bath_lbl=Label(F2,text="Bath soap",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font="ariel 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=9,pady=8)
        
        cream_lbl=Label(F2,text="Face Cream",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=1,column=0,padx=20,pady=5)
        cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font="ariel 15",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=8)

        wash_lbl=Label(F2,text="Face wash",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=2,column=0,padx=20,pady=5)
        wash_txt=Entry(F2,width=10,textvariable=self.face_wash,font="ariel 15",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=8)

    
        spray_lbl=Label(F2,text="Hair Spray",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=3,column=0,padx=20,pady=5)
        spray_txt=Entry(F2,width=10,textvariable=self.spray,font="ariel 15",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=8)
        
        gel_lbl=Label(F2,text="Hair Gel",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=4,column=0,padx=20,pady=5)
        gel_txt=Entry(F2,width=10,textvariable=self.gell,font="ariel 15",bd=7,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=8)

        body_lbl=Label(F2,text="Body lotion",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=5,column=0,padx=20,pady=5)
        body_txt=Entry(F2,width=10,textvariable=self.loshan,font="ariel 15",bd=7,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=8)
        
        #end of cosmatic

        # product in grocery

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="GROCERY",font=("times new roman",15,"bold"),bg="blue",fg="gold")
        F3.place(x=326,y=180,width=325,height=380)
        rice_lbl=Label(F3,text="Rice",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        rice_txt=Entry(F3,width=10,textvariable=self.rice,font="ariel 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=9,pady=8)
        
        food_lbl=Label(F3,text="Food oil",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=1,column=0,padx=20,pady=5)
        food_txt=Entry(F3,width=10,textvariable=self.food_oil,font="ariel 15",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=8)

        grains_lbl=Label(F3,text="Grains",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=2,column=0,padx=20,pady=5)
        grains_txt=Entry(F3,width=10,textvariable=self.daal,font="ariel 15",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=8)

    
        wheat_lbl=Label(F3,text="Wheat",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=3,column=0,padx=20,pady=5)
        wheat_txt=Entry(F3,width=10,textvariable=self.wheat,font="ariel 15",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=8)
        
        sugar_lbl=Label(F3,text="Sugar",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=4,column=0,padx=20,pady=5)
        sugar_txt=Entry(F3,width=10,textvariable=self.sugar,font="ariel 15",bd=7,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=8)

        tea_lbl=Label(F3,text="Tea",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=5,column=0,padx=20,pady=5)
        tea_txt=Entry(F3,width=10,textvariable=self.tea,font="ariel 15",bd=7,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=8)



       

        




        # product in coldrinks

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="COLDRINKS",font=("times new roman",15,"bold"),bg="blue",fg="gold")
        F4.place(x=652,y=180,width=325,height=380)

        

        
        slice_lbl=Label(F4,text="MAAZA",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        slice_txt=Entry(F4,width=10,textvariable=self.maaza,font="ariel 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=9,pady=8)
        
        maaza_lbl=Label(F4,text="coke",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=1,column=0,padx=20,pady=5)
        maaza_txt=Entry(F4,width=10,textvariable=self.cock,font="ariel 15",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=8)

        coke_lbl=Label(F4,text="frooti",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=2,column=0,padx=20,pady=5)
        coke_txt=Entry(F4,width=10,textvariable=self.frooti,font="ariel 15",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=8)

    
        dew_lbl=Label(F4,text="thumbsup",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=3,column=0,padx=20,pady=5)
        dew_txt=Entry(F4,width=10,textvariable=self.thumbsup,font="ariel 15",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=8)
        
        appy_lbl=Label(F4,text="Limca",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=4,column=0,padx=20,pady=5)
        appy_txt=Entry(F4,width=10,textvariable=self.limca,font="ariel 15",bd=7,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=8)

        frooti_lbl=Label(F4,text="Sprite",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=5,column=0,padx=20,pady=5)
        frooti_txt=Entry(F4,width=10,textvariable=self.sprite,font="ariel 15",bd=7,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=8)



        #BILL AREA

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=978,y=180,width=385,height=380)

        bill_title=Label(F5,text="BILL AREA",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)


        #BUTTON FRAME

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="BILLING MENU",font=("times new roman",15,"bold"),bg="blue",fg="gold")
        F6.place(x=0,y=562,width=1360,height=150)

        csprice_lbl=Label(F6,text="Total Cosmetic Price",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=0,column=0,padx=10,pady=2)
        csprice_txt=Entry(F6,width=10,textvariable=self.cosmetic_price,font="ariel 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=9,pady=0)

        gctax_lbl=Label(F6,text="Total Grocery Price",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=1,column=0,padx=10,pady=2)
        gctax_txt=Entry(F6,width=10,textvariable=self.grocery_price,font="ariel 15",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=9,pady=0)

        cdtax_lbl=Label(F6,text="Total Coldrinks Price",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=2,column=0,padx=10,pady=2)
        cdtax_txt=Entry(F6,width=10,textvariable=self.cold_drink_price,font="ariel 15",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=9,pady=0)

        cstax_lbl=Label(F6,text="Cosmetic Tax",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=0,column=2,padx=19,pady=2)
        cstax_txt=Entry(F6,width=10,textvariable=self.cosmetic_tax,font="ariel 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=19,pady=0)

        gtax_lbl=Label(F6,text="Grocery Tax",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=1,column=2,padx=19,pady=2)
        gtax_txt=Entry(F6,width=10,textvariable=self.grocery_tax,font="ariel 15",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=19,pady=0)

        ctax_lbl=Label(F6,text="Coldrinks Tax",fg="white",bg="blue",font=("calbiri",15,"bold")).grid(row=2,column=2,padx=19,pady=2)
        ctax_txt=Entry(F6,width=10,textvariable=self.cold_drink_tax,font="ariel 15",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=19,pady=0)

        #total and exit button

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=700,width=640,height=112)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=5,pady=15,width=13,height=2,font="arial 12 bold ").grid(row=0,column=0,padx=5,pady=5)


        generate_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=5,pady=15,width=13,height=2,font="arial 12 bold ").grid(row=0,column=1,padx=5,pady=5)


        clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=5,pady=15,width=13,height=2,font="arial 12 bold ").grid(row=0,column=2,padx=5,pady=5)
 

        exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="Red",fg="white",bd=5,pady=15,width=13,height=2,font="arial 12 bold ").grid(row=0,column=3,padx=5,pady=5)



    def total(self):

        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.spray.get()*180
        self.c_hg_p=self.gell.get()*140
        self.c_bl_p=self.loshan.get()*180


        #calulaing cosmetic price
        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_hs_p+
                                    self.c_hg_p+
                                    self.c_bl_p
                                  )
        self.cosmetic_price.set(str(self.total_cosmetic_price))

        #calculating cosmetic tax
        self.c_tax=(self.total_cosmetic_price*0.05)
        self.cosmetic_tax.set(str(self.c_tax))


        #calcuting grocery price
        self.g_r_p=self.rice.get()*80
        self.g_f_p=self.food_oil.get()*180
        self.g_d_p=self.daal.get()*60
        self.g_w_p=self.wheat.get()*2400
        self.g_s_p=self.sugar.get()*45
        self.g_t_p=self.tea.get()*150
        
        self.total_grocery_price=float(
                                  self.g_r_p+
                                self.g_f_p+
                                self.g_d_p+
                                self.g_w_p+
                                self.g_s_p+
                                self.g_t_p
                                )
        self.grocery_price.set(str(self.total_grocery_price))

        #calculating cosmetic tax
        self.g_tax=(self.total_grocery_price*0.05)
        self.grocery_tax.set(str(self.g_tax))


        #calculating cold drink price
        self.d_m_p=self.maaza.get()*60
        self.d_c_p=self.cock.get()*60
        self.d_f_p=self.frooti.get()*50
        self.d_t_p=self.thumbsup.get()*45
        self.d_l_p=self.limca.get()*40
        self.d_s_p=self.sprite.get()*60

        self.total_cold_drink_price=float(
                                    self.d_m_p+
                                    self.d_c_p+
                                    self.d_f_p+
                                    self.d_t_p+
                                    self.d_l_p+
                                    self.d_s_p
                                  )
        self.cold_drink_price.set(str(self.total_cold_drink_price))

        #Colddrink tax
        self.cd_tax=(self.total_cold_drink_price*0.05)
        self.cold_drink_tax.set(str(self.cd_tax))

        #Total Price
        self.total_bill=float(
                            self.total_cosmetic_price+
                            self.total_grocery_price+
                            self.total_cold_drink_price+
                            self.c_tax+
                            self.g_tax+
                            self.cd_tax
                        )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcome Webcode Retail\n")
        self.txtarea.insert(END,f"\n Bill No : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone No : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n*******************************************")
        self.txtarea.insert(END,f"\n Product\t\t  Qty\t\t     Price")
        self.txtarea.insert(END,f"\n*******************************************")

        
    def bill_area(self):

        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details are must")
        elif self.cosmetic_price.get()=="0.0" and self.grocery_price.get()=="0.0" and self.cold_drink_price.get():
            messagebox.showerror("Error","No Products Purchased")
        else:

            self.welcome_bill()

            #Cosmetics
            if(self.soap.get()!=0):
                self.txtarea.insert(END,f"\nBath Soap\t\t  {self.soap.get()}\t\t     {self.c_s_p}")

            if(self.face_cream.get()!=0):
                self.txtarea.insert(END,f"\nFace Cream\t\t  {self.face_cream.get()}\t\t     {self.c_fc_p}")

            if(self.face_wash.get()!=0):
                self.txtarea.insert(END,f"\nFace wash\t\t  {self.face_wash.get()}\t\t     {self.c_fw_p}")

            if(self.spray.get()!=0):
                self.txtarea.insert(END,f"\nSpray\t\t  {self.spray.get()}\t\t     {self.c_hs_p}")

            if(self.gell.get()!=0):
                self.txtarea.insert(END,f"\nGell\t\t  {self.gell.get()}\t\t     {self.c_hg_p}")\

            if(self.loshan.get()!=0):
                self.txtarea.insert(END,f"\nLotion\t\t  {self.loshan.get()}\t\t     {self.c_bl_p}")



            #Grocery
            if(self.rice.get()!=0):
                self.txtarea.insert(END,f"\nRice\t\t  {self.rice.get()}\t\t     {self.g_r_p}")

            if(self.food_oil.get()!=0):
                self.txtarea.insert(END,f"\nFood oil\t\t  {self.food_oil.get()}\t\t     {self.g_f_p}")

            if(self.daal.get()!=0):
                self.txtarea.insert(END,f"\nDaal\t\t  {self.daal.get()}\t\t     {self.g_d_p}")

            if(self.wheat.get()!=0):
                self.txtarea.insert(END,f"\nWheat\t\t  {self.wheat.get()}\t\t     {self.g_w_p}")

            if(self.sugar.get()!=0):
                self.txtarea.insert(END,f"\nSugar\t\t  {self.sugar.get()}\t\t     {self.g_s_p}")\

            if(self.tea.get()!=0):
                self.txtarea.insert(END,f"\nTea\t\t  {self.tea.get()}\t\t     {self.g_t_p}")



            #Cold Drinks
            if(self.maaza.get()!=0):
                self.txtarea.insert(END,f"\nMazza\t\t  {self.maaza.get()}\t\t     {self.d_m_p}")

            if(self.cock.get()!=0):
                self.txtarea.insert(END,f"\nCock\t\t  {self.cock.get()}\t\t     {self.d_c_p}")

            if(self.frooti.get()!=0):
                self.txtarea.insert(END,f"\nFrooti\t\t  {self.frooti.get()}\t\t     {self.d_f_p}")

            if(self.thumbsup.get()!=0):
                self.txtarea.insert(END,f"\nThumbsup\t\t  {self.thumbsup.get()}\t\t     {self.d_t_p}")

            if(self.limca.get()!=0):
                self.txtarea.insert(END,f"\nLimca\t\t  {self.limca.get()}\t\t     {self.d_l_p}")\

            if(self.sprite.get()!=0):
                self.txtarea.insert(END,f"\nSprite\t\t  {self.sprite.get()}\t\t     {self.d_s_p}")



            self.txtarea.insert(END,f"\n-------------------------------------------")
            if self.cosmetic_tax.get() !="0.0":
                self.txtarea.insert(END,f"\nCosmetic Tax\t\t\t\t     {self.cosmetic_tax.get()}")

            if self.grocery_tax.get() !="0.0":
                self.txtarea.insert(END,f"\nGrocery Tax\t\t\t\t     {self.grocery_tax.get()}")

            if self.cold_drink_tax.get() !="0.0":
                self.txtarea.insert(END,f"\nCold Drink Tax\t\t\t\t     {self.cold_drink_tax.get()}")

            self.txtarea.insert(END,f"\n-------------------------------------------")
            self.txtarea.insert(END,f"\nTotal Price\t\t\t\t    {self.total_bill}")
            self.txtarea.insert(END,f"\n-------------------------------------------")

            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved",f"Bill no. {self.bill_no.get()} Saved Succesfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid bill no")




    def clear_data(self):
        op=messagebox.askyesno("EXIT","Do you really want to clear?")
        if op>0:
            #=============Variables-------------
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            #Grocery-------------
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.daal.set(0)        
            self.sugar.set(0)
            self.tea.set(0)
            #-----------------Cold Drinks
            self.maaza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.limca.set(0)
            self.thumbsup.set(0)
            self.sprite.set(0)
            #------------Total Product Price and tax variable----------------
            self.tax.set("")
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            #-------------------Customer-----------
            self.c_name.set("")
            self.c_phon.set("")

            #
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")

            self.welcome_bill()


    def Exit_app(self):
        op=messagebox.askyesno("EXIT","Do you really want to exit?")
        if op>0:
            self.root.destroy()



       
root=Tk()
obj = Bill_App(root)
root.mainloop()
    
