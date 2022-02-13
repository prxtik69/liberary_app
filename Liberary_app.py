class Liberary():
    def __init__(self, list, name):
        self.BookList = list
        self.name = name
        self.lendDictionary = {}

    def DisplayBooks(self):
        print("We have following Books right now : ")
        for book in self.BookList:
            print(book)

    def AddBook(self, book):
        self.BookList.append(book)
        print(f"Added {book} to the Book List")

    def LendBook(self, book, name):
        if book not in self.BookList:
            print(
                f"We dont have this book in the Library , we have these Books Right Now!{self.BookList}")
            exit()
        elif book not in self.lendDictionary.keys():
            print(f"{name}We have updated our Database , Please take the book")
        else:
            print(f"The Book is already owner by {self.lendDictionary[book]}")

    def returnBook(self, book):
        self.lendDictionary.pop(book)

    def CheckBook(self, book):
        if book in self.lendDictionary.keys():
            print(f"This Book is Lended by {self.lendDictionary[book]}")
        else:
            print("Book is present in Liberary")

    def CheckBookHolders(self):
        for xyz in self.lendDictionary:
            print(f"{xyz} Book is lended by {self.lendDictionary[xyz]}")


PasswordForStaff = 'kachabadam'
if __name__ == '__main__':
    Pratik = Liberary(["Book1", "Book2", "Book3", "Book4"], "Pratik")

    while(True):
        print("Welcome to Liberary , Please Enter your choice")
        print("1. Display Books in Liberary")
        print("2. Add Book In Liberary")
        print("3. Lend Book from Liberary")
        print("4. Return Book to Liberary")
        print("5. Check Book in Liberary")
        print("6. To Check who has which books (NEED STAFF PASSWORD)")

        user_choice = int(input())

        # if user_choice not in ["1" , "2" , "3" , "4"]:
        # print("Please Enter Valid Choice")

        if user_choice == 1:
            Pratik.DisplayBooks()

        elif user_choice == 2:
            AddBook_input = input(
                "Enter The Name of Book , you want Add in Liberary : \n")
            Pratik.AddBook(AddBook_input)

        elif user_choice == 3:
            lendInputBook = input(
                "Enter the Name of Book , you want to Lend : \n")
            lendInputUser = input("Enter Your Name : \n")
            Pratik.LendBook(lendInputBook, lendInputUser)

        elif user_choice == 4:
            returnBookInput = input(
                "Enter the name of Book , you want to retur : \n")
            Pratik.returnBook(returnBookInput)

        elif user_choice == 5:
            TakeBookInput = input(
                "Enter the name of Book , you want to check : \n")
            Pratik.CheckBook(TakeBookInput)

        elif user_choice == 6:
            takeInputt = input("Enter the STAFF PASSWORD")
            if takeInputt == PasswordForStaff:
                # for key , value in lendDictionary:
                Pratik.CheckBookHolders()
            else:
                print("Invalid STAFF PASSWORD")

        else:
            print("Please enter Valid Option")

        print('Press c to Continue and q to Quit')

        user_choice2 = ""
        while(user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q" or user_choice2 == "Q":
                exit()

            elif user_choice2 == "c" or user_choice2 == "C":
                continue
