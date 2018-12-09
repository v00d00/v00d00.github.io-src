VirtualBox 3.0.0 Now available on Sabayon Overlay
#################################################
:date: 2010-03-24 00:22
:author: v00d00
:category: Uncategorized
:slug: virtualbox-3-0-0-now-available-on-sabayon-overlay
:status: published

ust committed the three ebuilds, the first is
app-emulation/virtualbox-bin-3.0.0 and the second is
app-emulation/vitualbox-modules-3.0.0 and finally
app-emulation/virtualbox-guest-additions.

I may add the  OSE but I haven’t seen anyone using that recently, so it
got left out this time.

This are in the overlay right now and support lots of cool stuff such as
SMP (Multiple Virtual CPUs) to guest operating systems, plus guests are
now able to access OpenGL 2.0 with hardware acceleration on supported
hardware / drivers.

These will hopefully be in mainline entropy after the normal testing
process, if you want then now you can simply emerge them.
