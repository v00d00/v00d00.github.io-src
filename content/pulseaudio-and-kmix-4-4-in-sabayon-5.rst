Pulseaudio and Kmix 4.4 in Sabayon 5
####################################
:date: 2010-03-23 22:33
:author: v00d00
:category: Linux, News, Uncategorized
:tags: alsa, kde4, pulseaudio, sabayon, sound, upmixing
:slug: pulseaudio-and-kmix-4-4-in-sabayon-5
:status: published

Recently there have been a number of issues reported in the forums and
other places of people having issues with pulseaudio and KMix after
updating to KDE 4.4.0.  I am glad to announce that most of those issues
should now be resolved with the latest round of updates being pushed out
by hard-working entropy maintainer Joost! Woot!

I identified the root of most of the problems which  seemed to be that
we were shipping a quite broken pulseaudio configuration based on
hard-wiring an ALSA module but also using the out dated HAL detection
module, this has now been corrected to using the shiny new udev
detection module by default. Other improvements to the new setup are up
mixing by default to 5.1 and LFE remixing.

I have also bumped the pulseaudio patch for KMix so that is working
nicely also, with multiple stream control working, global hotkey support
fixed and should fix most pulse + kde issues.

As usual a “equo update && equo upgrade  –ask” will grab you the latest
updates. If you have any issues please please please report a bug with
logs on the `Bugzilla <http://bugs.sabayon.org>`__.
