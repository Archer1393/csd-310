# Matthew Archer, Brandon Burnett, Justin Howell, Emely Pajarito
# 3/1/2023
# Milestone #3

import mysql.connector

config = {
    "user": "root",
    "password": "password",
    "host": "localhost"
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

sql1 = "DROP USER IF EXISTS 'outlander'@'localhost'"
sql2 = "CREATE USER 'outlander'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'"
sql3 = "GRANT ALL PRIVILEGES ON Outland_Adventures.* TO 'outlander'@'localhost'"
sql4 = "DROP DATABASE IF EXISTS Outland_Adventures"
cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql4)

cursor.execute("CREATE DATABASE Outland_Adventures")
cursor.execute(sql3)
db.close()
cursor.close()

config = {
    "user": "outlander",
    "password": "password",
    "host": "localhost",
    "database": "Outland_Adventures"
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

customer = '''CREATE TABLE Customer(
            f_name              VARCHAR(75)     NOT NULL,
            l_name              VARCHAR(75)     NOT NULL,
            age                 INT             NOT NULL,
            customer_ID         INT             NOT NULL    AUTO_INCREMENT, #1
            phone_number        VARCHAR(75)     NOT NULL,
            address             VARCHAR(75)     NOT NULL,
            equipment_bought    INT             NOT NULL, # Changed to INT after module 10 submission
            equipment_rented    INT             NOT NULL, # Changed to INT after module 10 submission
            equipment_id        INT             NOT NULL,
            trip_id             INT             NOT NULL,
            guides_id           INT             NOT NULL,

            PRIMARY KEY(customer_ID),

            CONSTRAINT fk_equipment FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id),
            
            CONSTRAINT fk_trip FOREIGN KEY(trip_id) REFERENCES trip(trip_id),

            CONSTRAINT fk_guides FOREIGN KEY(guides_id) REFERENCES guides(guides_id)
            )'''

equipment = '''CREATE TABLE Equipment(
            equipment_id              INT             NOT NULL    AUTO_INCREMENT, #2
            equipment_name            VARCHAR(75)     NOT NULL,
            equipment_amountSold      VARCHAR(75)     NOT NULL,
            equipment_amountOnHand    VARCHAR(75)     NOT NULL,
            equipment_condition1      VARCHAR(75)     NOT NULL,
            equipment_condition2      VARCHAR(75)     NOT NULL,
            equipment_condition3      VARCHAR(75)     NOT NULL,
            equipment_lastMaintenance VARCHAR(75)     NOT NULL,
            equipment_nextMaintenance VARCHAR(75)     NOT NULL,
            equipment_maintenanceCost INT             NOT NULL,
            equipment_amountMade      INT             NOT NULL,

            PRIMARY KEY(equipment_id)
)'''

trip = '''CREATE TABLE Trip(
        trip_id             INT         NOT NULL    AUTO_INCREMENT, #3
        trip_name           VARCHAR(75) NOT NULL,
        trip_bookingPerYear INT         NOT NULL, # Changed to INT after module 10 submission
        trip_locations      INT         NOT NULL, # Changed to INT after module 10 submission
        trip_costPerPerson  INT         NOT NULL, # Changed to INT after module 10 submission
        trip_highestBooked  INT         NOT NULL, # Changed to INT after module 10 submission
        trip_lowestBooked   INT         NOT NULL, # Changed to INT after module 10 submission
        trip_middleBooked   INT         NOT NULL, # Changed to INT after module 10 submission

        PRIMARY KEY(trip_id)
)'''

guides = '''CREATE TABLE Guides(
        guides_id                   INT NOT NULL    AUTO_INCREMENT, #4
        guides_name         VARCHAR(75) NOT NULL,
        guides_airfareCost          INT NOT NULL,
        guides_inoculationsCount    INT NOT NULL,
        guides_inventoryCount       INT NOT NULL,
        guides_inventorySold        INT NOT NULL,
        guides_supplyCount          INT NOT NULL,

        PRIMARY KEY(guides_id)
)'''

cursor.execute(trip)
cursor.execute(guides)
cursor.execute(equipment)
cursor.execute(customer)
##############################################################################################################################################################
# ADD DATA TO THE TABLES

popEquipment = '''INSERT INTO Equipment (equipment_id, equipment_name, equipment_amountSold, equipment_amountOnHand, equipment_condition1, equipment_condition2,
                equipment_condition3, equipment_lastMaintenance, equipment_nextMaintenance, equipment_maintenanceCost, equipment_amountMade) 
               VALUES ('2', 'Milwaukee', '120', '70', '(35) Good', '(20) Okay', '(15) Needs Replaced', '04-23-2021', '04-23-2022', '250', '1280')'''

popTrip = '''INSERT INTO Trip (trip_id, trip_name, trip_bookingPerYear, trip_locations, trip_costPerPerson, trip_highestBooked, trip_lowestBooked, trip_middleBooked)
            VALUES ('3', 'Outland Adventures', '500', '3', '1100', '250', '50', '200')'''

popGuides = '''INSERT INTO Guides (guides_id, guides_name, guides_airfareCost, guides_inoculationsCount, guides_InventoryCount, guides_inventorySold, guides_supplyCount)
            VALUES ('4', 'Mac & Duke', '550', '500', '175','525', '150')'''
###############
# ADD CUSTOMERS

customer1 = '''INSERT INTO Customer (f_name, l_name, age, customer_ID, phone_number, address, equipment_bought, equipment_rented, equipment_id, trip_id, guides_id) 
                VALUES ('Jack', 'Valentine', '28', '1', '712-370-7732', '123 Compton St', '1', '3', 
                (SELECT equipment_id FROM Equipment WHERE equipment_id = '2'),
                (SELECT trip_id FROM Trip WHERE trip_id = '3'),
                (SELECT guides_id FROM Guides WHERE guides_id = '4'))'''

customer2 = '''INSERT INTO Customer (f_name, l_name, age, customer_ID, phone_number, address, equipment_bought, equipment_rented, equipment_id, trip_id, guides_id) 
                VALUES ('Joesph', 'Jackson', '32', '2', '712-370-2189', '5564 Maple Ave', '3', '2', 
                (SELECT equipment_id FROM Equipment WHERE equipment_id = '2'),
                (SELECT trip_id FROM Trip WHERE trip_id = '3'),
                (SELECT guides_id FROM Guides WHERE guides_id = '4'))'''

customer3 = '''INSERT INTO Customer (f_name, l_name, age, customer_ID, phone_number, address, equipment_bought, equipment_rented, equipment_id, trip_id, guides_id) 
                VALUES ('Manny', 'Alverson', '37', '3', '402-555-4379', '9812 Harlem St', '4', '3', 
                (SELECT equipment_id FROM Equipment WHERE equipment_id = '2'),
                (SELECT trip_id FROM Trip WHERE trip_id = '3'),
                (SELECT guides_id FROM Guides WHERE guides_id = '4'))'''

customer4 = '''INSERT INTO Customer (f_name, l_name, age, customer_ID, phone_number, address, equipment_bought, equipment_rented, equipment_id, trip_id, guides_id) 
                VALUES ('Billy', 'Lamar', '41', '4', '712-569-1045', '9988 Sunset Blvd', '7', '4', 
                (SELECT equipment_id FROM Equipment WHERE equipment_id = '2'),
                (SELECT trip_id FROM Trip WHERE trip_id = '3'),
                (SELECT guides_id FROM Guides WHERE guides_id = '4'))'''

customer5 = '''INSERT INTO Customer (f_name, l_name, age, customer_ID, phone_number, address, equipment_bought, equipment_rented, equipment_id, trip_id, guides_id) 
                VALUES ('Pepe', 'Ramon', '26', '5', '712-370-4257', '7436 Niagra Ln', '2', '5', 
                (SELECT equipment_id FROM Equipment WHERE equipment_id = '2'),
                (SELECT trip_id FROM Trip WHERE trip_id = '3'),
                (SELECT guides_id FROM Guides WHERE guides_id = '4'))'''

customer6 = '''INSERT INTO Customer (f_name, l_name, age, customer_ID, phone_number, address, equipment_bought, equipment_rented, equipment_id, trip_id, guides_id) 
                VALUES ('Gerald', 'Sernova', '44', '6', '712-652-9073', '4416 Eugene Ave', '8', '5', 
                (SELECT equipment_id FROM Equipment WHERE equipment_id = '2'),
                (SELECT trip_id FROM Trip WHERE trip_id = '3'),
                (SELECT guides_id FROM Guides WHERE guides_id = '4'))'''

##############

cursor.execute(popEquipment)
db.commit()
cursor.execute(popTrip)
db.commit()
cursor.execute(popGuides)
db.commit()
cursor.execute(customer1)
db.commit()
cursor.execute(customer2)
db.commit()
cursor.execute(customer3)
db.commit()
cursor.execute(customer4)
db.commit()
cursor.execute(customer5)
db.commit()
cursor.execute(customer6)
db.commit()
##############################################################################################################################################################
# Print tables

cursor.execute("SELECT equipment_name, equipment_amountSold, equipment_amountOnHand, equipment_condition1, equipment_condition2, equipment_condition3," 
               "equipment_lastMaintenance, equipment_nextMaintenance, equipment_maintenanceCost, equipment_amountMade FROM Equipment")
result = cursor.fetchall()
print()
print("------Equipment Table------")
print("---On Average Per Month---")
for row in result:
    print("Equipment Name: {}".format(row[0]))
    print("Amount Sold: {}".format(row[1]))
    print("Amount on Hand: {}".format(row[2]))
    print("Condition (< 3yrs old): {}".format(row[3]))
    print("Condition (< 5yrs old): {}".format(row[4]))
    print("Condition (> 5yrs old): {}".format(row[5]))
    print("Last Maintenance: {}".format(row[6]))
    print("Next Maintenance: {}".format(row[7]))
    print("Maintenance Cost: ${}".format(row[8]))
    print("Amount Made (Yearly): ${}\n".format(row[9]))

cursor.execute("SELECT trip_name, trip_bookingPerYear, trip_locations, trip_costPerPerson, trip_highestBooked, trip_middleBooked, trip_lowestBooked FROM Trip")
result = cursor.fetchall()

print("------Trip Table------")
for row in result:
    print("Trip Name: {}".format(row[0]))
    print("Bookings Per Year: {}".format(row[1]))
    print("Locations: {}".format(row[2]))
    print("Cost Per Person: ${}".format(row[3]))
    print("Highest Amount Booked (Africa): {}".format(row[4]))
    print("Middle Amount Booked (Southern Europe): {}".format(row[5]))
    print("Lowest Amount Booked (Asia): {}\n".format(row[6]))

cursor.execute("SELECT guides_name, guides_airfareCost, guides_inoculationsCount, guides_inventoryCount, guides_inventorySold, guides_supplyCount FROM Guides")
result = cursor.fetchall()

print("------Guides Table------")
for row in result:
    print("Guides Name: {}".format(row[0]))
    print("Airfare Cost: ${}".format(row[1]))
    print("Inoculations Count: {}".format(row[2]))
    print("Inventory Count: {}".format(row[3]))
    print("Inventory Sold: {}".format(row[4]))
    print("Supply Count: {}\n".format(row[5]))

cursor.execute("SELECT f_name, l_name, age, phone_number, address, equipment_bought, equipment_rented FROM Customer")
result = cursor.fetchall()

print("------Customers Table------")
for row in result:
    print("First Name: {}".format(row[0]))
    print("Last Name: {}".format(row[1]))
    print("Age: {}".format(row[2]))
    print("Phone Number: {}".format(row[3]))
    print("Address: {}".format(row[4]))
    print("Equipment Bought: {}".format(row[5]))
    print("Equipment Rented: {}\n".format(row[6]))

##############################################################################################################################################################
### Query the tables to get the reports
### REPORT 1

cursor.execute("SELECT equipment_amountSold, equipment_amountOnHand, equipment_condition3, equipment_maintenanceCost,"
                "equipment_amountMade FROM Equipment")
report = cursor.fetchall()

print("------ Record 1 Table ------")
for row in report:
    print("Amount Sold: {}".format(row[0]))
    print("Amount On Hand: {}".format(row[1]))
    print("Current Equipment Condition: {}".format(row[2]))
    print("Monthly Maintenance Cost: ${}".format(row[3]))
    print("Amount Made This Year From Equipment Sales: ${}".format(row[4]))

cursor.execute("SELECT f_name, equipment_bought FROM Customer")
report = cursor.fetchall()
for row in report:
    print("{} bought {} piece(s) of equipment this year.".format(row[0], row[1]))

print()
print("-- The data above indicates that not enough equipment was sold\n"
      " throughout the year to continue selling to the public. As equipment\n"
      " is expensive to buy and maintain every month. --\n")

#######################################################################################################
### REPORT 2

cursor.execute("SELECT trip_name, trip_highestBooked, trip_middleBooked, trip_lowestBooked FROM Trip")
report = cursor.fetchall()

print("------ Record 2 Table ------")
for row in report:
        print("Trip Name: {}".format(row[0]))
        print("Highest trip booking (annually) 'Africa': {}".format(row[1]))
        print("Median trip booking (annually) 'Southern Europe': {}".format(row[2]))
        print("Lowest trip booking (annually) 'Asia': {}\n".format(row[3]))

print("-- From the above data in trip bookings for the year it shows that\n"
      " Asia is the downward most trending trip that we offer. This has been\n"
      " the case for the past few years. We believe it to be  due to the\n"
      " varying weather conditions and constant COVID restrictions that are\n"
      " still in place.\n")

######################################################################################################
### REPORT 3

cursor.execute("SELECT equipment_name, equipment_amountOnHand, equipment_condition1, equipment_condition2,"
                "equipment_condition3 FROM Equipment")
report = cursor.fetchall()

print("------ Record 3 Table ------")
for row in report:
    print("Equipment Name: {}".format(row[0]))
    print("Equipment On Hand: {}".format(row[1]))
    print("Equipment Current Condition (< 3yrs old): {}".format(row[2]))
    print("Equipment Current Condition (< 5yrs old): {}".format(row[3]))
    print("Equipment Current Condition (> 5yrs old): {}\n".format(row[4]))

print("-- Our current inventory, as displayed above, is very well kept and maintained. Most of our\n"
      " equipment is in good condition and young in age. Less than a quarter of our equipment is\n"
      " older than 5 years old and needs replacing. This helps us maintain excellent service, quality\n"
      " care to our customers, and ease of mind when out adventuring with us. --\n")

######################################################################################################

db.close()
cursor.close()