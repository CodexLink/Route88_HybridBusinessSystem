from kivy.app import App
from kivy.lang import Builder


KV = '''

<Row@BoxLayout>:
    ind: 1
    Button:
        text: str(root.ind)
    Button:
        text: "default"

BoxLayout:
    ind: 1
    orientation: "vertical"
    Button:
    BoxLayout:
        Button:
        RecycleView:
            id: rv
            data: [{"text":"first","ind":1}]

            viewclass: 'Row'
            RecycleBoxLayout:
                default_size_hint: 1, None
                default_size: None, dp(56)
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
        Button
    BoxLayout:
        Button:
            text: "Add"
            on_release:
                root.ind += 1
                rv.data.append({"ind": root.ind})
        Button:
            text: "Remove"
            on_release:
                root.ind = root.ind - 1 if root.ind > 0 else 0
                if len(rv.data): rv.data.pop(-1)

'''



class Test(App):
    def build(self):
        self.root = Builder.load_string(KV)
        return self.root


Test().run()