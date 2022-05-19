# #Task 2
#Part 1

print(" ")
n=int(input("Enter the number: "))
n = str(n)
temp = n[::-1]

if n == temp:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

# Part 2

print(" ")
str = str(input("Enter the string: "))

def len_(str) :     
    if str == '':
        return 0
    else :
        return 1 + len_(str[1:])

print(" ")
print (len_(str))

# Part 3

def part(l, r, list_):
    pivot, pointer = list_[r], l
    for i in range(l, r):
        if list_[i] <= pivot:
            list_[i], list_[pointer] = list_[pointer], list_[i]
            pointer += 1
    list_[pointer], list_[r] = list_[r], list_[pointer]
    return pointer
 
def sort(l, r, list_):
    if len(list_) == 1:
        return list_
    if l < r:
        pi = part(l, r, list_)
        sort(l, pi-1, list_)
        sort(pi+1, r, list_)
    return list_
 
table = [1, 2, 4, 2, 14, 56, 5, 9]

print(" ") 
print(sort(0, len(table)-1, table))


#Task 4


class Car:

    make = "None"
    model = "None"
    year = "None"
    color = "None"
    size = "None"
    price = "None"

    def __init__(self,make,model,year,color,size,price):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.size = size
        self.price = price

    def setMake(self,make):
        self.make = make

    def getMake(self):
        return self.make

    def setModel(self,model):
        self.model = model

    def getModel(self):
        return self.model

    def setYear(self,year):
        self.year = year

    def getYear(self):
        return self.year

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def setSize(self,size):
        self.size = size

    def getSize(self):
        return self.size

    def setPrice(self,price):
        self.price = price

    def getPrice(self):
        return self.price

    def toString(self):
        return ("{}, {}, {}, {}, {}, {}".format(self.make,self.model,self.year,self.color,self.size,self.price))

    def rentCar(self):
        return print("Your's rent have been succesful!")

    def returnCar(self):
        return print("Your rent have been finished!")

class MainPage:

    listOfCars = list()

    def __init__(self):
        self.listOfCars = list()

    def addCar(self,car):
        self.listOfCars.append(car)

    def deleteCar(self,car):
        self.listOfCars.remove(car)

    def clearThePage(self):
        self.listOfCars.clear()

    def sortByPriceLowerThan(self,price):
        price = int(price)
        new_table = list()
        for car in self.listOfCars:
            if(int(car.price) <= price):
                new_table.append(car)
            else:
                pass
        for x in new_table:
            print(x.toString())
        new_table = list()

    def sortByPriceHigherThan(self,price):
        price = int(price)
        new_table = list()
        for car in self.listOfCars:
            if(int(car.price) >= price):
                new_table.append(car)
            else:
                pass
        for x in new_table:
            print(x.toString())
        new_table = list()

    def sortBySize(self,size):
        size = size.lower()
        size = size.capitalize()
        new_table = list()
        for car in self.listOfCars:
            if(car.size == size):
                new_table.append(car)
            else:
                pass
        for x in new_table:
            print(x.toString())
        new_table = list()
                
    def setList(self,list_):
        self.listOfCars = list_

    def getList(self):
        return self.listOfCars

    def selectCar(self,car):
        return car


car1 = Car('Ford','Focus','1995','Yellow','Medium','123')
car2 = Car('Aston Martin', 'Virage', "2012", 'Orange', 'Large', "114")
car3 = Car('Mazda', 'B-Series', '1990', 'Blue', 'Medium', '105')
car4 = Car('Audi', '100', '1991', 'Puce', 'Small', '123')
car5 = Car('Ford', 'F350', '1997', 'Violet', 'Medium', '87')
car6 = Car('Hyundai', 'Elantra', '2005', 'Red', 'Large', '93')
car7 = Car('Jeep', 'Grand Cherokee', '1996', 'Khaki', 'Large', '73')
car8 = Car('Mitsubishi', 'Eclipse', '1994', 'Purple', 'Medium', '70')
car9 = Car('Mercedes-Benz', 'CLK-Class', '1998', 'Crimson', 'Small', '139')
car10 = Car('Hyundai', 'XG350', '2004', 'Blue', 'Small', '51')
car11 = Car('Saab', '9000', '1994', 'Yellow', 'Large', '36')
car12 = Car('Mercedes-Benz', '500SEL', '1993', 'Orange', 'Large', '89')
car13 = Car('Volkswagen', 'GTI', '2009', 'Purple', 'Large', '125')
mainPage = MainPage()

table = (car1,car2,car3,car4,car5,car6,car7,car8,car9,car10,car11,car12,car13)

for x in table:
    mainPage.addCar(x)

print(" ")
mainPage.sortByPriceLowerThan(100)
print(" ")
mainPage.sortByPriceHigherThan(100.0)
print(" ")
mainPage.sortBySize("medium")
print(" ")
mainPage.sortBySize("medIum")
print(" ")
mainPage.sortBySize("lARge")