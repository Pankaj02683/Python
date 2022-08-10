from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random


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
        self.combo_product.bind("<<Comboboxselected>>",self.price)


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

        self.Btnsearch=Button(search_frame,text="Search",font=('arial',10,"bold"),bg="orangered",fg="white",width=18,cursor="hand2")
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

        self.subtotal=ttk.Entry(Bill_counter,font=("times new roman",10,"bold"),width=24)
        self.subtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_tax=Label(Bill_counter,text="Govt Tax",font=("arial",12,"bold"),bg="white",bd=4)
        self.lbl_tax.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bill_counter,font=("times new roman",10,"bold"),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblamountTotal=Label(Bill_counter,text="Total",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblamountTotal.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.txtamountTotal=ttk.Entry(Bill_counter,font=("times new roman",10,"bold"),width=24)
        self.txtamountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #button frame
        Btn_frame=Frame(Bill_counter,bd=2,bg="white")
        Btn_frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_frame,height=2,text="Add To Cart",font=('arial',10,"bold"),bg="orangered",fg="white",width=18,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate=Button(Btn_frame,height=2,text="Generate Bill",font=('arial',10,"bold"),bg="orangered",fg="white",width=18,cursor="hand2")
        self.Btngenerate.grid(row=0,column=1)

        self.Btnsave=Button(Btn_frame,height=2,text="Save Bill",font=('arial',10,"bold"),bg="orangered",fg="white",width=18,cursor="hand2")
        self.Btnsave.grid(row=0,column=2)

        self.Btnprint=Button(Btn_frame,height=2,text="Print",font=('arial',10,"bold"),bg="orangered",fg="white",width=18,cursor="hand2")
        self.Btnprint.grid(row=0,column=3)

        self.Btnclear=Button(Btn_frame,height=2,text="Clear",font=('arial',10,"bold"),bg="orangered",fg="white",width=18,cursor="hand2")
        self.Btnclear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_frame,height=2,text="Exit",font=('arial',10,"bold"),bg="orangered",fg="white",width=18,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)


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
            self.combo_product.config(Value=self.pant) 
            self.combo_product.current(0) 


    def price(self,event="") :
        if self.combo_product.get()=="levis":
            self.combo_price.config(value=self.price_levis) 
            self.combo_price.current(0)         
            self.qty.set(1)




if __name__== '__main__':
    root=Tk()
    obj=bill_app(root)
    root.mainloop()