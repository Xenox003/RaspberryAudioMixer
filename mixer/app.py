import ui
import audio

audio_manager = None
alsa_manager = None

def main():
    global audio_manager
    global alsa_manager
    
    audio_manager = audio.manager.init()
    alsa_manager = audio.alsa.init()
    
    ui.window.init()
    
    
if __name__ == '__main__':
    main()