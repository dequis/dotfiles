# -*- coding: utf-8 -*-

from libqtile.config import Key, Screen, Group, Drag, Rule 
from libqtile.command import lazy
from libqtile import layout, widget
from libqtile import bar
from libqtile.dgroups import simple_key_binder
from libqtile.config import Match
import functools

## bindings

mod = "mod4"

keys = [
    Key([mod],            "j", lazy.layout.down()),
    Key([mod],            "k", lazy.layout.up()),
    Key([mod, "control"], "j", lazy.layout.shuffle_down()),
    Key([mod, "control"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "minus", lazy.layout.decrease_ratio()),
    Key([mod, "control"], "equal", lazy.layout.increase_ratio()),
    Key([mod],            "Tab", lazy.group.prev_window()),
    Key([mod, "shift"],   "Tab", lazy.group.next_window()),
    Key([mod, "shift"],   "Return", lazy.layout.toggle_split()),
    Key([mod, "control"], "f", lazy.window.toggle_fullscreen()),

    Key([mod], "minus", lazy.spawn("amixer set Master 3%- > /dev/null")),
    Key([mod], "equal", lazy.spawn("amixer set Master 3%+ > /dev/null")),
    Key([mod], "t", lazy.spawn("mpc toggle > /dev/null")),
    Key([mod], "s", lazy.spawn("sleep 0.1; scr")),
    Key([mod], "x", lazy.spawn("sleep 0.1; tmux neww \"sh -c 'xprop; read'\"")),
    Key([mod, "shift"], "x", lazy.spawn("sleep 0.1; tmux neww \"sh -c 'xwininfo; read'\"")),
    Key([mod, "shift"], "s", lazy.spawn("sleep 0.1; scr -s")),
    Key([mod], "bracketleft", lazy.spawn("bfg-set-intensity -1")),
    Key([mod], "bracketright", lazy.spawn("bfg-set-intensity +1")),

    Key([mod], "r", lazy.spawncmd("Run:")),
    Key([mod, "shift"], "r", lazy.spawncmd("Runeval:", command="qtinfo $(%s)")),
    Key([mod], "g", lazy.togroup()),

    Key([mod], "Left", lazy.screen.prevgroup()),
    Key([mod], "Right", lazy.screen.nextgroup()),
    Key([mod], "space", lazy.window.toggle_floating()),
    Key([mod], "m", lazy.window.toggle_minimize()),

    Key([mod, "control"], "Tab", lazy.nextlayout()),
    Key([mod, "control"], "w", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "a", lazy.execute("/usr/bin/awesome", ("awesome",))),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
]


## layouts

layoutconf = {
    'border_width': 0,
}

layouts = [
    layout.Max(),
    layout.Stack(stacks=2, **layoutconf),
    layout.Tile(**layoutconf),
    layout.MonadTall(**layoutconf),
    layout.RatioTile(**layoutconf),
]

floating_layout = layout.Floating(
    auto_float_types=[
        'dialog',
        'utility',
        'splash',
    ],
    **layoutconf
)


## screens / widgets

Sep = functools.partial(widget.Sep, linewidth=0, padding=3)

widget_defaults = dict(
    font="DejaVu Sans",
    fontsize=12,
    foreground=["FFFFFF.30", "FFFFFF.70"],
    fontshadow=["000000.90", "000000"],
    highlight_method='block',
    rounded=False,
)

widget_defaults['active'] = widget_defaults['foreground']

mono = widget_defaults.copy()
mono['font'] = "dejavu sans mono"
mono['fontsize'] = 14

cpugraph_conf = dict(
    width=50,
    line_width=1,
    margin_y=0,
    border_width=0,
    border_color='006600',
    graph_color='44B1FF',
    fill_color='44B1FF.7',
    frequency=1,
)

screens = [Screen(
    top = bar.Bar([
        widget.GroupBox(
            padding_x=10,
            padding_y=4,
            margin=0,
            borderwidth=1,
            inactive="606060",
            this_current_screen_border='44B1FF.45',
            urgent_alert_method='block',
            urgent_border=["FF0000", "660000"],
        ),
        Sep(),
        widget.Prompt(**mono),
        widget.TaskList(
            padding_x=16,
            padding_y=4,
            margin_y=0,
            border='44B1FF.45',
            borderwidth=1,
        ),
        Sep(),
        #widget.Image(
        #    filename="~/.config/qtile/music.png",
        #    margin=2,
        #),
        #widget.Mpd(
        #    do_color_progress=False,
        #    fmt_playing=u"%a - %t",
        #),
        Sep(padding=10),
        widget.TextBox(text="", name="info"),
        Sep(padding=10),
        #widget.CPUGraph(core=0, **cpugraph_conf),
        #widget.CPUGraph(core=1, **cpugraph_conf),
        #Sep(),
        widget.Systray(),
        widget.Clock(fmt="%a %d %b [%H:%M]"),
    ], 20, background=["454545", "000000"]),
)]

dgroups_key_binder = simple_key_binder(mod)

## groups

groups = [
    Group('term', init=True, persist=True, exclusive=True),
    Group('www', init=False, exclusive=True),
]

groups.extend([Group(x, init=False, persist=False) for x in
    ['gimp', 'qemu', 'mc', 'anki', 'steam', 'chrome', 'wine']])

dgroups_app_rules = [
    Rule(Match(
        wm_class=['MPlayer', 'Exe', 'feh', 'Pinentry']),
        float=True, intrusive=True, break_on_match=False),
    Rule(Match(title=['Event Tester']), float=True, intrusive=True),
    Rule(Match(wm_class=['Gnome-terminal', 'st-256color', 'st']), group='term'),
    Rule(Match(wm_class=['fontforge']), group='fontforge', float=True),
    Rule(Match(wm_class=['Gimp', 'gimp']), group='gimp', float=True),
    Rule(Match(wm_class=['anki', 'Anki']), group='anki', float=True),
    Rule(Match(wm_class=['chromium', 'Chromium']), group='chrome'),
    Rule(Match(wm_class=['Firefox', 'Aurora', 'Nightly', 'firefox-bin'],
        role=['browser']), group='www'),
    Rule(Match(wm_class=['Wine']), float=True, group='wine'),
    Rule(Match(wm_class=['Steam']), float=True, group='steam'),
    Rule(Match(title=['QEMU']), float=True, group='qemu'),
    Rule(Match(wm_class=['net-minecraft-MinecraftLauncher']), group='mc'),
]
