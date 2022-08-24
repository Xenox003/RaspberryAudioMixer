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
        self.ignores = []
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
        
    def update_connections(self):
        ports = {}
        connections = {}
        
        for port in self.client.get_ports(is_audio=True):
            ports[port.name] = port
            connections[port.name] = list(c.name for c in self.client.get_all_connections(port))
            
        for sink in self.get_sinks():
            del connections[sink]
            
        for source, sinks in connections.items():
            for sink in sinks:
                if source not in self.connections or sink not in self.connections[source]:
                    if any([ign('source',source) or ign('sink', sink) for ign in self.ignores]):
                        continue
                    self.client.disconnect(source,sink)
                    
        for source, sinks in self.connections.items():
            for sink in sinks:
                skip = False

                if sink not in ports:
                    skip=True

                if source not in ports:
                    skip=True

                if not skip and sink not in connections[source]:
                    print("Connecting '%s' and '%s'" % (source, sink))
                    self.client.connect(source, sink)
        
    def run(self):
        def target():
            while self.running:
                try:
                    self.update_connections()
                except:
                    print("Error handling connections")
                    traceback.print_exc()
                if self.running:
                    time.sleep(1)
        
        self.thread = threading.Thread(target=target)
        self.thread.start()


if __name__ == '__main__':
    init()