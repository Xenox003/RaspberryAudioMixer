import gi
import time
import random

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GLib

from .header_bar import HeaderBar

from .meter import MonoMeter
from .meter import StereoMeter

from .channel import Channel

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_default_size(800,480)
        
        self.page_container = Gtk.Stack()
        self.button_container = Gtk.Box()
        
        self.page_buttons = []
        self.pages = []
        
        
        mixer_page = self.add_page("mixer","Mixer")
        #meter1 = StereoMeter()
        #meter1.set_size_request(50,100)
        #GLib.timeout_add(33,test,meter1)
        
        channel1 = Channel(name="Test")
        
        mixer_page.add(channel1)
        
        devices_page = self.add_page("devices","Devices",Gtk.Button(label="Test"))
        settings_page = self.add_page("settings","System Settings")
        
        # Create box for Custom Header Bar in Fullscreen
        # (Header bar gets added to box in fullscreen mode so it's still accessable)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.add(self.page_container)
        self.add(box)
        
        # Custom Header Bar Implementation
        self.head_bar = HeaderBar(self,title="Raspberry Audio Mixer")
        self.head_bar.pack_start(self.button_container)
        self.set_titlebar(self.head_bar)
        
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
        button_name = button.get_name()
        page_name = button_name[:-4]
        self.page_container.set_visible_child_name(page_name)
        
         
    def add_page(self,name,label,page_widget=None):
        page_button = Gtk.Button()
        page_button.set_name("page-" + name + "-btn")
        page_button.set_label(label)
        
        page_button.connect("clicked",self.handle_page_button_click)
        
        self.page_buttons.append(page_button)
        self.button_container.add(page_button)
        
        if page_widget:
            page = page_widget
        else:
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
    
    if meter.l_value >= 1 and switcher == True:
        switcher = False
    elif meter.l_value <= 0 and switcher == False:
        switcher = True
        
    if switcher:
        meter.set_values(meter.l_value + 0.05,meter.r_value + 0.05)
    else:
        meter.set_values(meter.l_value - 0.05,meter.r_value - 0.05)
    
    return True
    
    
if __name__ == '__main__':
    init()