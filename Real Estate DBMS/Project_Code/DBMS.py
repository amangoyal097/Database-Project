import subprocess as sp
import pymysql
import pymysql.cursors
import time
#-----------------------------------------------------LOGIN-------------------------------------------------------------------------------
def login():
	tmp = sp.call('clear', shell=True)
	print("LOG IN TO THE SQL SERVER");
	global con
	username = input("Username: ")
	password = input("Password: ")
	try:
		con = pymysql.connect(host='localhost',
	                              user=username,
	                              password=password,
	                              db='ESTATE',
	                              cursorclass=pymysql.cursors.DictCursor)
	except:
		print()
		print("Failed,Please TRY AGAIN!")
		time.sleep(2)
		login()

#----------------------------------------------------ESTATE OUTPUT------------------------------------------------------------------------------

def main_output():
	tmp = sp.call('clear', shell=True);
	print("\t\t------------------------------------------------------------------------------------")
	print("\t\t                             WELCOME TO THE DATABASE OF                             ")
	print("\t\t                                  MAK REAL ESTATE                                     ")
	print("\t\t------------------------------------------------------------------------------------")
	print();print();

#-----------------------------------------------------ADMINISTRATOR------------------------------------------------------------------------------

def bankc_choice(choice):
	if(choice == 1):
		return 1
	elif(choice == 2):
		return 1
	elif(choice == 3):
		return 1
	else:
		print("Choice out of range")
		time.sleep(2)
		return 0

def agentc_choice(choice):
	if(choice == 1):
		return 1
	elif(choice == 2):
		return 1
	elif(choice == 3):
		return 1
	else:
		print("Choice out of range")
		time.sleep(2)
		return 0

def bank_change():
	main_output()
	print("MENTION THE NUMBER CORRESPONDING TO YOUR CHOICE");	
	print();
	print("1. Insert Bank Entries");
	print("2. Delete Bank Entries");
	print("3. Update Bank Entries");
	print();
	try:
		choice = int(input("Enter choice: "))
		if(bankc_choice(choice) == 1):
			return
		else:
			bank_change()
	except:
		print("\nINVALID CHOICE!!\nTRY AGAIN")
		time.sleep(2)
		choice_administrator()

def agent_change():
	main_output()
	print("MENTION THE NUMBER CORRESPONDING TO YOUR CHOICE");	
	print();
	print("1. Insert Agent Entries");
	print("2. Delete Agent Entries");
	print("3. Update Agent Entries");
	print();
	try:
		choice = int(input("Enter choice: "))
		if(agentc_choice(choice) == 1):
			return
		else:
			agent_change()
	except:
		print("\nINVALID CHOICE!!\nTRY AGAIN")
		time.sleep(2)
		choice_administrator()

def admin_choice(choice):
	if(choice == 1):
		bank_change()
		return 1
	elif(choice == 2):
		agent_change()
		return 1
	elif(choice == 3):
		return 2
	else:
		print("Choice out of range")
		time.sleep(2)
		return 0

def choice_administrator():
	main_output()
	print("MENTION THE NUMBER CORRESPONDING TO YOUR CHOICE");	
	print();
	print("1. Operations on Bank Entries");
	print("2. Operations on Agent Entries");
	print("3. Logout");
	print();
	try:
		choice = int(input("Enter choice: "))
		if(admin_choice(choice) != 1):
			return
		else:
			choice_administrator()
	except:
		print("\nINVALID CHOICE!!\nTRY AGAIN")
		time.sleep(2)
		choice_administrator()


def administrator():
	main_output()
	id = input("Enter the unique Administrator ID: ")
	if(id == "database are okish"):
		choice_administrator()
	else:
		print("Nope try again! Hint check README")
		time.sleep(2)
		administrator()
#---------------------------------------------------------Queries------------------------------------------------------------------------------

def queries():
	main_output()
	print("MENTION THE NUMBER CORRESPONDING TO YOUR CHOICE")
	print()
	print("1. List properties according to Property Subclass");
	print("2. Retrieve properties using Pincode,City or State");
	print("3. Retrieve properties greater or less than some cost");
	print("4. Retrieve properties using Pincode,City or State");
	print("3. Previous Menu");
	print();
	try:
		choice = int(input("Enter choice: "))
		if(query_choice(choice) == 2):
			return
		else:
			queries()
	except:
		print("\nINVALID CHOICE!!\nTRY AGAIN")
		time.sleep(2)
		queires()



#---------------------------------------------------------SELLER------------------------------------------------------------------------------

def seller():
	main_output()
	print("MENTION THE NUMBER CORRESPONDING TO YOUR CHOICE");	
	print();
	print("1. Signup as Seller");
	print("2. Signup as Buyer");
	print("3. Previous Menu");
	print();
	try:
		choice = int(input("Enter choice: "))
		if(register_choice(choice) == 2):
			return
		else:
			register()
	except:
		print("\nINVALID CHOICE!!\nTRY AGAIN")
		time.sleep(2)
		register()




#---------------------------------------------------------Propety Deal------------------------------------------------------------------------------

def property_deal():
	main_output()
	print("Enter the requried information")
	buyerid =    input("Enter ID of Buyer:       ")
	sellerid =   input("Enter ID of Seller:      ")
	propertyid = input("Enter ID of Property:    ")
	agentid =    input("Enter ID of Agent:       ")


#---------------------------------------------------------REGISTER------------------------------------------------------------------------------
def register_choice(choice):
	if(choice == 1):
		return 1
	elif(choice == 2):
		return 1
	elif(choice == 3):
		return 2
	else:
		print("Choice out of range")
		time.sleep(2)
		return 0

def register():
	main_output()
	print("MENTION THE NUMBER CORRESPONDING TO YOUR CHOICE");	
	print();
	print("1. Signup as Seller");
	print("2. Signup as Buyer");
	print("3. Previous Menu");
	print();
	try:
		choice = int(input("Enter choice: "))
		if(register_choice(choice) == 2):
			return
		else:
			register()
	except:
		print("\nINVALID CHOICE!!\nTRY AGAIN")
		time.sleep(2)
		register()





#-----------------------------------------------------MAIN CHOICE CHECK------------------------------------------------------------------------------

def main_choice(choice):
	if(choice == 1):
		administrator()
	elif (choice == 2):
		queries()
	elif(choice == 3):
		seller()
	elif(choice == 5):
		property_deal()
	elif (choice == 6):
		register()
	elif(choice == 7):
		print("BYE!!")
		global running
		running = False
	else:
		print("Please choose from the abobe mentioned choices")
		time.sleep(2)


#-----------------------------------------------------MAIN PROMPT-------------------------------------------------------------------------------

def main_prompt():
	print("MENTION THE NUMBER CORRESPONDING TO YOUR CHOICE");	
	print();
	print("1. Login as Administrator");
	print("2. Funtionalitie of the database");
	print("3. Login as Seller");
	print("4. Login as Buyer");
	print("5. Make a Property Deal");	
	print("6. New User Signup for Seller/Buyer");
	print("7. Quit");
	print();
	try:
		choice = int(input("Enter choice: "));
		main_choice(choice);
	except:
		print("\nINVALID CHOICE!!\nTRY AGAIN");
		time.sleep(2);


#-----------------------------------------------------MAIN-------------------------------------------------------------------------------

if __name__ == "__main__":
	login();
	global running
	running = True;
	while(running == True):
		main_output();
		main_prompt();
