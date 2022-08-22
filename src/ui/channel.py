import gi
from gi.repository import Gtk, Gdk

from .meter import StereoMeter
from .meter import MonoMeter

class Channel(Gtk.Box):
    def __init__(self,name,stereo=True):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        
        self.set_size_request(100,480)
        
        self.stereo = stereo
        self.name = name
        
        # Fader + Meter
        if stereo:
            meter = StereoMeter()
        else:
            meter = MonoMeter()
         
        allocation = self.get_size_request()
        meter.set_size_request(allocation.width / 2,allocation.height)
        
        self.add(meter)
        
            