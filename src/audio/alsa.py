import os
import time
import subprocess
import threading

def init():
    return AlsaManager()

class AlsaManager():
    def __init__(self,ignore_unknown = True):
        self.running = True
        
        self.ignore_unknown = ignore_unknown
        
        self.inputs = []
        self.outputs = []
        
        self.outputs.append(AlsaOutput("Test-Out","hw:uca222_4"))
        self.inputs.append(AlsaInput("Test-In","hw:uca222_4"))
        
        self.run()
        
    def get_input_list(self):
        device_list = []
        
        devices = os.popen("arecord -l")
        device_string = devices.read()
        device_string = device_string.split("\n")
        for line in device_string:
            if (line.find("card") != -1):
                line_start = line.find("card")+8
                line_end = line.find("[")-1
                device_list.append("hw:" + line[line_start:line_end])
                
        return device_list
        
        
    def get_output_list(self):
        device_list = []
        
        devices = os.popen("aplay -l")
        device_string = devices.read()
        device_string = device_string.split("\n")
        for line in device_string:
            if (line.find("card") != -1):
                line_start = line.find("card")+8
                line_end = line.find("[")-1
                device_list.append("hw:" + line[line_start:line_end])
                
        return device_list
    
    
    def run(self):
        def target():
            while self.running:
                try:
                    input_list = self.get_input_list()
                    output_list = self.get_output_list()
                    
                    if self.ignore_unknown:
                        output_list = [x for x in output_list if not x.startswith("hw:unknown")]
                        input_list = [x for x in input_list if not x.startswith("hw:unknown")]
                    
                    
                    for out in output_list:
                        if (not any(x.device == out for x in self.outputs)):
                            self.outputs.append(AlsaOutput(out[3:] + "_out",out))
                            
                    for inp in input_list:
                        if (not any(x.device == inp for x in self.inputs)):
                            self.inputs.append(AlsaInput(inp[3:] + "_in",inp))
                    
                    
                    print(input_list)
                    print(output_list)
                    
                except:
                    print("Error handling ALSA")
                    traceback.print_exc()
                if self.running:
                    time.sleep(5)
        
        self.thread = threading.Thread(target=target)
        self.thread.start()
        
        
class AlsaInput():
    def __init__(self,name,device,nchannels=2, rate=48000, period=256, quality=None, extra_parms=None):
        self.name = name
        self.device = device
        self.nchannels = nchannels
        self.rate = rate
        self.period = period
        self.quality = quality
        self.extra_parms = extra_parms
        
        self.channels = []
        for i in range(self.nchannels):
            self.channels.append("%s:capture_%d" % (self.name, i+1))
            
        self.running = True
        self.run()
            
    def run(self):
        def target():
            while self.running:
                try:
                    self.process = subprocess.Popen(["zita-a2j", "-j", self.name, "-d", self.device, "-r", str(self.rate), "-p", str(self.period), "-c", str(self.nchannels)] + (["-Q", str(self.quality)] if self.quality else []), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    self.output, self.error = self.process.communicate()
                    self.status = self.process.returncode
                except:
                    self.error = traceback.format_exc()
                    self.status = -1
                for i in range(10):
                    if not self.running:
                        break
                    time.sleep(0.5)
            
        self.thread = threading.Thread(target=target)
        self.thread.start()
        
class AlsaOutput():
    def __init__(self,name,device,nchannels=2, rate=48000, period=256, quality=None, extra_parms=None):
        self.name = name
        self.device = device
        self.nchannels = nchannels
        self.rate = rate
        self.period = period
        self.quality = quality
        self.extra_parms = extra_parms
        
        self.channels = []
        for i in range(self.nchannels):
            self.channels.append("%s:playback_%d" % (self.name, i+1))
            
        self.running = True
        self.run()
            
    def run(self):
        def target():
            while self.running:
                try:
                    self.process = subprocess.Popen(["zita-j2a", "-j", self.name, "-d", self.device, "-r", str(self.rate), "-p", str(self.period), "-c", str(self.nchannels)] + (["-Q", str(self.quality)] if self.quality else []) + (self.extra_parms if self.extra_parms else []), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    self.output, self.error = self.process.communicate()
                    self.status = self.process.returncode
                except:
                    self.error = traceback.format_exc()
                    self.status = -1
                for i in range(10):
                    if not self.running:
                        break
                    time.sleep(0.5)
            
        self.thread = threading.Thread(target=target)
        self.thread.start()
        
        
if __name__ == '__main__':
    init()