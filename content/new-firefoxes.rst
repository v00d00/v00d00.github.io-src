New Firefoxes
#############
:date: 2010-03-24 00:21
:author: v00d00
:category: Uncategorized
:slug: new-firefoxes
:status: published

Yesterday I pushed `3 new firefox
versions <http://gitweb.sabayonlinux.org/?p=overlay.git;a=tree;f=www-client/mozilla-firefox;hb=HEAD>`__
into the sabayon overlay, “whats so great about these firefoxes?” I hear
you ask, well there are a few things.

Firstly they branded correctly as “Sabayon” which means sites that pick
up on what OS your using will show you as usiong Sabayon and not Gentoo.
For example on my `blog <http://main.v00d00.net/>`__, when you post a
comment you will get a little Sabayon logo by your comment! (had to
patch the wordpress plugin, but it has been accepted upstream now)

Secondly they now use the Sabayon homepage as default, not gentoo.org,
which means in theory we could remove the firefox profile from skel (and
have one less thing to worry about). However skel also has some setting
to make sure Flash and Java work OOTB so maybe not a good idea to that
just yet, but we will see.

Finally, there are newer versions! woop! By default everyone will get an
upgrade to firefox 3.5\_rc2 (-r10). However there is still an older
(stabler) version of 3.0.11(-r10) available for those who dont want to
run a RC browser.

For the brave there is also a bleeding edge 9999(-r1) ebuild which pulls
the very latest code directly from the mozilla repository. I use the
9999 build with 0 problems. Please report any issues you encounter with
these new builds to the `sabayon
bugzilla <http://bugs.sabayonlinux.org/>`__.

4.2 is chugging along with testing nicley and the testers have just got
a pre-alpha of the CoreCD version too.  As always keep an eye on planet
for the latest updates
