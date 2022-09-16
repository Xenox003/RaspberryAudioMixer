# This module represents the Mixer Edit component in the Configure Section

import gi

from gi.repository import Gtk

import app

class Mixer(Gtk.Frame):
    def __init__(self,stereo=True):
        super().__init__()
        
        self.set_hexpand(True)
        
        self.name = "Mixer"
        self.stereo = stereo
        self.channels = [None] * 2
                
        grid = Gtk.Grid()
        grid.set_border_width(6)
        
        self.name_label = Gtk.Label()
        self.name_label.set_alignment(0,0.5)
        self.name_label.set_hexpand(True)
        grid.add(self.name_label)
        
        self.channel_1_label = Gtk.Label(label="Ch1")
        self.channel_1_label.set_alignment(0.5,0.5)
        self.channel_1_label.set_margin_right(10)
        grid.attach(self.channel_1_label,2,0,1,1)
        
        if self.stereo:
            self.channel_2_label = Gtk.Label(label="Ch2")
            self.channel_2_label.set_alignment(0.5,0.5)
            self.channel_2_label.set_margin_right(10)
            grid.attach(self.channel_2_label,3,0,1,1)
        
        btn = Gtk.Button(label="Edit")
        btn.connect("clicked", self.on_edit_button_clicked)
        grid.attach(btn,4,0,1,1)
        
        self.add(grid)
        
        self.update_ui()
    
    def update_ui(self):
        self.name_label.set_label(self.name)
        self.channel_1_label.set_label(str(self.channels[0] or "N/A"))
        
        if self.stereo:
            self.channel_2_label.set_label(str(self.channels[1] or "N/A"))
    
    def update_channels(self,index,device):
        self.channels[index] = device
    
    def on_edit_button_clicked(self,btn):
        dialog = EditMixerDialog(app.ui.window.mainWindow,self)
        response = dialog.run()
        
        self.name = dialog.name_entry.get_text()
        
        box_1_model = dialog.combo_box_1.get_model()
        box_1_index = dialog.combo_box_1.get_active()
        if box_1_index != -1:
            box_1_selected = box_1_model[box_1_index][0]
            self.update_channels(0,box_1_selected)
            
        
        if self.stereo:
            box_2_model = dialog.combo_box_2.get_model()
            box_2_index = dialog.combo_box_2.get_active()
            if box_2_index != -1:
                box_2_selected = box_2_model[box_1_index][0]
                self.update_channels(1,box_2_selected)
        
        self.update_ui()
        dialog.destroy()
        

class InputMixer(Mixer):
    def __init__(self,stereo=True):
        super().__init__(stereo=stereo)
        
    
    def get_channel_model(self):
        channel_model = Gtk.ListStore(str)
        
        for source in app.audio_manager.get_sources():
            channel_model.append([source])
        
        return channel_model

class OutputMixer(Mixer):
    def __init__(self,stereo=True):
        super().__init__(stereo=stereo)
        
    
    def get_channel_model(self):
        channel_model = Gtk.ListStore(str)
        
        for source in app.audio_manager.get_sinks():
            channel_model.append([source])
        
        return channel_model
        

class EditMixerDialog(Gtk.Dialog):
    def __init__(self,parent,device):
        super().__init__(title="Edit Mixer", transient_for=parent, flags=0)
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )
        
        self.set_default_size(300, 220)
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
        self.combo_box_1.set_model(device.get_channel_model())
        
        
        vbox.add(Gtk.Label(label="Channel 1"))
        vbox.add(self.combo_box_1)
        
        if device.stereo:
            self.combo_box_2 = Gtk.ComboBox()
            self.combo_box_2.set_entry_text_column(1)
            self.combo_box_2.set_size_request(200,-1)
            renderer_text = Gtk.CellRendererText()
            self.combo_box_2.pack_start(renderer_text, True)
            self.combo_box_2.add_attribute(renderer_text, "text", 0)
            self.combo_box_2.set_model(device.get_channel_model())
            
            vbox.add(Gtk.Label(label="Channel 2"))
            vbox.add(self.combo_box_2)
            
        self.get_content_area().add(vbox)
        self.show_all()