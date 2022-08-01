import os
from libqtile import widget
from libqtile.config import Key, Match
from libqtile.lazy import lazy

home = os.path.expanduser('~')

#### Groups (Workspace like) ####
group_names = [
    ("WWW", {
        'layout': 'monadtall', 
        'key':'1'}),
    ("WWW.", {
        'layout': 'monadtall', 
        'key':'2'}),
    ("DEV", {
        'layout': 'monadtall', 
        'key':'3',
        'matches': Match(wm_class='code')}),
    ("DEV.", {
        'layout': 'max', 
        'key':'4'}),
    ("TERM", {
        'layout': 'bsp', 
        'key':'q'}),
    ("DOCS", {
        'layout': 'monadtall', 
        'key':'w'}),
    ("ALT", {
        'layout': 'monadtall', 
        'key':'e'}),
    ("ALT.", {
        'layout': 'monadtall', 
        'key':'r',
        'matches': Match(wm_class='discord')})
]

def widgets():
    #### Colors for the widgets ####
    colors = {
        "panel_bg"		    :["#2a292c", "#2a292c"], 	# panel background
        "current_tab_bg"	:["#ff5555", "#ff5555"], 	# background for current screen tab
        "font_dark"		    :["#2a292c", "#2a292c"], 	# font color for widgets
        "font_white"		:["#ffffff", "#ffffff"],	# font color for group names
        "current_border"	:["#ff5555", "#ff5555"], 	# border line color for current tab
        "clock"			    :["#ff5555", "#ff5555"], 	# color for Clock and Date widget
        "layout"		    :["#7bcfc4", "#7bcfc4"], 	# color for Layout Type widget
        "updates"		    :["#e3f5a3", "#e3f5a3"], 	# color for the Updates widget
        "volume"		    :["#9996c6", "#9996c6"], 	# color for the Volume widget
        "memory"		    :["#db9356", "#db9356"], 	# color for the Memory widget
        "sensors"		    :["#fc9083", "#fc9083"], 	# color for the Thermal Sensors widget
        "screen_border"		:["#ff5555", "#ff5555"], 	# border line color for windows
        "even_widget"		:["#668bd7", "#668bd7"], 	# color for the even widgets
        "window_name"		:["#ff5555", "#ff5555"]  	# window name
    }
    separator_cfg = {
        'linewidth': 0,
        'padding': 4,
        'foreground': colors["font_dark"],
        'background': colors["panel_bg"]
    }
    textbox_cfg = {
        'font': 'Source Code Pro Medium',
        'background': colors["panel_bg"],
        'padding': 0,
        'fontsize': 14
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
        'CheckUpdates': {
            'distro': 'Arch_checkupdates',
            'display_format': '{updates}',
            'foreground': colors["updates"],
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
			filename = f"{home}/.config/qtile/icons/arch-logo.png"),
        widget.Sep(**separator_cfg),
    ]

    for widget_name in widgets_wanted:
        widget_list.append(widget.TextBox(text='[', foreground=widgets_wanted[widget_name]['foreground'],**textbox_cfg))
        if widget_name == 'CheckUpdates':
            widget_list.append(widget.TextBox(text='↺', foreground=widgets_wanted[widget_name]['foreground'],**textbox_cfg))
        widget_tmp = getattr(widget, '%s' % widget_name)
        widget_list.append(widget_tmp(**widgets_wanted[widget_name]))
        widget_list.append(widget.TextBox(text=']', foreground=widgets_wanted[widget_name]['foreground'],**textbox_cfg))
    
    widget_list.append(widget.Sep(**separator_cfg))

    return widget_list

def keys(mod):
    keys = list() 

    # Add the key shortcut to switch to any group
    for (name, kwargs) in group_names:
        keys.append(Key([mod], str(kwargs['key']), lazy.group[name].toscreen()))        # Switch to another group
        keys.append(Key([mod, "shift"], str(kwargs['key']), lazy.window.togroup(name))) # Send current window to another group
    
    return keys

def groups(): 
    group_names_copy = group_names.copy()
    # Remove the 'key' index from the dict
    # it's not needed to add the group name to the GroupBox
    for (name, kwargs) in group_names_copy:
        del kwargs['key']

    return group_names_copy
