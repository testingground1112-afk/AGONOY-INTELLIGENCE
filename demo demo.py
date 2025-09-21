from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivymd.theming import ThemeManager
from kivymd.uix.snackbar import Snackbar

Window.size = (360,640)

LabelBase.register(
    name="OpenSans-VariableFont_wdth,wght",
    fn_regular="OpenSans-VariableFont_wdth,wght.ttf",
    fn_bold="OpenSans-Bold.ttf"
)

KV = """
MainWindow:
    LoginScreen:
    SignupScreen:
    HomePage:

<LoginScreen>
    name: "login"
    mobile_num: m_number
    password: password

    FloatLayout:
        FitImage:
            source: "login_bg.jpg"

        Image:
            source: "logo.png"
            size_hint: None, None
            size: "180dp", "180dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.86}

        MDLabel:
            text: "Log in"
            bold: True
            font_name: "OpenSans-VariableFont_wdth,wght"
            halign: "left"
            font_size: "22sp"
            valign: "center"
            size_hint: None, None
            pos_hint: {"x": 0.1, "top": 0.73}

        BoxLayout:
            orientation: "vertical"
            size_hint: 0.9, None
            height: self.minimum_height
            pos_hint: {"center_x": 0.5, "center_y": 0.43}
            padding: "20dp"
            spacing: "15dp"

            MDTextField:
                id: m_number
                hint_text: "Enter mobile number"
                font_name: "OpenSans-VariableFont_wdth,wght"
                font_size: "12sp"
                height: "50dp"
                mode: "rectangle"
                multiline: False
                pos_hint: {"center_x": 0.5}
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1

            MDTextField:
                id: password
                hint_text: "Enter password"
                password: "True"
                font_name: "OpenSans-VariableFont_wdth,wght"
                font_size: "12sp"
                mode: "rectangle"
                pos_hint: {"center_x": 0.5}
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1

            MDRectangleFlatButton:
                text: "Login"
                size_hint_x: 1
                height: "55dp"
                text_color: "black"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                on_release: root.login_inter()

            MDRectangleFlatButton:
                text: "Signup"
                size_hint_x: 1
                height: "55dp"
                text_color: "black"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = "signup"


<SignupScreen>
    name: "signup"
    create_num: c_number
    c_pass: c_pass
    v_pass: v_pass

    FloatLayout:
        FitImage:
            source: "signup_bg.jpg"

        MDLabel:
            text: "Sign in"
            bold: True
            font_name: "OpenSans-VariableFont_wdth,wght"
            halign: "left"
            font_size: "22sp"
            valign: "center"
            size_hint: None, None
            pos_hint: {"x": 0.1, "top": 0.73}

        Image:
            source: "logo.png"
            size_hint: None, None
            size: "180dp", "180dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.86}

        BoxLayout:
            orientation: "vertical"
            size_hint: 0.9, None
            height: self.minimum_height
            pos_hint: {"center_x": 0.5, "center_y": 0.38}
            padding: "20dp"
            spacing: "15dp"

            MDTextField:
                id: c_number
                hint_text: "Create mobile number"
                size_hint_x: None
                mode: "rectangle"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                width: "280dp"
                font_size: "12sp"
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1

            MDTextField:
                id: c_pass
                hint_text: "Create password"
                password: "True"
                mode: "rectangle"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                size_hint_x: None
                width: "280dp"
                font_size: "12sp"
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1

            MDTextField:
                id: v_pass
                hint_text: "Verify your password"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                password: "True"
                mode: "rectangle"
                size_hint_x: None
                width: "280dp"
                font_size: "12sp"
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1

            MDRectangleFlatButton:
                text: "Signup"
                size_hint_x: 1
                height: "55dp"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                text_color: "black"
                on_release: root.signup_inter()

            MDRectangleFlatButton:
                text: "Back"
                size_hint_x: 1
                height: "55dp"
                text_color: "black"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                on_release: root.go_back()

<HomePage>
    name: "homepage"

    FloatLayout:

        MDTopAppBar:
            title: "Agonoy Intelligence"
            left_action_items: [["menu"]]
            right_action_items: [["dots-vertical"]]
            pos_hint: {"top": 1}
            elevation: 4

        BoxLayout:
            orientation: "vertical"
            size_hint: 0.9, None
            height: self.minimum_height
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            padding: "20dp"
            spacing: "15dp"

            MDFillRoundFlatButton:
                text: "Logout"
                size_hint_x: 1
                size_hint: None, None
                size: "200dp", "48dp"
                pos_hint: {"center_x": 0.5}
                on_release: root.logout()

        MDBottomAppBar:
            MDTopAppBar:
                type: "bottom"
                icon: "git"
                icon_color: 0, 1, 0, 1

"""

class LoginScreen(Screen):
    mobile_num = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_inter(self):
        mobile_n = self.mobile_num.text
        passw = self.password.text

        if not mobile_n or not passw:
            self.manager.show_message("Please enter both fields.")
        else:
            mobile_n = int(mobile_n)

            if mobile_n in self.manager.students:
                if passw == self.manager.students[mobile_n]:
                    self.manager.show_message("Welcome to Homepage!")
                    self.manager.current = "homepage"
                    self.mobile_num.text = ""
                    self.password.text = ""
                else:
                    self.manager.show_message("Invalid password, please try again.")
                    self.password.text = ""
            else:
                self.manager.show_message("Student not found, please sign up.")
                self.mobile_num.text = ""
                self.password.text = ""


class SignupScreen(Screen):
    create_num = ObjectProperty(None)
    c_pass = ObjectProperty(None)
    v_pass = ObjectProperty(None)

    def signup_inter(self):

        if not self.create_num.text or not self.c_pass.text:
            self.manager.show_message("Please enter given fields.")
            return

        if self.create_num.text.isdigit():
            if int(self.create_num.text) in self.manager.students:
                self.manager.show_message("Account already exists with this number.")
                self.create_num.text = ""
                self.c_pass.text = ""
                self.v_pass.text = ""
                return

            if self.c_pass.text == self.v_pass.text:
                self.manager.students[int(self.create_num.text)] = self.c_pass.text
                self.manager.show_message("Successfully created an account")
                self.c_pass.text = ""
                self.v_pass.text = ""
                self.create_num.text = ""
            else:
                self.manager.show_message("verify password not similar to new password")
                self.v_pass.text = ""

        else:
            self.manager.show_message("Mobile number must be digits only.")
            return

    def go_back(self):
        self.manager.current = "login"


class HomePage(Screen):
    def logout(self):
        self.manager.show_message("Goodbye!")
        self.manager.current = "login"

class MainWindow(ScreenManager):
    students = {}
    def show_message(self,ms):
        Snackbar(text=ms, duration=1.5).open()

class DemoApp(MDApp):
    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_string(KV)

if __name__ == "__main__":
    DemoApp().run()
