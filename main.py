from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class FazlakaApp(App):

    def build(self):

        root = BoxLayout(
            orientation='vertical'
        )

        lbl = Label(
            text='FAZLAKA NET'
        )

        root.add_widget(lbl)

        return root

if __name__ == '__main__':
    FazlakaApp().run()
