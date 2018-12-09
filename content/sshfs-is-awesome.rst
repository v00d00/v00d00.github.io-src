SSHFS is Awesome
################
:date: 2010-03-24 00:18
:author: v00d00
:category: Opinion, Sabayon
:tags: Awesome!, sshfs
:slug: sshfs-is-awesome
:status: published

Now sometimes you find a bit of Linux goodness that makes your geeky
bits tingle, I found one recently, its called SSHFS, and its part of the
awesome fuse framework. As you may have guessed it allows you to mount a
file system through a SSH connection, this means it can be read from and
saved to as any other part of your local file-system!

This leads to some cool possibilities, mounting a remote server over a
secure connection for easy file uploads and downloads, the ability to
run local scripts on remote files (WIN) and more.

Its ultra easy to use:

::

    emerge -av1 sys-fs/sshfs-fuse

or

::

    equo install sshfs-fuse

then

::

    sshfs username@server:/path/to/mountpoint

I have it set up to run when I login and I use RSA key based auth so no
passwords for ultraconvience at the price of a little bit of security.

Just thought I’d spread the word a bit.
