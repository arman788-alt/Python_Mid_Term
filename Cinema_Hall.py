class Star_Cinema:
    _hall_list = [] 

    def entry_hall(self, hall):
        self._hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self._rows = rows
        self._cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)


    def entry_show(self, id, movie_name, time):
        show_info = (id,movie_name,time)
        self.__show_list.append(show_info)
        seatMat = [[0 for i in range(self._cols)] for j in range(self._rows)]
        self.__seats[id] = seatMat



    def view_available_seats(self, id):
        show_exists = False
        for show in self.__show_list:
            if show[0] == id:
                show_exists = True
                print(f"!!----- Available Seats for Show -- {id}")
                for row in self.__seats[id]:
                    for seat in row:
                        print("0" if seat == 0 else "1", end=" ")
                    print()
                break

        if not show_exists:
            print("Show ID not found.")



    def book_seats(self, id, seat_list):
        show_exists = False
        for show in self.__show_list:
            if show[0] == id:
                show_exists = True
                for row, col in seat_list:
                    if row < 0 or row > self._rows or col < 0 or col > self._cols:
                        print(f"Invalid seat [{row}, {col}]. Seat is out of range.")
                    elif self.__seats[id][row][col] == 0:
                        self.__seats[id][row][col] = 1
                        print(f"Seat [{row}, {col}] booked successfully.")
                    else:
                        print(f"Seat {row}, {col} is already booked.")
                break

        if not show_exists:
            print("Show ID not found.")


   
    def view_show_list(self):
        print(f"!!------Show List for Hall :{self.hall_no}-------!!")
        cnt=1
        for show in self.__show_list:
            print(f"\n\t----Show : {cnt}----\n Show ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")
            cnt+=1
 

row, col = map(int, input("Enter Row And Col: ").split())
hallno = int(input("Enter hall no : "))
hall = Hall(row, col, hallno)

while True:

    print("!!-----Cinema Booking System------------!!")
    print("1.Add Show Information")
    print("2.View all shows today")
    print("3.Book seat for a show")
    print("4.View available seats for a show")
    print("5. Exit")


    op = int(input("Enter Option: "))

    if op == 1:
                h_id = input("Enter the hall id : ")
                movie = input("Enter the movie name : ")
                time = input("Enter the time of movie : ")
                hall.entry_show(h_id,movie,time)
                print()
                print("Add Show Information done.")
    

    elif op == 2:
        print("!!------- View Show Data --------!!")
        for show in Star_Cinema._hall_list:
            show.view_show_list()  

    elif op == 3:
        print(" !!---Book seat for a show---!!")
        show_id = input("Enter the ID of the show: ")
        num_seat = int(input("Enter the number of seats to book: "))
        seatBook = []
        for _ in range(num_seat):
            row = int(input("Enter the row of the seat: "))
            col = int(input("Enter the column of the seat: "))
            seatBook.append((row, col))
        hall.book_seats(show_id, seatBook)
              
        

    elif op == 3:
        print("!!----View available seats for a show ----!!")
        show_id = input("Enter the show id: ")
        hall.view_available_seats(show_id)


    elif op == 5:
        break

    else:
        print("Inavalid Option!")


