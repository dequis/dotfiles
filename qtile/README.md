# qtile config

http://qtile.org/

Bar style:

![](http://i.imgur.com/K8aDcPb.png)

Interesting stuff here:

 * win+x, win+shift+x open xprop and xwininfo
 * win+shift+r runs a command and makes it show the output in qtile using the "qtinfo" script i wrote (based on qtb)
 * win+control+a switches to AwesomeWM using an `exec` syscall
 * One of the few configs out there that uses dgroups!
 * Using `intrusive=True` and `break_on_match=False` for the floating apps rule
