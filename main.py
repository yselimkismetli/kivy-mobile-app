from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3
from kivymd.app import MDApp
from kivy.properties import ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "test.db")

kv = '''

BoxLayout:
    orientation: 'vertical'
    MDToolbar:
        id: toolbar
        elevation: 10
        title: "Sportable"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        ScreenManager:
            id: screen_manager
            HomeScreen:
                id: home
                name: 'home'
            FBScreen:
                id: fb
                name: 'fb'
            BBScreen:
                id: bb
                name: 'bb'
            VBScreen:
                id: vb
                name: 'vb'
            TScreen:
                id: ts
                name: 'ts'
            NScreen:
                id: news
                name: 'news'
                
        MDNavigationDrawer:
            id: nav_drawer
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: "Home Page"
                        on_press:
                            nav_drawer.set_state("close")
                            screen_manager.current = "home"
                        IconLeftWidget:
                            icon: "home-outline"
                    OneLineIconListItem:
                        text: "Football"
                        on_press:
                            nav_drawer.set_state("close")
                            screen_manager.current = "fb"
                        IconLeftWidget:
                            icon: "soccer"
                    OneLineIconListItem:
                        text: "Basketball"
                        on_press:
                            nav_drawer.set_state("close")
                            screen_manager.current = "bb"
                        IconLeftWidget:
                            icon: "basketball"
                    OneLineIconListItem:
                        text: "Volleyball"
                        on_press:
                            nav_drawer.set_state("close")
                            screen_manager.current = "vb"
                        IconLeftWidget:
                            icon: "volleyball"
                    OneLineIconListItem:
                        text: "Tennis"
                        on_press:
                            nav_drawer.set_state("close")
                            screen_manager.current = "ts"
                        IconLeftWidget:
                            icon: "tennis"
                    OneLineIconListItem:
                        text: "News"
                        on_press:
                            nav_drawer.set_state("close")
                            screen_manager.current = "news"
                        IconLeftWidget:
                            icon: "newspaper-variant-multiple"

<HomeScreen>:
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "700dp", "200dp"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            text: "Sportable application is a mobile application where you can follow the standings about sports such as football, basketball, volleyball and tennis, as well as read sports news."
            theme_text_color: "Secondary"
            size_hint_y: None
            height: "50dp"

        MDSeparator:
            height: "1dp"

<BBData>:
    canvas:
        Color:
            rgb: .3, .3, .3
        Line:
            width: 2
            rectangle: (*self.pos, *self.size)
    size_hint_y: None
    height: 48
    Label:
        text: root.bbPos
        color: 1, 0, 0, 1
    Label:
        text: root.bbName
        color: 1, 0, 0, 1
    Label:
        text: root.bbW
        color: 1, 0, 0, 1
    Label:
        text: root.bbL
        color: 1, 0, 0, 1
    Label:
        text: root.bbAV
        color: 1, 0, 0, 1
    Label:
        text: root.bbP
        color: 1, 0, 0, 1

<BBScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            size_hint_y: None
            height: 48
            text: 'Data List in a Scrollview Example'
        BoxLayout:  # Headings for 
            size_hint_y: None
            height: 28
            Label:
                text: 'Rank'
                color: 1, 0, 0, 1
            Label:
                text: 'Team'
                color: 1, 0, 0, 1
            Label:
                text: 'W'
                color: 1, 0, 0, 1
            Label:
                text: 'L'
                color: 1, 0, 0, 1
            Label:
                text: 'Average'
                color: 1, 0, 0, 3
            Label:
                text: 'Point'
                color: 1, 0, 0, 1
        ScrollView:
            do_scroll_y: True
            bar_width: dp(10)
            scroll_type: ['bars','content']
            BoxLayout:
                orientation: 'vertical'
                id:scroll_box
                size_hint_y: None
                height: self.minimum_height

<FBData>:
    canvas:
        Color:
            rgb: .3, .3, .3
        Line:
            width: 2
            rectangle: (*self.pos, *self.size)
    size_hint_y: None
    height: 48
    Label:
        text: root.fbPos
        color: 1, 0, 0, 1
    Label:
        text: root.fbName
        color: 1, 0, 0, 1
    Label:
        text: root.fbW
        color: 1, 0, 0, 1
    Label:
        text: root.fbL
        color: 1, 0, 0, 1
    Label:
        text: root.fbD
        color: 1, 0, 0, 1
    Label:
        text: root.fbP
        color: 1, 0, 0, 1


<FBScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            size_hint_y: None
            height: 48
            text: 'Data List in a Scrollview Example'
        BoxLayout:  # Headings for 
            size_hint_y: None
            height: 28
            Label:
                text: 'Rank'
                color: 1, 0, 0, 1
            Label:
                text: 'Team'
                color: 1, 0, 0, 1
            Label:
                text: 'W'
                color: 1, 0, 0, 1
            Label:
                text: 'L'
                color: 1, 0, 0, 1
            Label:
                text: 'D'
                color: 1, 0, 0, 1
            Label:
                text: 'Point'
                color: 1, 0, 0, 1
        ScrollView:
            do_scroll_y: True
            bar_width: dp(10)
            scroll_type: ['bars','content']
            BoxLayout:
                orientation: 'vertical'
                id:scroll_box
                size_hint_y: None
                height: self.minimum_height

<VBData>:
    canvas:
        Color:
            rgb: .3, .3, .3
        Line:
            width: 2
            rectangle: (*self.pos, *self.size)
    size_hint_y: None
    height: 48
    Label:
        text: root.vbPos
        color: 1, 0, 0, 1
    Label:
        text: root.vbName
        color: 1, 0, 0, 1
    Label:
        text: root.vbW
        color: 1, 0, 0, 1
    Label:
        text: root.vbL
        color: 1, 0, 0, 1
    Label:
        text: root.vbAV
        color: 1, 0, 0, 1
    Label:
        text: root.vbP
        color: 1, 0, 0, 1

<VBScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            size_hint_y: None
            height: 48
            text: 'Data List in a Scrollview Example'
        BoxLayout:  # Headings for 
            size_hint_y: None
            height: 28
            Label:
                text: 'Rank'
                color: 1, 0, 0, 1
            Label:
                text: 'Team'
                color: 1, 0, 0, 1
            Label:
                text: 'W'
                color: 1, 0, 0, 1
            Label:
                text: 'L'
                color: 1, 0, 0, 1
            Label:
                text: 'Average'
                color: 1, 0, 0, 1
            Label:
                text: 'Point'
                color: 1, 0, 0, 1
        ScrollView:
            do_scroll_y: True
            bar_width: dp(10)
            scroll_type: ['bars','content']
            BoxLayout:
                orientation: 'vertical'
                id:scroll_box
                size_hint_y: None
                height: self.minimum_height

<TData>:
    canvas:
        Color:
            rgb: .3, .3, .3
        Line:
            width: 2
            rectangle: (*self.pos, *self.size)
    size_hint_y: None
    height: 48
    Label:
        text: root.tPos
        color: 1, 0, 0, 1
    Label:
        text: root.tName
        color: 1, 0, 0, 1
    Label:
        text: root.tP
        color: 1, 0, 0, 1

<TScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            size_hint_y: None
            height: 48
            text: 'Data List in a Scrollview Example'
        BoxLayout:  # Headings for 
            size_hint_y: None
            height: 28
            Label:
                text: 'Rank'
                color: 1, 0, 0, 1
            Label:
                text: 'Player'
                color: 1, 0, 0, 1
            Label:
                text: 'Point'
                color: 1, 0, 0, 1
        ScrollView:
            do_scroll_y: True
            bar_width: dp(10)
            scroll_type: ['bars','content']
            BoxLayout:
                orientation: 'vertical'
                id:scroll_box
                size_hint_y: None
                height: self.minimum_height


<InfoCard>:

    orientation: "vertical"
    padding: "8dp"
    size_hint: None, None
    size: "300dp", "180dp"
    pos_hint: {"center_x": .5, "center_y": .5}

    MDLabel:
        text: root.title
        theme_text_color: "Secondary"
        size_hint_y: None
        height: self.texture_size[1]

    MDSeparator:
        height: "1dp"

    MDLabel:
        text: root.content
        theme_text_color: "Secondary"

<NScreen>:
    on_pre_enter: self.set_title()
    ScrollView:
        do_scroll_x: True
        do_scroll_y: False
        scroll_type: ['bars', 'content']
        bar_width: '10dp'
        BoxLayout:
            padding: '20dp'
            spacing: '20dp'
            id: card_box
            width: self.minimum_width
            size_hint_x: None

'''


class HomeScreen(Screen):
    pass

class BBData(BoxLayout):
    bbName = StringProperty()
    bbPos = StringProperty()
    bbW = StringProperty()
    bbL = StringProperty()
    bbAV = StringProperty()
    bbP = StringProperty()
   
class BBScreen(Screen):
    def on_kv_post(self, base_widget):
        with sqlite3.connect(db_path) as db:
            cur = db.cursor()
            cur.execute("SELECT * FROM Basketbol ORDER BY sira ASC")
            table = cur.fetchall()
            cur.close()

        for line in table:

            pos, name, win, lose, average, point = line
            w = BBData(bbPos=str(pos), bbName=name, bbW=str(win), bbL=str(lose), bbAV=str(average), bbP=str(point))
            self.ids.scroll_box.add_widget(w)

class FBData(BoxLayout):
    fbName = StringProperty()
    fbPos = StringProperty()
    fbW = StringProperty()
    fbL = StringProperty()
    fbD = StringProperty()
    fbP = StringProperty()
   

class FBScreen(Screen):
    def on_kv_post(self, base_widget):
        with sqlite3.connect(db_path) as db:
            cur = db.cursor()
            cur.execute("SELECT * FROM Futbol ORDER BY sira ASC")
            table = cur.fetchall()
            cur.close()

        for line in table:

            pos, name, win, lose, draw, point = line
            w = FBData(fbPos=str(pos), fbName=name, fbW=str(win), fbL=str(lose), fbD=str(draw), fbP=str(point))
            self.ids.scroll_box.add_widget(w)

class VBData(BoxLayout):
    vbName = StringProperty()
    vbPos = StringProperty()
    vbW = StringProperty()
    vbL = StringProperty()
    vbAV = StringProperty()
    vbP = StringProperty()
   
class VBScreen(Screen):
    def on_kv_post(self, base_widget):
        with sqlite3.connect(db_path) as db:
            cur = db.cursor()
            cur.execute("SELECT * FROM Voleybol ORDER BY sira ASC")
            table = cur.fetchall()
            cur.close()

        for line in table:

            pos, name, win, lose, average, point = line
            w = VBData(vbPos=str(pos), vbName=name, vbW=str(win), vbL=str(lose), vbAV=str(average), vbP=str(point))
            self.ids.scroll_box.add_widget(w)

class TData(BoxLayout):
    tPos = StringProperty()
    tName = StringProperty()
    tP = StringProperty()

class TScreen(Screen):
    def on_kv_post(self, base_widget):
        with sqlite3.connect(db_path) as db:
            cur = db.cursor()
            cur.execute("SELECT * FROM Tenis ORDER BY sira ASC")
            table = cur.fetchall()
            cur.close()

        for line in table:

            pos, name, point = line
            w = TData(tPos=str(pos), tName=name, tP=str(point))
            self.ids.scroll_box.add_widget(w)

class InfoCard(MDCard):

    title = StringProperty()
    content = StringProperty()

class NScreen(Screen):

    def set_title(self):
        with sqlite3.connect(db_path) as db:
            cur = db.cursor()
            cur.execute("SELECT * FROM Haberler")
            table = cur.fetchall()
            cur.close()

        for line in table:
            id, baslik, icerik = line
            self.ids.card_box.add_widget(InfoCard(title=baslik, content=icerik))

class ScrManage(ScreenManager):
    pass


class Sportable(MDApp):
    def build(self):
        return Builder.load_string(kv)


Sportable().run() 