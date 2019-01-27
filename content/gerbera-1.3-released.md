Title: Gerbera Media Server 1.3 Now Available
Date: 2018-04-29 10:20
Category: Gerbera
Tags: gerbera, mediaserver, upnp
Slug: gerbera-1-3-now-available
Authors: Ian Whyman

I am happy to announce that Gerbera Media Server 1.3.0 is now available.

We have had contributions from 12 different contributors, putting together 161 changes since 1.2\. Thank you so much to everyone involved!

A special thank you to [Eamonn](https://github.com/elmodaddyb) for all of his ongoing hard work!

## Changes

- C++17 is now required to build (clang, gcc-7, gcc-8)
- Improved Samsung DTV Support (Still not entirely complete, but some more models may work)
- Added FLAC, Wavpack, DSD to default configuration
- Fixed Transcoding bugs with HTTP Protocol
- Properly handle upnp:date for Album sorting on UPNP devices
- Exposed resource options to import scripts (audio channels etc)
- Added support for Classical music tags: Composer, Conductor, Orchestra
- Fix UI update bug for macOS
- Add online-content examples
- Improve scripted installation
- Add configurable title for UI Home
- Fix SQL bugs
- Create Gerbera Homebrew Tap (for macOS High Sierra & Mojave)
- Various bug fixes and ongoing refactoring
- Add CentOS install instructions

## Get it

Find out how to [install Gerbera](http://docs.gerbera.io/en/latest/install.html).

Download the source from [Github](https://github.com/gerbera/gerbera/releases/tag/v1.3.0).