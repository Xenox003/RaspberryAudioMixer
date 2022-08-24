import gi

from gi.repository import Gtk

class Device(Gtk.Box):
    def __init__(self,channel1=None,channel2=None,channel=None,stereo=True):
        super().__init__()
        
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
                
        self.add(Gtk.Button(label="Test"))
        

class InputDevice(Device):
    def __init__(self,channel1=None,channel2=None,channel=None,stereo=True):
        super().__init__(stereo=stereo,channel1=channel1,channel2=channel2,channel=channel)
        
        