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




#---------------------------------------------------------Propety Deal------------------------------------------------------------------------------

def property_deal():
	main_output()
	print("Enter the requried information")
	buyerid =    input("Enter ID of Buyer:       ")
	sellerid =   input("Enter ID of Seller:      ")
	propertyid = input("Enter ID of Property:    ")
	agentid =    input("Enter ID of Agent:       ")

#-----------------------------------------------------ADMINISTRATOR------------------------------------------------------------------------------


def insert_bank():
	main_output()
	bank = {}
	print("Enter the following Bank details")
	bank["name"] = input("Enter Name: ")
	bank["address"] = input("Enter Branch address: ")
	bank["interest"] = input("Enter interest rate offered by Bank: ")

def delete_bank():
	main_output()
	bankid = input("Enter the BankID u want to delete: ")

def update_bank():
	main_output()
	bankid = input("Enter the Bank name to update the interest rate: ")
	interest = input("Enter new interest rate: ")

def bankc_choice(choice):
	if(choice == 1):
		insert_bank()
		return 1
	elif(choice == 2):
		delete_bank()
		return 1
	elif(choice == 3):
		update_bank()
		return 1
	elif choice == 4:
		return 2
	else:
		print("Choice out of range")
		time.sleep(2)
		return 0

def insert_agent():
	main_output()
	agent = {}
	print("Enter details of the Agent")
	agent["name"] = input("Ente name: ")
	agent["mno"] = input("Enter Mobile Number: ")
	agent["salary"] = input("Enter salary: ")
	agent["bonus"] = 0;
	agent["supid"] = input("Enter id of Supervisor (0 for no supervisor)")


def delete_agent():
	main_output()
	agentid = input("Enter the AgentID u want to delete: ")

def update_agent():
	main_output()
	agentid = input("Enter the AgentID u want to update the salary to: ")
	salary = input("Enter the new salary of the salary: ")

def agentc_choice(choice):
	if(choice == 1):
		insert_agent()
		return 1
	elif(choice == 2):
		delete_agent()
		return 1
	elif(choice == 3):
		update_agent()
		return 1
	elif choice == 4:
		return 2
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
	print("4. Previous Menu")
	print();
	try:
		choice = int(input("Enter choice: "))
		if(bankc_choice(choice) == 2):
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
	print("4. Previous Menu")
	print();
	try:
		choice = int(input("Enter choice: "))
		if(agentc_choice(choice) == 2):
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
		property_deal()
		return 1
	elif(choice == 4):
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
	print("3. Register a property deal")
	print("4. Logout");
	print();
	try:
		choice = int(input("Enter choice: "))
		if(admin_choice(choice) == 2):
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
def query_choice(choice):
	if(choice == 1):
		return 1
	if(choice == 2):
		return 1
	if(choice == 3):
		return 1
	if(choice == 4):
		return 1
	if(choice == 5):
		return 1
	if(choice == 6):
		return 1
	if(choice == 7):
		return 1
	if(choice == 8):
		return 1
	if(choice == 9):
		return 1
	if(choice == 10):
		return 1
	elif(choice == 11):
		return 2
	else:
		print("Choice out of range")
		time.sleep(2)
		return 0

def queries():
	main_output()
	print("MENTION THE NUMBER CORRESPONDING TO YOUR CHOICE")
	print()
	print("1.  List properties according to Property Subclass");
	print("2.  Retrieve properties using Pincode,City or State");
	print("3.  Retrieve properties greater or less than some cost");
	print("4.  Retrieve properties using Pincode,City or State");
	print("5.  Get minimum cost per sq feet in a given city for a plot");
	print("6.  Get Interest rate for the bank");
	print("7.  Average Credit Score of the buyers the bank gives Loan too");
	print("8.  Type of Properties an Agent has dealt the most");
	print("9.  Subclass of Properties an Agent has dealt with the most");
	print("10. Get the minimum credit score needed to avail loan at the bank")
	print("11. Previous Menu");
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

def list_property():
	main_output()
	pid = input("Enter Property ID of the property u want to list: ")

def delete_property():
	main_output()
	pid = input("Enter Property ID of the property u want to delete: ")	

def seller_choice(choice):
	if choice == 1:
		list_property()
		return 1
	elif choice == 2:
		delete_property()
		return 1
	elif choice == 3:
		return 2
	else:
		print("Choice out of range")
		time.sleep(2)
		return 0

def seller():
	main_output()
	print("MENTION THE NUMBER CORRESPONDING TO YOUR CHOICE");	
	print();
	print("1. Get details about the propety u own");
	print("2. Remove a property from the database");
	print("3. Previous Menu")
	print();
	try:
		choice = int(input("Enter choice: "))
		if(seller_choice(choice) == 2):
			return
		else:
			seller()
	except:
		print("\nINVALID CHOICE!!\nTRY AGAIN")
		time.sleep(2)
		seller()


#---------------------------------------------------------REGISTER------------------------------------------------------------------------------

def register_residential():
	print()
	res = {}
	res["electime"] = input("Enter Electricity Time: ")
	res["watertime"] = input("Enter Water Time: ")
	res["type"] = input("Enter Type (Villa, Flat, Penthouse): ")
	res["life"] = input("Enter Lift Availability (Yes, No): ")
	res["area"] = input("Enter Carpet Area(In SqFeet): ")
	res["rooms"] = input("Entter number of bedrooms: ")
	res["parking"] = input("Enter number of reserved parking spots: ")

def services():
	print()
	cnt = int(input("Enter number of services offered: "))
	service = []
	for i in range(cnt):
		service.append(input("Enter service description: "))


def register_commercial():
	print()
	comm = {}
	comm["floors"] = input("Enter number of floors: ")
	comm["type"] = input("Enter Type (Office, Godown, Shop): ")
	comm["parking"] = input("Enter number of reserved parking spots: ")
	comm["year"] = input("Enter Year in which the proeperty was built: ")
	services()

def register_plot():
	print()
	plot = {}
	plot["area"] = input("Enter area in Acres: ")
	plot["bwall"] = input("Presence of Boundary Wall (Yes,No): ")
	plot["floors"] = input("Enter maximum number of floors that can be built: ")
	# plot["areainsqfeet"] = some formula

def register_person():
	person = {}
	print()
	print("Enter details of someone who has used this property before")
	person["name"] = input("Enter name: ")
	person["gender"] = input("Enter gender: ")
	person["occupation"] = input("Enter occupation: ")
	person["remarks"] = input("Enter remarks about the property: ")


def register_property():
	print()
	print("Enter the Details for the Property")
	prop = {}
	prop["pno"] = input("Enter Propety number: ")
	prop["sadd"] = input("Enter Street Address: ")
	prop["pincode"] = input("Enter PINCODE: ")
	prop["city"] = input("Enter City: ")
	prop["state"] = input("Enter State: ")
	prop["availdate"] = input("Enter the DATE from which the Propety will be available: ")
	prop["facedir"] = input("Enter the direction the main gate of the propety is facing: ")
	prop["cost"] = int(input("Enter the expected cost for the propety: "))
	subclass = input("Enter Type of Propety (Residential, Commercial, Plot): ")
	if subclass == "Residential":
		register_residential()
	elif subclass == "Commercial":
		register_commercial()
	elif subclass == "Plot":
		register_plot()
	else:
		print("Invalid entry")
	register_person()


def register_seller():
	main_output()
	sell = {}
	print("Enter the following details")
	sell["name"]  = input("Enter name: ")
	sell["email"] = input("Enter email: ")
	sell["mno"]   = input("Enter MobileNo:  ")
	sell["address"] = input("Enter Address: ")
	register_property()

def register_buyer():
	main_output()
	buy = {}
	print("Enter the following details")
	buy["name"]  = input("Enter name: ")
	buy["email"] = input("Enter email: ")
	buy["mno"]   = input("Enter MobileNo:  ")
	buy["address"] = input("Enter Address: ")	
	buy["creditscore"] = input("Enter Credit Score: ")

def register_choice(choice):
	if(choice == 1):
		register_seller()
		return 1
	elif(choice == 2):
		register_buyer()
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
	except Exception as e:
		print("\nINVALID ICE!!\nTRY AGAIN")
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
	elif (choice == 4):
		register()
	elif(choice == 5):
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
	print("2. Funtionalities of the database");
	print("3. Login as Seller");
	print("4. New User Signup for Seller/Buyer");
	print("5. Quit");
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
