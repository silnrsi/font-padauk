#!/usr/bin/python3
# encoding: utf-8
# this is a smith configuration file
# please adjust this template to your needs

# identify extra folders to include in package
DOCDIR = ["documentation", "web"]

# set the package and font family names
APPNAME = 'Padauk'
FAMILY = APPNAME

# retrieve all the authorship information from one of the master UFOs
getufoinfo('source/masters/Padauk-Regular.ufo')
# BUILDLABEL = "beta"

# mystrings = {
#    'Regular' : 'ပုံမှန်',
#    'Bold' : 'စာလုံးမဲ',
#    'Padauk' : 'ပိတောက်',
#    'Padauk Book' : 'ပိတောက်စာအုပ်'
#}
#namestrings = {
#    '-Regular' :     ('Padauk', 'Regular'),
#    '-BookBold' :    ('Padauk Book', 'Bold'),
#    '-Bold' :        ('Padauk', 'Bold'),
#    '-Book' :        ('Padauk Book', 'Regular')
#}

opts = preprocess_args({'opt' : '-r'}, {'opt' : '-s'}, {'opt' : '--no2'}, {'opt' : '--bake'}, {'opt': '--gr'})

scriptcode = 'mymr' if '--no2' in opts else 'mym2'

#tests = fonttest(extras = {
#    'xtest1' : tests({'xtest1' : cmd('cmptxtrender -p -k -e ot -s mym2 -l "${lang}" -e ot -s dflt -L mym2 -L dflt -t ${SRC[1]} -o ${TGT} --copy=otfonts --strip ${fileinfo} ${SRC[0]} ${SRC[0]}')})
#})

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

kw = {}
if '--gr' in opts:
    kw = {'graphite': gdl('source/${DS:FILENAME_BASE}.gdl',
        master = 'source/myanmar5.gdl',
        params = '-w3521 -w3530 -q -d -D -v5 -e gdlerr-' + '${DS:FILENAME_BASE}' + '.txt', make_params="-m _R",
        depends = ['source/myfeatures.gdl'])}

cmds = [
    cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['${source}']),
    cmd('gftools fix-nonhinting -q --no-backup ${DEP} ${TGT}'),
    # cmd('${TTFAUTOHINT} -n -W ${DEP} ${TGT}'),
    ]

designspace('source/Padauk.designspace',
    #params = '-l ${DS:FILENAME_BASE}_createinstance.log',
    target = process('${DS:FILENAME_BASE}.ttf', *cmds),
    instances = [] if '-r' in opts else None,
    ap = '${DS:FILENAME_BASE}.xml',
    classes = 'source/padauk_classes.xml',
    opentype = fea('source/${DS:FILENAME_BASE}.fea',
        master = 'source/padauk.fea',
        make_params="--omitaps='_R'",
        params = '-m source/${DS:FILENAME_BASE}.map',
        depends = ["source/padauk"+x+".feax" for x in
            ('_GPOS', '-mym2_GSUB')]),
    version = VERSION,
    script = 'mym2',
    extra_srcs = ['tools/bin/makegdl', 'source/myfeatures.gdl'],
    pdf = fret(params='-oi'),
    woff = woff('web/${DS:FILENAME_BASE}',
        metadata = '../source/padauk-WOFF-metadata.xml'),
    shortcircuit = False,
    **kw
)

bookpackage = package(
    appname = 'PadaukBook',
    version = VERSION,
    docdir = {'documentation': 'documentation', 'web_book': 'web'}
    )
designspace('source/PadaukBook.designspace',
    target = process('${DS:FILENAME_BASE}.ttf', *cmds),
    instances = ['Padauk Book Regular'] if '-r' in opts else None,
    ap = '${DS:FILENAME_BASE}.xml',
    classes = 'source/padauk_classes.xml',
    opentype = fea('source/${DS:FILENAME_BASE}.fea',
        master = 'source/padauk.fea',
        make_params="--omitaps='_R'",
        params = '-m source/${DS:FILENAME_BASE}.map',
        depends = ["source/padauk"+x+".feax" for x in
            ('_GPOS', '-mym2_GSUB')]),
    version = VERSION,
    script = 'mym2',
    extra_srcs = ['tools/bin/makegdl', 'source/myfeatures.gdl'],
    pdf = fret(params='-oi'),
    woff = woff('web_book/${DS:FILENAME_BASE}',
        metadata = '../source/padaukbook-WOFF-metadata.xml',
        dontship = True),
    shortcircuit = False,
    package = bookpackage,
    **kw
)

# Make language specific packages
languages = [
    ('kht', 'Namkio Khamti'),
    ('kyu', 'Deemawso'),
]

packages = {}
for dspace in ('', 'Book'):
    if '-s' in opts:
        continue
    for language in languages:
        code = language[0]
        package_name = language[1].replace(' ', '') + dspace
        langpackage = package(appname = package_name, version = VERSION)
        packages[package_name] = langpackage

        langcmds = cmds
        # langcmds.append(cmd('ttfremap -r -c ${SRC} ${DEP} ${TGT}', ['source/namkio_remap.txt'])),
        langcmds.append(cmd('psfdeflang -L ' + code + ' ${DEP} ${TGT}'))

        designspace('source/' + package_name + '.designspace',
            target = process('${DS:FILENAME_BASE}.ttf', *langcmds),
            instances = [] if '-r' in opts else None,
            ap = '${DS:FILENAME_BASE}.xml',
            classes = 'source/padauk_classes.xml',
            opentype = fea('source/${DS:FILENAME_BASE}.fea',
                master = 'source/padauk.fea',
                make_params="--omitaps='_R'",
                params = '-m source/${DS:FILENAME_BASE}.map',
                depends = ["source/padauk"+x+".feax" for x in
                    ('_GPOS', '-mym2_GSUB')]),
            version = VERSION,
            script = 'mym2',
            extra_srcs = ['tools/bin/makegdl', 'source/myfeatures.gdl'],
            pdf = fret(params='-oi'),
            shortcircuit = False,
            package = packages[package_name],
            **kw
        )

def configure(ctx) :
    ctx.find_program('ttfautohint')
#    ctx.find_program('ttx')
