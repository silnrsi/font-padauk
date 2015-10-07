#!/usr/bin/python
# encoding: utf-8

import codecs, os

TESTDIR='test-suite'
VERSION='2.98.2'
TTF_VERSION='2.982'
APPNAME='padauk'
SRCDIST="{0}-src.{1}".format(APPNAME, VERSION)
DESC_SHORT='Burmese Unicode 6 truetype font with OT and Graphite support'
DESC_LONG = '''
Padauk is a pan Burma Unicode font designed to support all the languages
that use the Burmese script. It supports all the characters in the Burmese
blocks for Unicode 6.0 and has OpenType and Graphite tables in it.

There is specific language styling support for: kht, ksw, kyu

There is feature support in Graphite for the following features: kdot, fdot,
lldt, wtri, ulon, utal, dotc, hsln (value: 0-2), nnya, vtta
'''
DEBPKG='ttf-sil-padauk'
COPYRIGHT='Copyright 2013 SIL International, all rights reserved'
LICENSE='OFL.txt'
DOCDIR='doc'
VCS='hg'

mystrings = {
    'Regular' : 'ပိုမှန်',
    'Bold' : 'စာလုံးမဲ',
    'Padauk' : 'ပိတောက်',
    'Padauk Book' : 'ပိတောက်စာအုပ်'
}
namestrings = {
    '' :            ('Padauk', 'Regular'),
    'bookbold' :    ('Padauk Book', 'Bold'),
    'bold' :        ('Padauk', 'Bold'),
    'book' :        ('Padauk Book', 'Regular')
}

opts = preprocess_args({'opt' : '--no2'})

scriptcode = 'mymr' if '--no2' in opts else 'mym2'

#                sfd_master = 'font-source/master.sfd',
                graphite = gdl('padauk' + f + '.gdl',
                                master = 'font-source/myanmar5.gdl',
                                params = '-w3521 -w3530 -q -d -v2', make_params="-m _R",
                                depends = ['font-source/myfeatures.gdl']),
#                tests = test,
                script = ['mym2'],
                extra_srcs = [fsf + '_src.ttf', 'bin/makegdl', 'font-source/myfeatures.gdl'],
                pdf = fret()
            )
