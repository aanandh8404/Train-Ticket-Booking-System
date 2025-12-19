class Train:
    def __init__(self,train_no, name, source, destination, seats, fare):
        self.train_no = train_no
        self.name = name
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare

class User:
    def __init__(self, name, password, mobile):
        self.name = name
        self.password = password
        self.mobile = mobile

class TrainBookingSystem:

    def __init__(self):
        self.users = []
        self.current_user = ""
        self.trains = []
        self.bookings = {}
        self.booking_id = 1000
        self.add_trains()

    def login(self):
        mobile = input("Enter Mobile no :")
        password = input("Enter Password :")
        if self.users:
            for user in self.users:
                if user.mobile == mobile and user.password == password:
                        self.current_user = user.name
                        print(self.current_user)
                        self.menu()
                else :
                    print("Invalid User")
        else :
            print("No user Found")

    def register(self):
        print("\n--------Register---------")
        name = input("Enter your Name :")
        password = input("Set Password :")
        mobile = input("Enter Mobile number :")
        print("Registered Successfully")

        self.users.append(User(name,password,mobile))

    def add_trains(self):
        self.trains.append(Train(101,"train1","Chennai","Coimbatore",400,500))
        self.trains.append(Train(102,"train2","Chennai","Bangalore",800,700))
        self.trains.append(Train(103, "train3","Chennai","Hyderabad",500,600))

    def view_trains(self):
        print("\nAvailable Trains :")
        for t in self.trains:
            print(f"Train no : {t.train_no} | Name : {t.name} | Route : {t.source} -> {t.destination}  | Seats Available : {t.seats} | fare : {t.fare}")

    def book_train(self):
        self.view_trains()
        train_no = int(input("\nEnter Train no to book :"))
        no_of_seats = int(input("Enter the number of seats to book :"))
        for t in self.trains:
            if t.train_no == train_no:
                if t.seats >= no_of_seats:
                    self.booking_id += 1
                    t.seats -= no_of_seats
                    self.bookings[self.booking_id] = {
                        "name" : t.name,
                        "passenger_name": self.current_user,
                        "passengers": no_of_seats,
                        "fare": no_of_seats * t.fare
                    }
                    print("Booking successfull")
                    break
                else:
                    print("Not Enough seats Available")
            else:
                print("Invalid train no")

    def view_booked(self):
        print("\n--------------Booked trains--------------")
        for b in self.bookings:
            train = self.bookings[b]
            if train["passenger_name"] == self.current_user:
                print("\nBooking id : ",b)
                print("Passenger Name :",train["passenger_name"])
                print("Train Name : ",train["name"])
                print("Total No of Seats :",train["passengers"])
                print("Price : Rs.",train["fare"])

    def cancel_ticket(self):
        b_id = int(input("Enter Booking id of Train to be Cancelled :"))
        for b in self.bookings:
            train = self.bookings[b]
            if b == b_id and train["passenger_name"] == self.current_user:
                del self.bookings[b]
                
                for t in self.trains:
                    if t.name == train["name"]:
                        t.seats += train["passengers"]
                        
                print("Ticket Cancelled successfully")
                break
            else:
                print("Invalid Booking id")
        # else :
        #     print("Invalid Booking id")

    def menu(self):
        while True:
            print("\nTrain Ticket Booking system")
            print("1.View Trains")
            print("2.Book Train")
            print("3.View Booked Trains")
            print("4.Cancel train")
            print("5.Logout")

            choice = int(input("Enter your Choice (1 - 5) :"))

            if choice == 1:
                self.view_trains()
            elif choice == 2:
                self.book_train()
            elif choice == 3:
                self.view_booked()
            elif choice == 4:
                self.cancel_ticket()
            elif choice == 5:
                print("Logged Out")
                break

            else :
                print("Invalid Choice")
    
    
    def start(self):
        while True:
            print("\n------Login-------")
            print("1.Login")
            print("2.Register")
            print("3.Exit")
            choice = int(input("Enter the choice :"))
            if choice == 1:
                if len(self.users) > 0:
                    self.login()
                else:
                    print("No users in data, Register first")
            elif choice == 2:
                self.register()
            elif choice == 3:
                print("Thank You")
                break
            else:
                print("Invalid Choice")

system = TrainBookingSystem()
system.start()
