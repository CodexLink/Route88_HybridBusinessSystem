from kivy.app import App
from kivy.lang import Builder

KV = '''
RecycleView:
    viewclass: 'Label'
    data: sorted([{"text":"!", "ind":3},{"text":"world", "ind":2},{"text":"hello", "ind":1}], key=lambda k: k["ind"])
    RecycleBoxLayout:
        id: layout
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
'''

class TestApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    TestApp().run()