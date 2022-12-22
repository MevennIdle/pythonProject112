from kivymd.app import MDApp
from kivy.lang.builder import Builder

kv = '''
<MySwiper@MDSwiperItem>

    FitImage:
        source: "image/x.jpg"  
        radius: [20,]
    FitImage:
        source: "image/y.jpg"
        radius: [20,]
    FitImage:
        source: "image/z.jpg"
        radius: [20,]



MDScreen:

    MDTopAppBar:
        id: toolbar
        title: "MDSwiper"
        elevation: 4
        pos_hint: {"top": 1}

    MDSwiper:
        size_hint_y: None
        height: root.height - toolbar.height - dp(40)
        y: root.height - self.height - toolbar.height - dp(20)

        MySwiper:
        MySwiper:

        MySwiper:

        MySwiper:

        MySwiper:
'''


class Main(MDApp):
    def build(self):
        return Builder.load_string(kv)

Main().run()