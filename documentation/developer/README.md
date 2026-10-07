# Developer documentation

## Build options

The smith build system can take project specific options,
specified in `wscript`, to control the build.

Option | Description
-------|------------
`-r`   | only build the regular font
`-s`   | only build the main font family
`--gr` | build Graphite rules - which are no longer needed for normal builds of the project, this is only needed for internal testing, and does not even work anymore without modifications to the project
`--no2`  | not used anymore
`--bake` | not used anymore

## Attachment points

Details about attachment points are in the file [AP.md](AP.md).
Note that while there is information on the attachment points used with Graphite (GDL),
the default build does not include Graphite.
The GDL information may still be useful for understanding the project.
