import gi

from gi.repository import Gtk

from .mixer import InputMixer,OutputMixer

class ConfigurePage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        
        self.inputDevices = []
        self.outputDevices = []
        
        input_mixers = Gtk.VBox()
        output_mixers = Gtk.VBox()
        
        # Setup Input Devices Topbar
        input_topbar = Gtk.Frame()
        input_topbar_grid = Gtk.Grid()
        input_topbar_label = Gtk.Label(label="Input")
        input_topbar_add_button = Gtk.Button(label="Add")
        
        input_topbar_grid.set_border_width(6)
        
        input_topbar_label.set_hexpand(True)
        
        input_topbar_grid.add(input_topbar_label)
        input_topbar_grid.attach(input_topbar_add_button,2,0,1,1)
        
        input_topbar.add(input_topbar_grid)
        input_mixers.add(input_topbar)
        
        input_mixers.set_margin_bottom(25)
        
        # Setup Output Devices Topbar
        output_topbar = Gtk.Frame()
        output_topbar_grid = Gtk.Grid()
        output_topbar_label = Gtk.Label(label="Output")
        output_topbar_add_button = Gtk.Button(label="Add")
        
        output_topbar_grid.set_border_width(6)
        
        output_topbar_label.set_hexpand(True)
        
        output_topbar_grid.add(output_topbar_label)
        output_topbar_grid.attach(output_topbar_add_button,2,0,1,1)
        
        output_topbar.add(output_topbar_grid)
        output_mixers.add(output_topbar)
        
        # Handle audio devices
        #audio_sources = app.audio.manager.get_sources()
        #audio_sinks = app.audio.manager.get_sinks()
        
        input_mixers.add(InputMixer())
        input_mixers.add(InputMixer(stereo=False))
        
        self.add(input_mixers)
        self.add(output_mixers)