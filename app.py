from dotenv import load_dotenv

from controller.MainMenu import MainMenu
from view.MainView import MainView
from view.UserInfoValidator import UserInfoValidator
from model.MemberModel import MemberModel
from controller.MemberMenu import MemberMenu
from view.MemberView import MemberView
from model.BookModel import BookModel
from model.CartModel import CartModel

load_dotenv()

member_view = MemberView()
book_model = BookModel()
cart_model = CartModel()
member_menu = MemberMenu(member_view, book_model, cart_model)
validator = UserInfoValidator()
main_view = MainView(validator)
member_model = MemberModel()
main_menu = MainMenu(main_view, member_model, member_menu)
main_menu.run()
