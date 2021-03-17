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

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#### Defaults ####
alt_key = "mod1" # mod1 = Alt key
mod = "mod4" # mod4 = Windows Key
#terminal = guess_terminal()
terminal = "alacritty" # My terminal of choice
browser = "brave"
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
    Key([mod, alt_key], "r",
        lazy.restart(),
        desc='Restart Qtile'),
    Key([mod, alt_key], "q",
        lazy.shutdown(),
        desc='Shutdowqn Qtile'),

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
    Key([mod, alt_key], "f",
        lazy.spawn("alacritty -e ranger"),
        desc='Open the file manager: Ranger'),

    #### Audio Controls
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("/usr/bin/pulseaudio-ctl down -5"),
        desc='Decrease the volume with phisical buttons'),
	 Key([], "XF86AudioRaiseVolume",
        lazy.spawn("/usr/bin/pulseaudio-ctl up -5"),
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

#### Groups (Workspace like) ####
group_names = [
    ("WWW", {'layout': 'monadtall', 'key':'1'}),
    ("WWW.", {'layout': 'monadtall', 'key':'2'}),
    ("DEV", {'layout': 'monadtall', 'key':'3'}),
    ("DEV.", {'layout': 'max', 'key':'4'}),
    ("TERM", {'layout': 'bsp', 'key':'q'}),
    ("DOCS", {'layout': 'monadtall', 'key':'w'}),
    ("ALT", {'layout': 'monadtall', 'key':'e'}),
    ("ALT.", {'layout': 'monadtall', 'key':'r'})
]

# Add the key shortcut to switch to any group
for (name, kwargs) in group_names:
    keys.append(Key([mod], str(kwargs['key']), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(kwargs['key']), lazy.window.togroup(name))) # Send current window to another group

# Remove the 'key' index from the dict
# it's not needed to add the group name to the GroupBox
for (name, kwargs) in group_names:
    del kwargs['key']

# Add the group name and layout type to the Group object
groups = [Group(name, **kwargs) for name, kwargs in group_names]

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {
    "border_width": 2,
    "margin": 6,
    "border_focus": "ff5555",
    "border_normal": "2a292c"
}

layouts = [
    # layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(**layout_theme),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


#### Widgets Configuration
widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

#### Color for the widgets ####
colors = {
	"panel_bg"		    :["#2a292c", "#2a292c"], 	# panel background
    "current_tab_bg"	:["#ff5555", "#ff5555"], 	# background for current screen tab
    "font_dark"		    :["#2a292c", "#2a292c"], 	# font color for widgets
	"font_white"		:["#ffffff", "#ffffff"],	# font color for group names
    "current_border"	:["#ff5555", "#ff5555"], 	# border line color for current tab
	"clock"			    :["#ff5555", "#ff5555"], 	# color for Clock and Date widget
	"layout"		    :["#7bcfc4", "#7bcfc4"], 	# color for Layout Type widget
	"pacman"		    :["#e3f5a3", "#e3f5a3"], 	# color for the Thermal Sensors widget
	"net"			    :["#f0ec74", "#f0ec74"], 	# color for the Volume widget
	"volume"		    :["#9996c6", "#9996c6"], 	# color for the Net widget
	"memory"		    :["#db9356", "#db9356"], 	# color for the Memory widget
	"sensors"		    :["#fc9083", "#fc9083"], 	# color for the Pacman widget
	"battery"		    :["#98bae5", "#98bae5"], 	# color for the Bettery widget
    "screen_border"		:["#ff5555", "#ff5555"], 	# border line color for windows
    "even_widget"		:["#668bd7", "#668bd7"], 	# color for the even widgets
    "window_name"		:["#ff5555", "#ff5555"]  	# window name
}

def init_widgets_list():
    separator_cfg = {
        'linewidth': 0,
        'padding': 4,
        'foreground': colors["font_dark"],
        'background': colors["panel_bg"]
    }
    textbox_cfg = {
        #'text'='[',
        #'foreground' = colors["font_white"],
        'background': colors["panel_bg"],
        'padding': 0,
        'fontsize': 20
    }
    widgets_wanted = {
        'GroupBox': {
            'font': "Ubuntu Bold",
            'fontsize': 9,
            'margin_y': 3,
            'margin_x': 0,
            'padding_y': 5,
            'padding_x': 2,
            'borderwidth': 3,
            'active': colors["font_white"],
            'inactive': colors["font_white"],
            'rounded': False,
            'highlight_color': colors["current_tab_bg"],
            'highlight_method': "line",
            'this_current_screen_border': colors["current_border"],
            'this_screen_border': colors ["screen_border"],
            'other_current_screen_border': colors["panel_bg"],
            'other_screen_border': colors["panel_bg"],
            'foreground': colors["font_white"],
            'background': colors["panel_bg"]
        },
        'WindowName': {
            'fmt': "{}",
            'foreground': colors["window_name"],
            'background': colors["panel_bg"],
            'padding': 0
        },
        'Memory': {
            'foreground': colors["memory"],
            'background': colors["panel_bg"],
            'padding': 5
        },
        'PulseVolume': {
            'foreground': colors["volume"],
            'background': colors["panel_bg"],
            'padding': 5
        },
        'ThermalSensor': {
            'tag_sensors': 'Core 0',
            'foreground': colors["sensors"],
            'background': colors["panel_bg"],
            'padding': 5,
        },
        #'CurrentLayoutIcon',
        'Battery': {
            'foreground': colors["layout"],
            'background': colors["panel_bg"],
            'battery': 0,
        },
        'CurrentLayout': {
            'foreground': colors["layout"],
            'background': colors["panel_bg"],
            'padding': 5
        },
        'Clock': {
            'foreground': colors["clock"],
            'background': colors["panel_bg"],
            'format': "%d/%m/%Y - %H:%M"
        },
        'Systray': {
            'foreground': colors["window_name"],
            'background': colors["panel_bg"],
            'padding': 5
        },
    }
    widget_list = [
        widget.Sep(**separator_cfg),
        widget.Image(
            background = colors["panel_bg"],
			filename = "~/.config/qtile/icons/arch-logo.png"),
        widget.Sep(**separator_cfg),
    ]

    for widget_name in widgets_wanted:
        widget_list.append(widget.TextBox(text='[', foreground=widgets_wanted[widget_name]['foreground'],**textbox_cfg))
        widget_tmp = getattr(widget, '%s' % widget_name)
        widget_list.append(widget_tmp(**widgets_wanted[widget_name]))
        widget_list.append(widget.TextBox(text=']', foreground=widgets_wanted[widget_name]['foreground'],**textbox_cfg))
    
    widget_list.append(widget.Sep(**separator_cfg))

    return widget_list

#screens = [
#    Screen(
#        top=bar.Bar(
#            [
#                widget.CurrentLayout(**widgets_wanted['CurrentLayout']),
#                widget.GroupBox(),
#                widget.Prompt(),
#                widget.WindowName(),
#                widget.Chord(
#                    chords_colors={
#                        'launch': ("#ff0000", "#ffffff"),
#                    },
#                    name_transform=lambda name: name.upper(),
#                ),
#                widget.TextBox("default config", name="default"),
#                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
#                widget.Systray(),
#                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
#                widget.QuickExit(),
#            ],
#            24,
#        ),
#    ),
#]

#screens = [
#    Screen(
#        top=bar.Bar(
#            [
#                widget.Sep(**separator_cfg),
#                widget.Image(
#                    background = colors["panel_bg"],
#                    filename = "~/.config/qtile/icons/arch-logo.png"),
#                widget.Sep(**separator_cfg),
#                widget.GroupBox(**widgets_wanted['GroupBox']),
#            ], 
#            opacity=0.95, 
#            size=20
#        )
#    )
#]

screens = [Screen(top=bar.Bar(widgets=init_widgets_list(), opacity=0.95, size=25))]

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
floating_layout = layout.Floating(float_rules=[
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
