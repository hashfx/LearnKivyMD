from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.core.window import Window  # regulates size of window
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from helper import username_build, list_build, toolbar, navigation_drawer, switch_screen
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem, ThreeLineIconListItem, \
    IconLeftWidget, ThreeLineAvatarIconListItem, ImageLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (300, 500)  # window size at runtime :: for development purposes only


def MyLabel():
    label = MDLabel(text='Hello KivyMD',  # Label: displays text on screen
                    halign='center',  # aligns text at center
                    # theme_text_color='Error',  # Theme colors: Primary, Secondary, Hint, Error
                    theme_text_color='Custom',  # custom color of text
                    text_color=(0.5, 0.3, 0.4, 1),  # custom color (r, g, b, a)
                    font_style='H1',  # font style
                    )

    icon_label = MDIcon(icon='language-python', halign='center')  # default icons of KivyMD
    # return icon_label
    return label


def MyScreen():
    screen = Screen()  # instantiated Screen
    btn_flat = MDFlatButton(text="Click!",
                            pos_hint={'center_x': 0.5, 'center_y': 0.5}  # displays at center of screen
                            )
    btn_rect = MDRectangleFlatButton(text="Click!",
                                     pos_hint={'center_x': 0.5, 'center_y': 0.5}  # displays at center of screen
                                     )
    btn_icon = MDIconButton(icon='android',
                            pos_hint={'center_x': 0.5, 'center_y': 0.5}  # displays at center of screen
                            )
    btn_float = MDFloatingActionButton(icon='language-python',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.5}  # displays at center of screen
                                       )

    screen.add_widget(btn_float)
    return screen


def MyInput():
    screen = Screen()
    """
    username = MDTextField(text='Enter username',  # default text
                           pos_hint={'center_x':0.5, 'center_y':0.5},  # center align input field
                           size_hint=(0.5, 1),  # width of input field
                           size_hint_x=None, width=300  # input-field-size doesn't change w.r.t screen size
                           )
    """
    # creating text-input-field using Builder method
    global username
    username = Builder.load_string(username_build)
    # adding button
    button = MDRectangleFlatButton(text='Submit',
                                   pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                   on_release=show_data
                                   )
    screen.add_widget(username)  # adding username to screen
    screen.add_widget(button)  # adding button to screen
    return screen


def close_dialog(obj):
    dialog.dismiss()  # closes the dialog box


def show_data(obj):
    """ displays data entered in input textfield """

    if username.text is "":
        val_str = 'Please enter a valid username!'
    else:
        val_str = username.text + ' does not exist'

    print("Clicked!")  # displays "clicked!" when button is clicked
    print(username.text)  # fetch username from textfield and displays on console

    # adds button to dialog box
    close_button = MDFlatButton(text='Close',  # displays 'close' on button
                                on_release=close_dialog  # button on_event response
                                )
    more_button = MDRectangleFlatButton(text='More')  # adds button to dialog box

    global dialog
    dialog = MDDialog(text=val_str,  # displays user input in dialog box if entered
                      title='Entered Username',  # title of dialog box
                      size_hint=(0.7, 1),  # responsive dialog box
                      buttons=[close_button, more_button]  # adding buttons to dialog box
                      )

    dialog.open()  # displays dialog box whenever button is clicked


def MyList():
    screen = Screen()

    scroll = ScrollView()  # creating ScrollView of lists :: displays list from top to bottom
    list_values = MDList()  # creating list of list items
    scroll.add_widget(list_values)  # adding list to ScrollView
    """ adding list itemd manually
    item1 = OneLineListItem(text='Item1')  # creates one-line list
    item2 = OneLineListItem(text='Item2')  # creates one-line list
    item3 = OneLineListItem(text='Item3')  # creates one-line list
    item4 = OneLineListItem(text='Item4')  # creates one-line list
    list_values.add_widget(item1)  # add list item to MDList
    list_values.add_widget(item2)
    list_values.add_widget(item3)
    list_values.add_widget(item4)
    """

    # adding list items using for loop
    for i in range(20):  # creates 20 list items
        # items = OneLineListItem(text='Item' + str(i))  # generate one line list item
        # items = TwoLineListItem(text='Item' + str(i), secondary_text='Description')  # generate two line list item
        # generate three line list item
        # items = ThreeLineListItem(text='Item' + str(i),  # primary text
        #                           secondary_text='Description',  # secondary text
        #                           tertiary_text='MetaDesc'  # tertiary text
        #                           )
        icon = IconLeftWidget(icon="android")
        # generate three line items list with icons
        # items = ThreeLineIconListItem(text='Item' + str(i),  # primary text
        #                               secondary_text='Description',  # secondary text
        #                               tertiary_text='MetaDesc'  # tertiary text
        #                               )
        avatar = ImageLeftWidget(source="favicon.png")
        # generate three line items list with avatar
        items = ThreeLineAvatarIconListItem(text='Item' + str(i),  # primary text
                                            secondary_text='Description',  # secondary text
                                            tertiary_text='MetaDesc'  # tertiary text
                                            )
        items.add_widget(avatar)  # adding avatar to items list
        list_values.add_widget(items)  # add list items to screen

    screen.add_widget(scroll)  # add ScrollView MDList to screen
    return screen


def MyTable():
    screen = Screen()
    table = MDDataTable(size_hint=(0.9, 0.6),  # x is 90%; y is 60% of screen and adds shadow to table
                        pos_hint={'center_x': 0.5, 'center_y': 0.5},  # displays table at center of screen
                        check=True,  # prefixes checkbox to table :: default: False
                        rows_num=10,  # how many rows should be displayed on screen
                        column_data=[  # table column data
                            ("Sr. No.", dp(30)),  # (column_data, table_width)
                            ("Institute", dp(30)),  # table item with its size
                            ("Eligibility", dp(20))
                        ],
                        row_data=[
                            ("1", "NDA", "10+2"),  # table row data (Institute, Eligibility)
                            ("2", "IMA", "UG")  # if table goes out of screen; KivyMD adds a scroll bar
                        ]
                        )
    table.bind(on_check_press=check_press)  # calls function check_press when checkbox is pressed
    table.bind(on_check_press=row_press)  # calls on_check_press when row is checked through checkbox
    screen.add_widget(table)  # adding table to screen
    return screen


def check_press(instance_table, current_row):  # table data where checkbox is pressed; value of row pressed
    print(instance_table, current_row)


def row_press(instance_table, instance_row):
    print(instance_table, instance_row)


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class SocialScreen(Screen):
    pass


sm = ScreenManager()  # ScreenManager added
sm.add_widget(MenuScreen(name='menu'))  # MenuScreen is accessed through name: menu
sm.add_widget(ProfileScreen(name='profile'))  # ProfileScreen is accessed through name: profile
sm.add_widget(SocialScreen(name='social'))  # SocialScreen is accessed through name: social


class MyMDApp(MDApp):  # name of app

    def navigation_draw(self):
        """method to be evoked when menu button of toolbar is clicked"""
        print("MenuBar Clicked!")  # displays text when menu button is clicked

    def build(self):  # building app

        # labels in KivyMD
        MyLabel()

        # Screen and buttons in KivyMD
        MyScreen()

        # Themes in KivyMD
        # ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen',
        # 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        self.theme_cls.primary_palette = "Teal"  # changes app theme to Teal

        # ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900', 'A100', 'A200', 'A400', 'A700']
        self.theme_cls.primary_hue = "200"  # sets hue

        # self.theme_cls.theme_style = "Dark"  # Theme['Light', 'Dark']

        # User Input in KivyMD
        MyInput()

        screen_list = Builder.load_string(list_build)
        screen_toolbar = Builder.load_string(toolbar)
        screen_nav_draw = Builder.load_string(navigation_drawer)
        screen_switch_screen = Builder.load_string(switch_screen)

        # return MyLabel()
        # return MyScreen()
        # return MyInput()
        # return MyList()
        # return MyTable()
        # return screen_toolbar
        # return screen_nav_draw
        return screen_switch_screen


if __name__ == '__main__':
    MyMDApp().run()  # running app
