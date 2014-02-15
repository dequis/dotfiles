# st config

st is [simple terminal](http://st.suckless.org/)

Interesting stuff here:

 * Spoilertext patch - if background and foreground are the same, selected text will appear as if it was white on black. Created against git cdb3b189 (2014-02-01)
 * The delete key works everywhere. The st FAQ has an entry for "Why doesn’t the Del key work in some programs?". It blames the programs and tells you to fix all of them individually. Fuck that.
 * Added LockMask to ignoremod to ignore caps lock too
 * Keybindings for ctrl-shift-left/right
 * Right click / control right click send `` `#`` and `` `@`` which are my tmux split window commands. I don't actually use this but I think it's a neat idea.

Might be worth noting that this config is much closer to the defaults than the urxvt one, most stuff worked out of the box.
