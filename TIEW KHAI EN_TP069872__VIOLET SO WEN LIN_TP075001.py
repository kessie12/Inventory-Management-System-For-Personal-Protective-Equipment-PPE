# TIEW KHAI EN, VIOLET SO WEN LIN
# TP069872, TP075001

#Title Page
print("\n")
print("-"*198)
tfile = open ("/Users/khaientiew/APU/Sem 1 - PYP/Assignment/PPE System/title.txt","r")
content = tfile.read()
print (content)
tfile.close()
print("-"*198,"\n")
print("Welcome to Personal Protective Equipment (PPE) Inventory Managemnet System")

#----Login---- 
def login():
    while True:
        print("\nWelcome to Login Page")
        usertype = input("\nPlease enter your usertype(admin/staff):")
        userpassword = input("\nPlease enter the password:")
        if usertype.upper() == ("ADMIN"):
            if userpassword == ("admin123"):
                print("You are login to admin page")
                
                admin_Menu()

            else:
                print("\nWrong password, please try again later...")
                

        elif usertype.upper() == ("STAFF"):
            if userpassword == ("staff789"):
                print("You are login to staff page")
                staff_menu()
            else:
                print("\nWrong password, please try again later...")
                login()
                
        else:
            print("\nInvalid input, please try again...")
            login() 


#----admin_menu---- 
def admin_Menu():
    print("\nYou are in the Menu Page")
    print("\nPress 1 - Add new user")
    print("Press 2 - Delete user") 
    print("Press 3 - Modify user") 
    print("Press 4 - Search user")
    print("Press 5 - Update Hospital Details")
    print("Press 6 - Update Supplier Details")
    print("Press 7 - Search Hospital")
    print("Press 8 - Search Supplier")
    print("Press 9 - Update PPE")
    print("Press 10 - Item inventory tracking")
    print("Press 11 - Search PPE transaction")
    print("Press 12 - Logout")
    option = input("\nPlease enter your option here:")
    if option == "1":
        add_user()
    elif option == "2":
        delete_user()
    elif option == "3":
        modify_user()    
    elif option == "4":
        search_user()
    elif option == "5":
        modify_hospital()
    elif option == "6":
        modify_supplier()
    elif option == "7":
        search_hospital()
    elif option == "8":            
        search_supplier()
    elif option == "9": 
        update_ppe()
    elif option == "10": 
        item_tracking()
    elif option == "11":
        search_ppe()           
    elif option == "12":
        login()            
    else:
        print("\nInvalid Option")
        print("Please enter a valid option")
        admin_Menu()

#----staff_menu---- 
def staff_menu():
    print("\nYou are now in the Menu page")
    print("Press 1 - Update Hospital Details")
    print("Press 2 - Update Supplier Details")
    print("Press 3 - Search Hospital")
    print("Press 4 - Search Supplier")
    print("Press 5 - Update PPE")
    print("Press 6 - Item inventory tracking")
    print("Press 7 - Search PPE transaction")
    print("Press 8 - Logout")    
    option = input("\nPlease enter your option here:")
    if option == "1":
        modify_hospital()
    elif option == "2":
        modify_supplier()
    elif option == "3":
        search_hospital()
    elif option == "4":            
        search_supplier()
    elif option == "5":
        update_ppe()            
    elif option == "6":
        item_tracking()
    elif option == "7":
        search_ppe()           
    elif option == "8":
        login()            

    else:
        print("\nInvalid Option")
        print("Please enter a valid option")
        staff_menu()
    
#----admin_add user---- 
def add_user():
    print("\nDo you want to add new user?")
    print("Press Y - add new user")
    print("Press N - return back to Menu")
    adduser = input("\nPlease enter your option here:")
    if adduser.upper() == ("Y"):
        ufile = open("users.txt","r")
        userlist=[]
        
        while True:
            userid=input("\nPlease enter the staff (IC/Passport):")
            if(userid not in userlist):
                    break
            else:
                print("\nInvalid Input")
                print("\nID already exists")

        while True:
            name=input("\nPlease enter the staff name:")
            break

        while True:
            pw=input("\nPlease enter your password(at least 8 characters):")
            if (len(pw)<8):
                print("Invalid password, password at least 8 characters")
                input("Please enter to continue")
                continue
            else:
                break

        while True:
            type=input("\nPlease enter the usertype(admin or staff):")
            if type not in  ("admin","staff"):
                print("\n Invalid input, please enter admin or staff")
                input("Please enter to re-enter")
            else:
                break

    elif adduser.upper() == ("N"):
        admin_Menu()

    else:
        print("\nInvalid input")
        add_user()

    with open ("users.txt","a") as userfile:
        userfile.write("\n{0} : {1} : {2} : {3}".format(userid, name, pw, type))
        userfile.close()
        print("\nThe new user -- "+name+", "+userid+", "+type+" added successfully.")
        admin_Menu()


#----admin_delete user---- 
def delete_user():
    print("\nDo you want to REMOVE USER?")
    print("Press Y - delete user")
    print("Press N - return back to Menu")
    option = input("\nPlease enter your option here:")

    if option.upper() == ("Y"):
        user_id = input("\nPlease enter the User ID you would like to remove:")
        userlist = []
        
        with open("users.txt", "r") as userfile:
            userlist = [line.strip().split() for line in userfile]

        flag = -1
        print(len(userlist))
        
        for cnt in range(len(userlist)):
            if user_id == userlist[cnt][0]:
                flag = cnt
                break

        if flag != -1:
            userlist.pop(flag)
            with open("users.txt", "w") as user_file:
                for user_info in userlist:
                    rec = " ".join(user_info)+"\n"
                    user_file.write(rec)
                print("\nUser: ",user_id," removed successfully.")
        else:
            print("\nUser not found.")
        delete_user()
            
        
    elif option.upper() == ("N"):
        admin_Menu()
        
    else:
        print("Invalid input")
        print("Please enter Y/N ONLY")
        delete_user()


#----admin_search_user---- 
def search_user():
    print("\nDo you want to search user?")
    print("Press Y - search user")
    print("Press N - return back to Menu")
    searchuser = input("\nPlease enter your option here:")
    if searchuser.upper() == ("Y"):

        chooseuser = input("\nPlease enter the User ID you would like to search:")
        userlist=[]
        userfile = open("users.txt","r")
        flag = False
        
        for line in userfile:
            line = line.rstrip() 
            if chooseuser in line.split(" "):
                flag = True
                print("-" * 100)
                print("User ID"+" : " +"Username"+" : " +"Password"+" : "+"User Type")
                print("-" * 100) 
                print(line)
                print("-" * 100)           
                print('\n')
                search_user()
                
            if flag == False: 
                print ("No Staff record under this ID.")
                search_user()

    elif searchuser.upper() == ("N"):
        admin_Menu()
    else:
        print("Invalid input")
        print("Please enter Y/N ONLY")
        search_user()


#----admin_modify user---- 
def modify_user():
    print("\nDo you want to MODIFY USER?")
    print("Press Y - modify user")
    print("Press N - return back to Menu")
    option = input("\nPlease enter your option here:")

    if option.upper() == ("Y"):
        user_id = input("\nPlease enter the User ID you would like to modify:")
        userlist = []
        
        with open("users.txt", "r") as userfile:
            userlist = [line.strip().split() for line in userfile]

        flag = -1
        
        for cnt in range(len(userlist)):
            if user_id == userlist[cnt][0]:
                flag = cnt
                break

        if flag != -1:
            userlist.pop(flag)
            with open("users.txt", "w") as user_file:
                for user_info in userlist:
                    rec = " ".join(user_info)+"\n"
                    user_file.write(rec)
        else:
            print("\nUser not found.")
            modify_user()
        
        ufile = open("users.txt","r")
        userlist=[]
        
        while True:
            userid=input("\nPlease enter the user new (IC/Passport):")
            if(userid not in userlist):
                    break
            else:
                print("\nInvalid Input")
                print("\nID already exists")

        while True:
            name=input("\nPlease enter the user name:")
            break

        while True:
            pw=input("\nPlease enter new password(at least 8 characters):")
            if (len(pw)<8):
                print("Invalid password, password at least 8 characters")
                input("Please enter to continue")
                continue
            else:
                break

        while True:
            type=input("\nPlease enter the usertype(admin or staff):")
            if type not in  ("admin","staff"):
                print("\n Invalid input, please enter admin or staff")
                input("Please enter to re-enter")
            else:
                break
            
        with open ("users.txt","a") as userfile:
            userfile.write("\n{0} : {1} : {2} : {3}".format(userid, name, pw, type))
            userfile.close()
            print("The new user -- "+name+", "+userid+", "+type+" modify successfully.")
            admin_Menu()
        
    elif option.upper() == ("N"):
        admin_Menu()
        
    else:
        print("Invalid input")
        print("Please enter Y/N ONLY")
        modify_user()


#----add_hospital---- 
def add_hospital():
    print("\nDo you want to add hospital?")
    print("Press Y - Add hospital")
    print("Press N - return back to Menu")
    addhosp = input("\nPlease enter your option here:")
    if addhosp.upper() == ("Y"):
        ufile = open("hospital.txt","r")
        hosplist=[]
        
        while True:
            hospcode=input("\nPlease enter the hospital code(H1/H2/H3):")
            if(hospcode not in hosplist):
                    break
            else:
                print("\nInvalid Input")
                print("\nID already exists")

        while True:
            name=input("\nPlease enter the hospital name:")
            break

        while True:
            pn=input("\nPlease enter hospital contact number:")
            break

        while True:
            pic=input("\nPlease enter the name of person in charge:")
            break

    elif addhosp.upper() == ("N"):
        staff_menu()

    else:
        print("\nInvalid input")
        add_hospital()

    with open ("supliers.txt","a") as userfile:
        userfile.write("\n{0}\t:\t{1}\t:\t{2}\t:\t{3}\t".format(hospcode, name, pn, pic))
        userfile.close()
        print("The new user -- "+hospcode+", "+name+", "+pn+", "+pic+" added successfully.")
        staff_menu()    


#----add_supplier---- 
def add_supplier():
    print("\nDo you want to add supplier?")
    print("Press Y - add supplier")
    print("Press N - return back to Menu")
    addsupp = input("\nPlease enter your option here:")
    if addsupp.upper() == ("Y"):
        ufile = open("supliers.txt","r")
        supplist=[]
        
        while True:
            suppcode=input("\nPlease enter the supplier code(S1/S2/S3):")
            if(suppcode not in supplist):
                    break
            else:
                print("\nInvalid Input")
                print("\nCode already exists")

        while True:
            name=input("\nPlease enter the supplier name:")
            break

        while True:
            pn=input("\nPlease enter supplier contact number:")
            break

        while True:
            pic=input("\nPlease enter the name of person in charge:")
            break

    elif addsupp.upper() == ("N"):
        admin_Menu()

    else:
        print("\nInvalid input")
        add_supplier()

    with open ("supliers.txt","a") as userfile:
        userfile.write("\n{0}\t:\t{1}\t:\t{2}\t:\t{3}\t".format(suppcode, name, pn, pic))
        userfile.close()
        print("The new user -- "+suppcode+", "+name+", "+pn+", "+pic+" added successfully.")
        admin_Menu()


#----modify_hospital---- 
def modify_hospital():
    print("\nDo you want to Update Hospital Details?")
    print("Press Y - Update hospital details")
    print("Press N - return back to Menu")
    option = input("\nPlease enter your option here:")

    if option.upper() == ("Y"):
        hospcode = input("\nPlease enter the hospital code you like to update:").upper()
        hosplist = []
        
        with open("hospital.txt", "r") as hospfile:
            hosplist = [line.strip().split() for line in hospfile]

        flag = -1
        
        for cnt in range(len(hosplist)):
            if hospcode == hosplist[cnt][0]:
                flag = cnt
                break

        if flag != -1:
            hosplist.pop(flag)
            with open("hospital.txt", "w") as hosp_file:
                for hosp_info in hosplist:
                    rec = " ".join(hosp_info)+"\n"
                    hosp_file.write(rec)
        else:
            print("\nHospital not found.")
            modify_hospital()
        
        ufile = open("hospital.txt","r")
        hosplist=[]
        
        while True:
            hospcode=input("\nPlease enter the hospital code(H1/H2/H3):").upper()
            if(hospcode not in hosplist):
                    break
            else:
                print("\nInvalid Input")
                print("\nHospital already exists")

        while True:
            name=input("\nPlease enter the hospital name:")
            break

        while True:
            pn=input("\nPlease enter hospital contact number:")
            break

        while True:
            pic=input("\nPlease enter the name of person in charge:")
            break
            
        with open ("hospital.txt","a") as userfile:
            userfile.write("\n{0} : {1} : {2} : {3} ".format(hospcode, name, pn, pic))
            userfile.close()
            print("The new user -- "+hospcode+", "+name+", "+pn+", "+pic+" added successfully.")
            staff_menu()
        
    elif option.upper() == ("N"):
        staff_menu()
        
    else:
        print("Invalid input")
        print("Please enter Y/N ONLY")
        modify_hospital()


#----modify_supplier---- 
def modify_supplier():
    print("\nDo you want to Update Supplier Details?")
    print("Press Y - Update supplier details")
    print("Press N - return back to Menu")
    option = input("\nPlease enter your option here:")

    if option.upper() == ("Y"):
        suppcode = input("\nPlease enter the supplier code you like to update:").upper()
        supplist = []
        
        with open("supliers.txt", "r") as suppfile:
            supplist = [line.strip().split() for line in suppfile]

        flag = -1
        
        for cnt in range(len(supplist)):
            if suppcode == supplist[cnt][0]:
                flag = cnt
                break

        if flag != -1:
            supplist.pop(flag)
            with open("supliers.txt", "w") as supp_file:
                for supp_info in supplist:
                    rec = " ".join(supp_info)+"\n"
                    supp_file.write(rec)
        else:
            print("\nSupplier not found.")
            modify_supplier()
        
        ufile = open("supliers.txt","r")
        supplist=[]
        
        while True:
            suppcode=input("\nPlease enter the supplier code(S1/S2/S3):").upper()
            if(suppcode not in supplist):
                    break
            else:
                print("\nInvalid Input")
                print("\nCode already exists")

        while True:
            name=input("\nPlease enter the supplier name:")
            break

        while True:
            pn=input("\nPlease enter supplier contact number:")
            break

        while True:
            pic=input("\nPlease enter the name of person in charge:")
            break
            
        with open ("supliers.txt","a") as userfile:
            userfile.write("\n{0} : {1} : {2} : {3} ".format(suppcode, name, pn, pic))
            userfile.close()
            print("The new user -- "+suppcode+", "+name+", "+pn+", "+pic+" added successfully.")
            staff_menu()
        
    elif option.upper() == ("N"):
        staff_menu()
        
    else:
        print("Invalid input")
        print("Please enter Y/N ONLY")
        modify_supplier()


#-----search_supplier---- 
def search_supplier():
    print("\nDo you want to search supplier?")
    print("Press Y - search supplier")
    print("Press N - return back to Menu")
    searchsupp = input("\nPlease enter your option here:")
    if searchsupp.upper() == ("Y"):

        choosesupp = input("\nPlease enter the supplier code you would like to search:").upper()
        supplist=[]
        suppfile = open("supliers.txt","r")
        flag = False
        
        for line in suppfile:
            line = line.rstrip() 
            if choosesupp in line.split(" "):
                flag = True
                print("=" * 100)
                print("Suplier code"+" : " +"Name"+" : " +"Phone Number"+" : "+"Person In Charge")
                print("=" * 100)
                print(line)           
                print('\n')
                staff_menu()
                
            if flag == False: 
                print ("No Supplier record under this code.")
                search_supplier()

    elif searchsupp.upper() == ("N"):
        staff_menu()
    else:
        print("Invalid input")
        print("Please enter Y/N ONLY")
        search_supplier()


#----search_hospital---- 
def search_hospital():
    print("\nDo you want to search hospital?")
    print("Press Y - search hospital")
    print("Press N - return back to Menu")
    searchhosp = input("\nPlease enter your option here:")
    if searchhosp.upper() == ("Y"):

        choosehosp = input("\nPlease enter the hospital code you would like to search:").upper()
        hosplist=[]
        hospfile = open("hospital.txt","r")
        flag = False
        
        for line in hospfile:
            line = line.rstrip() 
            if choosehosp in line.split(" "):
                flag = True
                print("=" * 100)
                print("Hospital code"+" : " +"Name"+" : " +"Phone Number"+" : "+"Person In Charge")
                print("=" * 100)
                print(line)           
                print('\n')
                staff_menu()
                
            if flag == False: 
                print ("\nNo Hospital record under this code.")
                search_hospital()

    elif searchhosp.upper() == ("N"):
        staff_menu()
    else:
        print("Invalid input")
        print("Please enter Y/N ONLY")
        search_hospital()


#----add_ppe---- 
def add_ppe():
    print("\nDo you want to add PPE?")
    print("Press Y - add ppe")
    print("Press N - return back to Admin Menu")
    addppe = input("\nPlease enter your option here:")
    if addppe.upper() == ("Y"):
        file = open("ppe.txt","r")
        ppelist=[]
        
        while True:
            ppecode=input("\nPlease enter the PPE code:")
            if(ppecode not in ppelist):
                    break
            else:
                print("\nInvalid Input")
                print("\nID already exists")

        while True:
            suppcode=input("\nPlease enter the Supplier code:")
            break

        while True:
            ppestock=input("\nPlease enter PPE stock:")
            break

    elif addppe.upper() == ("N"):
        admin_Menu()

    else:
        print("\nInvalid input")
        add_hospital()

    with open ("ppe.txt","a") as ppefile:
        ppefile.write("\n{0}:{1}:{2}".format(ppecode, suppcode, ppestock))
        ppefile.close()
        print("PPE added successfully.")
        add_ppe() 


#-----update item quantities----- 
def update_ppe():
    print("\nDo you want to UPDATE PPE STOCK?")
    print("Press Y - Update PPE Stock")
    print("Press N - return back to Menu")
    option = input("\nPlease enter your option here:")
    if option.upper() == ("Y"):
        print("\nHC / FS / MS / GL / GW / SC\n")
        ppe_data = []

        with open ("ppe.txt","r") as ppefile:
            ppe_data = [line.strip().split(":") for line in ppefile]
            print(ppe_data)
            ppe_code = input("\nPlease enter the PPE code to update the stock quantity:").upper()
            ppe_supplier = input("\nPlease enter relevant Supplier CODE(S1/S2/S3):").upper()
            print("\nR-Received, D-Distributed")
            ppe_trans = input("\nPlease enter transaction type(R/D):").upper()
            
        flag = -1
                
        for cnt in range(0,len(ppe_data)):
            if ppe_code in ppe_data[cnt][0]:
                ppe_ori = input("\nPlease enter the original stock(in boxes):")
                flag = cnt
                break

        if flag != -1:
            ppe_data.pop(flag)
            ppe_enter = input("\nPlease enter quantity needed for transaction(in boxes):")
            ppe_enter = int(ppe_enter)
            if ppe_trans == ("R"):
                    print("\nSupplier code:"+ppe_supplier)
                    
            elif ppe_trans == ("D"):
                ppe_hosp = input("\nPlease enter relevant Hospital CODE(H1/H2/H3):").upper()
                if int(ppe_ori) < (ppe_enter):
                    print("\nQuantity in stock is insufficient")
                    update_ppe()
                        
            with open("ppe.txt", "w") as ppefile:
                for cnt in ppe_data:
                    ppefile.write(":".join(cnt)+"\n")

                if ppe_trans == ("R"):
                    ppe_rstock = (int(ppe_ori) + int(ppe_enter))
                    ppefile.write("{0}:{1}:{2}".format(ppe_code, ppe_supplier, ppe_rstock))

                elif ppe_trans == ("D"):
                    ppe_dstock = (int(ppe_ori) - int(ppe_enter))
                    ppefile.write("{0}:{1}:{2}".format(ppe_code, ppe_supplier, ppe_dstock))
                    
                print("\nUpdate Successful")

                
            with open ("transaction.txt","a") as ppefile:
                from datetime import date
                Date = date.today()

                from datetime import datetime
                current_datetime = datetime.now()
                Time = current_datetime.time()

                if ppe_trans == ("R"):
                    ppe_r = ("+",ppe_enter)
                    ppefile.write("\n{0}:{1}:{2}:{3}:{4}:{5}".format(ppe_code, Date, Time, ppe_trans, ppe_supplier, ppe_r))

                elif ppe_trans == ("D"):
                    ppe_d = ("-",ppe_enter)
                    ppefile.write("\n{0}:{1}:{2}:{3}:{4}:{5}".format(ppe_code, Date, Time, ppe_trans, ppe_hosp, ppe_d))
                    
                ppefile.close()
                print("\nPPE transaction added successfully.")
                staff_menu() 

        else:
            print("\nInvalid input, please try again later.")
            update_ppe()
            
    elif option.upper() == ("N"):
        staff_menu()

    else:
        print("\nInvalid input")
        update_ppe()   


#item tracking 
def item_tracking():
    print("\n------PPE TRACKING-----")
    print("Press 1 - Print ALL PPE stock")
    print("Press 2 - Print SHORTAGE PPE")
    print("Press 3 - Check PARTICULAR PPE stock")
    print("Press 4 - Check PPE Transaction")
    print("Press 5 - Return back to Menu")
    option = input("\nPlease enter your option here:")
    if option == ("1"):
        item_track_1()
    elif option == ("2"):
        item_track_2()
    elif option == ("3"):
        item_track_3()
    elif option == ("4"):
        item_track_4()
    elif option == ("5"):
        staff_menu()
    else:
        print("Invalid input")
        print("Please enter valid option ")
        item_tracking()

#item_track_1 
def item_track_1():
    print("\nPRINTING PPE STOCK AVAILABLE......\n")
    
    with open ("ppe.txt","r") as ppe_file:
        ppe_data = [line.strip().split(" ") for line in ppe_file]
        ppe_data.sort()

        print("-" * 91)
        print("PPE Code"+" : " +"Supplier Code"+" : "+"Stock Available")
        print("-" * 91)
        print(ppe_data)
        print("-" * 91)
        print('\n')
        item_tracking()

#item_track_2 
def item_track_2():
    print("\nPRINTING SHORTAGE PPE STOCK......\n")
    
    with open("ppe.txt", "r") as ppe_file:
        ppe_data = []
        
        for ppe_line in ppe_file:
            ppe_line = ppe_line.strip().split(":")
            ppe_data.append(ppe_line)
        
        for i in range(0, len(ppe_data)):
            if int(ppe_data[i][2]) < 25:
                print("The Stock of", str(ppe_data[i][0]), "is only left", str(ppe_data[i][2]), "boxes and it's less than 25 boxes.")
                print("Please increase the stock available.")
            else:
                print(str(ppe_data[i][0]), "are available.")

        item_tracking()


#item_track_3 
def item_track_3():
    print("\nChecking Particular PPE STOCK......\n")
    
    search = input("\nPlease enter the PPE code you would like to search:").upper()
    ppe_list =[]
    with open("ppe.txt","r") as file:
        flag = False
        
        for line in file:
            line = line.strip().split(":")
            if search in line:
                flag = True
                print("-" * 33)
                print("PPE code"+" : " +"Supplier Code"+" : " +"Stock")
                print("-" * 33) 
                print(line)
                print("-" * 33)
                print('\n')
                
                
            if flag == False: 
                print ("No PPE record under this code.")
                item_track_3()

    item_tracking()


#item_track_4 
def item_track_4():
    with open("transaction.txt", "r") as transfile:
        transaction_list = []
        for content in transfile:
            sublist = content.strip().split(" ")
            transaction_list.append(sublist)

    print("-" * 100)
    print("Transaction Record".center(100))
    print("-" * 100)

    for loops in range(0, len(transaction_list)):
        print(transaction_list[loops])

    print("-" * 100)
    item_tracking()
    
#search_functionality
def search_ppe():
    with open("transaction.txt", "r") as transfile:
        transaction_list = []
        for content in transfile:
            sublist = content.strip().split(" ")
            transaction_list.append(sublist)
            transaction_list.sort()

    print("-" * 100)
    print("Transaction Record".center(100))
    print("-" * 100)

    for loops in range(0, len(transaction_list)):
        print(transaction_list[loops])

    print("-" * 100)
    staff_menu()

#Main Logic
login()
