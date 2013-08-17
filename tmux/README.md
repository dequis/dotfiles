# dx tmux config

interesting stuff here:

## bolsa

my desktop

* statusbar:

![](http://dump.dequis.org/RzADi.png)

* window-status-format with rounded corners using [modified powerline font](http://dequis.org/PowerlineSymbols.otf)
* status-right shows list of sessions, with the current one highlighted
* bind `;` to run `tmx_` commands (in the bin dir here) that provide additional functionality:
    * `tmx_init`: handles initialization of the two pinned tabs, ncmpcpp and carl0s (irssi)
    * `tmx_session`: creates a new session and links the pinned tabs to this new one.
    * `tmx_nuke`: nukes the current session if there are less than three tabs open - avoids detaching the tmux client like kill-session usually does
    * `tmx_renumber`: shitty and buggy window renumber script that uses the tmux builtin functionality
    * `tmx_asd`: `tmx_session` + `mkasd`, see the asd script somewhere else in this repo

## futari

my phone

* statusbar:

![](http://dump.dequis.org/-D-6D.png)

* battery script (in `bin/batt`)
