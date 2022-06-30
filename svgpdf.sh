#!/bin/bash
#mkdir "$PWD"/pdf
for file in $PWD/*.svg
    do
        /Applications/Inkscape.app/Contents/MacOS/inkscape  --without-gui --export-pdf=${filename%.svg}.pdf "$file"
    done
