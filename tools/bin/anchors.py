#!/usr/bin/python3

import fontParts.world as fontparts
import sys

# Open UFO
ufo = sys.argv[1]
font = fontparts.OpenFont(ufo)

# Modify UFO

for glyph in font:
    if not glyph.name.endswith('.sml'):
        continue
    if glyph.name.startswith('u1008'):
        continue
    bounds = glyph.bounds
    if bounds is None:
        continue
    (xmin, ymin, xmax, ymax) = bounds
    xcenter = (xmin + xmax) / 2

    glyph.appendAnchor('_SJ', (xcenter, ymax + 25))
    glyph.appendAnchor('SJ', (xcenter, ymin - 25))

    if glyph.name in ('u100A.sml', 'u100C.sml'):
        for anchor in glyph.anchors:
            if anchor.name == '_BSM':
                glyph.appendAnchor('_BD', (anchor.x, anchor.y))

# Save UFO
font.changed()
font.save()
font.close()
