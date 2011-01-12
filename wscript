#!/usr/bin/python
# encoding: utf-8

#from waflib import Context
import codecs

TESTDIR='test-suite'
VERSION='2.7.5'
TTF_VERSION='2.705'
APPNAME='padauk'
DESC_SHORT='Burmese Unicode 6 truetype font with OT and Graphite support'
DESC_LONG = ''
COPYRIGHT='Copyright SIL International, all rights reserved'
LICENSE='OFL.txt'

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

#def init(ctx) :
#    Context.load_tool("font", tooldir=["/home/mhosken/Work/shorts/waf/trunk/bin"])
test = fonttest(targets = { 'pdfs' : tex(), 
                            'svg' : svg(files={
                                            'ksw_Wordlist.txt' : 'lang=ksw',
                                            'kyu_wdl.txt' : 'lang=ksw',
                                            'my_HeadwordSyllables.txt' : 'ulon=1'},
                                        grsvg_gr = 'graphite',
                                        grsvg_ot = 'icu'
                                       )}
               )

for f in ['', 'bold', 'book', 'bookbold'] :
    fsf = 'font-source/padauk' + f
    if len(f) :
        target = 'Padauk-' + f + '.ttf'
    else :
        target = 'Padauk.ttf'

    legacyfile = '../super/padauk' + f + '.ttf'
#    import pdb; pdb.set_trace()
    fnt = font(target = process(target, name(namestrings[f][0], lang='en-US',
                                                full=((namestrings[f][0] + " " + namestrings[f][1]) if 'bold' in f else namestrings[f][0])),
                                        name(mystrings[namestrings[f][0]], lang='my',
                                                full=(((mystrings[namestrings[f][0]] + " " + mystrings[namestrings[f][1]]) if 'bold' in f else mystrings[namestrings[f][0]])))),
                version = TTF_VERSION,
                license = ofl("Padauk"),
                copyright = COPYRIGHT,
                source = legacy(fsf + '_src.ttf',
                                source = legacyfile,
                                xml = create(fsf + '_unicode_patched.xml',
                                             cmd('xsltproc -o ${TGT} --path .. --stringparam metricsFile '
                                                    '${SRC[0].path_from(bld.srcnode.search("font-source"))} '
                                                    '${SRC[1].bldpath()} ${SRC[2].bldpath()}',
                                                [create(fsf + '_metrics.xml',
                                                        cmd('../bin/ttfgetadv ${SRC} ${TGT}', [legacyfile])),
                                                 'font-source/patch_padauk_unicode.xsl',
                                                 'font-source/padauk_unicode.xml'])),
                                ap = '../super/padauk' + f + '.xml'),
                ap = fsf + '.xml',
                classes = 'font-source/padauk_classes.xml',
                opentype = volt(fsf + '.vtp',
                                master = fsf + '_src.vtp',
                                make_params = '-t -m "_R _LL _L"',
                                params = '-i -x font-source/padauk' + f + '_tt.xml'),
                graphite = gdl(fsf + '.gdl',
                                master = 'font-source/myanmar5.gdl',
                                params = '-w3521 -q -d -v2'),
                tests = test,
                script = 'mymr'
            )

    process(fnt.ap, cmd('xsltproc -o ${TGT} '
                        '--stringparam metricsFile ${SRC[0].path_from(bld.srcnode.search("font-source"))} '
                        '--stringparam fontXml ${SRC[1].path_from(bld.srcnode.search("font-source"))} '
                        '${SRC[2].bldpath()} ${DEP}',
                        [fsf + '_metrics.xml', fnt.legacy.xml, fsf + '_src.xsl']))

def configure(ctx) :
    ctx.env['MAKE_GDL'] = 'perl ../bin/makegdl'
