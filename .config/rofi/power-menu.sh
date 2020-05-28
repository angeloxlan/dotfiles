#!/usr/bin/env bash

# to edit themes in place with live reload:

# ag -l | entr -r $HOME/.config/rofi/on
# use -normal-window flag on rofi if you want to not have to close rofi to get
# back to your editor.
# https://www.reddit.com/r/qtools/comments/amswu9/autoloading_rofi_for_quick_themeing_experience/

options="     lock
    logout
     sleep
   hibernate
    reboot
   shutdown"
themes_dir=$HOME/.config/rofi
theme=${1:-$themes_dir/power-menu.rasi}
selection=$(echo -e "${options}" | rofi -dmenu -config $theme -columns 6 -lines 1 -width 1000)

case "${selection}" in
    "     lock")
        dm-tool lock;;
    "    logout")
        pkill qtile;;
    "     sleep")
        dm-tool lock && systemctl suspend;;
    "   hibernate")
        dm-tool lock && systemctl hibernate;;
    "    reboot")
        systemctl reboot;;
    "   shutdown")
        systemctl poweroff -i;;
esac

