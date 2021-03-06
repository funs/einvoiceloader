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
from kivy.uix.scrollview import ScrollView
from kivy.properties import ListProperty, ObjectProperty,StringProperty
import kivy.resources
from einvoice import einvoice



class MainScreen(Screen):
    kivy.resources.resource_add_path('./src')
    p = kivy.resources.resource_find('DroidSansFallback.ttf')
    #data = []
    #result_text = ''
    #listdata = ListProperty([])


    def loadcsv(self,filepath):
        print(filepath)
        data = einvoice.getInvoice(filepath)
        return data
    '''
    def savexls(self,filepath,data):
        print(filepath)
        einvoice.saveExcel(filepath,data)
        '''
    def change_result_text(self,data):
        listdata = einvoice.setlist(data)
        return listdata

class TableScreen(Screen):
    kivy.resources.resource_add_path('./src')
    p = kivy.resources.resource_find('DroidSansFallback.ttf')

    result_text = StringProperty('')
    listdata = ListProperty()
    contentstring = StringProperty('')


class MyScreenManager(ScreenManager):
    kivy.resources.resource_add_path('./src')
    p = kivy.resources.resource_find('DroidSansFallback.ttf')

    #contentstring = StringProperty('')
    #data = ListProperty([])



class EinvoiceApp(App):
    #data = []
    #result_text = StringProperty('')
    listdata = ListProperty([])
    contentstring = StringProperty('')

    kivy.resources.resource_add_path('./src')
    p = kivy.resources.resource_find('DroidSansFallback.ttf')

    def refresh_textinput(self,change):
        self.contentstring = einvoice.compare_content(self.data,change.text)
        #print(self.contentstring)
        return self.contentstring

    def on_pause(self):
      # Here you can save data if needed
      return True

    def on_resume(self):
      # Here you can check if any data needs replacing (usually nothing)
      pass

    def build(self):
        return MyScreenManager()

if __name__ == "__main__":
   EinvoiceApp().run()