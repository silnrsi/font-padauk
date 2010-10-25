#!/usr/bin/python

#from waflib import Context

TESTDIR='test-suite'
VERSION='2.7.5'
TTF_VERSION='2.705'
APPNAME='padauk'
DESC_SHORT='Burmese Unicode 6 truetype font with OT and Graphite support'
DESC_LONG = ''
COPYRIGHT='Copyright SIL International, all rights reserved'
LICENSE='OFL.txt'

#def init(ctx) :
#    Context.load_tool("font", tooldir=["/home/mhosken/Work/shorts/waf/trunk/bin"])
for f in ['', 'bold', 'book', 'bookbold'] :
    fsf = 'font-source/padauk' + f
    if len(f) :
        target = 'Padauk-' + f + '.ttf'
    else :
        target = 'Padauk.ttf'

    legacyfile = '../super/padauk' + f + '.ttf'
    fnt = font(target = process(target, name("Padauk Book" if 'book' in f else "Padauk", lang="en-US")),
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
                                params = '-w3521 -q -d -v2')
            )

    process(fnt.ap, cmd('xsltproc -o ${TGT} '
                        '--stringparam metricsFile ${SRC[0].path_from(bld.srcnode.search("font-source"))} '
                        '--stringparam fontXml ${SRC[1].path_from(bld.srcnode.search("font-source"))} '
                        '${SRC[2].bldpath()} ${DEP}',
                        [fsf + '_metrics.xml', fnt.legacy.xml, fsf + '_src.xsl']))

def configure(ctx) :
    ctx.env['MAKE_GDL'] = 'perl ../bin/makegdl'
