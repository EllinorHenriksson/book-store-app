"""
The starting point of the application
See example.env for the required environment variables

Author: Ellinor Henriksson <eh224kr@student.lnu.se>
"""

from dotenv import load_dotenv

from controller.MainMenu import MainMenu
from view.MainView import MainView
from view.validators.MainViewValidator import MainViewValidator
from model.Member import Member
from controller.MemberMenu import MemberMenu
from view.MemberView import MemberView
from model.Book import Book
from model.Cart import Cart
from view.validators.MemberViewValidator import MemberViewValidator
from model.Order import Order
from model.Odetails import Odetails

load_dotenv()

member_view_validator = MemberViewValidator()
member_view = MemberView(member_view_validator)
book_model = Book()
cart_model = Cart()
order_model = Order()
odetails_model = Odetails()
member_menu = MemberMenu(member_view, book_model, cart_model, order_model, odetails_model)
main_view_validator = MainViewValidator()
main_view = MainView(main_view_validator)
member_model = Member()
main_menu = MainMenu(main_view, member_model, member_menu)
main_menu.run()
