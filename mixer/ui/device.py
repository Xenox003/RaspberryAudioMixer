import gi

from gi.repository import Gtk

import app

class Device(Gtk.Frame):
    def __init__(self,channel1=None,channel2=None,channel=None,stereo=True):
        super().__init__()
        
        self.set_hexpand(True)
        
        self.name = "Device"
        self.stereo = stereo
        self.hardware = []
        
        if (self.stereo):
            # Use args channel1 and channel2 when stereo
            self.hardware.append(channel1)
            self.hardware.append(channel2)
        else:
            # Use args channel1 or channel when stereo
            if (channel1 != None):
                self.hardware.append(channel1)
            else:
                self.hardware.append(channel)
                
        grid = Gtk.Grid()
        grid.set_border_width(6)
        
        name_label = Gtk.Label(label="Device1")
        name_label.set_alignment(0,0.5)
        name_label.set_hexpand(True)
        
        """
        self.combo_box_1 = Gtk.ComboBox()
        self.combo_box_1.set_entry_text_column(1)
        self.combo_box_1.set_size_request(200,-1)
        renderer_text = Gtk.CellRendererText()
        self.combo_box_1.pack_start(renderer_text, True)
        self.combo_box_1.add_attribute(renderer_text, "text", 0)
        
        if self.stereo:
            self.combo_box_2 = Gtk.ComboBox()
            self.combo_box_2.set_entry_text_column(1)
            self.combo_box_2.set_size_request(200,-1)
            renderer_text = Gtk.CellRendererText()
            self.combo_box_2.pack_start(renderer_text, True)
            self.combo_box_2.add_attribute(renderer_text, "text", 0)
        
        grid.add(name_label)
        grid.attach(self.combo_box_1,2,0,1,1)
        if self.stereo:
            grid.attach(self.combo_box_2,3,0,1,1)
        """
        btn = Gtk.Button(label="Edit")
        btn.connect("clicked", self.on_button_clicked)
        grid.attach(btn,2,0,1,1)
        
        self.add(grid)
        
    def on_button_clicked(self,btn):
        dialog = EditDeviceDialog(app.ui.window.mainWindow,self)
        response = dialog.run()
        
        dialog.destroy()
        

class InputDevice(Device):
    def __init__(self,channel1=None,channel2=None,channel=None,stereo=True):
        super().__init__(stereo=stereo,channel1=channel1,channel2=channel2,channel=channel)
        
        self.sources_model = 
        
        #self.update_sources()
        
    
    def get_channel_model(self):
        channel_model = Gtk.ListStore(str)
        
        for source in app.audio_manager.get_sources():
            self.channel_model.append([source])
        
        return channel_model
    
        

class EditDeviceDialog(Gtk.Dialog):
    def __init__(self,parent,device):
        super().__init__(title="Edit Device", transient_for=parent, flags=0)
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )
        
        self.set_default_size(300, 200)
        self.set_border_width(6)
        
        vbox = Gtk.VBox()
        
        self.name_entry = Gtk.Entry()
        self.name_entry.set_text(device.name)
        self.name_entry.set_alignment(0.5)
        
        vbox.add(self.name_entry)
        
        self.combo_box_1 = Gtk.ComboBox()
        self.combo_box_1.set_entry_text_column(1)
        self.combo_box_1.set_size_request(200,-1)
        renderer_text = Gtk.CellRendererText()
        self.combo_box_1.pack_start(renderer_text, True)
        self.combo_box_1.add_attribute(renderer_text, "text", 0)
        self.combo_box_1.
        
        vbox.add(Gtk.Label(label="Channel 1"))
        vbox.add(self.combo_box_1)
        
        if device.stereo:
            self.combo_box_2 = Gtk.ComboBox()
            self.combo_box_2.set_entry_text_column(1)
            self.combo_box_2.set_size_request(200,-1)
            renderer_text = Gtk.CellRendererText()
            self.combo_box_2.pack_start(renderer_text, True)
            self.combo_box_2.add_attribute(renderer_text, "text", 0)
            
            vbox.add(Gtk.Label(label="Channel 2"))
            vbox.add(self.combo_box_2)
            
        self.get_content_area().add(vbox)
        self.show_all()