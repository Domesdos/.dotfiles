#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}


#set wallpaper at startup
nitrogen --restore

#starting utility applications at boot time
# run nm-applet &
# run pamac-tray &
# run xfce4-power-manager &
# numlockx on &
# blueberry-tray &
picom --config $HOME/.config/qtile/scripts/picom.conf &
# /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &

#starting user applications at boot time
# run volumeicon &

#disable screensaver and power management
xset s noblank
xset s off
xset -dpms
