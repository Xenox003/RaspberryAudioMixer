## UDEV Configuration

The UDEV Config tells the Raspberry Pi how to rename specific audio and MIDI devices plugged into it.
It identifies and uniquely names the devices using they model and the USB port they are plugged into.


[10-soundcard-names.rules](udev/10-soundcard-names.rules) to be placed in /etc/udev/rules

[soundcard-name.sh](udev/soundcard-name.sh) to be placed in /root/udev

[midi-name.sh](udev/midi-name.sh) also to be placed in /root/udev


#### Examples

Interfaces of the Model "Behringer UCA222" get renamed to "uca222_(USB_Port)_(USB_SUB)"



#### Credits

Adapted from [Jackie](https://github.com/lukas2511/jackie) by [lukas2511](https://github.com/lukas2511)
