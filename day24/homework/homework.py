from kivy.app import app
from kivy.uix.button import button
from kivy.uibox.layout import boxlayout
from kivy.ui.label import label

class ANApp(app):
    def buitld(self):
      root_widget = boxlayout(orietation='verifical')
      output label  = label (size_hint_y =0.76,font_size=55)
      button_symbols =   ('1' , '2' , '3' , '4' , '5',
                      '6', '7' '8' , '9' ,'0',  , 
                         '+' , '-' ,':' , '=' , '/'   , )
                          
                     
 button_grid= GridLayout(cols=4 ,size_hint_y=2) 
for symbol in button_symbols:
           button_grid.add_widget(button (text=symbol ))
   clear_button(text='clear', size_hint_y=none,height=100)                      # type: ignore