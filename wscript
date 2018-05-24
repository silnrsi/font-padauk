#!/usr/bin/python
# encoding: utf-8

import codecs, os

TESTDIR='tests'
VERSION='3.004'
TTF_VERSION='3.004'
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

for f in ['-Regular', '-Bold', '-Book', '-BookBold'] :
    fsf = 'source/masters/Padauk' + f
    sf  = 'source/Padauk' + f
    target = namestrings[f][0].replace(' ', '') + '-' + namestrings[f][1].replace(' ', '')

    fnt = font(target = process(target + '.ttf',
                        name(namestrings[f][0], lang='en-US', subfamily = namestrings[f][1]),
                        cmd('${TTFAUTOHINT} -n -W ${DEP} ${TGT}'),
                        cmd('${TTX} -f -o ' + target + '.ttx' + ' ${DEP}; ${TTX} -f -o ${TGT} ' + target + '.ttx')
                        ),
                version = TTF_VERSION,
#                license = ofl("Padauk"),
                copyright = COPYRIGHT,
                source = fsf + '.ufo',
                ap = sf + '.xml',
                classes = 'source/padauk_classes.xml',
#                buildusingfontforge = 1,
                opentype = fea('source/padauk' + f + '.fea',
                                old_make_fea = True,
                                master = sf + '_ext.fea',
                                preinclude = sf + '_init.fea',
                                make_params="-m _R -z 8 --markattach BSM,LM,LLM=cLowerMarkAttach --markattach BDM=",
                                depends = map(lambda x:"source/padauk-"+x+".fea", 
                                    ('mym2_features', 'mym2_GSUB', 'dflt_GSUB'))),
#                sfd_master = 'source/master.sfd',
                graphite = gdl('padauk' + f + '.gdl',
                                master = 'source/myanmar5.gdl',
                                params = '-w3521 -w3530 -q -d -D -v2', make_params="-m _R",
                                depends = ['source/myfeatures.gdl']),
#                tests = test,
                script = ['mym2', 'DFLT'],
                extra_srcs = ['tools/bin/makegdl', 'source/myfeatures.gdl'],
                pdf = fret(params="-r -oi"),
#                tests = tests
                woff = woff(params = '-v ' + VERSION + ' -m ../source/padauk-WOFF-metadata.xml')
            )

def configure(ctx) :
    ctx.find_program('ttfautohint')
    ctx.find_program('ttx')
