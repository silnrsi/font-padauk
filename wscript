#!/usr/bin/python
# encoding: utf-8

import codecs, os

TESTDIR='tests'
VERSION='3.901'
TTF_VERSION='3.901'
APPNAME='Padauk'
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
COPYRIGHT='Copyright 2018 SIL International, all rights reserved'
#LICENSE='OFL.txt'
DOCDIR='documentation'
#VCS='git'
STANDARDS='tests/reference'
out = 'results'
#README="README.md"

mystrings = {
    'Regular' : 'ပိုမှန်',
    'Bold' : 'စာလုံးမဲ',
    'Padauk' : 'ပိတောက်',
    'Padauk Book' : 'ပိတောက်စာအုပ်'
}
namestrings = {
    '-Regular' :     ('Padauk', 'Regular'),
    '-BookBold' :    ('Padauk Book', 'Bold'),
    '-Bold' :        ('Padauk', 'Bold'),
    '-Book' :        ('Padauk Book', 'Regular')
}

opts = preprocess_args({'opt' : '--no2'})
devver = getversion()

scriptcode = 'mymr' if '--no2' in opts else 'mym2'

#tests = fonttest(extras = {
#    'xtest1' : tests({'xtest1' : cmd('cmptxtrender -p -k -e ot -s mym2 -l "${lang}" -e ot -s dflt -L mym2 -L dflt -t ${SRC[1]} -o ${TGT} --copy=otfonts --strip ${fileinfo} ${SRC[0]} ${SRC[0]}')})
#})

ftmlTest('tools/ftml.xsl')

# for f in ['-Regular', '-Bold', '-Book', '-BookBold'] :

designspace('source/Padauk.designspace',
    params = '-l ${DS:FILENAME_BASE}_createinstance.log',
    target = process('${DS:FILENAME_BASE}.ttf',
        cmd('${TTFAUTOHINT} -n -W ${DEP} ${TGT}'),
#        cmd('${TTX} -f -o ' + target + '.ttx' + ' ${DEP}; ${TTX} -f -o ${TGT} ' + target + '.ttx')
    ),
#    version = TTF_VERSION,
#    license = ofl("Padauk"),
#    copyright = COPYRIGHT,
    ap = '${DS:FILENAME_BASE}.xml',
    classes = 'source/padauk_classes.xml',
    opentype = fea('source/${DS:FILENAME_BASE}.fea',
        master = 'source/padauk.fea',
        make_params="--omitaps='_R'",
        buildusingsilfont = True,
        params = '-m source/${DS:FILENAME_BASE}.map',
        depends = ["source/padauk"+x+".feax" for x in
            ('_GPOS', '-mym2_GSUB', '-dflt_GSUB')]),
    graphite = gdl('source/${DS:FILENAME_BASE}.gdl',
        master = 'source/myanmar5.gdl',
        params = '-w3521 -w3530 -q -d -D -v2', make_params="-m _R",
        depends = ['source/myfeatures.gdl']),
    script = ['mym2', 'DFLT'],
    extra_srcs = ['tools/bin/makegdl', 'source/myfeatures.gdl'],
    pdf = fret(params="-r -oi"),
    woff = woff('web/${DS:FILENAME_BASE}.woff', params = '-v ' + VERSION + ' -m ../source/padauk-WOFF-metadata.xml')
)

def configure(ctx) :
    ctx.find_program('ttfautohint')
    ctx.find_program('ttx')
