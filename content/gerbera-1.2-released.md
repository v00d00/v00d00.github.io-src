Title: Gerbera Media Server 1.2 Now Available
Date: 2018-04-29 10:20
Category: Gerbera
Tags: gerbera, mediaserver, upnp
Slug: gerbera-1-2-now-available
Authors: Ian Whyman

I am happy to announce that Gerbera Media Server 1.2.0 is now available.

We have had contributions from 15 different contributors, putting together 172 changes since 1.1\. Thank you so much to everyone involved!

## New Web UI

The most noticeable change since v1.1 will be new awesome new Web UI. We shipped a beta of this in the previous version, but now it it is ready for prime time, and enabled by default.

![filesystem-view](/images/filesystem-view.png)

Thank you to [Eamonn](https://github.com/elmodaddyb) for all of his ongoing hard work!

![gerbera-import-webui](/images/gerbera-import-webui.gif)

## UPnP Search

Gerbera now supports searching! This allows clients to offload the hard work of finding your media to the server, this is both faster an more reliable than clients doing it themselves.

If you are a BubbleUPnP user on android, this means the "Random Tracks" feature now works.

Thank you to [astylos](https://github.com/astylos) for this great feature!

## Improved Docs

Some of you have mentioned that Gerbera's documentation, as with many other free software projects, has not been as good as it could or should have been.

We are happy to point you to [docs.gerbera.io](http://docs.gerbera.io/), kindly hosted by [Read the Docs](https://readthedocs.org/).

If you wish to help, it is very easy to get started, simply open a pull request against Sphinx files in the `doc` folder.

## Bye, Youtube

Youtube support has not worked for a long time so it has been removed from the code base entirely. Similar functionality may return in a future release.

## Bugfixes

*   Fixed AUXDATA truncation with UTF-8 characters.
*   Improved message when libupnp fails to bind correctly.
*   Allow use of FFMpeg to extract AUXDATA
*   Duktape JS scripting errors are now visible in log file
*   Fixed a crash in EXIV2 image handler.
*   Fixed "root path" sometimes missing for scripted layouts.

## Get it

Find out how to [install Gerbera](http://docs.gerbera.io/en/latest/install.html).

Download the source from [Github](https://github.com/gerbera/gerbera/releases/tag/v1.2.0).