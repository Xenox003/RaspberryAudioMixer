#from ui import window
import audio

def main():
    audio_manager = audio.manager.init()
    alsa_manager = audio.alsa.init()
    
    #window.init()
    
if __name__ == '__main__':
    main()