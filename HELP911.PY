#911 HELP 
print("Welcom to 911 Help system.We are happy to assist you")
print("The creators are Darnell Richards,Kevin Cargill Jr.,Estifferson Peguero,Eduardo Moya")
print("Application description")
print("---------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------")
print("-----------------------------9 1 1    H E L P    S Y S T E M --------------------------------\n")
rows = 8
for i in range (0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
for i in range (rows, 0, -1):
    for j in range(0, i -1):
        print("*", end=' ')
    print("\r")

def name():
    n=input("Enter your name:")
    return n;

def address():
    a=input("Enter the location of the incident:")
    return a;
    
def phone():
    p=input("Enter your phone number:")
    return p;

name1=name();
add=address();
ph=phone();
rows = 4
for i in range (0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
for i in range (rows, 0, -1):
    for j in range(0, i -1):
        print("*", end=' ')
    print("\r")
print(name1);
print(add);
print(ph);


print("----------------------------------------------------------")
print("----------------------------------------------------------")


print("Select one of the following numbers")
print("1.Fire")
print("2.Robbery")
print("3.Medical")
print("4.Accident")
print("5.Shooting")

print("----------------------------------------------------------")
print("----------------------------------------------------------")


var =(int(input("Type in one of the following numbers:")))


if var == 1:
    print("Fire fighters are on the way!!")
    a=(int(input("How many people are affected?:")))
    if a >= 4:
        print ("More firefighters coming to",add)
    else:
        print ("Fire fighters are coming to",add)
    
    
elif  var == 2:
    print("Police are on the way to investigate the situation at",add)
    a=input("Do you need any medical help? Just type yes or no.")
    if a =='yes':
      print ("Ambulance on the way!!")
    if a =='no':
        print("Help is on the way to!!")
    

elif var == 3:
    print ("Ambulance on the way to",add)
    
elif var == 4:
    print ("1.Car")
    print ("2.Bike/Motorcycle")
    print ("3.Airplane")
    a = (int(input("What kind of accident?")))
    print ("Police on the way to",add)
    
    

elif var == 5:
    print ("Police on the way to",add)
    a = (input("Do you have extra information yes or no:"))
    if a == 'yes':
       input("What else?:")
       print ("Assistance is coming!!")
    if a == "no":
        print ("Help is on the way!!")
       


    
    
    
    
    
    

    



    
    

    



    
    










