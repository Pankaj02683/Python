from distutils.log import ERROR
from fileinput import filename
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile


class bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Super Canteen Management")

        #======Variables========
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()


        #Product Categories
        self.Category=["Select Option","Clothing","Lifestyle","Food"]
        
        
        self.SubCatclothing=["Pant","T-Shirt","Shirt"]
        self.pant=["Levis","Monte Carlo","Pepe Jeans"]
        self.price_levis=3500
        self.price_monte=4500
        self.price_pepe=5500

        self.Tshirt=["Polo","Roadster","Fila"]
        self.price_polo=1500
        self.price_Roadster=1000
        self.price_Fila=1800

        self.shirt=["Peter England","Louis Phillipe","Addidas"]
        self.price_peter=1500
        self.price_louis=1200
        self.price_addidas=2000

        
        self.SubCatlifestyle=["Bath Soap","Face Wash","Hair Oil","Shampoo"]
        self.bathsoap=["Lux","Cinthol","Lifebouy"]
        self.price_lux=35
        self.price_cinthol=38
        self.price_Lifebouy=30

        self.facewash=["Himalya","St.Botanica"]
        self.price_himalya=100
        self.price_Botanica=200

        self.hairoil=["Dabour Almonds","Parachute"]
        self.price_dabour=70
        self.price_parachute=68

        self.shampoo=["Dove","Clinic Plus"]
        self.price_dove=2
        self.price_clinic=1
        

        self.SubcatFood=["Biscuits","Chips","Coca Cola"]

        self.biscuits=["Good Day","Coconut"]
        self.price_gooday=10
        self.price_coconut=5

        self.chips=["Lays","Uncle Chips"]
        self.price_lays=5
        self.price_unclechips=5

        self.cocacola=["Pepsi","Coke","Limca"]
        self.price_pepsi=20
        self.price_coke=20
        self.price_limca=30

        #image1
        img=Image.open("Store Management/image/blog.jpg")
        img=img.resize((510,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=510,height=200)

        #image2
        img_2=Image.open("Store Management/image/good.jpg")
        img_2=img_2.resize((500,200),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=510,y=0,width=500,height=200)

        #image3
        img_3=Image.open("Store Management/image/store.jpg")
        img_3=img_3.resize((520,200),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        lbl_img_3=Label(self.root,image=self.photoimg_3)
        lbl_img_3.place(x=1010,y=0,width=520,height=200)


        lbl_title=Label(self.root,text="SUPER CANTEEN MANAGEMENT",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=200,width=1530,height=50)


        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=250,width=1530,height=550)

        #Customer Labelframe
        cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(cust_Frame,text="Mobile No",font=("arial",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(cust_Frame,textvariable=self.c_phon,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)


        self.lbl_custname=Label(cust_Frame,text="Customer Name",font=("arial",12,"bold"),bg="white")
        self.lbl_custname.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txtcustname=ttk.Entry(cust_Frame,textvariable=self.c_name,font=("times new roman",12,"bold"),width=24)
        self.txtcustname.grid(row=1,column=1,sticky=W,padx=5,pady=2)


        self.lbl_Email=Label(cust_Frame,text="Email",font=("arial",12,"bold"),bg="white")
        self.lbl_Email.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(cust_Frame,textvariable=self.c_email,font=("times new roman",12,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)


        #Product Labelframe
        product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        product_Frame.place(x=370,y=5,width=600,height=140)

        #category
        self.lblcategory=Label(product_Frame,text="Select Categories",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblcategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.combo_category=ttk.Combobox(product_Frame,value=self.Category,font=("arial",8,"bold"),width=24,state="readonly")
        self.combo_category.current(0)
        self.combo_category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.combo_category.bind("<<ComboboxSelected>>",self.Categories)


        #subcategory
        self.lblsubcategory=Label(product_Frame,text="SubCategories",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblsubcategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.combo_subcategory=ttk.Combobox(product_Frame,value=[""],font=("arial",8,"bold"),width=24,state="readonly")
        self.combo_subcategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.combo_subcategory.bind("<<ComboboxSelected>>",self.Product_add)


        #product name
        self.lblproduct=Label(product_Frame,text="Product Name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.combo_product=ttk.Combobox(product_Frame,textvariable=self.product,font=("arial",8,"bold"),width=24,state="readonly")
        self.combo_product.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.combo_product.bind("<<ComboboxSelected>>",self.price)


        #Price
        self.lblprice=Label(product_Frame,text="Price",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblprice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.combo_price=ttk.Combobox(product_Frame,textvariable=self.prices,font=("arial",8,"bold"),width=24,state="readonly")
        self.combo_price.grid(row=0,column=3,sticky=W,padx=5,pady=2)


        #Qty
        self.lblqty=Label(product_Frame,text="Quantity",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblqty.grid(row=1,column=2,stick=W,padx=5,pady=2)

        self.comboqty=ttk.Entry(product_Frame,textvariable=self.qty,font=("times new roman",9,"bold"),width=24)
        self.comboqty.grid(row=1,column=3,sticky=W,padx=5,pady=2)


        #Middle frame
        Middleframe=Frame(Main_Frame,bd=10)
        Middleframe.place(x=10,y=150,width=960,height=340)

        #image4
        img_4=Image.open("Store Management/image/super.jpg")
        img_4=img_4.resize((480,340),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        lbl_img_4=Label(Middleframe,image=self.photoimg_4)
        lbl_img_4.place(x=0,y=0,width=480,height=340)

        #image5
        img_5=Image.open("Store Management/image/market.jpg")
        img_5=img_5.resize((480,340),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        lbl_img_5=Label(Middleframe,image=self.photoimg_5)
        lbl_img_5.place(x=480,y=0,width=480,height=340)


        #search
        search_frame=Frame(Main_Frame,bd=2,bg="white")
        search_frame.place(x=990,y=10,width=500,height=40)

        self.lblBill=Label(search_frame,text="Bill Number",font=("arial",12,"bold"),bg="red",fg="white")
        self.lblBill.grid(row=0,column=0,stick=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(search_frame,textvariable=self.search_bill,font=("times new roman",12,"bold"),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.Btnsearch=Button(search_frame,text="Search",command=self.find_bill,font=('arial',10,"bold"),bg="orangered",fg="white",width=18,cursor="hand2")
        self.Btnsearch.grid(row=0,column=2)


        #bill frame area
        RightLabelframe=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelframe.place(x=980,y=45,width=525,height=350)

        scroll_y=Scrollbar(RightLabelframe,orient=VERTICAL)
        self.textarea=Text(RightLabelframe,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill Counter Labelframe
        Bill_counter=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bill_counter.place(x=0,y=400,width=1520,height=125)

        self.lblsubtot=Label(Bill_counter,text="Sub Total",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblsubtot.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.subtotal=ttk.Entry(Bill_counter,textvariable=self.sub_total,font=("times new roman",10,"bold"),width=24)
        self.subtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_tax=Label(Bill_counter,text="Govt Tax",font=("arial",12,"bold"),bg="white",bd=4)
        self.lbl_tax.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bill_counter,textvariable=self.tax_input,font=("times new roman",10,"bold"),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblamountTotal=Label(Bill_counter,text="Total",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblamountTotal.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.txtamountTotal=ttk.Entry(Bill_counter,textvariable=self.total,font=("times new roman",10,"bold"),width=24)
        self.txtamountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #button frame
        Btn_frame=Frame(Bill_counter,bd=2,bg="white")
        Btn_frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_frame,height=2,text="Add To Cart",command=self.Additem,font=('arial',10,"bold"),bg="orangered",fg="white",width=18,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate=Button(Btn_frame,height=2,text="Generate Bill",command=self.gen_bill,font=('arial',10,"bold"),bg="orangered",fg="white",width=18,cursor="hand2")
        self.Btngenerate.grid(row=0,column=1)

        self.Btnsave=Button(Btn_frame,height=2,text="Save Bill",command=self.save_bill,font=('arial',10,"bold"),bg="orangered",fg="white",width=18,cursor="hand2")
        self.Btnsave.grid(row=0,column=2)

        self.Btnprint=Button(Btn_frame,height=2,text="Print",command=self.print,font=('arial',10,"bold"),bg="orangered",fg="white",width=18,cursor="hand2")
        self.Btnprint.grid(row=0,column=3)

        self.Btnclear=Button(Btn_frame,height=2,text="Clear",command=self.clear,font=('arial',10,"bold"),bg="orangered",fg="white",width=18,cursor="hand2")
        self.Btnclear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_frame,height=2,text="Exit",command=self.root.destroy,font=('arial',10,"bold"),bg="orangered",fg="white",width=18,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]


    #Functions

    def Additem(self):
        Tax=2
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("ERROR","Please Select The Product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()} \t\t{self.m} ")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))


    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("ERROR","Please Add Item To Cart")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n\n ======================================================")
            self.textarea.insert(END,f"\nSub Amount :\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\nTax Amount :\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\nTotal Amount :\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n ======================================================\n")

    def save_bill(self):
        op=messagebox.askyesno("Bill No","Do You Want to save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('Store Management/bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Bill Saved",f"Bill No :{self.bill_no.get()} Saved Successfully")
            f1.close

    def print(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("Store Management/bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"Store Management/bills/{i}",'r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=="no":
            messagebox.showerror("ERROR","Invalid Bill Number")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set("")
        self.qty.set("")
        self.l=[0]
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.welcome()

    
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\tWelcome to My Super Store")
        self.textarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number : {self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email : {self.c_email.get()}")

        self.textarea.insert(END,"\n=======================================================")
        self.textarea.insert(END,f"\nProducts\t\t\tQuantity\t\tPrice")
        self.textarea.insert(END,"\n=======================================================")


    def Categories(self,event=""):
        if self.combo_category.get()=="Clothing":
            self.combo_subcategory.config(value=self.SubCatclothing)
            self.combo_subcategory.current(0)

        if self.combo_category.get()=="Lifestyle":
            self.combo_subcategory.config(value=self.SubCatlifestyle)
            self.combo_subcategory.current(0)

        if self.combo_category.get()=="Food":
            self.combo_subcategory.config(value=self.SubcatFood)
            self.combo_subcategory.current(0)

    def Product_add(self,event=""):
        if self.combo_subcategory.get()=="Pant":
            self.combo_product.config(value=self.pant) 
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="T-Shirt":
            self.combo_product.config(value=self.Tshirt) 
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Shirt":
            self.combo_product.config(value=self.shirt) 
            self.combo_product.current(0)

        #Lifestyle
        if self.combo_subcategory.get()=="Bath Soap":
            self.combo_product.config(value=self.bathsoap)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Face Wash":
            self.combo_product.config(value=self.facewash)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Hair Oil":
            self.combo_product.config(value=self.hairoil)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Shampoo":
            self.combo_product.config(value=self.shampoo)
            self.combo_product.current(0)


        #Food
        if self.combo_subcategory.get()=="Biscuits":
            self.combo_product.config(value=self.biscuits)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Chips":
            self.combo_product.config(value=self.chips)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Coca Cola":
            self.combo_product.config(value=self.cocacola)
            self.combo_product.current(0)        
 


    def price(self,event=""):
        if self.combo_product.get()=="Levis":
            self.combo_price.config(value=self.price_levis) 
            self.combo_price.current(0)         
            self.qty.set(1)

        if self.combo_product.get()=="Monte Carlo":
            self.combo_price.config(value=self.price_monte) 
            self.combo_price.current(0)         
            self.qty.set(1)

        if self.combo_product.get()=="Pepe Jeans":
            self.combo_price.config(value=self.price_pepe) 
            self.combo_price.current(0)         
            self.qty.set(1)   

        #Shirt
        if self.combo_product.get()=="Peter England":
            self.combo_price.config(value=self.price_peter) 
            self.combo_price.current(0)         
            self.qty.set(1)

        if self.combo_product.get()=="Louis Phillipe":
            self.combo_price.config(value=self.price_louis) 
            self.combo_price.current(0)         
            self.qty.set(1)

        if self.combo_product.get()=="Addidas":
            self.combo_price.config(value=self.price_addidas) 
            self.combo_price.current(0)         
            self.qty.set(1)

        #T-Shirt
        if self.combo_product.get()=="Polo":
            self.combo_price.config(value=self.price_polo) 
            self.combo_price.current(0)         
            self.qty.set(1)

        if self.combo_product.get()=="Roadster":
            self.combo_price.config(value=self.price_Roadster) 
            self.combo_price.current(0)         
            self.qty.set(1)

        if self.combo_product.get()=="Fila":
            self.combo_price.config(value=self.price_Fila) 
            self.combo_price.current(0)         
            self.qty.set(1)


        #Bath Soap
        if self.combo_product.get()=="Lux":
            self.combo_price.config(value=self.price_lux) 
            self.combo_price.current(0)         
            self.qty.set(1)

        if self.combo_product.get()=="Lifebouy":
            self.combo_price.config(value=self.price_Lifebouy) 
            self.combo_price.current(0)         
            self.qty.set(1)

        if self.combo_product.get()=="Cinthol":
            self.combo_price.config(value=self.price_cinthol) 
            self.combo_price.current(0)         
            self.qty.set(1)

        #Face Wash
        if self.combo_product.get()=="Himalya":
            self.combo_price.config(value=self.price_himalya) 
            self.combo_price.current(0)         
            self.qty.set(1)

        if self.combo_product.get()=="St.Botanica":
            self.combo_price.config(value=self.price_Botanica) 
            self.combo_price.current(0)         
            self.qty.set(1)

        #Hair Oil
        if self.combo_product.get()=="Dabour Almonds":
            self.combo_price.config(value=self.price_dabour) 
            self.combo_price.current(0)         
            self.qty.set(1)

        if self.combo_product.get()=="Parachute":
            self.combo_price.config(value=self.price_parachute) 
            self.combo_price.current(0)         
            self.qty.set(1)

        #Shampoo
        if self.combo_product.get()=="Dove":
            self.combo_price.config(value=self.price_dove) 
            self.combo_price.current(0)         
            self.qty.set(1)

        if self.combo_product.get()=="Clinic Plus":
            self.combo_price.config(value=self.price_clinic) 
            self.combo_price.current(0)         
            self.qty.set(1)

        #Biscuits
        if self.combo_product.get()=="Good Day":
            self.combo_price.config(value=self.price_gooday) 
            self.combo_price.current(0)         
            self.qty.set(1)

        if self.combo_product.get()=="Coconut":
            self.combo_price.config(value=self.price_coconut) 
            self.combo_price.current(0)         
            self.qty.set(1)

        #Lays
        if self.combo_product.get()=="Lays":
            self.combo_price.config(value=self.price_lays) 
            self.combo_price.current(0)         
            self.qty.set(1)

        if self.combo_product.get()=="Uncle Chips":
            self.combo_price.config(value=self.price_unclechips) 
            self.combo_price.current(0)         
            self.qty.set(1)

        #Coca Cola
        if self.combo_product.get()=="Coke":
            self.combo_price.config(value=self.price_coke) 
            self.combo_price.current(0)         
            self.qty.set(1)

        if self.combo_product.get()=="Pepsi":
            self.combo_price.config(value=self.price_pepsi) 
            self.combo_price.current(0)         
            self.qty.set(1)

        if self.combo_product.get()=="Limca":
            self.combo_price.config(value=self.price_limca) 
            self.combo_price.current(0)         
            self.qty.set(1)




if __name__== '__main__':
    root=Tk()
    obj=bill_app(root)
    root.mainloop()