QDbusViewer and Integer Arrays
##############################
:date: 2011-07-20 14:24
:author: v00d00
:category: Linux, Sabayon
:tags: array, Dbus, Development, integer, qdbusviewer
:slug: qdbusviewer-and-integer-arrays
:status: published

This post is a "things that should be easily googleable but aren't" type
post.

When an application is returning a dbus array of integers (Dbus type
'ai'), qdbusviewer will give you a message similar to:

::

    unable to find method <MethodName> on path <DbusPath> in interface <Interface>

This message is sign of a failing in qdbusviewer and not in the
application (as I discovered to today after a couple of hours of
confusion!)

The solution is to use another dbus client, for example:

::

    $ dbus-send --session --type=method_call --print-reply --dest=<Interface> <DbusPath> <MethodName> 
    method return sender=:1.165 -> dest=:1.171 reply_serial=2
    array [       int32 0       int32 1    ]

Hopefully that will save someone some pain.
