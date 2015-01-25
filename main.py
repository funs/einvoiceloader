# -*- coding:utf-8 -*-
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ListProperty, ObjectProperty
import einvoice

class MainWidget(Screen):
    def loadcsv(self,filepath):
        print(filepath)
        self.data = einvoice.getInvoice(filepath)
        return self.data
    def savexls(self,filepath,data):
        print(filepath)
        einvoice.saveExcel(filepath,data)
class TableWidget(Screen):
        def showresult(self):
            print(self.data)
class MyScreenManager(ScreenManager):
    pass

class EinvoiceApp(App):
    def build(self):
        return MyScreenManager()

if __name__ == "__main__":
   EinvoiceApp().run()