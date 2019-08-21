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
from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp
from kivy.properties import ListProperty
import MySQLdb

'''
    MD_Route88_System_GUI(App), Default Class: App
    This Class contains GUI Changing Components Only. All Other Functions 
'''


class MD_Route88_System_GUI(App):
    
    rows = {"Id": '0',"Brand": '0',"Km Run": '0'}
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
            if WindowActive == 'Route88_FirstTimeSetup': # Screen -> Route88_FirstTimeSetup
                self.root.ids.FirstTimer_DataFirstName.text = ""
                self.root.ids.FirstTimer_DataLastName.text = ""
                self.root.ids.FirstTimer_DataJobPosition.text = ""
                self.root.ids.FirstTimer_DataPasswordInit.text = ""
                self.root.ids.FirstTimer_DataPasswordConfirm.text = ""
            elif WindowActive == 'Route88_POS_SystemView': # Screen -> Route88_POS_SystemView
                pass
            elif WindowActive == 'Route88_DashboardView': # Screen -> Route88_StaffAccount_Delete
                pass
            elif WindowActive == 'Route88_Inventory_SystemView': # Screen -> Route88_Inventory_SystemView
                pass
            elif WindowActive == 'Route88_StaffAccount_View': # Screen -> Route88_StaffAccount_Add
                pass
            elif WindowActive == 'Route88_StaffAccount_Add': # Screen -> Route88_StaffAccount_Edit
                self.root.ids.NewStaff_FirstName.text = ''
                self.root.ids.NewStaff_LastName.text = ''
                self.root.ids.NewStaff_JobPosition.text = ''
                self.root.ids.NewStaff_PasswordInit.text = ''
                self.root.ids.NewStaff_PasswordConfirm.text = ''
            elif WindowActive == 'Route88_StaffAccount_Delete': # Screen -> Route88_StaffAccount_Selection
                pass
            elif WindowActive == 'Route88_StaffAccount_Edit': # Screen -> Route88_StaffAccount_Selection
                self.root.ids.ExistingEdit_FirstName.text = ''
                self.root.ids.ExistingEdit_LastName.text = ''
                self.root.ids.ExistingEdit_JobPosition.text = ''
                self.root.ids.ExistingEdit_PasswordInit.text = ''
                self.root.ids.ExistingEdit_PasswordConfirm.text = ''
            elif WindowActive == 'Route88_StaffAccount_Selection': # Screen -> Route88_StaffAccount_Selection
                self.root.ids.ExistingChange_Password.text = ''
                pass
            else:
                raise Exception
        except Exception as ErrorMessage:
            KivyDebugErrPrint.error("Invalid ScreenName: Candidate Value of 'WindowActive' didn't get any match from ScreenDesign_Handler.screen_names. Please restart or if the problem persist, contact developer @CodexLink.")
            #raise Exception("Invalid ScreenName: Candidate Value of 'WindowActive' didn't get any match from ScreenDesign_Handler.screen_names. Please restart or if the problem persist, contact developer @CodexLink.")

    '''
    '''

    def MDGUI_DataSubmission(self, WindowCandidate):
        if bool(MDGUI_DataValidate(WindowCandidate)) == True:
            pass

    def MDGUI_DataValidate(self, WindowCandidate):
        pass

    def get_data(self):
        try:
            con = MySQLdb.connect(host='localhost', user='root', passwd='', db='test')
            cur = con.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM Cars")
            #self.rows = cur.fetchall()
            self.rows = cur.fetchall()
            for row in self.rows:
                print('text:{0}, name:{1}, km:{2}'.format(row['id'],row['brand'],row['km']))
            print(self.rows)
        except Exception as ErrorMessage:
            self.MDGUI_SnackbarHandler(str(ErrorMessage))
            KivyDebugErrPrint.error('Database Error: {}'.format(ErrorMessage))

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
