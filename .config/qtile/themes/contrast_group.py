import os
from random import randint
from libqtile import widget
from libqtile.config import Key, Match
from libqtile.lazy import lazy

home = os.path.expanduser('~')

#### Groups (Workspace like) ####
group_names = [
    ("WWW", {
        'label': '\uf269', 
        'layout': 'monadtall', 
        'key':'1'}),
    ("WWW.", {
        'label': '\uf267', 
        'layout': 'monadtall', 
        'key':'2'}),
    ("DEV", {
        'label': '\uf121', 
        'layout': 'monadtall', 
        'key':'3'}),
    ("DEV.", {
        'label': '\uf3b2', 
        'layout': 'max', 
        'key':'4'}),
    ("TERM", {
        'label': '\uf120', 
        'layout': 'bsp', 
        'key':'q'}),
    ("DOCS", {
        'label': '\uf07b', 
        'layout': 'monadtall', 
        'key':'w'}),
    ("ALT", {
        'label': '\uf12e', 
        'layout': 'monadtall', 
        'key':'e'}),
    ("ALT.", {
        'label': '\uf086', 
        'layout': 'monadtall', 
        'key':'r',
        'matches': Match(wm_class='discord')})
]

def widgets():
    #### Colors for the widgets ####
    fixed_colors = {
        "panel_bg"		    :["#2a292c", "#2a292c"], 	# panel background
        "panel_group"       :["#695f7c", "#695f7c"],    # panel grouping background
        "current_tab_bg"	:["#ffffff", "#ffffff"], 	# background for current screen tab
        "foreground"		:["#2a292c", "#2a292c"], 	# font color for group names
        "active"		    :["#ffffff", "#ffffff"],	# font color for group names when active (with opened windows)
        "current_border"	:["#a7a7a7", "#a7a7a7"], 	# border line color for current tab (selected group)
        "inactive"          :["#49484b", "#49484b"],    # inactive group color when inactive (no windows opened)
        "screen_border"		:["#ffffff", "#ffffff"], 	# border line color for windows
    }
    rnd_colors = [
        ["#ffa0be", "#ffa0be"],
        ["#fffcc7", "#fffcc7"], 
        ["#b6e2d3", "#b6e2d3"],
        ["#fae8e0", "#fae8e0"],
        ["#fbe7c6", "#fbe7c6"],
        ["#f5b2aa", "#f5b2aa"],
        ["#ef7c8e", "#ef7c8e"],
        ["#95c2d4", "#95c2d4"],
        ["#da5699", "#da5699"],
        ["#f8c835", "#f8c835"],
        ["#e34569", "#e34569"],
        ["#babc71", "#babc71"],
    ]
    separator_cfg = {
        'linewidth': 5,
        'padding': 0,
        'foreground': fixed_colors["foreground"],
        'background': fixed_colors["panel_bg"]
    }
    image_sep_open = {
        'margin': 0,
        'background': fixed_colors["panel_bg"],
        'filename': f"{home}/.config/qtile/themes/img/cg_open_group.png",
        'scale': True
    }
    image_sep_close = {
        'margin': 0,
        'background': fixed_colors["panel_bg"],
        'filename': f"{home}/.config/qtile/themes/img/cg_close_group.png",
        'scale': True
    }

    widgets_wanted = {
        'GroupBox': {
            'font': "Font Awesome 5 Free",
            'fontsize': 15,
            'margin_y': 3.5,
            'margin_x': 0,
            'padding_y': 7,
            'padding_x': 5,
            'borderwidth': 5,
            'active': fixed_colors["active"],
            'inactive': fixed_colors["inactive"],
            'rounded': False,
            'highlight_color': fixed_colors["current_tab_bg"],
            'highlight_method': "block",
            'this_current_screen_border': fixed_colors["current_border"],
            'this_screen_border': fixed_colors ["screen_border"],
            'other_current_screen_border': fixed_colors["panel_bg"],
            'other_screen_border': fixed_colors["panel_bg"],
            'foreground': fixed_colors["foreground"],
            'background': fixed_colors["panel_group"]
        },
        'WindowName': {
            'fmt': "{}",
            'font': 'Ubuntu Bold',
            'foreground': rnd_colors[randint(0, len(rnd_colors)-1)],
            'background': fixed_colors["panel_group"],
            'padding': 0
        },
        'CheckUpdates': {
            'font': 'Ubuntu Bold',
            'distro': 'Arch_checkupdates',
            'display_format': '{updates}',
            'foreground': rnd_colors[randint(0, len(rnd_colors)-1)],
            'background': fixed_colors["panel_group"],
            'padding': 1
        },
        'Memory': {
            'font': 'Ubuntu Bold',
            'foreground': rnd_colors[randint(0, len(rnd_colors)-1)],
            'background': fixed_colors["panel_group"],
            'padding': 1
        },
        'PulseVolume': {
            'font': 'Ubuntu Bold',
            'foreground': rnd_colors[randint(0, len(rnd_colors)-1)],
            'background': fixed_colors["panel_group"],
            'padding': 1,
        },
        'ThermalSensor': {
            'font': 'Ubuntu Bold',
            'tag_sensors': 'Core 0',
            'foreground': rnd_colors[randint(0, len(rnd_colors)-1)],
            'background': fixed_colors["panel_group"],
            'padding': 1,
        },
        'CurrentLayout': {
            'font': 'Ubuntu Bold',
            'foreground': rnd_colors[randint(0, len(rnd_colors)-1)],
            'background': fixed_colors["panel_group"],
            'padding': 1
        },
        'Clock': {
            'font': 'Ubuntu Bold',
            'foreground': rnd_colors[randint(0, len(rnd_colors)-1)],
            'background': fixed_colors["panel_group"],
            'format': "%d/%m/%Y - %H:%M",
            'padding': 1,
        },
        'Systray': {
            'foreground': rnd_colors[randint(0, len(rnd_colors)-1)],
            'background': fixed_colors["panel_group"],
            'padding': 1,
        },
    }
    widget_list = [
        widget.Sep(**separator_cfg),
        widget.Image(
                margin=0,
                background = fixed_colors["panel_bg"],
                filename = f"{home}/.config/qtile/icons/arch-logo.png",
                scale = True), 
        widget.Sep(**separator_cfg),
    ]
    
    for widget_name in widgets_wanted:
        widget_list.append(widget.Sep(**separator_cfg)),
        widget_list.append(widget.Image(**image_sep_open))
        if widget_name == 'CheckUpdates':
            widget_list.append(widget.TextBox(
                text='↺',
                foreground=fixed_colors['active'],
                font='Ubuntu Mono',
                background=fixed_colors["panel_group"],
                padding=0,
                fontsize=18))
        widget_tmp = getattr(widget, '%s' % widget_name)
        widget_list.append(widget_tmp(**widgets_wanted[widget_name]))
        widget_list.append(widget.Image(**image_sep_close))
    
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
