import sqlite3,sys,datetime

globals()['con'] = sqlite3.connect('Gst_Database.db')
globals()['cursorObj'] = con.cursor()


def register():
    
    New_Name = str(input("Enter Your Shop Name : "))
    New_id = str(input(" Your GST Id : "))
    New_pass = str(input("Set New Password : "))
    cursorObj.execute('INSERT INTO user_details(Gst_No,Name,User_password) VALUES(?,?,?)',(New_id,New_Name,New_pass,))    
    con.commit()
    print("Registration Success")

def forgot(id):
    npass = str(input("Set New Password"))
    cursorObj.execute('UPDATE user_details SET User_password = ? where Gst_No = ?',(npass,id,))
    con.commit()
    print("Updation Success")
    login(0)
    

def login(count):
    
    count = count+1
    globals()['user_id'] = str(input(" GST Id : "))
    if(count == 3):
        print("Forgotton password..?")
        opt = input("yes/no")
        if opt=="yes":
            forgot(user_id)
        else:
            login(count)
                  
    else:
        
        user_pass = str(input("Enter your Password : "))
        cursorObj.execute("SELECT * FROM user_details WHERE Gst_No = ? and User_password = ?",[(user_id),(user_pass)])
        results = cursorObj.fetchall()
        if results:
            for i in results:
               print('Welcome', i[1])
               count=0
               
        else:
            print("Error!!..Renter")
            login(count)
        
    
def del_acc():
    D_id = str(input(" Your GST Id : "))
    D_pass = str(input("Your Password : "))
    cursorObj.execute("DELETE FROM user_details WHERE Gst_No = ? and User_password = ?",[(D_id),(D_pass)])
    cursorObj.execute("DELETE FROM gst_details WHERE Gst_No = ? ",[(D_id)])
    con.commit()
    print("Account Deleted Successfully...")
    try:
        sys.exit()
    finally:
        print("Thank you for using our service")
    
print("----------Welcome to GST Dairy-------------")
print("================================================")
print("1. New User")
print("2. Existing User")
print("3. Delete your Account")
choice = int(input("Enter your Choice : "))
if(choice == 1):
    register()
elif choice == 2:
    count = 0
    login(count)
elif choice == 3:
    del_acc()
else:
    try:
        sys.exit()
    finally:
        print("Thanks for Using")
        
def sql_connection():
 
    try:
        con = sqlite3.connect('Gst_Database.db')
        print("----------Welcome to GST Calculator-------------")
        print("================================================")
        return con
    except:
        print("Error")      

con = sql_connection()

 
print("----------INPUT TAX CALCULATION-------------")
print("================================================")
con = sqlite3.connect('Gst_Database.db')
p = int(input("Enter the product ID: "))    
cursorObj.execute('SELECT Gst_Percentage FROM gst_values WHERE id ={}'.format(p))
for row in cursorObj.fetchall():
    globals()['x'] = row[0]*100
    print("GST Percentage : ",int(x),"%")     
RPrice = int(input("Enter the price of 1 Raw material Bought:"))
n = int(input("Enter the Quantity of raw material"))
RTax = RPrice * x
ITax =RTax * n
Q=RPrice*n
ITax =ITax+Q
print("Input tax :", ITax)





print("----------OUTPUT TAX CALCULATION-------------")
print("================================================")
print("Output tax Calculation")
cursorObj = con.cursor()
a =int(input("Enter the Product Id of Manufactured: "))
sql_cmd = 'SELECT Gst_Percentage FROM gst_values WHERE id ={}'.format(a)
cursorObj.execute(sql_cmd)
for row in cursorObj.fetchall():
    globals()['Tax'] = row[0]*100;
    print("GST Percentage : ",int(Tax),"%")
s = int(input("Enter the selling price of your Product:"))
t=int(input("Enter the Quantity of Items sold:"))
Mtax = s * Tax
GTax = Mtax * t
W=s*t
GTax=GTax+W
print("Output Tax is:", GTax)
    


def calc():
    if GTax > ITax:
        GST=GTax-ITax
        Credits=0
    elif GTax < ITax:
        Credits=ITax-GTax
        GST=0
    else:
        GST=0
        Credits=0

    now = datetime.datetime.now()


    print("GST TO BE PAID IS:", GST)
    print("YOUR CREDIT BALANCE:", Credits)
    cursorObj.execute('INSERT INTO gst_details(Gst_No,Input_Tax,Ouput_Tax,Gst_Tax,Credits,Update_date) VALUES(?,?,?,?,?,?)',(s_id,ITax,GTax,GST,Credits,now))
    con.commit()

calc()


