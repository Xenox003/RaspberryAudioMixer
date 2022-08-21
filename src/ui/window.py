import gi
import time
import random

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GLib

from .meter import MonoMeter

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_default_size(800,480)
        
        self.head_bar = Gtk.HeaderBar()
        self.head_bar.set_show_close_button(True)
        self.head_bar.props.title = "Raspberry Audio Mixer"
        self.set_titlebar(self.head_bar)
        
        self.page_container = Gtk.Stack()
        self.button_container = Gtk.Box()
        
        self.page_buttons = []
        self.pages = []
        
        self.add_page("mixer","Mixer")
        
        self.head_bar.pack_start(self.button_container)
        self.add(self.page_container)
        
        
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
         
    def handle_page_button_click(self,button):
        name = button.get_name()
        name = name[:-4]
        self.page_container.set_visible_child_name(name)
         
    def add_page(self,name,label):
        page_button = Gtk.Button()
        page_button.set_name("page-" + name + "-btn")
        page_button.set_label(label)
        
        page_button.connect("clicked",self.handle_page_button_click)
        
        self.page_buttons.append(page_button)
        self.button_container.add(page_button)
        
        page = Gtk.Box()
        page.set_name("page-" + name)
        page.set_visible(True)
        
        self.pages.append(page)
        self.page_container.add_named(page,"page-" + name)
        
        return page
            
        
        
        

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