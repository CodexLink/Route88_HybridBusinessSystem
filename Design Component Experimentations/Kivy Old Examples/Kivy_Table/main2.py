import sqlite3 as lite

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
except:
    pass


from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty


Builder.load_string("""

<MyLayout>:
    orientation: "vertical"
    BoxLayout:
        size_hint_y: 0.1
        Label:
            text: 'ID'
        Label:
            text: 'Brand'
        Label:
            text: 'Km'
    BoxLayout:
        RecycleView:
            data: [{'text':"{}".format(id)} for id,name,km in root.rows]
            viewclass: "Label"
            RecycleBoxLayout:
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: "vertical"
        RecycleView:
            data: [{'text':"{}".format(name)} for id,name,km in root.rows]
            viewclass: "Label"
            RecycleBoxLayout:
                default_size: None, dp(56)
                orientation: "vertical"
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
        RecycleView:
            data: [{'text':"{}".format(km)} for id,name,km in root.rows]
            viewclass: "Label"
            RecycleBoxLayout:
                default_size: None, dp(56)
                orientation: "vertical"
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
    Button:
        size_hint_y: 0.1
        text: "Get data"
        on_press: root.get_data()

""")


class MyLayout(BoxLayout):
    rows = ListProperty([("Id","Brand","Km Run")])
    def get_data(self):
        cur.execute("SELECT * FROM Cars")
        self.rows = cur.fetchall()
        print(self.rows)


runTouchApp(MyLayout())
