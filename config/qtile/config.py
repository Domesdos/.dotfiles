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


import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')
myTerm = "kitty"


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

keys = [

# Window management
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "x", lazy.window.kill()),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# Spawning programs
    Key([mod], "Print", lazy.spawn(myTerm+" flameshot gui")),
    Key([mod, "shift"], "Print", lazy.spawn(myTerm+' flameshot full -p /home/mw/Screenshots')),
    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod, "shift"], "f", lazy.spawn(myTerm+" -T 'ranger' ranger")),
    Key([mod, "shift"], "Return", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=12'")),
    Key([mod, "shift"], "b", lazy.spawn('vivaldi-stable')),

# SUPER + SHIFT +  KEY
    Key([mod, "shift"], "q", lazy.shutdown()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

# CHANGE FOCUS
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
]


# Set workspaces
groups = []
group_names = ["1", "2", "3", "4", "5"]
group_labels = ["Browser", "Terminal", "Social", "Gaming", "Misc"]
group_layouts = ["monadtall", "monadtall", "monadtall", "floating", "monadtall"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])



def init_layout_theme():
    return {"margin":5,
            "border_width":2,
            "border_focus": "#bd93f9",
            "border_normal": "#20212b"
            }

layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(margin=2, border_width=2, border_focus="#bd93f9", border_normal="#20212b"),
    layout.MonadWide(margin=2, border_width=2, border_focus="#bd93f9", border_normal="#20212b"),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]




# Bar colors
def init_colors():
    return [["#20212b", "#20212b"], # color 0 | Background default
            ["#f8f8f2", "#f8f8f2"], # color 1 | Foreground default
            ["#bd93f9", "#bd93f9"], # color 2
            ["#6a8caf", "#6a8caf"], # color 3
            ["#75b79e", "#75b79e"], # color 4
            ["#f1935c", "#f1935c"], # color 5
            ["#eef9bf", "#eef9bf"], # color 6
            ["#f67280", "#f67280"], # color 7
            ["#4baea0", "#4baea0"], # color 8
            ["#a9a9a9", "#a9a9a9"]] # color 9


colors = init_colors()

# Bar widgets
def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 12,
                padding = 2,
                background=colors[0],
                foreground=colors[1])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
               widget.GroupBox(
                   font="Noto Sans Bold",
                   fontsize = 12,
                   padding_x = 5,
                   borderwidth = 0,
                   disable_drag = True,
                   active = colors[1],
                   inactive = colors[9],
                   rounded = False,
                   highlight_method = "text",
                   this_current_screen_border = colors[2],
               ),
               widget.Spacer(length = 400),
               widget.TextBox(
                   font = "FontAwesome",
                   fontsize = 16,
                   text = "",
               ),
               widget.CurrentLayout(
                   foreground = colors[3],
               ),
               widget.TextBox(
                   font="FontAwesome",
                   fontsize = 16,
                   text = "",
               ),
               widget.Sep(
                   linewidth = 1,
                   padding = 10,
               ),
               widget.Systray(),
               widget.Spacer(length = 40),
               widget.WindowName(
                   fontsize = 12,
                   foreground = colors[5],
               ),
               widget.ThermalSensor(
                   foreground = colors[6],
                   foreground_alert = colors[5],
                   ),
               widget.Spacer(length = 10),
               widget.Pacman(
                   foreground = colors[3],
                   unavailable = colors[3],
                   fmt = 'Updates: {0}',
               ),
               widget.Spacer(length = 10),
               widget.TextBox(
                   text = "Net: ",
                   foreground = colors[8],
               ),
               widget.NetGraph(
                   border_width = 0,
                   graph_color = colors[8],
                   type = "line",
                   line_width = 1,
               ),
               widget.Net(
                   foreground = colors[8],
                   format = '{down}',
               ),
               widget.Spacer(length = 10),
               widget.CPU(
                   foreground = colors[7],
                   format = 'CPU: {freq_current}GHz - {load_percent}%',
               ),
               widget.Spacer(length = 10),
               widget.Memory(
                   format = 'Memory: {MemUsed}M/{MemTotal}M',
                   update_interval = 1,
                   fontsize = 12,
                   foreground = colors[5],
               ),
               widget.Spacer(length = 10),
               widget.Clock(
                   foreground = colors[6],
                   fontsize = 12,
                   format="%a. %d.%m.%Y | %H:%M Uhr"
               ),
               widget.Spacer(length = 10),
              ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26))]
screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

# @hook.subscribe.client_new
# def assign_app_group(client):
#     d = {}
#     #########################################################
#     ################ assgin apps to groups ##################
#     #########################################################
#     d["1"] = ["Navigator", "Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
#               "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]
#     d["2"] = [ "Atom", "Subl3", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
#                "atom", "subl3", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
#     d["3"] = ["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
#               "inkscape", "nomacs", "ristretto", "nitrogen", "feh", ]
#     d["4"] = ["Gimp", "gimp" ]
#     d["5"] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld" ]
#     d["6"] = ["Vlc","vlc", "Mpv", "mpv" ]
#     d["7"] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer",
#               "virtualbox manager", "virtualbox machine", "vmplayer", ]
#     d["8"] = ["Thunar", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
#               "thunar", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
#     d["9"] = ["Evolution", "Geary", "Mail", "Thunderbird",
#               "evolution", "geary", "mail", "thunderbird" ]
#     d["0"] = ["Spotify", "Pragha", "Clementine", "Deadbeef", "Audacious", #               "spotify", "pragha", "clementine", "deadbeef", "audacious" ]
#     ##########################################################
#     wm_class = client.window.get_wm_class()[0]
#
#     for i in range(len(d)):
#         if wm_class in list(d.values())[i]:
#             group = list(d.keys())[i]
#             client.togroup(group)
#             client.group.cmd_toscreen()

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME



main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'Arcolinux-welcome-app.py'},
    {'wmclass': 'Arcolinux-tweak-tool.py'},
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wmclass': 'Arandr'},
    {'wmclass': 'feh'},
    {'wmclass': 'Galculator'},
    {'wmclass': 'arcolinux-logout'},
    {'wmclass': 'xfce4-terminal'},
    {'wname': 'branchdialog'},
    {'wname': 'Open File'},
    {'wname': 'pinentry'},
    {'wmclass': 'ssh-askpass'},
    {'wname': 'Steam'},
    {'wmclass': 'Steam'},
    # {'wname': 'ranger'},

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
