import os

def main():
    basepath = os.path.dirname(__file__)
    builddir = os.path.join(basepath, 'prebuilt')
    if not os.path.exists(builddir):
        os.makedirs(builddir)
    dest = os.path.join(builddir, 'main')
    src = os.path.join(basepath, 'src', 'main.m')
    if not os.path.exists(dest) or os.stat(dest).st_mtime < os.stat(src).st_mtime:
        CFLAGS = '-Os -Wall'
        LDFLAGS = '-g -framework Foundation -framework AppKit'
        os.system('cc -o "%(dest)s" "%(src)s" %(CFLAGS)s %(LDFLAGS)s' % locals())
        os.system('strip "%(dest)s"' % locals())
    return dest

if __name__ == '__main__':
    main()
