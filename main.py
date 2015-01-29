# -*- coding:utf-8 -*-
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ListProperty, ObjectProperty,StringProperty
import einvoice

class MainScreen(Screen):
    result_text = StringProperty('')
    listdata = ListProperty()
    def loadcsv(self,filepath):
        print(filepath)
        self.data = einvoice.getInvoice(filepath)
        return self.data
    def savexls(self,filepath,data):
        print(filepath)
        einvoice.saveExcel(filepath,data)
    def change_result_text(self):
        self.listdata = self.data
        try:
            for i in self.data:
                for j in i:
                    print(j)
                #print('\n')
        except Exception as err:
            print(err)

        self.result_text = str(self.listdata)

class TableScreen(Screen):
    result_text = StringProperty('')

class EinvoiceApp(App):
    pass

if __name__ == "__main__":
   EinvoiceApp().run()