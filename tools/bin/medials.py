#!/usr/bin/python3

import fontParts.world as fontparts
import sys
import csv


def get_info(glyph):
    new_small_medials = [
        'u1001.sml',
        'u1003.sml',
        'u1004.sml',
        'u1008.sml',
        'u1009.sml',
        'u100A.sml',
        'u100C.sml',
        'u100D.sml',
        'u100E.sml',
        'u100F.sml',
        'u1014.sml',
        'u1016.sml',
        'u1017.sml',
        'u1018.sml',
        'u101A.sml',
        'u101B.sml',
        'u101C.sml',
        'u101D.sml',
        'u101F.sml',
        'u1020.sml',
        'u1021.sml',
        'u103F.sml',
        'u1050.sml',
        'u1051.sml',
    ]

    # if glyph.name.startswith('u1008'):
    #     return

    # name
    glyph_name = glyph.name
    if glyph_name in new_small_medials:
        glyph_name = glyph_name.upper()
    info = {'Aname': glyph_name}

    # bounding box
    bounds = glyph.bounds
    (xmin, ymin, xmax, ymax) = bounds
    info['xmin'] = xmin
    info['ymin'] = ymin
    info['xmax'] = xmax
    info['ymax'] = ymax
    info['xcenter'] = (xmin + xmax) / 2
    info['xwidth'] = xmax - xmin
    info['xclass'] = 'wide' if info['xwidth'] > 403 else 'narrow'
    info['yheight'] = ymax - ymin

    for anchor in glyph.anchors:
        if anchor.name in ('_BD', '_BS'):
            anchor.y = -100  # maybe -95

    for anchor in glyph.anchors:
        info[anchor.name + 'x'] = anchor.x
        info[anchor.name + 'y'] = anchor.y

    return info


def clone(font, source_name, target_name):
    source = font[source_name]
    target = font[target_name]

    # re-center glyph
    bounds = source.bounds
    (xmin, ymin, xmax, ymax) = bounds
    source_xcenter = (xmin + xmax) / 2

    bounds = target.bounds
    (xmin, ymin, xmax, ymax) = bounds
    target_xcenter = (xmin + xmax) / 2

    shift = source_xcenter - target_xcenter
    target.moveBy((shift, 0))

    # remove some anchors from target
    for anchor in target.anchors:
        if anchor.name != '_SJ':
            target.removeAnchor(anchor)

    # replace from the source glyph anchors that were removed
    for anchor in source.anchors:
        if anchor.name != '_SJ':
            target.appendAnchor(anchor.name, (anchor.x, anchor.y))


# Open UFO
ufo = sys.argv[1]
font = fontparts.OpenFont(ufo)

# Modify UFO

# fix x position of anchors

# wide
clone(font, 'u101E.sml', 'u1003.sml')
clone(font, 'u101E.sml', 'u100A.sml')  # maybe not this
clone(font, 'u1000.sml', 'u100C.sml')  # maybe not this
clone(font, 'u1000.sml', 'u100F.sml')
clone(font, 'u101E.sml', 'u1018.sml')
clone(font, 'u1000.sml', 'u101A.sml')
clone(font, 'u1000.sml', 'u101C.sml')
clone(font, 'u1000.sml', 'u1020.sml')  # maybe not this
clone(font, 'u1000.sml', 'u103F.sml')

# narrow
clone(font, 'u1002.sml', 'u1001.sml')
clone(font, 'u103D.sml', 'u1004.sml')
clone(font, 'u100B.sml', 'u100D.sml')
clone(font, 'u103D.sml', 'u100E.sml')
clone(font, 'u1013.sml', 'u1014.sml')
clone(font, 'u1001.sml', 'u1016.sml')  # needs to be manually shifted up (-459) to match u1001.sml
clone(font, 'u1007.sml', 'u1014.sml')

# get information and fix height of anchors
fields = set()
small_medials = {}
for glyph in font:
    if not glyph.name.endswith('.sml'):
        continue

    info = get_info(glyph)
    small_medials[glyph.name] = info
    fields.update(info.keys())

with open(ufo.replace('ufo', 'csv'), 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, sorted(fields))
    writer.writeheader()
    for glyph_name in sorted(small_medials.keys()):
        info = small_medials[glyph_name]
        writer.writerow(info)

# Save UFO
font.changed()
font.save()
font.close()
