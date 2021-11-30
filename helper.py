# input-text-field using Builder method
# create a variable and add all widgets as to be added in *.kv file
username_build = """
MDTextField:
    hint_text: "Enter username"  # placeholder text
    helper_text: "then click the SUBMIT button"  # text to be appeared below input field
    helper_text_mode: "on_focus"  # on_focus:when textfield is clicked ; persistent: always on screen
    icon_right: "android"  # displays icon at right of textfield
    icon_right_color: app.theme_cls.primary_color  # inherits icon color from app theme
    pos_hint: {'center_x':0.5, 'center_y':0.5}  # center align textfield
    size_hint_x: None  # input field size won't change w.r.t. screen resize
    width: 300  # constant width 300
"""

# list using Builder Method
list_build = """
Screen:
    ScrollView:
        MDList:
            id: container  # id to be used in case of Builder method
            # OneLineListItem:
            #     text: 'Item 1'
            # OneLineListItem:
            #     text: 'Item 2'
"""

# toolbar to bbe appeared at top of the screen
toolbar = """
Screen:
    BoxLayout:
        orientation: 'vertical'  # orientation of toolbar
        MDToolbar:
            title: 'MyApplication'  # title of toolbar
            left_action_items: [["menu", lambda x: app.navigation_draw()]]  # icon at left with response
            right_action_items: [["clock", lambda x: app.navigation_draw()]]  # icon at right with response
            elevation: 10  # generates shadow under toolbar
            
        MDLabel:  # displays a label on screen
            text: 'Hello, Label!'
            halign: 'center'  # aligns label at center of screen
            
        MDBottomAppBar:  # displays toolbar at bottom of the screen
            MDToolbar:
                # title: 'StatusBar'  # title of toolbar
                left_action_items: [["cup", lambda x: app.navigation_draw()]]  # icon at left with response
                mode: 'end'  # action_button modes :: 'end' ; 'free-end'
                type: 'bottom'  # elevates action_button
                icon: 'apple'  # icon of action_button
                on_action_button: app.navigation_draw()  # response of action_button
"""

# Flow of Navigation Drawer
# Screen -> NavigationLayout -> ScreenManager -> Screen -> BoxLayout -> MDToolbar + widget
# Screen -> NavigationLayout -> NavigationDrawer

navigation_drawer = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'  # orientation of toolbar
                    MDToolbar:
                        title: 'MyApplication'  # title of toolbar
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]  # toggle nav_draw
                        elevation: 10  # generates shadow under toolbar
                    Widget:
                        
        MDNavigationDrawer:
            id: nav_drawer  # when button is clicked, id:nav is called
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'favicon.png'  # image added to Navigation Drawer
                MDLabel:
                    text: '   Harsh Soni'
                    font_style: 'Subtitle1'
                    size_hint_y: None  # do not use automatic height
                    height: self.texture_size[1]
                MDLabel:
                    text: '    IG@hash.prog'
                    font_style: 'Caption'
                    size_hint_y: None  # do not use automatic height
                    height: self.texture_size[1]
                MDLabel:
                    text: '    gh@hashfx'
                    font_style: 'Caption'
                    size_hint_y: None  # do not use automatic height
                    height: self.texture_size[1]
                    
                ScrollView:  # aligns everything to top
                    MDList:  # list inside Navigation Drawer
                        TwoLineIconListItem:
                            text: 'hash.prog'
                            secondary_text: 'Instagram'
                            IconLeftWidget:
                                icon: 'instagram'
                        TwoLineIconListItem:
                            text: 'hashfx'
                            secondary_text: 'Github'
                            IconLeftWidget:
                                icon: 'github'
"""

switch_screen = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    SocialScreen:
    
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press: root.manager.current = 'profile'  # on_click: return ProfileScreen
    MDRectangleFlatButton:
        text: 'Social Profile'
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        on_press: root.manager.current = 'social'  # on_click: return SocialScreen
        
<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Welcome!'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'  # on_click: return MenuScreen
        
<SocialScreen>:
    name: 'social'
    MDLabel:
        text: 'Yeah boi, full SocialBaazi!'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        on_press: root.manager.current = 'menu'  # on_click: return MenuScreen
"""
