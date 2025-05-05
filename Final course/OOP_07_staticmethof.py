
# Static methods are similar to class methods, except they don't receive any additional arguments; they are identical to normal functions that belong to a class.


# They are marked with the @staticmethod decorator.

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  #regular method
  def describe_book(self):
    print(self.title, 'by', self.author)

  #staticmethod
  @staticmethod
  def books_in_series(series_name, number_of_books):
    print('There are', number_of_books, 'books in the', series_name, 'series')

# Creating an instance of Book
my_book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")

# Using the instance method to describe the book
my_book.describe_book()

# calling the static method
Book.books_in_series("Harry Potter", 7)

# When should you use static methods instead of class methods? Static methods don't accept the cls parameter, meaning they can't access or modify the class's state. They are useful when you require functionality that doesn't depend on the class's behavior or instance state and doesn't affect it. Essentially, static methods are suited for tasks that are self-contained and do not require knowledge of the class or instance.
# 🌟 Class methods are called on the class itself, not on individual instances

# 🌟 Class methods are defined using the @classmethod decorator and accept the cls argument

# 🌟 Static methods, defined with the @staticmethod decorator, are similar to class methods but do not have access to the class's state