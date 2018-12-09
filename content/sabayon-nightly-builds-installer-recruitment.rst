Sabayon - Nightly Builds, Installer & Recruitment
#################################################
:date: 2010-04-26 09:47
:author: v00d00
:category: Gentoo, News, Sabayon, Uncategorized
:tags: 5.3, artwork, entropy, molecule, nightly builds, sabayon, sabayon 5.3, sabayon beta
:slug: sabayon-nightly-builds-installer-recruitment
:status: published

|image0|

Well, it’s been a while since I’ve blogged, so I think its time I
started doing it more regularly again. So what is going down in Sabayon
HQ? Well there have been many interesting developments recently which I
want to talk about.

Firstly we have the brand spanking new shiny Anaconda installer, this
has been well publicised by `wolfden <http://wgo.wolf911.us/?p=357>`__
and `Lxnay <http://planet.sabayon.org/?p=1487>`__ and is really shaping
up nicely, its about time the installer got an update and it is looking
awesome, everyone has been testing (and breaking) the new installer and
progress looks excellent. This is of course mainline Anaconda that is
used in Fedora and RHEL et al and has inherited all the great features
from it with some new sabayon specific stuff too, this version is more
closely based on vanilla upstream git and as such we should inherit all
the work that is being done upstream a lot faster.

Next up is nightly builds of sabayon, yes you read that correctly. The
idea is that you will have one ISO on your hard disk which you will keep
updated using rsync’s binary diff capabilities and the Sabayon rsync
servers to only update the parts of the ISO that have changed, this is
how we have been distributing ISOs to testers for a while now and is
much quicker and easier than the old version using Xdelta. What has been
done is that we have a scripted molecule install which creates a new ISO
at 0200 UTC every night using the latest packages from the mainline
repository, from these images the rysnc is updated and you can download
the changes, simple but clever if you ask me.

Finally – recruitment. Getting people to work on an open source project
is never easy, its not easy to find volunteers for anything in reality
as time is such an expensive commodity. I have decided to step down from
my position as artwork guy and as such Sabayon is looking for a
replacement, if you have some design and theming skills, or even if you
don’t why not get in
`contact <mailto:ian.whyman@sabayon.org?subject=Artwork%20Replacement>`__
with me and I’ll get you started.

You will need a good eye, ability to work in a team an interest in
Sabayon and ability to use SVG, it would be preferred if you had some
knowledge of bash scripts, ebuilds and linux theming, but we can train
you if your designs are great. Once again, please do get in contact,
either mail me, start a thread in the forums and show us your stuff or
leave a comment even.

…and that’s all I can think of for now.

.. |image0| image:: http://upload.wikimedia.org/wikipedia/commons/b/be/Sabayon4foot.png
   :width: 131px
   :height: 131px
