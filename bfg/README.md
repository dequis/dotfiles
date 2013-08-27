# bfgminer scripts

these scripts use the rpc interface of bfgminer to do cool stuff. RPC scripts depend on netcat and jshon.

* bfg-get-intensity: what it says on the tin.
* bfg-set-intensity: parameter: either absolute or relative intensity value, where relative is formatted like "+1" or "-1"
* bfg-status-widget: shows intensity, temperature and hashrate in a nice format to use as tmux statusbar widget.
* bfg-idle-check: called as a cron job, uses the [xprintidle](https://aur.archlinux.org/packages/xprintidle/) command to increase intensity after periods of idleness.
