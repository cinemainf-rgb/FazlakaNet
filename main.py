from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class FazlakaApp(App):

    def build(self):

        root = BoxLayout(
            orientation="vertical"
        )

        title = Label(
            text="FAZLAKA NET"
        )

        btn = Button(
            text="TEST BUTTON"
        )

        root.add_widget(title)
        root.add_widget(btn)

        return root

if __name__ == "__main__":
    FazlakaApp().run()
