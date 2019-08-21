from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout

items = [{'SP1': 'Artikelnummer', 'SP2': 'Name', 'SP3': 'Groesse'},
         {'SP1': '510001', 'SP2': 'Big Pump', 'SP3': '1.50 L'},
         {'SP1': '523001', 'SP2': 'Leonie Still', 'SP3': '1.50 L'},
         {'SP1': '641301', 'SP2': 'Cola Mix', 'SP3': '1.50 L'}
         ]



Builder.load_string('''
<Tabelle@BoxLayout>:
    orientation: 'horizontal'
    spalte1_SP: 'spalte1'
    spalte2_SP: 'spalte2'
    spalte3_SP: 'spalte3'
    Label:
        id: SP1
        text: root.spalte1_SP
    Label:
        id: SP2
        text: root.spalte2_SP
    Label:
        id: SP3
        text: root.spalte3_SP

<RV>:
    viewclass: 'Tabelle'
    RecycleBoxLayout:
        default_size: None, dp(20)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'spalte1_SP': str(x['SP1']), 'spalte2_SP': str(x['SP2']), 'spalte3_SP': str(x['SP3'])} for x in items]


class TestApp(App):
    def build(self):
        return RV()


if __name__ == '__main__':
    TestApp().run()