#! /bin/bash

# Get every wallpaper name in a list and get a random number
# to select a random wallpaper from the list
WALLPAPERS=$HOME"/Pictures/wallpapers"
ALIST=( `ls -w1 $WALLPAPERS` )
RANGE=${#ALIST[@]}
let "number = $RANDOM % $RANGE"

nitrogen --set-scaled --save $WALLPAPERS/${ALIST[$number]}
brightnessctl set 100% &
cbatticon -u 5 &
picom &
pcloud &
nm-applet &
discord &
