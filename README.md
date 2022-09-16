# RaspberryAudioMixer

Raspberry Audio Mixer is a collection of programs and scripts which turn a Raspberry PI 4 together with some audio interfaces into a audio mixing console

## Software
The system consists of 3 main parts:

- Python APP
- UDEV Configuration
- Volume Control App

#### Python APP
This piece of code is the main brain behind the system, it acts as an controller for the JACK Audio Server and connects all the pieces together.

#### UDEV Configuration
The UDEV Configuration is a script that renames audio interfaces so they get named the same every time. The audio devices get identified by the port on the PI they are plugged in to
This configuration is able to handle interfaces like the Behringer UCA 222 or the Rode NT-USB

#### Volume Control App
...


## Diagram
![RaspberryAudioMixerSoftware drawio](https://user-images.githubusercontent.com/68594244/187948941-c31ea6c9-11b6-478f-892b-78d0ab960859.png)


## Utilities
The system uses some publicly availible software to be able to run correctly:

- Jack Audio Server
- Zita


# Inspiration
This project was inspired by:

- [Jackie](https://github.com/lukas2511/jackie) by [lukas2511](https://github.com/lukas2511)
- [jack_mixer](https://github.com/jack-mixer/jack_mixer)

In addition this project makes use of:

- [Custom Header Bar](https://gist.github.com/KurtJacobson/6b045b6fc38907a2f18c38f6de2929e3) by [Kurt Jacobson](https://gist.github.com/KurtJacobson)
