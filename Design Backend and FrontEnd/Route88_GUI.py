from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.config import Config
from kivy.logger import Logger as KivyDebugErrPrint
from kivymd.button import MDIconButton
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from kivy.clock import Clock
from random import choice as RandomizePick
import mysql.connector

from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp
from kivy.properties import ListProperty
import sqlite3 as lite


'''
    MD_Route88_System_GUI(App), Default Class: App
    This Class contains GUI Changing Components Only. All Other Functions 
'''


class MD_Route88_System_GUI(App):
    
    rows = ListProperty([("Id","Brand","Km Run")])
    theme_cls = ThemeManager()
    title = "Route88 System"
    Icon_Status = 'brightness-1'
    __rand_primary_palette = ['Pink', 'Blue', 'Indigo', 'BlueGrey', 'Brown', 'LightBlue', 'Purple',
                              'Yellow', 'DeepOrange', 'Green', 'Red', 'Teal', 'Orange', 'Cyan', 'Amber', 'DeepPurple', 'Lime']

    def build(self):
        self.__MainClassBuildFile = Builder.load_file(
            "MD_Route88_DesignFile.kv")
        self.theme_cls.primary_palette = (
            RandomizePick(self.__rand_primary_palette))
        self.theme_cls.primary_hue = '400'
        self.theme_cls.theme_style = 'Light'
        return self.__MainClassBuildFile

    def on_start(self):
        try:
            Config.set('graphics', 'width', '1024')
            Config.set('graphics', 'height', '768')
            Config.set('graphics', 'show_cursor', '1')
            Config.set('graphics', 'minimum_width', '1024')
            Config.set('graphics', 'minimum_height', '768')
            Config.set('kivy', 'exit_on_escape', '0')
            Config.write()
            # Returns String for CriticalComponent_Check Function whether to proceed or not,
            return 'Passed'
        except Exception as ErrorMessage:
            self.MDUserNotif_SnackbarHandler(str(ErrorMessage))
            return 'Failed'

    def MDGUI_PaletteChange(self):
        self.theme_cls.primary_palette = (
            RandomizePick(self.__rand_primary_palette))

    def MDGUI_SchemeChange(self):
        if self.root.ids.ToolbarMain.darkBooleanParameter == True and self.theme_cls.theme_style == 'Dark':
            self.root.ids.ToolbarMain.darkBooleanParameter = False
            self.root.ids.ToolbarMain.right_action_items = [['invert-colors', lambda x: MD_Route88_System_GUI.MDGUI_PaletteChange(
                self)], ['brightness-2', lambda x: MD_Route88_System_GUI.MDGUI_SchemeChange(self)]]
            self.theme_cls.theme_style = 'Light'

        elif self.root.ids.ToolbarMain.darkBooleanParameter == False and self.theme_cls.theme_style == 'Light':
            self.root.ids.ToolbarMain.darkBooleanParameter = True
            self.root.ids.ToolbarMain.right_action_items = [['invert-colors', lambda x: MD_Route88_System_GUI.MDGUI_PaletteChange(
            )], ['brightness-7', lambda x: MD_Route88_System_GUI.MDGUI_SchemeChange(self)]]
            self.theme_cls.theme_style = 'Dark'

    def MDGUI_SnackbarHandler(self, params_message):
        Snackbar(text=params_message).show()

    '''
    def MDGUI_ClearTextField(self, WindowActive), where WindowActive is self.root.ids.ScreenDesign_Handler.current
        This function iterates through List of Screen_Names inside of GUI. The objective of this function is to clear
        all text fields associated within that screen name. Automated Detection of Text Field names might not be possible.
    '''
    def MDGUI_ClearTextField(self, WindowActive):
        try:
            WindowCandidate = [WindowName for WindowName in self.root.ids.ScreenDesign_Handler.screen_names]
            print(WindowCandidate)
            for ActiveWindowCandidate in WindowCandidate:
                if WindowActive == WindowCandidate[0]: # Screen -> Route88_FirstTimeSetup
                    print
                    self.root.ids.FirstTimer_DataFirstName.text = ""
                    self.root.ids.FirstTimer_DataLastName.text = ""
                    self.root.ids.FirstTimer_DataJobPosition.text = ""
                    self.root.ids.FirstTimer_DataPassword.text = ""
                elif WindowActive == WindowCandidate[1]: # Screen -> Route88_POS_SystemView
                    pass
                elif WindowActive == WindowCandidate[2]: # Screen -> Route88_Inventory_SystemView
                    pass
                elif WindowActive == WindowCandidate[3]: # Screen -> Route88_StaffAccount_Add
                    pass
                elif WindowActive == ActiveWindowCandidate[4]: # Screen -> Route88_StaffAccount_Delete
                    pass
                elif WindowActive == ActiveWindowCandidate[5]: # Screen -> Route88_StaffAccount_Edit
                    pass
                elif WindowActive == ActiveWindowCandidate[6]: # Screen -> Route88_StaffAccount_Selection
                    pass
                else:
                    raise Exception
        except Exception as ErrorMessage:
            KivyDebugErrPrint.error("Invalid ScreenName: Candidate Value of 'WindowActive' didn't get any match from ScreenDesign_Handler.screen_names. Please restart or if the problem persist, contact developer @CodexLink.")
            #raise Exception("Invalid ScreenName: Candidate Value of 'WindowActive' didn't get any match from ScreenDesign_Handler.screen_names. Please restart or if the problem persist, contact developer @CodexLink.")

    '''
    '''
    # This Function Member is for Screen 'Route88_FirstTimeSetup' only.
    def MDGUI_FirstTimeSubmit(self):
        pass
    '''
    '''
    def MDGUI_DataSubmission(self, WindowActive):
        pass

    def get_data(self):
        con = lite.connect('test.db')
        cur = con.cursor()
        try:
            with con:
                cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
                cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
                cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
                cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
                cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
                cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
                cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
                cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
                cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")
                cur.execute("INSERT INTO Cars VALUES(9,'Audi',52642)")
                cur.execute("INSERT INTO Cars VALUES(10,'Mercedes',57127)")
                cur.execute("INSERT INTO Cars VALUES(11,'Skoda',9000)")
                cur.execute("INSERT INTO Cars VALUES(12,'Volvo',29000)")
                cur.execute("INSERT INTO Cars VALUES(13,'Bentley',350000)")
                cur.execute("INSERT INTO Cars VALUES(14,'Citroen',21000)")
                cur.execute("INSERT INTO Cars VALUES(15,'Hummer',41400)")
                cur.execute("INSERT INTO Cars VALUES(16,'Volkswagen',21600)")
                cur.execute("INSERT INTO Cars VALUES(17,'Audi',52642)")
                cur.execute("INSERT INTO Cars VALUES(18,'Mercedes',57127)")
                cur.execute("INSERT INTO Cars VALUES(19,'Skoda',9000)")
                cur.execute("INSERT INTO Cars VALUES(20,'Volvo',29000)")
                cur.execute("INSERT INTO Cars VALUES(21,'Bentley',350000)")
                cur.execute("INSERT INTO Cars VALUES(22,'Citroen',21000)")
                cur.execute("INSERT INTO Cars VALUES(23,'Hummer',41400)")
                cur.execute("INSERT INTO Cars VALUES(24,'Volkswagen',21600)")
                cur.execute("INSERT INTO Cars VALUES(25,'Audi',52642)")
                cur.execute("INSERT INTO Cars VALUES(26,'Mercedes',57127)")
                cur.execute("INSERT INTO Cars VALUES(27,'Skoda',9000)")
                cur.execute("INSERT INTO Cars VALUES(28,'Volvo',29000)")
                cur.execute("INSERT INTO Cars VALUES(29,'Bentley',350000)")
                cur.execute("INSERT INTO Cars VALUES(30,'Citroen',21000)")
                cur.execute("INSERT INTO Cars VALUES(31,'Hummer',41400)")
                cur.execute("INSERT INTO Cars VALUES(32,'Volkswagen',21600)")
        except:
            pass
        cur.execute("SELECT * FROM Cars")
        self.rows = cur.fetchall()
        print(self.rows)


class MySQLDatabaseHandler:
    def Database_Init():
        pass


class MD_Route88(MD_Route88_System_GUI, MySQLDatabaseHandler):
    def __init__(self):
        return super().__init__()

    def InitEverything(self):
        pass


"""
    NON-RELATABLE TO MAIN CLASS
        This are the class that has no connection with the main class that is used to initialize the whole program.

    NON-RELATABLE TO MAIN CLASS > AvatarSampleWidget Initializes an Item with Picture on the Left and Items to the right
    think of it as a MDListItem but with pictures on the left
"""
class AvatarSampleWidget(ILeftBody, Image):
    pass

"""
    NON-RELATABLE TO MAIN CLASS > IconLeftSampleWidget, Same Descriptions as AvatarSampleWidget, but it is only icons that gets displayed on the right
"""
class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass

"""
    NON-RELATABLE TO MAIN CLASS > IconRightSampleWidget, same as IconLeftSameplWidget
"""
class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass




"""
    Procedural: Class Initialization and Component Check
"""
if __name__ == '__main__':
    ## Create for Component Check here.
    # MySQLDatabaseHandler().Database_Init()

    MD_Route88_System_GUI().run()
