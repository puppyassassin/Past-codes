import datetime

# Function to write books_data to a file
def write_to_file(file_name, books_data):
    with open(file_name, 'w') as file:
        for book in books_data:
            # Create a string representing each book's information separated by commas
            line = f"{book['ISBN']},{book['Author']},{book['Title']},{book['Publisher']},{book['Genre']},{book['Publication_Year']},{book['Purchase_Date']},{book['Status']}\n"
            file.write(line)

# Function to read a file and convert its content to book data
def read_file_to_books(file_name):
    # Initialize empty lists to store different book attributes
    books_data = []
    isbn_codes_list = []
    author_list = []
    title_list = []
    publisher_list = []
    genre_list = []
    year_published_list = []
    date_purchased_list = []
    book_status_list = []

    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Split each line by comma to retrieve book attributes
            book_values = line.strip().split(',')
            if len(book_values) >= 8:
                # Create a dictionary representing a book and append its attributes to respective lists
                book = {
                    "ISBN": book_values[0],
                    "Author": book_values[1],
                    "Title": book_values[2],
                    "Publisher": book_values[3],
                    "Genre": book_values[4],
                    "Publication_Year":book_values[5],
                    "Purchase_Date": book_values[6],
                    "Status": book_values[7]
                }

                # Append values to respective lists
                isbn_codes_list.append(book_values[0])
                author_list.append(book_values[1])
                title_list.append(book_values[2])
                publisher_list.append(book_values[3])
                genre_list.append(book_values[4])
                year_published_list.append(book_values[5])
                date_purchased_list.append(book_values[6])
                book_status_list.append(book_values[7])

                books_data.append(book)

    return books_data, isbn_codes_list, author_list, title_list, publisher_list, genre_list, year_published_list, date_purchased_list, book_status_list

def write_book_data():
    file_name = "books_23093024.txt"
    books_data, isbn_codes_list, author_list, title_list, publisher_list, genre_list, year_published_list, date_purchased_list, book_status_list = read_file_to_books(file_name)

    # function to add isbn no.
    def isbn():
        while True:
            try:
                add1 = int(input("Enter the ISBN of the book: "))
                if len(str(add1)) != 13:
                    print("Invalid input! ISBN must have exactly 13 digits.")
                    continue
                else:
                    break
            except:
                print("Please enter actual numbers.")
        return str(add1)

    # funtion to add author name
    def author():
        add2 = input("Enter the name of the author: ").title()
        return add2

    # function to add book title
    def title():
        add3 = input("Enter the title of the book: ")
        return add3

    # function to add publisher name
    def publisher():
        add4 = input("Enter the name of the publisher: ")
        return add4

    # function to add book genre
    def genre():
        add5 = input("Enter the genre of the book: ")
        while add5.isnumeric() == True:
            print("Please enter the genre correctly.")
            add5 = input("Enter the genre of the book: ")
        return add5

    # funtion to add year of publish
    def year():
        current_year = datetime.date.today().year
        while True:
            try:
                add6 = input("Enter the year of publish: ")
                if len(str(add6)) != 4 or not add6.isnumeric():
                    print("Invalid input! Please a 4 digits number.")
                    add6 = int(add6)
                    continue
                elif not 0000 <= int(add6) <= current_year:
                    print("Enter an actual year that exists.")
                    continue
                else:
                    break
            except:
                print(end="")
        return add6

    # function to add date of purchased
    def date_(add6):
        current_year = datetime.date.today().year
        while True:
            add7 = str(input("Enter the date of purchase in the form of 'year-month-day' with numbers: "))
            try:
                year, month, day = add7.split('-')
                datetime.date(int(year), int(month), int(day))
            except:
                print("Please enter a correct date as stated.")
            else:
                if int(year) < int(add6):
                    print("This year is earlier than the year of publish.")
                    continue

                elif int(year)>current_year:
                    print("This year is later than the current year.")
                else:
                    break
        return add7

# function to add status of book
    def status():
        add8 = input("Enter the current status of the book (read/to-read): ").lower()
        while add8 != 'read' and add8 != 'to-read':
            print("Please enter the terms specified.")
            add8 = input("Enter the current status of the book (read/to-read): ").lower()
        return add8

    # all function above combine to make add book function
    def add_book():
        nonlocal books_data
        books = int(input("How many books would you like to add? = "))
        for _ in range(books):
            isbn_val = isbn()
            author_val = author()
            title_val = title()
            publisher_val = publisher()
            genre_val = genre()
            year_val = year()
            date_val = date_(add6=year_val)
            status_val = status()
            print()

            book = {
                "ISBN": isbn_val,
                "Author": author_val,
                "Title": title_val,
                "Publisher": publisher_val,
                "Genre": genre_val,
                "Publication_Year": year_val,
                "Purchase_Date": date_val,
                "Status": status_val
            }

            # Print added book information
            print("Added Book Information:")
            print("ISBN:", isbn_val)
            print("Author:", author_val)
            print("Title:", title_val)
            print("Publisher:", publisher_val)
            print("Genre:", genre_val)
            print("Publication Year:", year_val)
            print("Purchase Date:", date_val)
            print("Status:", status_val)
            print("=" * 20)  # Separator between books

            books_data.append(book)  # Add the new book to the books_data list

        return books_data

    updated_books_data = add_book()

    # Write the updated data back to the file
    write_to_file(file_name, updated_books_data)


write_book_data()