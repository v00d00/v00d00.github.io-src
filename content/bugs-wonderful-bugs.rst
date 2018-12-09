Bugs! Wonderful Bugs!
#####################
:date: 2010-03-24 00:08
:author: v00d00
:category: Uncategorized
:slug: bugs-wonderful-bugs
:status: published

The Sabayon `bugzilla <http://bugs.sabayonlinux.org/>`__ recently
reached the 1000 bug milestone, note this reported bugs, currently we
are running at 75 open bugs which includes bugs for every one of the
thousands of entropy packages and new entropy package requests, which
isn’t too bad, in my opinion at least.

We have to remember that there are 3 core developers, 2 entropy
maintainers and about 1o or so core staff, which is the entire Sabayon
team and such our resources are not usually freely available.

Anyway, when browsing the bugzilla there are a few trends I would like
to comment on, firstly and the bane of Azerthoth’s existence it seems,
is that every single bug needs some basic information on a selection of
things that are relevant to the bug.

-  Hardware Issue – Dmesg, lspci or lsusb as appropriate, kernel
   version, entropy version.
-  Entropy Package Issue – Exact version number of the package, Full
   install log, Any error messages produced by the application when run
   from a command line, entropy version, branch number and Arch.
-  Live Disk Issues – Did you check the MD5, Did you burn slow?
-  Overlay/Ebuild Issue – emerge –info output, full build log, portage
   version.

Just adding these simple bits of information makes the developers lives
easier and allows the issue to get fixed quicker, so its best for
everyone.

Secondly then is the issue of bug naming. For example the below is very
bad and well, annoying:

::

     mail crashed

What does this tell the developers scanning through a buglist or seeing
a notification email? Nothing at all about the actual issue, on the
other hand a name like:

::

    mail-client/evolution-2.8.3-r2: crash if I close the mail window while checking for new POP mail

Will definitely speed up the process and mean that it canbe put into the
hands of the right people to deal with it straight away. Yay!

Finally then, is the issue of user persistence. Our bugzilla has a
number of open bugs that are waiting on users to come back to the
developers with feedback from possible fixes, version bumps, backports,
recompiles etc. The users who went to the time and effort to report the
bug now seem to have disappeared completely and the bug is just left
hanging  open for a while until it gets closed as invalid due to lack of
user input and the issue is therefore never really resolved 100%.

It is important that users stay with their issues and check it
occasionally, by default bugzilla should mail you on activity on your
bug so please keep an eye out for any updates.

So, that was enough moaning for me for today, but please try to remember
the above information, its quite simple and helps to make the process
nice and simple.
