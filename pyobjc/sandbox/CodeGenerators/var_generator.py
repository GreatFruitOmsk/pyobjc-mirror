# Non-string variables
#
# This is script is rather fragile, and tuned to the MacOS 10.1 header-files.
#
# We should probably use bgen, but how does one use that tool?

import re
import os
from dupfile import *

IDENT='[A-Za-z_][A-Za-z0-9_]*'
attribute_unused=re.compile(r'__attribute__\(\(_?_?unused_?_?\)\)')

def process_file(outfp, filename, match_prefix='', ignore_list=()):

    MATCH_RE=re.compile(r'%(match_prefix)s\s+(const\s+)?(%(IDENT)s)\s+(%(IDENT)s\s*(,\s*%(IDENT)s)*)\s*;'%{'match_prefix':match_prefix, 'IDENT':IDENT})

    fp = open(filename, 'r')

    outfp.write("\n\t/* From: %s */\n"%os.path.basename(filename))

    in_class = 0

    for ln in fp.xreadlines():
        ln = attribute_unused.sub(' ', ln.strip())
        # Skip declarations in objective-C class definitions
        if not in_class:
            if ln.startswith("@interface"):
                in_class = 1
                continue
        else:
            if ln.startswith("@end"):
                in_class = 0
            continue

        m = MATCH_RE.search(ln)
        if not m: continue


        tp = m.group(2)
        ident = m.group(3)

        vals = [ x.strip() for x in ident.split(',') ]
        for  v in vals:
            if v in ignore_list: continue
            outfp.write('\tif (add_%s(d, "%s", %s) < 0) return;\n'%(tp, v, v))

def generate(dirname, fn = None, match_prefix='', ignore_list=()):
    if fn:
        fp = dupfile(fn, 'w')
    else:
        import sys
        fp = sys.stdout
        del sys

    fp.write("/*\n")
    fp.write(" * Various constants. This file is generated from files in\n")
    fp.write(" * %s\n"%dirname)
    fp.write(" * \n")
    fp.write(" * #Include this into the module init function\n")
    fp.write(" */\n")
    fnames = [ os.path.join(dirname, fn)
                        for fn in os.listdir(dirname)
                        if fn.endswith('.h') ]
    for f in fnames:
        process_file(fp, f, match_prefix, ignore_list)

if __name__ == "__main__":
    import sys
    generate(sys.argv[1], match_prefix=sys.argv[2])
