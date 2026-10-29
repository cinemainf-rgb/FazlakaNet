from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.spinner import Spinner

from kivy.uix.textinput import TextInput

from kivy.uix.button import Button

from kivy.uix.label import Label

import random
import string

from router_api import RouterAPI

from database import Database

from printer import print_card


class FazlakaApp(App):

    def build(self):

        self.router = RouterAPI()

        self.db = Database()

        root = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=5
        )

        self.ip = TextInput(
            hint_text='IP'
        )

        self.port = TextInput(
            text='8728'
        )

        self.user = TextInput(
            hint_text='Username'
        )

        self.password = TextInput(
            hint_text='Password'
        )

        connect_btn = Button(
            text='CONNECT'
        )

        connect_btn.bind(
            on_press=self.connect_router
        )

        self.profile_spinner = Spinner(
            text='Profiles'
        )

        self.count_input = TextInput(
            text='1'
        )

        sell_btn = Button(
            text='SELL CARD'
        )

        sell_btn.bind(
            on_press=self.sell_card
        )

        self.status = Label(
            text='Disconnected'
        )

        root.add_widget(self.ip)
        root.add_widget(self.port)
        root.add_widget(self.user)
        root.add_widget(self.password)
        root.add_widget(connect_btn)
        root.add_widget(self.profile_spinner)
        root.add_widget(self.count_input)
        root.add_widget(sell_btn)
        root.add_widget(self.status)

        return root

    def connect_router(
        self,
        instance
    ):

        ok = self.router.connect(
            self.ip.text,
            self.port.text,
            self.user.text,
            self.password.text
        )

        if ok:

            profiles = (
                self.router.get_profiles()
            )

            self.profile_spinner.values = (
                profiles
            )

            if profiles:

                self.profile_spinner.text = (
                    profiles[0]
                )

            self.status.text = (
                "Connected"
            )

    def sell_card(
        self,
        instance
    ):

        code = ''.join(
            random.choices(
                string.digits,
                k=7
            )
        )

        profile = (
            self.profile_spinner.text
        )

        self.router.create_user(
            code,
            profile
        )

        self.db.add_sale(
            code,
            profile
        )

        print_card(
            code,
            profile
        )

        self.status.text = (
            f"Created {code}"
        )


if __name__ == '__main__':
    FazlakaApp().run()
