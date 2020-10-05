INSERT INTO COMMERCIAL(Floors,Type,ParkingSpace,YearBuilt,PropertyID) VALUES('1','shop','40','2000','3');
INSERT INTO COMMERCIAL(Floors,Type,ParkingSpace,YearBuilt,PropertyID) VALUES('4','Office','3000','2010','7');
INSERT INTO COMMERCIAL(Floors,Type,ParkingSpace,YearBuilt,PropertyID) VALUES('2','Godown','0','2011','2');
INSERT INTO RESIDENTIAL(ElectricityTime,WaterTime,CarpetAreaInSqFt,LiftAvailibility,Type,BedRooms,ReservedParking,PropertyID) VALUES('18','24','250','No','villa','3','2','6');
INSERT INTO RESIDENTIAL(ElectricityTime,WaterTime,CarpetAreaInSqFt,LiftAvailibility,Type,BedRooms,ReservedParking,PropertyID) VALUES('19','24','200','No','villa','3','2','8');
INSERT INTO RESIDENTIAL(ElectricityTime,WaterTime,CarpetAreaInSqFt,LiftAvailibility,Type,BedRooms,ReservedParking,PropertyID) VALUES('24','22','150','Yes','flat','1','1','9');
INSERT INTO SERVICES(PropertyID,ServiceDesc) VALUES('3','Atm, supermarket and railway station available nearby');
INSERT INTO SERVICES(PropertyID,ServiceDesc) VALUES('7','Near by airport');
INSERT INTO SERVICES(PropertyID,ServiceDesc) VALUES('10','Park and stadium near by');
INSERT INTO SERVICES(PropertyID,ServiceDesc) VALUES('2','Youthful community, constant water and electricity supplies');
INSERT INTO PERSON(Name,Gender,Occupation,Remarks,PropertyID) VALUES('Arun','Male','Doctor','happy to live there, Great view, ','6');
INSERT INTO PERSON(Name,Gender,Occupation,Remarks,PropertyID) VALUES('Yash','Male','Transponster','happy to live there','8');
INSERT INTO PERSON(Name,Gender,Occupation,Remarks,PropertyID) VALUES('Modi','Male','Software Engineer','Well built','1');
INSERT INTO PERSON(Name,Gender,Occupation,Remarks,PropertyID) VALUES('Amit','Male','Housewife','happy to live there','9');
INSERT INTO PERSON(Name,Gender,Occupation,Remarks,PropertyID) VALUES('Shradha','Female','Doctor','The place was a mess','3');
INSERT INTO PERSON(Name,Gender,Occupation,Remarks,PropertyID) VALUES('Tanvi','Female','Businessman','Looked fondly to my time there','2');
INSERT INTO DEPENDENT(Age,Name,Gender,Relationship,AgentID) VALUES('20','Aman Goyal','Male','Family Friend','3');
INSERT INTO DEPENDENT(Age,Name,Gender,Relationship,AgentID) VALUES('65','Keshav Bajaj','Male','Uncle','5');
INSERT INTO DEPENDENT(Age,Name,Gender,Relationship,AgentID) VALUES('45','Mayank Goel','Male','Uncle','1');
INSERT INTO DEPENDENT(Age,Name,Gender,Relationship,AgentID) VALUES('35','Eshan Gupta','Male','Friend','9');
INSERT INTO BANKINTEREST(Name,InterestRate) VALUES('Metro Bank','10');
INSERT INTO BANKINTEREST(Name,InterestRate) VALUES('Union Bank of India (UK) Ltd','12.5');
INSERT INTO BANKINTEREST(Name,InterestRate) VALUES('TurkishBank UK','9.9');
INSERT INTO BANKINTEREST(Name,InterestRate) VALUES('Bank Sepah International PLC','13.5');
INSERT INTO BANKINTEREST(Name,InterestRate) VALUES('Handelsbanken London','11.3');
INSERT INTO BANKINTEREST(Name,InterestRate) VALUES('Barclays Bank','5.6');
INSERT INTO BANKINTEREST(Name,InterestRate) VALUES('Deutsche Bank','4.7');
INSERT INTO BANKINTEREST(Name,InterestRate) VALUES('Bank of China','6.7')
INSERT INTO CITYTOSTATE(State,City) VALUES('Maharashtra','Mumbai');
INSERT INTO CITYTOSTATE(State,City) VALUES('Bihar','Patna');
INSERT INTO CITYTOSTATE(State,City) VALUES('Telangana','Hyderbad');
INSERT INTO CITYTOSTATE(State,City) VALUES('Maharashtra','Pune');
INSERT INTO CITYTOSTATE(State,City) VALUES('Rajasthan','Jaipur');
INSERT INTO CITYTOSTATE(State,City) VALUES('Punjab','Barnala');
INSERT INTO CITYTOSTATE(State,City) VALUES('Punjab','Amritsar');
INSERT INTO CITYTOSTATE(State,City) VALUES('Kerala','Thiruvanthpuram');
INSERT INTO STREETTOPINCODE(Pincode,StreetAddress) VALUES('800001','Real Dad Road');
INSERT INTO STREETTOPINCODE(Pincode,StreetAddress) VALUES('324005','Amar Corner, Hadapsar');
INSERT INTO STREETTOPINCODE(Pincode,StreetAddress) VALUES('968004','Govind Puri, Kalkaji');
INSERT INTO STREETTOPINCODE(Pincode,StreetAddress) VALUES('148101','Bombay Talkies Compound, Malad');
INSERT INTO STREETTOPINCODE(Pincode,StreetAddress) VALUES('654879','Kattedan');
INSERT INTO STREETTOPINCODE(Pincode,StreetAddress) VALUES('328895','Canal Street');
INSERT INTO STREETTOPINCODE(Pincode,StreetAddress) VALUES('300598','Maiden Lane');
INSERT INTO STREETTOPINCODE(Pincode,StreetAddress) VALUES('920045','Houston Street');
INSERT INTO STREETTOPINCODE(Pincode,StreetAddress) VALUES('920008','Conventry Street');
INSERT INTO STREETTOPINCODE(Pincode,StreetAddress) VALUES('800015','Dalal Street');
INSERT INTO PINCODETOCITY(Pincode,City) VALUES('800001','Patna');
INSERT INTO PINCODETOCITY(Pincode,City) VALUES('324005','Hyderabad');
INSERT INTO PINCODETOCITY(Pincode,City) VALUES('968004','Mumbai');
INSERT INTO PINCODETOCITY(Pincode,City) VALUES('148101','Barnala');
INSERT INTO PINCODETOCITY(Pincode,City) VALUES('654879','Amritsar');
INSERT INTO PINCODETOCITY(Pincode,City) VALUES('328895','Thiruvanthpuram');
INSERT INTO PINCODETOCITY(Pincode,City) VALUES('300598','Jaipur');
INSERT INTO PINCODETOCITY(Pincode,City) VALUES('920045','Pune');
INSERT INTO PINCODETOCITY(Pincode,City) VALUES('920008','Pune');
INSERT INTO PINCODETOCITY(Pincode,City) VALUES('800015','Patna');