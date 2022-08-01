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
        'key':'3',
        'matches': Match(wm_class='code')}),
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
        "panel_bg"          :["#2a292c", "#2a292c"], 	# panel background
        "group_1"           :["#6f6f6e", "#6f6f6e"],
        "group_2"           :["#6f6f6f", "#636363"],
        "group_3"           :["#5f5f5f", "#5f5f5f"],
        "group_4"           :["#4f4f4f", "#4f4f4f"],
        "group_5"           :["#3f3f3f", "#3f3f3f"],
        "group_6"           :["#2f2f2f", "#2f2f2f"],
        "group_7"           :["#1f1f1f", "#1f1f1f"],
        "group_8"           :["#0b0b0b", "#0b0b0b"],
        "current_tab_bg"    :["#ffffff", "#ffffff"], 	# background for current screen tab
        "foreground"        :["#ffffff", "#ffffff"], 	# font color for group names
        "active"            :["#ffffff", "#ffffff"],	# font color for group names when active (with opened windows)
        "current_border"    :["#a7a7a7", "#a7a7a7"], 	# border line color for current tab (selected group)
        "inactive"          :["#49484b", "#49484b"],    # inactive group color when inactive (no windows opened)
        "screen_border"     :["#ffffff", "#ffffff"], 	# border line color for windows
    }
    separator_cfg = {
        'linewidth': 5,
        'padding': 0,
    }
    img_sep_cfg = {
        'margin': 0,
        'scale': True
    }

    widget_list = [
        widget.Sep(background=fixed_colors["panel_bg"], foreground=fixed_colors["panel_bg"], **separator_cfg),
        widget.Image(
            background = fixed_colors["group_3"],
            filename = f"{home}/.config/qtile/icons/arch-logo.png",
            **img_sep_cfg),
        widget.Image(
            filename = f"{home}/.config/qtile/themes/img/rounded_right3.png",
            background = fixed_colors["group_1"],
            **img_sep_cfg),
        widget.GroupBox(
            font = "font awesome 5 free",
            fontsize = 15,
            margin_y = 3.5,
            margin_x = 0,
            padding_y = 7,
            padding_x = 5,
            borderwidth = 5,
            active = fixed_colors["active"],
            inactive = fixed_colors["inactive"],
            rounded = False,
            highlight_color = fixed_colors["current_tab_bg"],
            highlight_method = "block",
            this_current_screen_border = fixed_colors["current_border"],
            this_screen_border = fixed_colors ["screen_border"],
            other_current_screen_border = fixed_colors["panel_bg"],
            other_screen_border = fixed_colors["panel_bg"],
            foreground = fixed_colors["foreground"],
            background = fixed_colors["group_1"]),
        widget.Image(
            filename = f"{home}/.config/qtile/themes/img/rounded_right1.png",
            background = fixed_colors["panel_bg"],
            **img_sep_cfg),
        widget.Sep(background=fixed_colors["panel_bg"], foreground=fixed_colors["panel_bg"], **separator_cfg),
        widget.Image(
            filename = f"{home}/.config/qtile/themes/img/rounded_left1.png",
            background = fixed_colors["panel_bg"]),
        widget.WindowName(
            fmt = "{}",
            font = 'Ubuntu Bold',
            foreground = fixed_colors["foreground"],
            background = fixed_colors["group_1"],
            padding = 0),
        widget.Image(
            filename = f"{home}/.config/qtile/themes/img/rounded_right1.png",
            background = fixed_colors["panel_bg"]),
        widget.Sep(background=fixed_colors["panel_bg"], foreground=fixed_colors["panel_bg"], **separator_cfg),
        widget.Image(
            filename = f"{home}/.config/qtile/themes/img/rounded_left2.png",
            background = fixed_colors["panel_bg"]),
        widget.TextBox(
                text='↺',
                foreground=fixed_colors['foreground'],
                font='Ubuntu Mono',
                background=fixed_colors["group_2"],
                padding=0,
                fontsize=18),
        widget.CheckUpdates(
            font = 'Ubuntu Bold',
            distro = 'Arch_checkupdates',
            display_format = '{updates}',
            foreground = fixed_colors["foreground"],
            background = fixed_colors["group_2"],
            padding = 1),
        widget.Sep(background=fixed_colors["group_2"], foreground=fixed_colors["group_2"], **separator_cfg),
        widget.Image(
            filename = f"{home}/.config/qtile/themes/img/rounded_left3.png",
            background = fixed_colors["group_2"]),
        widget.Memory(
            font = 'Ubuntu Bold',
            foreground = fixed_colors["foreground"],
            background = fixed_colors["group_3"],
            padding = 1),
        widget.Sep(background=fixed_colors["group_3"], foreground=fixed_colors["group_3"], **separator_cfg),
        widget.Image(
            filename = f"{home}/.config/qtile/themes/img/rounded_left4.png",
            background = fixed_colors["group_3"]),
        widget.PulseVolume(
            font = 'Ubuntu Bold',
            foreground = fixed_colors["foreground"],
            background = fixed_colors["group_4"],
            padding = 1),
        widget.Sep(background=fixed_colors["group_4"], foreground=fixed_colors["group_4"], **separator_cfg),
        widget.Image(
            filename = f"{home}/.config/qtile/themes/img/rounded_left5.png",
            background = fixed_colors["group_4"]),
        widget.ThermalSensor(
            font = 'Ubuntu Bold',
            tag_sensors = 'core 0',
            foreground = fixed_colors["foreground"],
            background = fixed_colors["group_5"],
            padding = 1),
        widget.Sep(background=fixed_colors["group_5"], foreground=fixed_colors["group_5"], **separator_cfg),
        widget.Image(
            filename = f"{home}/.config/qtile/themes/img/rounded_left6.png",
            background = fixed_colors["group_5"]),
        widget.CurrentLayout(
            font = 'Ubuntu Bold',
            foreground = fixed_colors["foreground"],
            background = fixed_colors["group_6"],
            padding = 1),
        widget.Sep(background=fixed_colors["group_6"], foreground=fixed_colors["group_6"], **separator_cfg),
        widget.Image(
            filename = f"{home}/.config/qtile/themes/img/rounded_left7.png",
            background = fixed_colors["group_6"]),
        widget.Clock(
            font = 'Ubuntu Bold',
            foreground = fixed_colors["foreground"],
            background = fixed_colors["group_7"],
            format = "%d/%m/%Y - %H:%M",
            padding = 1),
        widget.Sep(background=fixed_colors["group_7"], foreground=fixed_colors["group_7"], **separator_cfg),
        widget.Image(
            filename = f"{home}/.config/qtile/themes/img/rounded_left8.png",
            background = fixed_colors["group_7"]),
        widget.Systray(
            foreground = fixed_colors["foreground"],
            background = fixed_colors["group_8"],
            padding = 1),
        widget.Sep(background=fixed_colors["group_8"], foreground=fixed_colors["group_8"], **separator_cfg),
    ]

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

def bar():
    bar_config = {
        'background': '#ff000080',
        'margin': 6,
        'opacity': 0.75,
    }

    return bar_config
