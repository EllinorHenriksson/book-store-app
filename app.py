from controller.MainMenu import MainMenu
from view.MainView import MainView
from model.Member import Member
"""
mainView = MainView()
mainMenu = MainMenu(mainView)
mainMenu.run()
"""

member = Member("eh224krlnu.se.com")
member.set_fname("Ellinor")
print(member.fname)
print(member.email)