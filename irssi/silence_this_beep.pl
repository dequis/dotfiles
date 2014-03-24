# /silence_this_beep
#
# Command to silence this beep (during an event), or the next one.
#
# Usage with trigger.pl:
# /trigger add -privmsgs -masks 'nickname!*@*' -command silence_this_beep
#
# You probably also want to add the nick to activity_hide_targets

use strict;
use warnings;

use Irssi;

our $VERSION = '1.0';
our %IRSSI = (
  authors     => 'dx',
  name        => 'Silence this beep',
  description => 'Command to silence this beep, or the next one.',
  license     => 'MIT',
);

sub beep_silencer {
    Irssi::signal_stop();
    Irssi::signal_remove('beep', 'beep_silencer');
}

Irssi::command_bind silence_this_beep => sub {
    Irssi::signal_add_first('beep', 'beep_silencer')
};
