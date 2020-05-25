# Qtile window manager (http://www.qtile.org)     
# Custom configuration by Angel Aguirre (http://www.instagram.com/angelo.lla/)
#
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

##### IMPORTS #####
import os
import re
import socket
import subprocess
import psutil
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401

##### DEFINING SOME VARIABLES #####
mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                                    # My terminal of choice
myConfig = "/home/angel/.config/qtile/config.py"    # The Qtile config file location
home = os.path.expanduser('~')

##### KEYBINDINGS #####
keys = [
         ### The essentials
         Key(
             [mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches Terminal'
             ),
         Key(
             [mod, "shift"], "Return",
             lazy.spawn("rofi -show combi"),
             desc='Rofi Run Launcher'
             ),
         Key(
             [mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key(
             [mod, "shift"], "c",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key(
             [mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key(
             [mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdowqn Qtile'
             ),
         Key(
             [mod], "Escape",
             lazy.spawn(home + "/.config/rofi/power-menu.sh"),
             desc='Show power menu'
             ),

         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),

         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),

         ### Treetab controls
         Key([mod, "control"], "k",
             lazy.layout.section_up(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "control"], "j",
             lazy.layout.section_down(),
             desc='Move down a section in treetab'
             ),

         ### Window controls
         Key(
             [mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key(
             [mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key(
             [mod], "h",
             lazy.layout.left(),
             desc='Move focus left in current stack pane'
             ),
         Key(
             [mod], "l",
             lazy.layout.right(),
             desc='Move focus right in current satck pane'
             ),
         Key(
             [mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),
         Key(
             [mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),
         Key(
             [mod], "u",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key(
             [mod], "i",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key(
             [mod, "shift"], "h",
             lazy.layout.shuffle_left(),
             desc='Move window to the left in current stack'
             ),
         Key(
             [mod, "shift"], "l",
             lazy.layout.shuffle_right(),
             desc='Move window to the right in current stack'
            ),
         Key(
             [mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key(
             [mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key(
             [mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),

         ### Stack controls
         Key(
             [mod, "shift"], "space",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
         Key(
             [mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key(
             [mod, "control"], "Return",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),

	 ### Applications
	 Key(
             [mod], "b",
             lazy.spawn("firefox"),
             desc='Luch firefox browser'
             ),
	 Key(
             [mod], "f",
             lazy.spawn("thunar"),
             desc='Open the file manager: Thunar'
             ),
	 Key(
             [mod], "r",
             lazy.spawn("alacritty -e ranger"),
             desc='Open the file manager: Ranger'
             ),

	 ### Volume Controls
	 Key(
	     [], "XF86AudioLowerVolume",
             lazy.spawn("/usr/bin/pulseaudio-ctl down -5"),
             desc='Decrease the volume with phisical buttons'
             ),
	 Key(
	     [], "XF86AudioRaiseVolume",
             lazy.spawn("/usr/bin/pulseaudio-ctl up -5"),
             desc='Increase the volume with phisical buttons'
             ),
	 Key(
	     [], "XF86AudioMute",
             lazy.spawn("/usr/bin/pulseaudio-ctl mute"),
             desc='Toggle mute/unmute phisical button'
             ),
	 Key(
	     [mod, "mod1"], "h",
	     lazy.spawn("pacmd set-card-profile 0 output:hdmi-stereo"),
	     desc='Change audio output to HDMI'
	     ),
	 Key(
	     [mod, "mod1"], "a",
	     lazy.spawn("pacmd set-card-profile 0 output:analog-stereo"),
	     desc='Change audio output to Analog-Stereo'
	     ),

	 ### Brightness Controls
	 Key(
	     [], "XF86MonBrightnessUp",
             lazy.spawn("brightnessctl set +10%"),
             desc='Increase the brightness of the screen: Laptop'
             ),
	 Key(
	     [], "XF86MonBrightnessDown",
             lazy.spawn("brightnessctl set 10%-"),
             desc='Decrease the brightness of the screen: Laptop'
             ),
]

##### GROUPS #####
group_names = [("WWW", {'layout': 'monadtall'}),
               ("WWW2", {'layout': 'monadtall'}),
               ("DEV", {'layout': 'monadtall'}),
               ("DEV2", {'layout': 'max'}),
               ("TERM", {'layout': 'bsp'}),
               ("DOCS", {'layout': 'monadtall'}),
               ("ALT1", {'layout': 'monadtall'}),
               ("ALT2", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group	

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "ff5555",
                "border_normal": "2a292c"
                }

##### THE LAYOUTS #####
layouts = [
    #layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    #layout.Stack(num_stacks=2),
    #layout.TreeTab(
     #    font = "Ubuntu",
     #    fontsize = 10,
     #    sections = ["FIRST", "SECOND"],
     #    section_fontsize = 11,
     #    bg_color = "141414",
     #    active_bg = "90C435",
     #    active_fg = "000000",
     #    inactive_bg = "384323",
     #    inactive_fg = "a0a0a0",
     #    padding_y = 5,
     #    section_top = 10,
     #    panel_width = 320
     #    ),
     layout.Floating(**layout_theme),
]

##### COLORS #####
colors = {
		"panel_bg"		:["#2a292c", "#2a292c"], 	# panel background
         	"current_tab_bg"	:["#ff5555", "#ff5555"], 	# background for current screen tab
         	"font_dark"		:["#2a292c", "#2a292c"], 	# font color for widgets
		"font_white"		:["#ffffff", "#ffffff"],	# font color for group names
         	"current_border"	:["#ff5555", "#ff5555"], 	# border line color for current tab
		"clock"			:["#ff5555", "#ff5555"], 	# color for Clock and Date widget
		"layout"		:["#7bcfc4", "#7bcfc4"], 	# color for Layout Type widget
		"pacman"		:["#e3f5a3", "#e3f5a3"], 	# color for the Thermal Sensors widget
		"net"			:["#f0ec74", "#f0ec74"], 	# color for the Volume widget
		"volume"		:["#9996c6", "#9996c6"], 	# color for the Net widget
		"memory"		:["#db9356", "#db9356"], 	# color for the Memory widget
		"sensors"		:["#fc9083", "#fc9083"], 	# color for the Pacman widget
		"battery"		:["#98bae5", "#98bae5"], 	# color for the Bettery widget
         	"screen_border"		:["#ff5555", "#ff5555"], 	# border line color for windows
         	"even_widget"		:["#668bd7", "#668bd7"], 	# color for the even widgets
         	"window_name"		:["#ff5555", "#ff5555"]  	# window name
	  }

##### PROMPT #####
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 12,
    padding = 2,
    background=colors["font_white"]
)
extension_defaults = widget_defaults.copy()

##### WIDGETS #####

def init_widgets_list():
    widgets_list = [
               widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors["font_dark"],
                        background = colors["panel_bg"]
                        ),
               widget.TextBox(
                        text='[',
                        foreground = colors["font_white"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.GroupBox(font="Ubuntu Bold",
                        fontsize = 9,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 2,
                        borderwidth = 3,
                        active = colors["font_white"],
                        inactive = colors["font_white"],
                        rounded = False,
                        highlight_color = colors["current_tab_bg"],
                        highlight_method = "line",
                        this_current_screen_border = colors["current_border"],
                        this_screen_border = colors ["screen_border"],
                        other_current_screen_border = colors["panel_bg"],
                        other_screen_border = colors["panel_bg"],
                        foreground = colors["font_white"],
                        background = colors["panel_bg"]
                        ),
               widget.TextBox(
                        text=']',
                        foreground = colors["font_white"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.TextBox(
                        text='[',
                        foreground = colors["window_name"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.WindowName(
                        foreground = colors["window_name"],
                        background = colors["panel_bg"],
                        padding = 0
                        ),
               widget.TextBox(
                        text=']',
                        foreground = colors["window_name"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.TextBox(
                        text='[',
                        foreground = colors["pacman"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.Pacman(
                        execute = "alacritty",
                        update_interval = 1800,
                        foreground = colors["pacman"],
                        background = colors["panel_bg"]
                        ),
               widget.TextBox(
                        text="Updates",
                        padding = 5,
                        foreground=colors["pacman"],
                        background=colors["panel_bg"]
                        ),
               widget.TextBox(
                        text=']',
                        foreground = colors["pacman"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.TextBox(
                        text='[',
                        foreground = colors["memory"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.Memory(
                        foreground = colors["memory"],
                        background = colors["panel_bg"],
                        padding = 5
                        ),
               widget.TextBox(
                        text=']',
                        foreground = colors["memory"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.TextBox(
                        text='[',
                        foreground = colors["net"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.Net(
                        interface = "enp2s0",
                        format = '{down} ↓↑ {up}',
                        foreground = colors["net"],
                        background = colors["panel_bg"],
                        padding = 5
                        ),
               widget.TextBox(
                        text=']',
                        foreground = colors["net"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.TextBox(
                        text='[',
                        foreground = colors["volume"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.TextBox(
                       text=" Vol:",
                        foreground=colors["volume"],
                        background=colors["panel_bg"],
                        padding = 0
                        ),
               widget.PulseVolume(
                        foreground = colors["volume"],
                        background = colors["panel_bg"],
                        padding = 5
                        ),
               widget.TextBox(
                        text=']',
                        foreground = colors["volume"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.TextBox(
                        text='[',
                        foreground = colors["sensors"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
	       widget.ThermalSensor(
			tag_sensors = 'Core 0',
			foreground = colors["sensors"],
			background = colors["panel_bg"],
			padding = 5,
			),
               widget.TextBox(
                        text=']',
                        foreground = colors["sensors"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.TextBox(
                        text='[',
                        foreground = colors["layout"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.CurrentLayoutIcon(
                        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                        foreground = colors["layout"],
                        background = colors["panel_bg"],
                        padding = 0,
                        scale=0.7
                        ),
               widget.CurrentLayout(
                        foreground = colors["layout"],
                        background = colors["panel_bg"],
                        padding = 5
                        ),
               widget.TextBox(
                        text=']',
                        foreground = colors["layout"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.TextBox(
                        text='[',
                        foreground = colors["clock"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.Clock(
                        foreground = colors["clock"],
                        background = colors["panel_bg"],
			format="%d/%m/%Y - %H:%M"
                        #format="%A, %B %d  [ %H:%M ]"
                        ),
               widget.TextBox(
                        text=']',
                        foreground = colors["clock"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.TextBox(
                        text='[',
                        foreground = colors["window_name"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.Systray(
                        background=colors["panel_bg"],
                        padding = 5
                        ),
               widget.TextBox(
                        text=']',
                        foreground = colors["window_name"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        foreground = colors["panel_bg"],
                        background = colors["panel_bg"]
                        ),
              ]
    # Checking if the battery is plugged
    # If is plugged add it to the widgets_list
    if psutil.sensors_battery() is not None:
	       widgets_list.insert(
	    		17,
			wwidget.TextBox(
                        text='[',
                        foreground = colors["battery"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),
	       )
	       widgets_list.insert(
			18,
			widget.Battery(
			format = '{char} {percent:2.0%} {hour:d}:{min:02d}',
			unknown_char = '?',
			foreground = colors["font_dark"],
			background = colors["battery"],
			padding = 5,
		   )
	       )
	       widgets_list[19] = widget.TextBox(
                        text=']',
                        foreground = colors["battery"],
                        background = colors["panel_bg"],
                        padding=0,
                        fontsize=20
                        ),

    return widgets_list

##### SCREENS ##### (TRIPLE MONITOR SETUP)

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.95, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=0.95, size=20)),]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

##### DRAG FLOATING WINDOWS #####
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

##### FLOATING WINDOWS #####
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

##### STARTUP APPLICATIONS #####
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
