class Vehicle_rental:

    def __init__(self):
        self.vehicles=[
            {'Vehicle_type' : 'Car','Vehicle_number' : 'KA01RL1234','Rent' : 1600,'Vehicle_company' :'TATA','Vehicle_model' : 'Nexon','Engine_capacity' : '1200cc','Seating_capacity':5},
            {'Vehicle_type' : 'Car','Vehicle_number' : 'KA01MA2233','Rent' : 2000,'Vehicle_company' :'TOYOTA','Vehicle_model' : 'Innova','Engine_capacity' : '1600cc','Seating_capacity':7},
            {'Vehicle_type' : 'Car','Vehicle_number' : 'KA07DG8121','Rent' : 800,'Vehicle_company' :'NISSAN','Vehicle_model' : 'Micra','Engine_capacity' : '800cc','Seating_capacity':5},
            {'Vehicle_type' : 'Car','Vehicle_number' : 'KA01DQ3421','Rent' : 1200,'Vehicle_company' :'MARUTI','Vehicle_model' : 'Eratiga','Engine_capacity' : '950cc','Seating_capacity':7},
            {'Vehicle_type' : 'Bike','Vehicle_number' : 'KA01DF2893','Rent' : 400,'Vehicle_company' :'HONDA','Vehicle_model' : 'Activa','Engine_capacity' : '125cc','Seating_capacity':2},
            {'Vehicle_type' : 'Bike','Vehicle_number' : 'KA05PD3376','Rent' : 750,'Vehicle_company' :'RE','Vehicle_model' : 'Bullet350','Engine_capacity' : '349cc','Seating_capacity':2},
            {'Vehicle_type' : 'Bike','Vehicle_number' : 'KA05EJ7854','Rent' : 450,'Vehicle_company' :'TVS','Vehicle_model' : 'Raider','Engine_capacity' : '200cc','Seating_capacity':2},
            {'Vehicle_type' : 'Bike','Vehicle_number' : 'KA07DG5321','Rent' : 550,'Vehicle_company' :'BAJA','Vehicle_model' : 'NS200','Engine_capacity' : '200cc','Seating_capacity':2},
            ]
            

    @staticmethod
    def greet():
        print("\n!!.....Welcome to Nama Vehicle Rentals.....!!\n")

    @staticmethod
    def greet_1():
        print('!!.....Thank you please visit again.....!!')


    def vehicle_details(self):
        for val in self.vehicles:
            for k,v in val.items():
                print(k,':',v)
            print()

         
    def car_details(self):
        for val in self.vehicles:
            if val['Vehicle_type']=='Car':
                for k,v in val.items():
                    print(k,':',v)
                print()

    def car_total_rent(self,model,days):
        car=False
        for val in self.vehicles:
            if val['Vehicle_model']==model:
                car=True
                print("----------TOTAL RENT----------")
                print()
                print('Vehicle :',val['Vehicle_model'])
                print('Rent per day :',val['Rent'])
                print('Number of days :',days)
                print()
                print('------------------------------')
                print()
                print('The Total Rent :', val['Rent'],'X', days, '=' ,val['Rent']*days)
                break
        if not car: 
            print()
            print('This car is not available, so please check for other car')
            

            

    def bike_details(self):
            for val in self.vehicles:
                if val['Vehicle_type']=='Bike':
                    for k,v in val.items():
                        print(k,':',v)
                    print()   


    def bike_total_rent(self,model,days):
            bike=False
            for val in self.vehicles:
                if val['Vehicle_model']==model :
                    bike=True
                    print("----------TOTAL RENT----------")
                    print()
                    print('Vehicle :',val['Vehicle_model'])
                    print('Rent per day :',val['Rent'])
                    print('Number of days :',days)
                    print()
                    print('------------------------------')
                    print()
                    print('The Total Rent :', val['Rent'],'X', days, '=' ,val['Rent']*days)
                    break
            if not bike:
                print()
                print('This bike is not available, so please check for other bike')
                

v1=Vehicle_rental()

v1.greet()

while True:
    choice=print(
        "Our Services : \n"
        "1.Display All The Vehicles. \n"
        "2.Display All The Cars. \n"
        "3.Display all the Bikes. \n"
        "4.Calcuate the rent of a car.  \n"
        "5.Calcuate the rent of a bike. "
        "\n6.Exit"
        )

    
    opt=int(input("Enter your choice :"))
    print()

    match opt:

        case 1:
            v1.vehicle_details()

        case 2:
            v1.car_details()
            print()

        case 3:
            v1.bike_details()
            print()

        case 4:
            model=input("Enter which car model you want ot rent :")
            days=int(input("Enter the numbers of days to rent the car :"))
            v1.car_total_rent(model,days)
            print()

        case 5:
            model=input("Enter which bike model you want ot rent :")
            days=int(input("Enter the numbers of days to rent the bike :"))
            v1.bike_total_rent(model,days)
            print()

        case 6:
            v1.greet_1()
            break

        case _:
            print("Invalid option")
            print()
    

