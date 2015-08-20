ABOUT:

ANIMATED is a simple Python script written by Sophie Kirschner.
e-mail: sophiek@pineapplemachine.com

Its purpose is to supersede the old SWANTBLS.EXE program which served a similar
purpose of eating up an input file and outputting an ANIMATED lump. These lumps
allow you to add animated flats and textures to Boom and ZDoom ports without
overriding vanilla animations.

The author can't be held liable for damage done by this program. Anyone is free
to distribute and modify this program as they see fit provided they give credit
where it's due.

HOW TO:

Run `python animated.py` to input a files defining in combination any number of
animations, and output a lmp file formatted for Boom and ZDoom compatibility.
The default input paths are ANIMATED.json, which might contain the animations
you're adding, and VANILLA.lmp, which contains all the animations in vanilla.
Since Boom loads only the most recent ANIMATED lump and they aren't cumulative,
it's necessary to include the vanilla animations in the lump in this way.

Input and output paths can be specified using the -i and -o arguments. For
example: `python animated.py -i myanims.json vanilla.lmp -o myanims.lmp`.

The default output path is ANIMATED.lmp. The outputted lmp should be added to a
wad using a utility such as Slade.

Example of what input json might look like, defining some vanilla animations:

[
    ["tex", "BFALL1", "BFALL4", 4],
    ["tex", "ROCKRED1", "ROCKRED3", 3],
    ["flat", "NUKAGE1", "NUKAGE3", 3],
    ["flat", "SLIME09", "SLIME12", 4]
]

The first value in each item should be one of "tex", "flat", or "texdecal". This
tells the source port what sort of animation this is.

The second value is the first texture in the sequence. The third is the final
texture. All textures in between must be numerically sequential like vanilla
animations. For example, BFALL1 -> BFALL2 -> BFALL3 -> BFALL4. 

The fourth and final value is a number of delay frames. Lower numbers cause the
animation to go faster. All vanilla animations have delays of between 2 and 4
frames.
