from distutils.core import setup
import py2app

plist = dict(NSMainNibFile='PyInterpreter')
setup(
    app = ["PyInterpreter.py"],
    data_files = ["PyInterpreter.nib"],
    options = dict(py2app=dict(plist=plist)),
)
