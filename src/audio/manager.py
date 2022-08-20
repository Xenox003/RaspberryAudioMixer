import threading
import time
import jack
import os

def init():
    return AudioManager()


class AudioManager():
    def __init__(self):
        self.running = True
        
        self.connections = {}
        self.client = jack.Client("AudioManager")
        self.run()
        
    def get_sources(self):
        return list([x.name for x in self.client.get_ports(is_audio=True, is_output=True)])

    def get_sinks(self):
        return list([x.name for x in self.client.get_ports(is_audio=True, is_input=True)])
    
    def connect(self,source,sink):
        if source not in self.connections:
            self.connections[source] = []
        if sink not in self.connections[source]:
            self.connections[source].append(sink)
            return True
        return False
    
    def disconnect(self,source,sink):
        if source not in self.connections:
            return
        if sink in self.connections[source]:
            self.connections[source].remove(sink)
        
    def run(self):
        def target():
            while self.running:
                try:
                    #self.ensure_connections()
                    print(self.get_sources())
                    print(self.get_sinks())
                except:
                    print("Error handling connections")
                    traceback.print_exc()
                if self.running:
                    time.sleep(1)
        
        self.thread = threading.Thread(target=target)
        self.thread.start()


if __name__ == '__main__':
    init()