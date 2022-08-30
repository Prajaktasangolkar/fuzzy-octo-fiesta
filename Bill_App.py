from tkinter import*
import random
import os
from tkinter import messagebox
import mysql.connector as connector

# ============main heading ============================
class Bill_App:
    # def _init_(self):
    #     self.con = connector.connect(
    #         host='localhost', user='root', password='Praju25', database='customer')

    #     query = 'create table if not exists user(billNumber int primary key,userName varchar(200), phone varchar(12))'
    #     cur = self.con.cursor()
    #     cur.execute(query)
    #     print("Created")

    def insert_user(self, billNumber, username, phone):
        print("Insert operation begins.")
        print(username)
        query = "insert into user(billNumber, userName, phone)values({}, '{}', '{}')".format(
            billNumber, username, phone)
        # query = f"INSERT INTO customer(cname,cphn) values ('{username}',{phone})"
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")
    def _init_(self, root):
        self.con = connector.connect(
            host='localhost', user='root', password='Praju25', database='customer')

        query = 'create table if not exists user(billNumber int primary key,userName varchar(200), phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Store Billing Software", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg=bg_color, fg="White", relief=GROOVE)
        title.pack(fill=X)
    # ================variables=======================
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
       
    # ============grocery==============================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
       
       
    # ==============Total product price================
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
     
    # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
    # ===============Tax================================
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
       
    # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="yellow", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color,fg="white", font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg=bg_color,fg="white", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg=bg_color,fg="white", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

    # ===================Medical====================================
        F2 = LabelFrame(self.root, text="Medical Purpose", font=('times new roman', 15, 'bold'), bd=10, fg="yellow", bg=bg_color)
        F2.place(x=10, y=180, width=525, height=350)

        sanitizer_lbl = Label(F2, text="Sanitizer", font=('times new roman', 16, 'bold'), bg=bg_color, fg="lightgreen")
        sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sanitizer_txt = Entry(F2, width=10, textvariable=self.sanitizer, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sanitizer_txt.grid(row=0, column=1, padx=10, pady=10)

        mask_lbl = Label(F2, text="Mask", font=('times new roman', 16, 'bold'), bg=bg_color, fg="lightgreen")
        mask_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mask_txt = Entry(F2, width=10, textvariable=self.mask, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mask_txt.grid(row=1, column=1, padx=10, pady=10)

        hand_gloves_lbl = Label(F2, text="Hand Gloves", font=('times new roman', 16, 'bold'), bg=bg_color, fg="lightgreen")
        hand_gloves_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        hand_gloves_txt = Entry(F2, width=10, textvariable=self.hand_gloves, font=('times new roman', 16, 'bold'), bd=5, relief =GROOVE)
        hand_gloves_txt.grid(row=2, column=1, padx=10, pady=10)

    # ==========GroceryItems=========================
        F3 = LabelFrame(self.root, text="Grocery Items", font=('times new roman', 15, 'bold'), bd=10, fg="yellow", bg=bg_color)
        F3.place(x=440, y=180, width=425, height=350)

        rice_lbl = Label(F3, text="Rice", font=('times new roman', 16, 'bold'),bg=bg_color, fg="lightgreen")
        rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        rice_txt = Entry(F3, width=10, textvariable=self.rice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        food_oil_lbl = Label(F3, text="Food Oil", font=('times new roman', 16, 'bold'), bg=bg_color, fg="lightgreen")
        food_oil_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        food_oil_txt = Entry(F3, width=10, textvariable=self.food_oil, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        food_oil_txt.grid(row=1, column=1, padx=10, pady=10)

        wheat_lbl = Label(F3, text="Wheat", font=('times new roman', 16, 'bold'),bg=bg_color, fg="lightgreen")
        wheat_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        wheat_txt = Entry(F3, width=10, textvariable=self.wheat, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        wheat_txt.grid(row=2, column=1, padx=10, pady=10)

      

   

    # =================BillArea======================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=900, y=180, width=390, height=350)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    # =======================ButtonFrame=============
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="yellow", bg=bg_color)
        F6.place(x=0, y=540, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Medical Price", font=('times new roman', 15, 'bold'), bg=bg_color, fg="white")
        m1_lbl.grid(row=0, column=0, padx=20, pady=5, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.medical_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=5)

        m2_lbl = Label(F6, text="Total Grocery Price", font=('times new roman', 15, 'bold'), bg=bg_color, fg="white")
        m2_lbl.grid(row=1, column=0, padx=20, pady=5, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=5)

        
        m4_lbl = Label(F6, text="Medical Tax", font=('times new roman', 15, 'bold'),  bg=bg_color, fg="white")
        m4_lbl.grid(row=0, column=2, padx=20, pady=5, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.medical_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=5)

        m5_lbl = Label(F6, text="Grocery Tax", font=('times new roman', 14, 'bold'),  bg=bg_color, fg="white")
        m5_lbl.grid(row=1, column=2, padx=20, pady=5, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=5)


    # =======Buttons-======================================
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="#535C68", fg="white", pady=15, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="#535C68", fg="white", pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

#================totalBill==========================
    def total(self):
        self.m_h_g_p = self.hand_gloves.get()*12
        self.m_s_p = self.sanitizer.get()*2
        self.m_m_p = self.mask.get()*5
        
        self.total_medical_price = float(self.m_m_p+self.m_h_g_p+self.m_s_p)

        self.medical_price.set("Rs. "+str(self.total_medical_price))
        self.c_tax = round((self.total_medical_price*0.05), 2)
        self.medical_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p = self.rice.get()*10
        self.g_f_o_p = self.food_oil.get()*10
        self.g_w_p = self.wheat.get()*10
        
        self.total_grocery_price = float(self.g_r_p+self.g_f_o_p+self.g_w_p)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*5), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        # self.c_d_s_p = self.sprite.get()*10
        # self.c_d_l_p = self.limka.get()*10
        # self.c_d_m_p = self.mazza.get()*10
        self.total_bill = float(self.total_medical_price+self.total_grocery_price+self.c_tax+self.g_tax)

        
       
#==============welcome-bill==============================
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome Webcode Retail")
        self.txtarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")

#=========billArea=================================================
    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.medical_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" :
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
    # ============medical===========================
        if self.sanitizer.get() != 0:
            self.txtarea.insert(END, f"\n Sanitizer\t\t{self.sanitizer.get()}\t\t{self.m_s_p}")
        if self.mask.get() != 0:
            self.txtarea.insert(END, f"\n Sanitizer\t\t{self.mask.get()}\t\t{self.m_m_p}")
        if self.hand_gloves.get() != 0:
            self.txtarea.insert(END, f"\n Hand Gloves\t\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}")
        # if self.dettol.get() != 0:
        #     self.txtarea.insert(END, f"\n Dettol\t\t{self.dettol.get()}\t\t{self.m_d_p}")
        # if self.newsprin.get() != 0:
        #     self.txtarea.insert(END, f"\n Newsprin\t\t{self.newsprin.get()}\t\t{self.m_n_p}")
        # if self.thermal_gun.get() != 0:
        #     self.txtarea.insert(END , f"\n Thermal Gun\t\t{self.sanitizer.get()}\t\t{self.m_t_g_p}")
    # ==============Grocery============================
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_o_p}")
        if self.wheat.get() != 0:
            self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
        # if self.daal.get() != 0:
        #     self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
        # if self.flour.get() != 0:
        #     self.txtarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t\t{self.g_f_p}")
        # if self.maggi.get() != 0:
        #     self.txtarea.insert(END, f"\n Maggi\t\t{self.maggi.get()}\t\t{self.g_m_p}")
        # #================ColdDrinks==========================
        # if self.sprite.get() != 0:
        #     self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.c_d_s_p}")
        # if self.limka.get() != 0:
        #     self.txtarea.insert(END, f"\n Sanitizer\t\t{self.limka.get()}\t\t{self.c_d_l_p}")
        # if self.mazza.get() != 0:
        #     self.txtarea.insert(END, f"\n Mazza\t\t{self.mazza.get()}\t\t{self.c_d_m_p}")
        # if self.coke.get() != 0:
        #     self.txtarea.insert(END, f"\n Dettol\t\t{self.coke.get()}\t\t{self.c_d_c_p}")
        # if self.fanta.get() != 0:
        #     self.txtarea.insert(END, f"\n Fanta\t\t{self.newsprin.get()}\t\t{self.c_d_f_p}")
        # if self.mountain_duo.get() != 0:
        #     self.txtarea.insert(END, f"\n Mountain Duo\t\t{self.sanitizer.get()}\t\t{self.c_m_d}")
        #     self.txtarea.insert(END, f"\n--------------------------------")
        # ===============taxes==============================
        if self.medical_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Medical Tax\t\t\t{self.medical_tax.get()}")
        if self.grocery_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
        # if self.cold_drinks_tax.get() != '0.0':
        #     self.txtarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")

        self.txtarea.insert(END, f"\n Total Bil:\t\t\t Rs.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------")
        self.save_bill()

    #=========savebill============================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            self.insert_user(self.bill_no.get(),self.c_name.get(),self.c_phone.get())
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return

    # ===================find_bill================================
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                 self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    # ======================clear-bill======================
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.sanitizer.set(0)
            self.mask.set(0)
            self.hand_gloves.set(0)
            
    # ============grocery==============================
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            
    # # =============coldDrinks=============================
    #         self.sprite.set(0)
    #         self.limka.set(0)
    #         self.mazza.set(0)
    #         self.coke.set(0)
    #         self.fanta.set(0)
    #         self.mountain_duo.set(0)
    # ====================taxes================================
            self.medical_price.set("")
            self.grocery_price.set("")
            # self.cold_drinks_price.set("")

            self.medical_tax.set("")
            self.grocery_tax.set("")
            # self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()
        # =====================
        # ===============
   
    # ===========exit=======================
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()
