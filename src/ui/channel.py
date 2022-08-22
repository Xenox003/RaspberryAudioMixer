import gi
from gi.repository import Gtk, Gdk

from .meter import StereoMeter
from .meter import MonoMeter

class Channel(Gtk.Box):
    def __init__(self,name,stereo=True):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        
        self.set_size_request(100,340)
        
        self.stereo = stereo
        self.name = name
        
        # Name Label
        title = Gtk.Label(label=name)
        
        # Control Buttons
        button_mon = Gtk.ToggleButton(label="MON")
        button_mute = Gtk.ToggleButton(label="M")
        button_solo = Gtk.ToggleButton(label="S")
        
        hbox_m_s = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        hbox_m_s.add(button_mute)
        hbox_m_s.add(button_solo)
        
        # Fader + Meter
        if stereo:
            meter = StereoMeter()
        else:
            meter = MonoMeter()
        
        allocation = self.get_size_request()
        meter.set_size_request(allocation.width / 2,allocation.height)
        meter.set_values(0.5,0.3)
        
        slider_adjustment = Gtk.Adjustment(0,-60,12,1,10,0)
        slider = Gtk.Scale(orientation=Gtk.Orientation.VERTICAL, adjustment=slider_adjustment, inverted=True)
        #slider.set_draw_value(False)
        
        hbox_meter = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        hbox_meter.add(slider)
        hbox_meter.add(meter)
        
        # Main Component
        vbox_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        vbox_main.add(title)
        vbox_main.add(hbox_meter)
        vbox_main.add(hbox_m_s)
        vbox_main.add(button_mon)
        
        # Frame Component
        frame = Gtk.Frame()
        frame.add(vbox_main)
        
        self.add(frame)
        
            