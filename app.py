from controller.MainMenu import MainMenu
from view.MainView import MainView

mainView = MainView()
mainMenu = MainMenu(mainView)
mainMenu.run()
