#!/bin/bash
if [ -z "$(groups $USER | grep sudo)" ]; then
	zenity --no-wrap --error --title="Install Thonny" --text="This user does not have administrative privilege"
	exit
fi
if [ `lsb_release -r -s` != "22.04" ]; then
	zenity --no-wrap --error --title="Install Thonny" --text="OS not supported"
	exit
fi
if [ ! -f /usr/bin/thonny417 ]; then
	sudo dpkg --configure -a
	sudo dpkg -i files/thonny417_4.1.7_amd64.deb
	zenity --no-wrap --info --title="Install Thonny" --text="<b>Thonny Installed</b>"
else
	zenity --no-wrap --info --title="Install Thonny" --text="Thonny already installed"
fi
