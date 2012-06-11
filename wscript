#!/usr/bin/python
# encoding: utf-8

#from waflib import Context
import codecs, os

TESTDIR='test-suite'
VERSION='2.94'
TTF_VERSION='2.9'
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
COPYRIGHT='Copyright SIL International, all rights reserved'
LICENSE='OFL.txt'
DOCDIR='doc'

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

test = fonttest(targets = {
        'pdfs' : tex(),
        'svg' : svg(files={
                        'badSequences.txt' : '',
                        'blk_syllables.txt' : 'lang=blk',
                        'kht_extas.txt' : 'lang=kht',
                        'kht_syllables.txt' : 'lang=kht',
                        'ksw_Wordlist.txt' : 'lang=ksw',
                        'kyu_regression.txt' : 'lang=kyu',
                        'kyu_syllables.txt' : 'lang=kyu',
                        'mnw_shorto62_syllables.txt' : 'lang=mnw',
                        'mon.txt' : 'lang=mnw',
                        'my_HeadwordSyllables.txt' : 'ulon=1',
                        'pwo_syllables.txt' : 'lang=pwo',
                        'regression.txt' : '',
                        'sanskrit.txt' : '',
                        'shn_syllables.txt' : ''},
                    grsvg_gr = 'graphite',
                    grsvg_ot = 'harfbuzzng'),
        'test' : tests({
            'regression' :
                cmd('cmptxtrender -k -e ${shaper} -s "${script}" -t ${SRC[1].bldpath()} -o ${TGT} ${fileinfo} ${SRC[0].bldpath()} ${SRC[2].bldpath()}')})
    })

# import pdb; pdb.set_trace()
opts = preprocess_args({'opt' : '--nosuper'})
for f in ['', 'bold', 'book', 'bookbold'] :
    fsf = 'font-source/padauk' + f
    if len(f) :
        target = 'Padauk-' + f + '.ttf'
    else :
        target = 'Padauk.ttf'

    legacyfile = '../super/padauk' + f + '.ufo'
    if os.path.exists(src(legacyfile)) and '--nosuper' not in opts :
        source = create(fsf + '_super.sfd', cmd('ufo2sfd -a ${SRC[1].bldpath()} -b R ${SRC[0].bld_dir()} ${TGT}',
                                                [legacyfile + '/fontinfo.plist', '../super/padauk' + f + '.xml']),
                                            cmd('../bin/fixsfd ${DEP} ${TGT}'))
        legmetrics = create(fsf + '_metrics.xml',
                            cmd(src('bin/ttfgetadv') + ' ${SRC} ${TGT}', [source]))
        legxml = create(fsf + '_unicode_patched.xml',
                     cmd('xsltproc -o ${TGT} --path .. --stringparam metricsFile '
                            '${SRC[0].path_from(bld.srcnode.search("font-source"))} '
                            '${SRC[1].bldpath()} ${SRC[2].bldpath()}',
                         [legmetrics,
                             'font-source/patch_padauk_unicode.xsl',
                             'font-source/padauk_unicode.xml']))
        srcfile = legacy(fsf + '_src.sfd',
                        source = source,
                        xml = legxml,
                        ap = '../super/padauk' + f + '.xml')
    else :
        srcfile = fsf + '_src.sfd'

#    import pdb; pdb.set_trace()
    fnt = font(target = process(target, 
#                       name(mystrings[namestrings[f][0]], lang='my', nopost=1,
#                            full=(((mystrings[namestrings[f][0]] + " " + mystrings[namestrings[f][1]])
#                                if 'bold' in f else mystrings[namestrings[f][0]]))),
                        name(namestrings[f][0], lang='en-US', subfamily = namestrings[f][1]),
                        cmd('hackos2 -u 1 ${DEP} ${TGT}')),
                version = TTF_VERSION,
                license = ofl("Padauk"),
                copyright = COPYRIGHT,
                source = srcfile,
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
                script = 'mymr',
                extra_srcs = [fsf + '_src.ttf', 'bin/makegdl', 'font-source/myfeatures.gdl']
            )
#    if 'bold' not in f :
#        process(fnt.target, cmd('${TTFNAME} -r 17 ${DEP} ${TGT}'))
    
    if os.path.exists(src(legacyfile)) and '--nosuper' not in opts :
        process(fnt.ap, cmd('xsltproc -o ${TGT} '
                        '--stringparam metricsFile ${SRC[0].path_from(bld.srcnode.search("font-source"))} '
                        '--stringparam fontXml ${SRC[1].path_from(bld.srcnode.search("font-source"))} '
                        '${SRC[2].bldpath()} ${DEP}',
                        [legmetrics, legxml, fsf + '_src.xsl']))
        

def configure(ctx) :
    ctx.env['MAKE_GDL'] = 'perl ' + src('bin/makegdl')

def srcdist(ctx) :
    for p in package.packages() :
        for f in p.fonts :
            try :
                del f.legacy
            except :
                pass
            
    
