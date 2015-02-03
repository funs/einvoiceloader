# -*- coding:utf-8 -*-
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListView
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ListProperty, ObjectProperty,StringProperty
import kivy.resources
import einvoice



class MainScreen(Screen):
    #kivy.resources.resource_add_path('.')
    try:
        #p = kivy.resources.resource_find('/system/fonts/DroidSansFallback.ttf')
        p = kivy.resources.resource_find('/system/fonts/DroidSansFallback.ttf')
    except Exception as err:
        #p = kivy.resources.resource_find('DroidSansFallback.ttf')
        pass
    data = ListProperty([])
    result_text = StringProperty('')
    listdata = ListProperty([])


    def loadcsv(self,filepath):
        print(filepath)
        self.data = einvoice.getInvoice(filepath)
        return self.data
    '''
    def savexls(self,filepath,data):
        print(filepath)
        einvoice.saveExcel(filepath,data)
        '''
    def change_result_text(self):
        self.listdata = einvoice.setlist(self.data)


class TableScreen(Screen):
    #kivy.resources.resource_add_path('.')
    try:
        p = kivy.resources.resource_find('/system/fonts/DroidSansFallback.ttf')
    except Exception as err:
        pass

    result_text = StringProperty('')
    listdata = ListProperty()
    contentstring = StringProperty('')

class MyScreenManager(ScreenManager):
    contentstring = StringProperty('')
    data = ListProperty('')
    try:
        p = kivy.resources.resource_find('/system/fonts/DroidSansFallback.ttf')
    except Exception as err:
        pass

    def refresh_textinput(self,change):
        self.contentstring = einvoice.compare_content(self.data,change.text)
        print(self.contentstring)

class EinvoiceApp(App):
    def build(self):
        return MyScreenManager()

if __name__ == "__main__":
   EinvoiceApp().run()