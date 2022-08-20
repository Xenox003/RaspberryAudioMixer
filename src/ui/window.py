import gi
import time
import random

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GLib

import meter

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_default_size(800,480)
        
        self.head_bar = Gtk.HeaderBar()
        self.head_bar.set_show_close_button(True)
        self.head_bar.props.title = "Raspberry Audio Mixer"
        self.set_titlebar(self.head_bar)
        
        self.button_container = Gtk.Box()
        self.page_container = Gtk.Stack()
        
        button_container = Gtk.Box()
        
        button = Gtk.Button()
        button.set_label("Test")
        
        button2 = Gtk.Button()
        button2.set_label("Test2")
        
        button_container.add(button)
        button_container.add(button2)
        
        self.head_bar.pack_start(button_container)
        
        
        """
        self.hbox_main = Gtk.HBox()
        self.hbox_main.set_spacing(0)
        self.hbox_main.set_border_width(0)
        
        self.scroll_channels = Gtk.ScrolledWindow()
        self.scroll_channels.set_policy(Gtk.PolictyType.AUTOMATIC,Gtk.PolictyType.AUTOMATIC) 
        
        self.box_channels = Gtk.Box()
        self.box_channels.set_spacing(0)
        self.box_channels.set_border_width(0)
        
        self.box_outputs = Gtk.Box()
        self.box_outputs.set_spacing(0)
        self.box_outputs.set_border_width(0)
        
        
        meter1 = meter.MonoMeter()
        meter2 = meter.MonoMeter()
        meter3 = meter.MonoMeter()
        
        grid = Gtk.Grid(column_homogeneous=True,
                         column_spacing=10,
                         row_spacing=10)
        grid.set_hexpand(True)
        grid.set_vexpand(True)
        
        grid.add(meter1)
        grid.attach(meter2,1,0,2,1)
        grid.attach(meter3,2,0,2,1)
        
        self.add(grid)
        GLib.timeout_add(33,test,meter1)
        GLib.timeout_add(33,test,meter2)
        GLib.timeout_add(33,test,meter3)
        """
        
    def add_page(self,name):
        button = Gtk.Button()
        button.set_label(name)
        
        
        

def init():
    mainWindow = MainWindow()
    mainWindow.connect("destroy",Gtk.main_quit)
    mainWindow.show_all()

    Gtk.main()
      

switcher = True
def test(meter):
    global switcher
    
    if meter.value >= 1 and switcher == True:
        switcher = False
    elif meter.value <= 0 and switcher == False:
        switcher = True
        
    if switcher:
        meter.set_value(meter.value + 0.05)
    else:
        meter.set_value(meter.value - 0.05)
    
    return True
    
    
if __name__ == '__main__':
    init()