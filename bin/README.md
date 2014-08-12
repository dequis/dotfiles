Small scripts and shell scripts I wrote

* asd: Returns a placeholder word selected from an english dictionary filtered to pick easy to remember words. Also saves it to the X clipboard.
* namehash: generates 5 character filenames that hold a portion of the file md5 hash
* zxc: uploads to dump.dequis.org using filenames returned by namehash
* scr: takes a screenshot and uploads it using zxc. uses [escrotum](https://github.com/Roger/escrotum) instead of scrot
* lsr: list N most recent files, where N is the first argument. wraps ls mostly transparently
* sendmail: cheapest sendmail, i made this one back in 2009, place in /usr/bin/sendmail and get cron emails and other stuff in ~/mail
* tz: show the current time of a specified timezone
* ixwrap: wrap a command and send the output to [ix](http://ix.io), including the commandline itself
* dix: shitty replacement for ix - uploads to dump instead using zxc

tmux related scripts are in tmux/bin/ in this repo
