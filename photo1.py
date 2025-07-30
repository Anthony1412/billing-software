from tkinter import *
import math, random, os
from tkinter import messagebox
from datetime import datetime

TAX_RATE = 0.05  # 5% Tax Rate

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1360x768+0+0')
        self.root.title("Billing Software")
        self.root.configure(bg="#f0f2f5")
        
        # Ensure bills folder exists
        if not os.path.exists("bills"):
            os.mkdir("bills")
        
        # Custom colors
        self.primary_color = "#2c3e50"
        self.secondary_color = "#34495e"
        self.accent_color = "#3498db"
        self.success_color = "#27ae60"
        self.danger_color = "#e74c3c"
        self.light_color = "#ecf0f1"
        self.dark_color = "#2c3e50"
        
        # Fonts
        self.title_font = ("Helvetica", 28, "bold")
        self.heading_font = ("Helvetica", 14, "bold")
        self.normal_font = ("Helvetica", 12)
        self.button_font = ("Helvetica", 12, "bold")
        
        self.create_title_bar()
        self.initialize_variables()
        self.create_customer_frame()
        self.create_product_frames()
        self.create_bill_area()
        self.create_menu_buttons()
        self.welcome_bill()

    def create_title_bar(self):
        title_frame = Frame(self.root, bd=0, relief=FLAT, bg=self.primary_color)
        title_frame.pack(fill=X)
        
        title = Label(title_frame, text="RETAIL BILLING SOFTWARE", bd=0, 
                     bg=self.primary_color, fg="white", font=self.title_font, pady=15)
        title.pack()
        
        # Add a subtle separator
        separator = Frame(self.root, height=2, bd=0, relief=FLAT, bg=self.accent_color)
        separator.pack(fill=X, padx=5)

    def initialize_variables(self):
        # Cosmetic items
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.loshan = IntVar()
        # Grocery items
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        # Cold drinks
        self.maaza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.limca = IntVar()
        self.thumbsup = IntVar()
        self.sprite = IntVar()
        # Prices & Taxes
        self.cosmetic_price = StringVar(value="0.0")
        self.grocery_price = StringVar(value="0.0")
        self.cold_drink_price = StringVar(value="0.0")
        self.cosmetic_tax = StringVar(value="0.0")
        self.grocery_tax = StringVar(value="0.0")
        self.cold_drink_tax = StringVar(value="0.0")
        # Customer details
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar(value=str(random.randint(1000, 9999)))
        self.search_bill = StringVar()

    def create_customer_frame(self):
        F1 = LabelFrame(self.root, bd=5, relief=FLAT, text="Customer Details",
                        font=self.heading_font, bg=self.light_color, fg=self.dark_color)
        F1.place(x=10, y=100, width=1340, height=70)
        
        # Customer Name
        Label(F1, text="Name:", bg=self.light_color, fg=self.dark_color, 
              font=self.normal_font).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        Entry(F1, width=20, textvariable=self.c_name, font=self.normal_font, 
              bd=2, relief=SOLID).grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Phone Number
        Label(F1, text="Phone:", bg=self.light_color, fg=self.dark_color, 
              font=self.normal_font).grid(row=0, column=2, padx=10, pady=5, sticky="w")
        Entry(F1, width=20, textvariable=self.c_phon, font=self.normal_font, 
              bd=2, relief=SOLID).grid(row=0, column=3, padx=5, pady=5, sticky="w")
        
        # Bill Number
        Label(F1, text="Bill No:", bg=self.light_color, fg=self.dark_color, 
              font=self.normal_font).grid(row=0, column=4, padx=10, pady=5, sticky="w")
        Entry(F1, width=15, textvariable=self.bill_no, font=self.normal_font, 
              bd=2, relief=SOLID, state='readonly').grid(row=0, column=5, padx=5, pady=5, sticky="w")
        
        # Search Bill
        Label(F1, text="Search Bill:", bg=self.light_color, fg=self.dark_color, 
              font=self.normal_font).grid(row=0, column=6, padx=10, pady=5, sticky="w")
        Entry(F1, width=15, textvariable=self.search_bill, font=self.normal_font, 
              bd=2, relief=SOLID).grid(row=0, column=7, padx=5, pady=5, sticky="w")
        
        # Search Button
        search_btn = Button(F1, text="SEARCH", command=self.find_bill, width=10, 
                           bd=0, font=self.button_font, bg=self.accent_color, 
                           fg="white", activebackground=self.secondary_color)
        search_btn.grid(row=0, column=8, padx=10, pady=5)
        search_btn.bind("<Enter>", lambda e: search_btn.config(bg=self.secondary_color))
        search_btn.bind("<Leave>", lambda e: search_btn.config(bg=self.accent_color))

    def create_product_frames(self):
        self.create_product_section("Cosmetics", 10, 190, [
            ("Bath Soap", self.soap, 40), 
            ("Face Cream", self.face_cream, 50),
            ("Face Wash", self.face_wash, 60), 
            ("Hair Spray", self.spray, 70),
            ("Hair Gel", self.gell, 45), 
            ("Body Lotion", self.loshan, 55)
        ])
        
        self.create_product_section("Grocery", 340, 190, [
            ("Rice (kg)", self.rice, 60), 
            ("Food Oil (L)", self.food_oil, 120),
            ("Daal (kg)", self.daal, 80), 
            ("Wheat (kg)", self.wheat, 40),
            ("Sugar (kg)", self.sugar, 45), 
            ("Tea (pkt)", self.tea, 50)
        ])
        
        self.create_product_section("Cold Drinks", 670, 190, [
            ("Maaza", self.maaza, 35), 
            ("Coke", self.cock, 40),
            ("Frooti", self.frooti, 30), 
            ("ThumbsUp", self.thumbsup, 40),
            ("Limca", self.limca, 35), 
            ("Sprite", self.sprite, 40)
        ])

    def create_product_section(self, title, x, y, items):
        frame = LabelFrame(self.root, bd=3, relief=GROOVE, text=title.upper(),
                           font=self.heading_font, bg=self.light_color, fg=self.dark_color)
        frame.place(x=x, y=y, width=320, height=380)
        
        # Header with prices
        Label(frame, text="Product", bg=self.light_color, fg=self.dark_color, 
              font=self.normal_font).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        Label(frame, text="Qty", bg=self.light_color, fg=self.dark_color, 
              font=self.normal_font).grid(row=0, column=1, padx=10, pady=5)
        Label(frame, text="Price", bg=self.light_color, fg=self.dark_color, 
              font=self.normal_font).grid(row=0, column=2, padx=10, pady=5)
        
        # Add products with prices
        for idx, (label, var, price) in enumerate(items, start=1):
            # Product name and price label
            Label(frame, text=f"{label} (₹{price})", bg=self.light_color, 
                  fg=self.dark_color, font=self.normal_font).grid(row=idx, column=0, padx=10, pady=5, sticky="w")
            
            # Quantity entry
            Entry(frame, width=5, textvariable=var, font=self.normal_font, 
                  bd=2, relief=SOLID, justify=CENTER).grid(row=idx, column=1, padx=5, pady=5)
            
            # Price display (calculated later)
            Label(frame, text="0", bg=self.light_color, fg=self.dark_color, 
                  font=self.normal_font).grid(row=idx, column=2, padx=10, pady=5)

    def create_bill_area(self):
        F5 = Frame(self.root, bd=3, relief=GROOVE, bg=self.light_color)
        F5.place(x=1000, y=190, width=350, height=380)
        
        # Bill title with current date
        bill_title = Label(F5, text=f"BILL NO. {self.bill_no.get()}", 
                          font=self.heading_font, bd=0, bg=self.accent_color, 
                          fg="white", pady=10)
        bill_title.pack(fill=X)
        
        # Date label
        date_label = Label(F5, text=f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", 
                          font=("Helvetica", 10), bg=self.light_color, fg=self.dark_color)
        date_label.pack(anchor="ne", padx=10, pady=5)
        
        # Scrollable text area
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set, 
                           font=("Courier", 12), bd=0, bg="white", padx=10, pady=10)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        
        # Footer with shop info
        footer = Label(F5, text="Thank you for shopping with us!", 
                      font=("Helvetica", 10, "italic"), bg=self.light_color, 
                      fg=self.dark_color, pady=5)
        footer.pack(fill=X)

    def create_menu_buttons(self):
        menu_frame = Frame(self.root, bd=0, relief=FLAT, bg=self.light_color)
        menu_frame.place(x=1000, y=580, width=350, height=150)
        
        buttons = [
            ("Total", self.total, self.success_color),
            ("Generate Bill", self.bill_area, self.primary_color),
            ("Clear", self.clear_data, self.danger_color),
            ("Exit", self.exit_app, self.secondary_color)
        ]
        
        for idx, (text, command, color) in enumerate(buttons):
            btn = Button(menu_frame, text=text, command=command, width=15, 
                        height=1, bd=0, font=self.button_font, bg=color, 
                        fg="white", activebackground=self.secondary_color)
            btn.grid(row=idx//2, column=idx%2, padx=5, pady=5, sticky="nsew")
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.secondary_color))
            btn.bind("<Leave>", lambda e, b=btn, c=color: b.config(bg=c))
            
            # Configure grid weights for responsive buttons
            menu_frame.grid_columnconfigure(idx%2, weight=1)
            menu_frame.grid_rowconfigure(idx//2, weight=1)

    def total(self):
        # Calculate total for cosmetics
        self.cosmetic_total = (
            self.soap.get() * 40 +
            self.face_cream.get() * 50 +
            self.face_wash.get() * 60 +
            self.spray.get() * 70 +
            self.gell.get() * 45 +
            self.loshan.get() * 55
        )
        self.cosmetic_price.set(str(self.cosmetic_total))
        self.cosmetic_tax.set(str(round(self.cosmetic_total * TAX_RATE, 2)))
        
        # Calculate total for grocery
        self.grocery_total = (
            self.rice.get() * 60 +
            self.food_oil.get() * 120 +
            self.daal.get() * 80 +
            self.wheat.get() * 40 +
            self.sugar.get() * 45 +
            self.tea.get() * 50
        )
        self.grocery_price.set(str(self.grocery_total))
        self.grocery_tax.set(str(round(self.grocery_total * TAX_RATE, 2)))
        
        # Calculate total for cold drinks
        self.cold_drink_total = (
            self.maaza.get() * 35 +
            self.cock.get() * 40 +
            self.frooti.get() * 30 +
            self.thumbsup.get() * 40 +
            self.limca.get() * 35 +
            self.sprite.get() * 40
        )
        self.cold_drink_price.set(str(self.cold_drink_total))
        self.cold_drink_tax.set(str(round(self.cold_drink_total * TAX_RATE, 2)))
        
        # Calculate overall total
        self.total_bill = (
            float(self.cosmetic_price.get()) +
            float(self.grocery_price.get()) +
            float(self.cold_drink_price.get()) +
            float(self.cosmetic_tax.get()) +
            float(self.grocery_tax.get()) +
            float(self.cold_drink_tax.get())
        )
        
        # Update bill area with totals
        self.welcome_bill()
        self.txtarea.insert(END, f"\n\n{'Cosmetics Total':<20}: ₹{self.cosmetic_price.get():>10}")
        self.txtarea.insert(END, f"\n{'Grocery Total':<20}: ₹{self.grocery_price.get():>10}")
        self.txtarea.insert(END, f"\n{'Cold Drinks Total':<20}: ₹{self.cold_drink_price.get():>10}")
        self.txtarea.insert(END, f"\n{'Total Tax':<20}: ₹{float(self.cosmetic_tax.get()) + float(self.grocery_tax.get()) + float(self.cold_drink_tax.get()):>10.2f}")
        self.txtarea.insert(END, f"\n{'='*40}")
        self.txtarea.insert(END, f"\n{'Total Amount':<20}: ₹{self.total_bill:>10.2f}")
        self.txtarea.insert(END, f"\n{'='*40}")

    def welcome_bill(self):
        self.txtarea.delete(1.0, END)
        self.txtarea.insert(END, "\t    WELCOME TO RETAIL SHOP\n")
        self.txtarea.insert(END, f"\nBill No. : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone No. : {self.c_phon.get()}")
        self.txtarea.insert(END, f"\n{'-'*40}")
        self.txtarea.insert(END, "\nProduct\t\tQTY\tPrice")
        self.txtarea.insert(END, f"\n{'-'*40}")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error", "Customer Details are Required")
        elif self.cosmetic_price.get() == "0.0" and self.grocery_price.get() == "0.0" and self.cold_drink_price.get() == "0.0":
            messagebox.showerror("Error", "No Products Selected")
        else:
            self.welcome_bill()
            
            # Add cosmetics to bill
            if self.soap.get() != 0:
                self.txtarea.insert(END, f"\nBath Soap\t\t{self.soap.get()}\t{self.soap.get() * 40}")
            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f"\nFace Cream\t\t{self.face_cream.get()}\t{self.face_cream.get() * 50}")
            if self.face_wash.get() != 0:
                self.txtarea.insert(END, f"\nFace Wash\t\t{self.face_wash.get()}\t{self.face_wash.get() * 60}")
            if self.spray.get() != 0:
                self.txtarea.insert(END, f"\nHair Spray\t\t{self.spray.get()}\t{self.spray.get() * 70}")
            if self.gell.get() != 0:
                self.txtarea.insert(END, f"\nHair Gel\t\t{self.gell.get()}\t{self.gell.get() * 45}")
            if self.loshan.get() != 0:
                self.txtarea.insert(END, f"\nBody Lotion\t\t{self.loshan.get()}\t{self.loshan.get() * 55}")
            
            # Add grocery to bill
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\nRice\t\t{self.rice.get()}\t{self.rice.get() * 60}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\nFood Oil\t\t{self.food_oil.get()}\t{self.food_oil.get() * 120}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\nDaal\t\t{self.daal.get()}\t{self.daal.get() * 80}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\nWheat\t\t{self.wheat.get()}\t{self.wheat.get() * 40}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\nSugar\t\t{self.sugar.get()}\t{self.sugar.get() * 45}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\nTea\t\t{self.tea.get()}\t{self.tea.get() * 50}")
            
            # Add cold drinks to bill
            if self.maaza.get() != 0:
                self.txtarea.insert(END, f"\nMaaza\t\t{self.maaza.get()}\t{self.maaza.get() * 35}")
            if self.cock.get() != 0:
                self.txtarea.insert(END, f"\nCoke\t\t{self.cock.get()}\t{self.cock.get() * 40}")
            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\nFrooti\t\t{self.frooti.get()}\t{self.frooti.get() * 30}")
            if self.thumbsup.get() != 0:
                self.txtarea.insert(END, f"\nThumbsUp\t\t{self.thumbsup.get()}\t{self.thumbsup.get() * 40}")
            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\nLimca\t\t{self.limca.get()}\t{self.limca.get() * 35}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\nSprite\t\t{self.sprite.get()}\t{self.sprite.get() * 40}")
            
            self.txtarea.insert(END, f"\n{'-'*40}")
            self.total()
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op:
            bill_data = self.txtarea.get(1.0, END)
            bill_no = self.bill_no.get()
            file_path = f"bills/{bill_no}.txt"
            
            with open(file_path, "w") as f:
                f.write(bill_data)
            
            messagebox.showinfo("Saved", f"Bill No: {bill_no} saved successfully")
            self.bill_no.set(str(random.randint(1000, 9999)))

    def find_bill(self):
        bill_no = self.search_bill.get()
        file_path = f"bills/{bill_no}.txt"
        
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                self.txtarea.delete(1.0, END)
                self.txtarea.insert(END, f.read())
        else:
            messagebox.showerror("Error", "Bill Not Found")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you want to clear all data?")
        if op:
            # Clear all input fields
            for var in [self.soap, self.face_cream, self.face_wash, self.spray, 
                       self.gell, self.loshan, self.rice, self.food_oil, 
                       self.wheat, self.daal, self.sugar, self.tea, self.maaza, 
                       self.cock, self.frooti, self.limca, self.thumbsup, self.sprite]:
                var.set(0)
            
            # Reset prices and taxes
            for var in [self.cosmetic_price, self.grocery_price, self.cold_drink_price,
                       self.cosmetic_tax, self.grocery_tax, self.cold_drink_tax]:
                var.set("0.0")
            
            # Clear customer details
            self.c_name.set("")
            self.c_phon.set("")
            self.search_bill.set("")
            
            # Generate new bill number
            self.bill_no.set(str(random.randint(1000, 9999)))
            
            # Reset bill area
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you want to exit?")
        if op:
            self.root.destroy()

root = Tk()
app = Bill_App(root)
root.mainloop()