# Book Management System

# Import datetime and Texttable
from datetime import datetime
"""from texttable import Texttable"""


# Defining read_file() function
def read_text_file():
    # Declaring initial lists
    isbn_list = []
    author_list = []
    title_list = []
    publisher_list = []
    genre_list = []
    year_published_list = []
    date_purchased_list = []
    book_status_list = []

    # Opening file, read it, and put them into lists
    with open("books_23093024.txt", "r") as file:
        for lines in file:
            # Strip() to avoid spaces in front and behind the string
            # Split(",") to split the elements in the text file using comma
            books_data = lines.strip().split(",")

            isbn_list.append(books_data[0].strip())
            author_list.append((books_data[1].strip()))
            title_list.append(books_data[2].strip())
            publisher_list.append(books_data[3].strip())
            genre_list.append(books_data[4].strip())
            year_published_list.append(books_data[5].strip())
            date_purchased_list.append(books_data[6].strip())
            book_status_list.append(books_data[7].strip())

    return (isbn_list, author_list, title_list, publisher_list, genre_list, year_published_list, date_purchased_list,
            book_status_list)


# Defining add_book() function
def add_book(isbn_list, author_list, title_list, publisher_list, genre_list, year_published_list,
             date_purchased_list, book_status_list):
    # Informing the user about the function they choose in the main menu
    print("============================")
    print("=    ADD BOOK RECORD(S)    =")
    print("============================")

    # Setting default add_num, add_date_purchased_formatted, and current_year
    add_num = 1
    add_date_purchased_formatted = 0000-0-0
    current_year = datetime.now().year

    # While loop to allow user to have multiple attempts when they fail to enter the input
    while True:
        add_num_input = input("Please enter the number of book record(s) that you want to add.(or 'exit' to quit)\n")

        # Allow user to quit
        if add_num_input.lower() == 'exit':
            return

        # Try except block to error handling. Making sure user enter integer.
        try:
            # Prompt user to enter the number of book record(s) that they want to add
            add_num = int(add_num_input)

            # Make sure user enter numbers that are more than 0 as it is impossible to add 0 or lesser books
            if add_num <= 0:
                print(f"It is impossible to add {add_num} book(s). Please enter number that is greater than 0.")
                continue

        except ValueError:
            print("Number of book record(s) can only be in integer form (Example: 1). Please try again.")
            continue

        else:
            # Exiting the loop if user enter input correctly
            break

    # For loop to allow user add multiple books based on the number of books they entered before
    for x in range(add_num):
        # While loop to allow user to have multiple attempts when they fail to enter the input
        while True:
            add_isbn = input("ISBN of the book: ")

            # Make sure user enter integers
            if not add_isbn.isdigit():
                print("Invalid ISBN entered! ISBN must be in integer form.")
                continue

            # Make sure user cannot enter negative number for isbn of the book
            if int(add_isbn) < 0:
                print("Invalid ISBN entered! ISBN cannot be a negative number.")
                continue

            # Make sure user enter 13 digits which the number of digits that isbn have
            if len(add_isbn) != 13:
                print("Invalid ISBN entered! ISBN must have exactly 13 digits.")
                continue

            # Exiting the loop if user enter input correctly
            break

        # While loop to allow user to have multiple attempts when they fail to enter the input
        while True:
            add_author = input("Author of the book: ").title()

            # Prevent user leaving empty
            if add_author == '' or add_author.istitle() == False:
                print("Please enter the Author correctly.")
                continue

            else:
                # Exiting the loop if user enter input correctly
                break

        # While loop to allow user to have multiple attempts when they fail to enter the input
        while True:
            add_title = input("Title of the book: ").title()

            # Prevent user leaving empty
            if add_title == '':
                print("Title cannot be blank.")
                continue

            else:
                # Exiting the loop if user enter input correctly
                break

        # While loop to allow user to have multiple attempts when they fail to enter the input
        while True:
            add_publisher = input("Publisher of the book: ").title()

            # Prevent user leaving empty
            if add_publisher == '':
                print("Publisher cannot be blank.")
                continue

            else:
                # Exiting the loop if user enter input correctly
                break

        # While loop to allow user to have multiple attempts when they fail to enter the input
        while True:
            add_genre = input("Genre of the book: ").title()

            # Make sure the genre is in the form of alphabet
            if not add_genre.isalpha():
                print("Please enter a valid genre.")
                continue

            # Prevent user leaving empty
            if add_genre == '':
                print("Genre cannot be blank.")
                continue

            # Exiting the loop if user enter input correctly
            break

        # While loop to allow user to have multiple attempts when they fail to enter the input
        while True:
            add_year_published = input("Year published of the book:  ")

            # Make sure user enter in the form of digit
            if not add_year_published.isdigit():
                print("Invalid year entered! Year must be in integer form.")
                continue

            # Make sure user cannot enter negative numbers
            if int(add_year_published) < 0:
                print("Invalid year entered! Year cannot be negative number.")
                continue

            # Make sure user enter the correct format of year, which is XXXX
            if len(add_year_published) != 4:
                print("Invalid year entered! Year must have exactly 4 digits.")
                continue

            # Exiting the loop if user enter input correctly
            break

        # While loop to allow user to have multiple attempts when they fail to enter the input
        while True:
            # Try except block to error handling. Making sure user enter correct input
            try:
                add_date_purchased = input("Date purchased of the book (YYYY-MM-DD): ")
                # Converting the input of the user to desired format
                add_date_purchased_formatted = datetime.strptime(add_date_purchased, "%Y-%m-%d").date()
                year = add_date_purchased_formatted.year

            except ValueError:
                print("Invalid date entered! Please enter in the form of YYYY-M(M)-D(D).")
                continue

            else:
                # Prevent user enter input that is invalid
                if int(year) > current_year:
                    print("You cannot travel to future and purchase a book.")
                    continue

                if int(year) < int(add_year_published):
                    print("You cannot purchase a book if it is not published.")
                    continue

                else:
                    # Exiting the loop if user enter input correctly
                    break

        # While loop to allow user to have multiple attempts when they fail to enter the input
        while True:
            add_status = input("Status of the book (read/to-read): ").lower()

            # Make sure user enter correct input
            if add_status != 'read' and add_status != 'to-read':
                print("Invalid status entered! Please enter read/to-read only.")
                continue

            else:
                # Exiting the loop if user enter input correctly
                break

        # Adding all the information to the list
        isbn_list.append(add_isbn)
        author_list.append(add_author)
        title_list.append(add_title)
        publisher_list.append(add_publisher)
        genre_list.append(add_genre)
        year_published_list.append(add_year_published)
        date_purchased_list.append(add_date_purchased_formatted)
        book_status_list.append(add_status)

        # Informing the user that the book is successfully added in the system
        print(f"The book \"{add_title}\" added successfully!\n————————————————————————————————————————————")


# Defining delete_book() function
def delete_book(isbn_list, author_list, title_list, publisher_list, genre_list, year_published_list,
                date_purchased_list, book_status_list):
    # Informing the user about the function they choose in the main menu
    print("=============================")
    print("=   DELETE BOOK RECORD(S)   =")
    print("=============================")

    # Setting default delete_num, delete_option, and book_index
    delete_num = 1
    delete_option = 1
    book_index = 0

    # While loop to allow user to have multiple attempts when they fail to enter the input
    while True:
        delete_num_input = input("Please enter the number of book record(s) that you want to delete.(or 'exit' to quit)"
                                 "\n")

        # Allow user to quit
        if delete_num_input.lower() == 'exit':
            return

        # Try except block to error handling. Making sure user enter integer.
        try:
            # Prompt user to enter the number of book record(s) that they want to delete
            delete_num = int(delete_num_input)

            # Prevent user enter invalid input
            if delete_num > len(isbn_list) or delete_num <= 0:
                print(f"It is impossible to delete {delete_num} book(s). Please try again.")
                continue

        except ValueError:
            print("Number of book record(s) can only be in integer form (Example: 1). Please try again.")
            continue

        else:
            # Exiting the loop if user enter input correctly
            break

    # While loop to allow user to have multiple attempts when they fail to enter the input
    while True:
        # Try except block to error handling. Making sure user enter integer.
        try:
            # Prompt user to select one of the method to search for the book they want.
            print("Please enter 1, 2, or 3 to select the method to locate the book record that you want to delete:")
            delete_option = int(input("[1]\tISBN of the book\n[2]\tAuthor name of the book\n[3]\tTitle of the book\n"))

        except ValueError:
            print("Invalid option selected! Please enter 1, 2, or 3 only.")
            continue

        # Prevent user enter input that is not in the range of 1 to 3
        if delete_option not in [1, 2, 3]:
            print("Invalid option selected! Please enter 1, 2, or 3 only.")
            continue

        # Exiting the loop if user enter input correctly
        break

    # Prompt user to enter the book_information to locate the book that they want to delete
    # While loop to allow user to have multiple attempts when they fail to enter the input
    for x in range(delete_num):
        # While loop to allow user to have multiple attempts when they fail to enter the input
        while True:
            if delete_option == 1:
                delete_isbn = input("ISBN of the book: ")

                # Make sure user enter integers
                if not delete_isbn.isdigit():
                    print("Invalid ISBN entered! ISBN must be in integer form.")
                    continue

                # Make sure user enter 13 digits which the number of digits that isbn have
                if len(delete_isbn) != 13:
                    print("Invalid ISBN entered! ISBN must have exactly 13 digits.")
                    continue

                # Make sure user enter valid and existing isbn
                if delete_isbn not in isbn_list:
                    print("Book with given ISBN not found. Please try again.")
                    continue

                # Locate the book that user want to delete
                book_index = isbn_list.index(delete_isbn)

                # Exiting the loop if user enter correctly
                break

            elif delete_option == 2:
                delete_author = input("Author of the book: ").lower()

                # Create author_list that are lower case to make sure user can still able to search the book based on
                # the author even though they did not enter the name of the author in capital letter for the first
                # letter of their names.
                author_list_lowercase = [author.lower() for author in author_list]

                # Make sure user enter valid and existing author name
                if delete_author not in author_list_lowercase:
                    print("Book with given author name not found. Please try again.")
                    continue

                # Locate the book that user want to delete
                book_index = author_list_lowercase.index(delete_author)

                # Exiting the loop if user enter correctly
                break

            elif delete_option == 3:
                delete_title = input("Title of the book: ").lower()

                # Create title_list that are lower case to make sure user can still able to search the book based on the
                # title even though they did not enter the title in capital letter when necessary.
                title_list_lowercase = [title.lower() for title in title_list]

                # Make sure user enter valid and existing title
                if delete_title not in title_list_lowercase:
                    print("Book with given title name not found. Please try again.")
                    continue

                # Locate the book that user want to delete
                book_index = title_list_lowercase.index(delete_title)

                # Exiting the loop if user enter correctly
                break

        # Deleting the book record(s) that user want to delete
        del isbn_list[book_index]
        del author_list[book_index]
        del title_list[book_index]
        del publisher_list[book_index]
        del genre_list[book_index]
        del year_published_list[book_index]
        del date_purchased_list[book_index]
        del book_status_list[book_index]

        # Informing user that the book is successfully deleted
        print("Book record deleted successfully!\n————————————————————————————————————————————")


# Defining update_edit_book() function
def update_edit_book(isbn_list, author_list, title_list, publisher_list, genre_list, year_published_list,
                     date_purchased_list, book_status_list):
    # Informing the user about the function they choose in the main menu
    print("=============================")
    print("=  UPDATE/EDIT BOOK RECORD  =")
    print("=============================")

    # Setting default update_option, book_index
    update_option = 1
    book_index = 0

    # Prompt user to select the method that they want to use to search for book
    # While loop to allow user have multiple attempts when they fail to enter the input
    while True:
        # Prompt user to select one of the method to search for the book they want.
        print("Please enter 1, 2, or 3 to select the method to search for book (or 'exit' to quit):")
        update_input = input("[1]\tISBN of the book\n[2]\tAuthor name of the book\n[3]\tTitle of the book\n")

        # Allow user to quit
        if update_input.lower() == 'exit':
            return

        # Try except block to error handling. Making sure user enter integer.
        try:
            update_option = int(update_input)

        except ValueError:
            print("Invalid option selected! Please enter 1, 2, or 3 only.")
            continue

        # Prevent user enter input that is not in the range of 1 to 3
        if update_option not in [1, 2, 3]:
            print("Invalid option selected! Please enter 1, 2, or 3 only.")
            continue

        # Exiting the loop if user enter input correctly
        break

    # While loop to allow user to have multiple attempts when they fail to enter the input
    while True:
        if update_option == 1:
            update_isbn = input("ISBN of the book: ")

            # Make sure user enter integers
            if not update_isbn.isdigit():
                print("Invalid ISBN entered! ISBN must be in integer form.")
                continue

            # Make sure user enter 13 digits which the number of digits that isbn have
            if len(update_isbn) != 13:
                print("Invalid ISBN entered! ISBN must have exactly 13 digits.")
                continue

            # Make sure user enter valid and existing isbn
            if update_isbn not in isbn_list:
                print("Book with given ISBN not found. Please try again.")
                continue

            # Locate the book that user want to update/edit
            book_index = isbn_list.index(update_isbn)

            # Exiting the loop if user enter input correctly
            break

        elif update_option == 2:
            update_author = input("Author of the book: ").lower()

            # Create author_list that are lower case to make sure user can still able to search the book based on
            # the author even though they did not enter the name of the author in capital letter for the first
            # letter of their names.
            author_list_lowercase = [author.lower() for author in author_list]

            # Make sure user enter valid and existing author name
            if update_author not in author_list_lowercase:
                print("Book with given author name not found. Please try again.")
                continue

            # Locate the book that user want to update/edit
            book_index = author_list_lowercase.index(update_author)

            # Exiting the loop if user enter input correctly
            break

        elif update_option == 3:
            update_title = input("Title of the book: ").lower()

            # Create title_list that are lower case to make sure user can still able to search the book based on the
            # title even though they did not enter the title in capital letter when necessary.
            title_list_lowercase = [title.lower() for title in title_list]

            # Make sure user enter valid and existing title
            if update_title not in title_list_lowercase:
                print("Book with given title name not found. Please try again.")
                continue

            # Locate the book that user want to update/edit
            book_index = title_list_lowercase.index(update_title)

            # Exiting the loop if user enter input correctly
            break

    # While loop to allow user to have multiple attempts when they fail to enter the input
    while True:
        # Try except block to error handling. Making sure user enter integer.
        try:
            print(f"Please select the option from 1 to 8 to update the information of \"{title_list[book_index]}\"")
            new_book_information = int(input("[1]\tISBN of the book\n[2]\tAuthor of the book\n[3]\tTitle of the book\n"
                                             "[4]\tPublisher of the book\n[5]\tGenre of the book\n"
                                             "[6]\tYear published of the book\n[7]\tDate purchased of the book\n"
                                             "[8]\tStatus of the book\n"))

        except ValueError:
            print("Invalid option selected! Please select the option from 1 to 8 only!")
            continue

        else:
            if new_book_information == 1:
                # While loop to allow user to have multiple attempts when they fail to enter the input
                while True:
                    updated_isbn = input("ISBN of the book (Updated): ")

                    # Make sure user enter integers
                    if not updated_isbn.isdigit():
                        print("Invalid ISBN entered! ISBN must be in integer form.")
                        continue

                    # Make sure user enter 13 digits which the number of digits that isbn have
                    if len(updated_isbn) != 13:
                        print("Invalid ISBN entered! ISBN must have exactly 13 digits.")
                        continue

                    # Update/edit the book
                    isbn_list[book_index] = updated_isbn

                    # Informing user that the ISBN is updated successfully
                    print("ISBN updated successfully!")

                    # Exiting the loop if user enter input correctly
                    break

            elif new_book_information == 2:
                # While loop to allow user to have multiple attempts when they fail to enter the input
                while True:
                    new_author = input("Author of the book (Updated): ").title()

                    # Prevent user leaving empty
                    if new_author == '':
                        print("Author cannot be blank.")
                        continue

                    # Update/edit the book
                    author_list[book_index] = new_author

                    # Informing user that the author is updated successfully
                    print("Author updated successfully!")

                    # Exiting the loop if user enter input correctly
                    break

            elif new_book_information == 3:
                # While loop to allow user to have multiple attempts when they fail to enter the input
                while True:
                    new_title = input("Title of the book (Updated): ").title()

                    # Prevent user leaving empty
                    if new_title == '':
                        print("Title cannot be blank.")
                        continue

                    # Update/edit the book
                    title_list[book_index] = new_title

                    # Informing user that the title is updated successfully
                    print("Title updated successfully!")

                    # Exiting the loop if user enter input correctly
                    break

            elif new_book_information == 4:
                # While loop to allow user to have multiple attempts when they fail to enter the input
                while True:
                    new_publisher = input("Publisher of the book (Updated): ").title()

                    # Prevent user leaving empty
                    if new_publisher == '':
                        print("Publisher cannot be blank.")
                        continue

                    # Update/edit the book
                    publisher_list[book_index] = new_publisher

                    # Informing user that the publisher is updated successfully
                    print("Publisher updated successfully!")

                    # Exiting the loop if user enter input correctly
                    break

            elif new_book_information == 5:
                # While loop to allow user to have multiple attempts when they fail to enter the input
                while True:
                    new_genre = input("Genre of the book (Updated): ").title()

                    # Prevent user leaving empty
                    if new_genre == '':
                        print("Genre cannot be blank.")
                        continue

                    # Prevent user enter input that is not alphabet
                    if not new_genre.isalpha():
                        print("Please enter a valid genre.")
                        continue

                    # Update/edit the book
                    genre_list[book_index] = new_genre

                    # Informing the user that the genre is updated successfully
                    print("Genre updated successfully!")

                    # Exiting the loop if user enter input correctly
                    break

            elif new_book_information == 6:
                # While loop to allow user to have multiple attempts when they fail to enter the input
                while True:
                    # Try except block to error handling. Making sure user enter integer.
                    try:
                        new_year_published = int(input("Year published of the book (Updated): "))

                        # Make sure user enter valid input, as year must be in the form of XXXX
                        if len(str(new_year_published)) != 4:
                            print("Invalid input! Year must be in the form of 4 digits.\nExample: 2023")
                            continue

                    except ValueError:
                        print("Invalid year entered! Year can only be in integer form.")
                        continue

                    else:
                        # Update/edit the book
                        year_published_list[book_index] = new_year_published

                        # Informing the user that the year published is updated successfully
                        print("Year published updated successfully!")

                        # Exiting the loop if user enter input correctly
                        break

            elif new_book_information == 7:
                # While loop to allow user to have multiple attempts when they fail to enter the input
                while True:
                    # Try except block to error handling.
                    try:
                        new_date_purchased = input("Date purchased of the book (Updated): ")

                        # Converting the input of the user to the desired format
                        datetime.strptime(new_date_purchased, "%Y-%m-%d")

                        # Update/edit the book
                        date_purchased_list[book_index] = new_date_purchased

                        # Informing the user that the date purchased is updated successfully
                        print("Date purchased updated successfully!")

                        # Exiting the loop if user enter input correctly
                        break

                    except ValueError:
                        print("Invalid input! Purchased date must be in the format of YYYY-MM-DD ")
                        continue

            elif new_book_information == 8:
                # While loop to allow user to have multiple attempts when they fail to enter the input
                while True:
                    new_status = input("Status of the book (Updated): ").lower()

                    # Making sure user enter valid status of the book
                    if new_status not in ["read", "to-read"]:
                        print("Invalid input! Status of the book can only be read/to-read.")
                        continue

                    # Update/edit the book
                    book_status_list[book_index] = new_status

                    # Informing the user that the status is updated successfully
                    print("Status updated successfully!")

                    # Exiting the loop if user enter input correctly
                    break

            # Making sure user enter a valid option (in the range of 1 to 8)
            else:
                print("Invalid option selected! Please enter 1 to 8 only")
                continue

            # Exiting the loop if user enter input correctly
            break


# Defining display() function
def display(isbn_list, author_list, title_list, publisher_list, genre_list, year_published_list,
            date_purchased_list, book_status_list):
    # Informing the user about the function they choose in the main menu
    print("===========================")
    print("=         DISPLAY         =")
    print("===========================")

    # Handle situation when there is totally no book in the system
    if not isbn_list:
        print("No books to display.")
        return

    # Setting up the table
    t = Texttable()
    t.set_cols_width([4, 15, 30, 20, 15, 15, 15, 15, 10])

    # Adding headers for the table
    t.add_row(['#', 'ISBN', 'Title', 'Author', 'Publisher', 'Genre', 'Year Published', 'Date Purchased', 'Status'])

    # Drawing the table line by line
    for row in range(len(isbn_list)):
        t.set_cols_dtype(["a", "i", "t", "t", "t", "t", "i", "t", "t"])
        t.add_row([
            row + 1,
            isbn_list[row],
            title_list[row],
            author_list[row],
            publisher_list[row],
            genre_list[row],
            year_published_list[row],
            date_purchased_list[row],
            book_status_list[row]
        ])

    # Printing the table
    print(t.draw())


# Defining search_for_book() function
def search_for_book(isbn_list, author_list, title_list, publisher_list, genre_list, year_published_list,
                    date_purchased_list, book_status_list):
    # Informing the user about the function they choose in the main menu
    print("============================")
    print("=    SEARCH FOR BOOK(S)    =")
    print("============================")

    # Setting default search_option, book_index
    search_option = 1
    book_index = 0

    # Prompt user to select the method that they want to use to search for book
    # While loop to allow user have multiple attempts when they fail to enter the input
    while True:
        # Prompt user to select one of the method to search for the book they want.
        print("Please enter 1, 2, or 3 to select the method to search for book (or 'exit' to quit):")
        search_input = input("[1]\tISBN of the book\n[2]\tAuthor name of the book\n[3]\tTitle of the book\n")

        # Allow user to quit
        if search_input.lower() == 'exit':
            return

        # Try except block to error handling. Making sure user enter integer.
        try:
            search_option = int(search_input)

        except ValueError:
            print("Invalid option selected! Please enter 1, 2, or 3 only.")
            continue

        # Prevent user enter input that is not in the range of 1 to 3
        if search_option not in [1, 2, 3]:
            print("Invalid option selected! Please enter 1, 2, or 3 only.")
            continue

        # Exiting the loop if user enter input correctly
        break

    # While loop to allow user to have multiple attempts when they fail to enter the input
    while True:
        if search_option == 1:
            search_isbn = input("ISBN of the book: ")

            # Make sure user enter integers
            if not search_isbn.isdigit():
                print("Invalid ISBN entered! ISBN must be in integer form.")
                continue

            # Make sure user enter 13 digits which the number of digits that isbn have
            if len(search_isbn) != 13:
                print("Invalid ISBN entered! ISBN must have exactly 13 digits.")
                continue

            # Make sure user enter valid and existing isbn
            if search_isbn not in isbn_list:
                print("Book with given ISBN not found. Please try again.")
                continue

            # Locate the book that user want to search
            book_index = isbn_list.index(search_isbn)

            # Exiting the loop if user enter input correctly
            break

        elif search_option == 2:
            search_author = input("Author of the book: ").lower()

            # Create author_list that are lower case to make sure user can still able to search the book based on
            # the author even though they did not enter the name of the author in capital letter for the first
            # letter of their names.
            author_list_lowercase = [author.lower() for author in author_list]

            # Make sure user enter valid and existing author name
            if search_author not in author_list_lowercase:
                print("Book with given author name not found. Please try again.")
                continue

            # Locate the book that user want to search
            book_index = author_list_lowercase.index(search_author)

            # Exiting the loop if user enter input correctly
            break

        elif search_option == 3:
            search_title = input("Title of the book: ").lower()

            # Create title_list that are lower case to make sure user can still able to search the book based on the
            # title even though they did not enter the title in capital letter when necessary.
            title_list_lowercase = [title.lower() for title in title_list]

            # Make sure user enter valid and existing title
            if search_title not in title_list_lowercase:
                print("Book with given title name not found. Please try again.")
                continue

            # Locate the book that user want to search
            book_index = title_list_lowercase.index(search_title)

            # Exiting the loop if user enter input correctly
            break

    # Printing results
    print("Book information")
    print(f"ISBN\t\t\t: {isbn_list[book_index]}")
    print(f"Author\t\t\t: {author_list[book_index]}")
    print(f"Title\t\t\t: {title_list[book_index]}")
    print(f"Genre\t\t\t: {genre_list[book_index]}")
    print(f"Publisher\t\t: {publisher_list[book_index]}")
    print(f"Year published\t: {year_published_list[book_index]}")
    print(f"Date purchased\t: {date_purchased_list[book_index]}")
    print(f"Status\t\t\t: {book_status_list[book_index]}")


# Defining write_text_file() function
def write_text_file(isbn_list, author_list, title_list, publisher_list, genre_list, year_published_list,
                    date_purchased_list, book_status_list):
    # Opening text file and write all the information in the list back to the file
    with open("books_23093024.txt", "w") as file:
        # Writing file line by line
        for i in range(len(isbn_list)):
            books_data = (f"{isbn_list[i]}, {author_list[i]}, {title_list[i]}, {publisher_list[i]},"
                          f"{genre_list[i]}, {year_published_list[i]}, {date_purchased_list[i]},"
                          f" {book_status_list[i]}")

            # Avoid an empty line at the end of the text file
            if i < len(isbn_list) - 1:
                books_data += '\n'

            file.write(books_data)


# Defining menu function
def main_menu():
    # Reading all the information from text file and put them to their list respectively
    (isbn_list, author_list, title_list, publisher_list, genre_list, year_published_list, date_purchased_list,
     book_status_list) = read_text_file()

    # While loop to allow user to have multiple attempts when they fail to enter the input
    while True:
        # Try except block to handle error when user enter input that is not integer
        try:
            # Printing menu for user to choose the function that they want to use
            print(f"{'Menu':>20}")
            print("[1]\tAdd Book Record(s)\n[2]\tDelete Book Record(s)\n[3]\tUpdate/Edit Book Record(s)")
            print("[4]\tDisplay\n[5]\tSearch For Book(s)\n[6]\tExit")
            option = int(input("Please enter option 1 to 6\n"))

        except ValueError:
            print("Invalid option selected! Please enter option 1 to 6 only.")
            continue

        else:
            if option == 1:
                # While loop to allow user to have multiple attempts when they fail to enter the input
                while True:
                    add_book(isbn_list, author_list, title_list, publisher_list, genre_list, year_published_list,
                             date_purchased_list, book_status_list)

                    # Allow user to add multiple book
                    cont = input("Do you want to continue adding book? [y/n]\n")

                    while cont.lower() not in ['y', 'n', 'yes', 'no']:
                        print("Invalid input!")
                        cont = input("Do you want to continue adding book? [y/n]\n")

                    if cont.lower() == 'y' or cont.lower() == 'yes':
                        continue

                    elif cont.lower() == 'n' or cont.lower() == 'no':
                        break

            elif option == 2:
                # While loop to allow user to have multiple attempts when they fail to enter the input
                while True:
                    delete_book(isbn_list, author_list, title_list, publisher_list, genre_list, year_published_list,
                                date_purchased_list, book_status_list)

                    # Allow user to delete multiple book
                    cont = input("Do you want to continue delete book? [y/n]\n")

                    while cont.lower() not in ['y', 'n', 'yes', 'no']:
                        print("Invalid input!")
                        cont = input("Do you want to continue delete book? [y/n]\n")

                    if cont.lower() == 'y' or cont.lower() == 'yes':
                        continue

                    elif cont.lower() == 'n' or cont.lower() == 'no':
                        break

            elif option == 3:
                # While loop to allow user to have multiple attempts when they fail to enter the input
                while True:
                    update_edit_book(isbn_list, author_list, title_list, publisher_list, genre_list,
                                     year_published_list,
                                     date_purchased_list, book_status_list)

                    # Allow user to update/edit multiple book
                    cont = input("Do you want to continue update/edit book? [y/n]\n")

                    while cont.lower() not in ['y', 'n', 'yes', 'no']:
                        print("Invalid input!")
                        cont = input("Do you want to continue update/edit book? [y/n]\n")

                    if cont.lower() == 'y' or cont.lower() == 'yes':
                        continue

                    elif cont.lower() == 'n' or cont.lower() == 'no':
                        break

            elif option == 4:
                # While loop to allow user to have multiple attempts when they fail to enter the input
                while True:
                    display(isbn_list, author_list, title_list, publisher_list, genre_list, year_published_list,
                            date_purchased_list, book_status_list)

                    # Allow user to display the book records multiple time
                    cont = input("Do you want to continue display the book record(s)? [y/n]\n")

                    while cont.lower() not in ['y', 'n', 'yes', 'no']:
                        print("Invalid input!")
                        cont = input("Do you want to continue display the book record(s)? [y/n]\n")

                    if cont.lower() == 'y' or cont.lower() == 'yes':
                        continue

                    elif cont.lower() == 'n' or cont.lower() == 'no':
                        break

            elif option == 5:
                # While loop to allow user to have multiple attempts when they fail to enter the input
                while True:
                    search_for_book(isbn_list, author_list, title_list, publisher_list, genre_list, year_published_list,
                                    date_purchased_list, book_status_list)

                    # Allow user to search multiple books
                    cont = input("Do you want to continue search for book? [y/n]\n")

                    while cont.lower() not in ['y', 'n', 'yes', 'no']:
                        print("Invalid input!")
                        cont = input("Do you want to continue search for book? [y/n]\n")

                    if cont.lower() == 'y' or cont.lower() == 'yes':
                        continue

                    elif cont.lower() == 'n' or cont.lower() == 'no':
                        break

            elif option == 6:
                # Writing all the information in the lists back to the text file
                write_text_file(isbn_list, author_list, title_list, publisher_list, genre_list, year_published_list,
                                date_purchased_list, book_status_list)

                # Printing the "Thank you" message after they used this book management system.
                print("Thank you for using BOOK MANAGEMENT SYSTEM. SEE YOU NEXT TIME!")

                # Exiting the program
                break

            # Handle situations when user enter option that is invalid. (Not in the range of 1 to 6)
            else:
                print("Invalid option selected! Please select option from 1 to 6 only.")
                continue


# Calling main_menu() to start the book management system
main_menu()


