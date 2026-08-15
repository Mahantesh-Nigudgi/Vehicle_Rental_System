# Nama Vehicle Rentals

Hi! This is a small Python project I made. It is a simple **Vehicle Rental System** that runs in the terminal (command line). It is not a big project, just something to practice Python basics like classes, loops, dictionaries and match-case statements.

## What this project does

Basically you can:

1. See all the vehicles (cars + bikes)
2. See only the cars
3. See only the bikes
4. Calculate the total rent for a car (you give the model name and number of days)
5. Calculate the total rent for a bike (same as above)
6. Exit the program (it says thank you when you exit)

That's it! Pretty simple menu based program.

## Vehicles available

### Cars

| Company | Model    | Engine  | Seats | Rent/Day |
|---------|----------|---------|-------|----------|
| TATA    | Nexon    | 1200cc  | 5     | 1600     |
| TOYOTA  | Innova   | 1600cc  | 7     | 2000     |
| NISSAN  | Micra    | 800cc   | 5     | 800      |
| MARUTI  | Eratiga  | 950cc   | 7     | 1200     |

### Bikes

| Company | Model      | Engine  | Seats | Rent/Day |
|---------|------------|---------|-------|----------|
| HONDA   | Activa     | 125cc   | 2     | 400      |
| RE      | Bullet350  | 349cc   | 2     | 750      |
| TVS     | Raider     | 200cc   | 2     | 450      |
| BAJA    | NS200      | 200cc   | 2     | 550      |

(This data is just hardcoded in the code itself, there is no database or file, it's just a list of dictionaries.)

## What you need to run it

- Just Python installed (3.10 or above, because I used `match`/`case` which only works from Python 3.10 onwards)

## How to run

Open your terminal in the folder where the file is and type:

```bash
python Vehicle_rental_system.py
```

Then a welcome message will show up and you will see a menu like this:

```
Our Services :
1.Display All The Vehicles.
2.Display All The Cars.
3.Display all the Bikes.
4.Calcuate the rent of a car.
5.Calcuate the rent of a bike.
6.Exit
```

Just type the number of what you want to do and press enter.

## Example

If I choose option 4 and type "Nexon" and "3" days, it shows:

```
----------TOTAL RENT----------

Vehicle : Nexon
Rent per day : 1600
Number of days : 3

------------------------------

The Total Rent : 1600 X 3 = 4800
```

If I type a model that doesn't exist, like "Fortuner", it now tells me:

```
This car is not available, so please check for other car
```

And if I choose option 6, it prints a thank you message and the program stops.

## Files

- `Vehicle_rental_system.py` - this has everything, the class and the main loop, I didn't split it into multiple files.

## About the class (Vehicle_rental)

Here are the functions/methods I made inside the class:

- `greet()` - prints the welcome message at the start
- `greet_1()` - prints the thank you message when you exit (option 6)
- `vehicle_details()` - shows all vehicles
- `car_details()` - shows only cars
- `bike_details()` - shows only bikes
- `car_total_rent(model, days)` - finds the car by model name and calculates rent, and tells me if the car doesn't exist
- `bike_total_rent(model, days)` - same as above but for bikes



Thanks for checking out my project!