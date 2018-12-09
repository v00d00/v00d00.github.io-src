#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ian Whyman'
SITENAME = 'v00d00.net'
SITEURL = ''

THEME = 'themes/pelican-alchemy/alchemy'

STATIC_PATHS = ['images', 'static']

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# http://docs.getpelican.com/en/stable/plugins.html#how-to-use-plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify']

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}

SITESUBTITLE = "/dev/random"
SITEIMAGE = "/images/terminal-solid.svg width=150 height=150"

LINKS = (
)

ICONS = (
    ('github', 'https://github.com/v00d00'),
    ('twitter', 'https://twitter.com/thevoodoo'),
)

HIDE_AUTHORS = True
