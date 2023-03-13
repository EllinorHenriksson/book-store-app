from dotenv import load_dotenv

from controller.MainMenu import MainMenu
from view.MainView import MainView
from view.UserInfoValidator import UserInfoValidator
from model.MemberModel import MemberModel

load_dotenv()

validator = UserInfoValidator()
main_view = MainView(validator)
member_model = MemberModel()
main_menu = MainMenu(main_view, member_model)
main_menu.run()
