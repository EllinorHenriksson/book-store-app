from dotenv import load_dotenv

from controller.MainMenu import MainMenu
from view.MainView import MainView
from view.UserInfoValidator import UserInfoValidator
from model.MemberModel import MemberModel
from controller.MemberMenu import MemberMenu
from view.MemberView import MemberView

load_dotenv()

member_view = MemberView()
member_menu = MemberMenu(member_view)
validator = UserInfoValidator()
main_view = MainView(validator)
member_model = MemberModel()
main_menu = MainMenu(main_view, member_model, member_menu)
main_menu.run()
