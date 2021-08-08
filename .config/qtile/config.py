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


#### IMPORTS ####
import os
import subprocess
from typing import List  # noqa: F401
from libqtile import qtile
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from random import randint

import themes

#### Defaults ####
alt_key = "mod1" # mod1 = Alt key
mod = "mod4" # mod4 = Windows Key
#terminal = guess_terminal()
terminal = "alacritty" # My terminal of choice
browser = "firefox"
file_manager = "thunar"
home = os.path.expanduser('~')

#### Key Shortcuts Configuration ####
keys = [
    ## Essential shortcuts

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab",
        lazy.prev_layout(),
        desc='Toggle backwards through layouts'),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"), 

    ## Window controls ##

    # Move between windows in current stack
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Changing windows sizes
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='Normalize window size ratios'),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='Toggle window between minimum and maximum sizes'),
    Key([mod], "u",
        lazy.layout.shrink(),
        desc='Shrink the windows size'),
    Key([mod], "i",
        lazy.layout.grow(),
        desc='Grow the windows size'),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", 
        lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", 
        lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", 
        lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", 
        lazy.layout.grow_up(), 
        desc="Grow window up"),
    
    ### Switch focus to specific monitor (out of two)
    Key([mod], "a",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 1'
        ),
    Key([mod], "s",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 2'
        ),

    # Changing to floating windows
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'),

    ## Stack Layout controls
    Key([mod, "shift"], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'),
    Key([mod], "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'),
    Key([mod, "control"], "Return",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    ## User applications and menus usage 
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "Return",
        lazy.spawn("rofi -show combi"),
        desc='Rofi Run Launcher'),
    Key([mod], "Escape",
        lazy.spawn(home + "/.config/rofi/power-menu.sh"),
        desc='Show power menu'),
    Key([mod], "b",
        lazy.spawn(browser),
        desc='Luch deafault browser'),
    Key([mod], "f",
        lazy.spawn(file_manager),
        desc='Open the default file manager'),
    Key([mod, "control"], "f",
        lazy.spawn("urxvt -e ranger"), 
        #lazy.function(lambda: qtile.cmd_spawn(terminal + ' -e ranger')),        
        desc='Open the file manager: Ranger'),
    Key([mod, "control"], "p",
        lazy.spawn("flameshot gui"),
        desc='Open flameshot to take a screenshot'),

    #### Audio Controls
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("/usr/bin/pulseaudio-ctl down -2"),
        desc='Decrease the volume with phisical buttons'),
	 Key([], "XF86AudioRaiseVolume",
        lazy.spawn("/usr/bin/pulseaudio-ctl up -2"),
        desc='Increase the volume with phisical buttons'),
	 Key([], "XF86AudioMute",
        lazy.spawn("/usr/bin/pulseaudio-ctl mute"),
        desc='Toggle mute/unmute phisical button'),
    
    #### Brightness Controls
	Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +10%"),
        desc='Increase the brightness of the screen: Laptop'),
	 Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 10%-"),
        desc='Decrease the brightness of the screen: Laptop'),
]

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {
    "border_width": 2,
    "margin": 6,
    "border_focus": "ff5555",
    "border_normal": "2a292c"
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Tile(**layout_theme),
    # layout.Columns(border_focus_stack='#d75f5f'),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


#### Widgets Configuration
widget_defaults = dict(
    font='Source Code Pro',
    fontsize=12,
    padding=0,
)
extension_defaults = widget_defaults.copy()

##### Dinamically add the widgets, key shortcuts for the groups and group names
## Get the list available inside the 'themes' directory
themes_list = [theme for theme in dir(themes) if not theme.startswith('__')]
theme_obj = getattr(themes, '%s' % themes_list[randint(0, len(themes_list)-1)])
#theme_obj = getattr(themes, '%s' % 'theme_name')
## Add the key shortcut to switch to any group
keys.extend(theme_obj.keys(mod))
## Add the group name and layout type to the Group object
groups = [Group(name, **kwargs) for name, kwargs in theme_obj.groups()]
### Add the widgets to the screen bar
## Get the bar configuration, if not, use default
if hasattr(theme_obj, 'bar'):
    bar_config = theme_obj.bar()
else:
    bar_config = {
        'background': '#000000',
        'margin': 0,
        'opacity': 0.95,
    }
 
widget_list1 = theme_obj.widgets()
widget_list2 = theme_obj.widgets(False)

screens = [Screen(top=bar.Bar(widgets=widget_list1, size=25, **bar_config)),
            Screen(top=bar.Bar(widgets=widget_list2, size=25, **bar_config))]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


# Default config values
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(border_focus='ffffff', float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title='galculator'),  # Calculator of user choice
])
auto_fullscreen = True
focus_on_window_activation = "smart"

##### STARTUP APPLICATIONS #####
@hook.subscribe.startup_once
def start_once():
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
