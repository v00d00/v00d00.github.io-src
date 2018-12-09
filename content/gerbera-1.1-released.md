Title: Gerbera 1.1 Released
Date: 2017-09-29 10:20
Category: Gerbera
Tags: gerbera, mediaserver, upnp
Slug: gerbera-1-1-released
Authors: Ian Whyman

[![Gerbera Logo](/images/gerbera-logo-horiz.png)](https://gerbera.io/)

I am proud to announce the second release of the Gerbera media server. There have been over 110 commits since 1.0 from 13 awesome contributors.

## So whats new?

### Modern UI Preview

@elmodaddyb has been hard at work on the next generation UI for Gerbera. Built using Boostrap4 with TDD methodologies; this will be the default Web UI in a future version. This release includes a read only preview of the interface. Access it by visiting `gerbera.html` on your v1.1 install e.g. `http://localhost:49152/gerbera.html`

You can keep track of the progress [on the New UI github issue](https://github.com/gerbera/gerbera/issues/84).

![](https://user-images.githubusercontent.com/8599799/28802450-7605ea34-7624-11e7-8185-3425a6000d32.png)

### Raspberry Pi / 32bit fixes

Post 1.0 we had a number of issues reported by Raspberry Pi users. Investigation found that we were not properly supporting large files in the build system for 32 bit hosts. We have added LFS support and Gerbera now runs great on Raspberry Pi!

Unfortunately this issue highlighted a bug in libupnp - client apps should fail to build when their LFS state did not match libupnp. This has been [fixed](https://github.com/ukleinek/pupnp/commit/74c98de50a03f603d6fedf3d4f0377b274d54d75) upstream.

### Video thumbnail support

Support for video thumbnails using FFMpegThumbnailer is back. You can enable video thumbnail support by passing `-DWITH_FFMPEGTHUMBNAILER=1` at build time and set `<ffmpegthumbnailer enabled="yes">` in your config file to get pretty thumbnails for your video files.

### Protocol Extensions

You can now enable incomplete DLNA protocol extensions in Gerbera. With this option Gerbera makes changes to the data sent to devices to enable support for less picky DLNA renderers. It also enables AlbumArt/Thumbnails on some devices (e.g. various LG TVs).

Full DLNA support is high on the ToDo list, however we are still waiting for custom HTTP header support in libupnp before we can implement it. If you want to help (or know somebody who can), [please check out libupnp's github]https://github.com/mrjimenez/pupnp/pull/49).

### BSD Fixes

We have had some great feedback and patches from BSD users since 1.0 and we have merged user patches to add support for INotify via libinotify and to add support for native UUID generation functions.

### Album Artists

AlbumArtist metadata is now extracted from media files (where supported) and is used to populate the "creator" field for albums. It is also available for use with custom JavaScript powered layouts.

### OSX improvements

@elmodaddyb spent some time getting Gerbera running on OSX and [produced some build instructions](https://github.com/gerbera/gerbera#on-macos), we now ship an [OSX Launchd script](https://github.com/gerbera/gerbera/tree/master/scripts/launchd) in the repo.

### Other notable changes

*   MySQL is no longer enabled by default in CMake, you will need to pass `-DWITH_MYSQL=1` at build time if you want support. We recommend using SQLite.

*   The `--pidfile` option has been removed, as we removed the `--daemon` option in the previous release retaining `--pidfile` option did not make sense. Please update your scripts if you were using this flag.

*   We have moved to a new github organisation, check us out at [github.com/gerbera](https://github.com/gerbera) 👍

And more!

As always a huge thanks to everyone who has contributed to this release.

See [how to install Gerbera](https://github.com/gerbera/gerbera#installing) on your OS/Distro or [download the source](https://github.com/gerbera/gerbera/releases/tag/v1.1.0) from Github.

### Note on LibUPnP support

This release supports <=libupnp 1.8.2 due to breaking changes in libupnp master branch, 1.2 will most likely require >=1.8.3.