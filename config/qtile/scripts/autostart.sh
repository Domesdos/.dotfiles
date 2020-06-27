#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}


#set wallpaper at startup
nitrogen --restore

picom --config $HOME/.config/qtile/scripts/picom.conf &
# /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &

#disable screensaver and power management
xset s noblank
xset s off
xset -dpms

#set monitor refreshrate to 144hz
xrandr -r 144
