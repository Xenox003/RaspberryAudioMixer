import gi
from gi.repository import Gtk, Gdk

class Channel(Gtk.Box):
    def __init__(self,name,stereo=True):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        
        self.stereo = stereo
        self.name = name