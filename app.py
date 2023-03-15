from dotenv import load_dotenv

from controller.MainMenu import MainMenu
from view.MainView import MainView
from view.validators.MainViewValidator import MainViewValidator
from model.MemberModel import MemberModel
from controller.MemberMenu import MemberMenu
from view.MemberView import MemberView
from model.BookModel import BookModel
from model.CartModel import CartModel
from view.validators.MemberViewValidator import MemberViewValidator
from model.OrderModel import OrderModel
from model.OdetailsModel import OdetailsModel

load_dotenv()

member_view_validator = MemberViewValidator()
member_view = MemberView(member_view_validator)
book_model = BookModel()
cart_model = CartModel()
order_model = OrderModel()
odetails_model = OdetailsModel()
member_menu = MemberMenu(member_view, book_model, cart_model, order_model, odetails_model)
main_view_validator = MainViewValidator()
main_view = MainView(main_view_validator)
member_model = MemberModel()
main_menu = MainMenu(main_view, member_model, member_menu)
main_menu.run()
