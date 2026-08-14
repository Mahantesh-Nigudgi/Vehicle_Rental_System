class Vehicle_rental:

    def __init__(self):
        self.vehicles=[
            {'Vehicle_type' : 'Car','Vehicle_number' : 'KA01RL1234','Rent' : 1600,'Vehicel_company' :'TATA','Vechile_model' : 'Nexon','Engine_capcity' : '1200cc','Seating_capacity':5},
            {'Vehicle_type' : 'Car','Vehicle_number' : 'KA01MA2233','Rent' : 2000,'Vehicel_company' :'TOYOTA','Vechile_model' : 'Innova','Engine_capcity' : '1600cc','Seating_capacity':7},
            {'Vehicle_type' : 'Car','Vehicle_number' : 'KA07DG8121','Rent' : 800,'Vehicel_company' :'NISSAN','Vechile_model' : 'Micra','Engine_capcity' : '800cc','Seating_capacity':5},
            {'Vehicle_type' : 'Car','Vehicle_number' : 'KA01DQ3421','Rent' : 1200,'Vehicel_company' :'MARUTI','Vechile_model' : 'Eratiga','Engine_capcity' : '950cc','Seating_capacity':7},
            {'Vehicle_type' : 'Bike','Vehicle_number' : 'KA01DF2893','Rent' : 400,'Vehicel_company' :'HONDA','Vechile_model' : 'Activa','Engine_capcity' : '125cc','Seating_capacity':2},
            {'Vehicle_type' : 'Bike','Vehicle_number' : 'KA05PD3376','Rent' : 750,'Vehicel_company' :'RE','Vechile_model' : 'Bullet350','Engine_capcity' : '349cc','Seating_capacity':2},
            {'Vehicle_type' : 'Bike','Vehicle_number' : 'KA05EJ7854','Rent' : 450,'Vehicel_company' :'TVS','Vechile_model' : 'Raider','Engine_capcity' : '200cc','Seating_capacity':2},
            {'Vehicle_type' : 'Bike','Vehicle_number' : 'KA07DG5321','Rent' : 550,'Vehicel_company' :'BAJA','Vechile_model' : 'NS200','Engine_capcity' : '200cc','Seating_capacity':2},
            ]
            

    @staticmethod
    def greet():
        print("\n!!.....Welcome to Nama Vehicle Rentals.....!!\n")


    def vehicle_details(self):
        for val in self.vehicles:
            for k,v in val.items():
                print(k,':',v)
            print()

         
    def car_details(self):
        for val in self.vehicles:
            # print(val)
            if val['Vehicle_type']=='Car':
                for k,v in val.items():
                    print(k,':',v)
                print()

    def car_total_rent(self,model,days):
        for val in self.vehicles:
            if val['Vechile_model']==model:
                if val['Vechile_model']==model:
                    print("----------TOTAL RENT----------")
                    print()
                    print('Vehicle :',val['Vechile_model'])
                    print('Rent per day :',val['Rent'])
                    print('Number of days :',days)
                    print()
                    print('------------------------------')
                    print()
                    print('The Total Rent :', val['Rent'],'X', days, '=' ,val['Rent']*days)
                else:
                    print()
                    print('This car is not available, so please check for other car')
                    break

            

    def bike_details(self):
            for val in self.vehicles:
                if val['Vehicle_type']=='Bike':
                    for k,v in val.items():
                        print(k,':',v)
                    print()   


    def bike_total_rent(self,model,days):
            for val in self.vehicles:
                if val['Vechile_model']==model:
                    if val['Vechile_model']==model:
                        print("----------TOTAL RENT----------")
                        print()
                        print('Vehicle :',val['Vechile_model'])
                        print('Rent per day :',val['Rent'])
                        print('Number of days :',days)
                        print()
                        print('------------------------------')
                        print()
                        print('The Total Rent :', val['Rent'],'X', days, '=' ,val['Rent']*days)
                    else:
                        print()
                        print('This bike is not available, so please check for other bike')
                        break

v1=Vehicle_rental()

v1.greet()

while True:
    choice=print("Our Services :\n1.Display All The Vehicles .\n2.Display All The Cars. \n3.Display all the Bikes. \n4.Calcuate the rent of a car.  \n5.Calcuate the rent of a bike. \n6.Exit")
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
            print('!!.....Thank you please visit again.....!!')
            break

        case _:
            print("Invalid option")
            print()
    

