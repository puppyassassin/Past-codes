isbn_codes_list=['9780735211292', '9780451529060','9781612681139','9781982172008','9781407230023',
 '9780393355949','9780061056581','9780547750330','9780307588371','9780425212189',
 '9780571221240','9780060935467','9781400079988','9781400078370','9781455582877',
 '9780345806789','9780451526342','9780091876043','9781599869773','9780330321143']

author_list=["James Clear", "Charles Darwin", "Robert.T.Kiyosaki", "Chris Miller", "Philip K.Dick",
 "Chuck Palahniuk", "Elizabeth Hand", "Eric Schlosser", "Gillian Flynn", "Robert Graysmith",
 "Richard Kelly", "Harper Lee", "Leo Tolstoy", "Natsuo Kirino", "Nicholas Sparks",
 "Stephen King", "George Orwell", "Spencer Johnson", "Sun Tzu", "Walter Mosley"]

title_list=["Atomic Habits", "On the origin of species","Rich Dad Poor Dad: What the Rich Teach Their Kids About Money That the Poor and Middle Class Do Not!",
 "Chip War: The Fight for the World's Most Critical Technology","Do Androids Dream of Electric Sheep?", "Fight Club: A Novel","12 Monkeys",
 "Fast Food Nation: The Dark Side of the All-American Meal", "Gone Girl","Zodiac: The Shocking True Story of the Hunt for the Nation's Most Elusive Serial Killer",
 "The Donnie Darko Book", "To Kill a Mockingbird", "War and Peace (Vintage Classics)","Out: A Thriller", "The Notebook", "The Shining", "Animal Farm",
 "WHO MOVED MY CHEESE?","The Art Of War", "Devil in a Blue Dress"]

publisher_list=["Avery", "Atheneum", "Plata Publishing", "Scribner",
 "Gollancz", "W. W. Norton & Company", "Harper Collins", "Mariner Books Classics",
 "Random House Publishing Group", "Berkley", "Farrar", "Harper Perennial",
 "Vintage", "Vintage", "Grand Central Publishing", "Anchor",
 "Signet", "Vermilion", "Filiquarian", "Pan Books"]

genre_list=["Self-help", "Scientific literature", "Personal finance", "Nonfiction thriller",
 "Dystopian science fiction", "Satire", "Science Fiction", "Non-fiction",
 "Psychological thriller", "True Crime", "Horror Fiction", "Southern Gothic fiction",
 "Historical fiction", "Mystery", "Romance", "Horror Fiction", "Satire",
 "Self-help", "Treatise", "Mystery"]

year_published_list=["2018", "1967", "2022", "2022", "2021", "2018", "1995", "2012", "2014",
 "2007", "2003", "2002", "2008", "2005", "2014", "2013", "1996", "1999",
 "2007", "1992"]

date_purchased_list=["2021-9-7", "2018-4-12", "2023-3-1", "2023-6-11", "2022-10-10",
"2020-9-11", "2016-3-19", "2015-3-3", "2019-6-24", "2018-4-2",
 "2017-11-14", "2014-6-5", "2015-9-26", "2014-2-14", "2023-7-4",
 "2015-7-25", "2016-5-5", "2017-3-4", "2018-1-18", "2019-8-16"]

book_status_list=["read", "to-read", "read", "read", "to-read", "to-read", "read", "read",
 "to-read", "read", "to-read", "read", "to-read", "to-read", "read", "to-read",
 "to-read", "to-read", "to-read", "read"]

import datetime

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
    isbn_codes_list.append(add1)
    return add1

# funtion to add author name
def author():
    add2 = input("Enter the name of the author: ")
    while add2.istitle() == False:
        print("Please enter the names correctly.")
        add2 = input("Enter the name of the author: ")
    author_list.append(add2)
    return add2

# function to add book tittle
def tittle():
    add3 = input("Enter the tittle of the book: ")
    while add3.replace(" ","").isalpha() == False:
        print("Please enter the tittle correctly.")
        add3 = input("Enter the tittle of the book: ")
    title_list.append(add3)
    return add3

# function to add publisher name
def publisher():
    add4 = input("Enter the name of the publisher: ")
    while add4.isnumeric() == True:
        print("Please enter the publisher name correctly.")
        add4 = input("Enter the name of the publisher: ")
    publisher_list.append(add4)
    return add4

# function to add book genre
def genre():
    add5 = input("Enter the genre of the book: ")
    while add5.isnumeric() == True:
        print("Please enter the genre correctly.")
        add5 = input("Enter the genre of the book: ")
    genre_list.append(add5)
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
                print("Enter an actual year that exist.")
                continue
            else:
                break
        except:
            print(end="")
    year_published_list.append(add6)
    return add6

# function to add date of purchased
def date_(add6):
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
            else:
                break
    date_purchased_list.append(add7)
    return add7

# function to add status of book
def status():
    add8 = input("Enter the current status of the book(read/to-read): ").lower()
    while add8 != 'read' and add8 != 'to-read':
        print("Please enter the terms specified.")
        add8 = input("Enter the current status of the book(read/to-read): ").lower()
    book_status_list.append(add8)
    return add8

# all function above combine to make add book function
def add_book():
    books = int(input("How many books would you like to add? = "))
    num = books
    for x in range(num):
        isbn()
        author()
        tittle()
        publisher()
        genre()
        date_(add6=year())
        status()
        print()


#executing function to add book information
add_book()



# cheking to see if the informations are added
print(isbn_codes_list)
print(author_list)
print(title_list)
print(publisher_list)
print(genre_list)
print(year_published_list)
print(date_purchased_list)
print(book_status_list)
