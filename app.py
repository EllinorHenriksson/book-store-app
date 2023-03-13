from controller.MainMenu import MainMenu
from view.MainView import MainView
from view.UserInfoValidator import UserInfoValidator

validator = UserInfoValidator()
mainView = MainView(validator)
mainMenu = MainMenu(mainView)
mainMenu.run()
