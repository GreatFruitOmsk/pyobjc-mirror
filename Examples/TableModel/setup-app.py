#!/usr/bin/env pythonw
"""
Python script for building the applet.
"""

import objc.builder

objc.builder.build_applet(
	app_name= 'TableModelPY',
	main_py = 'TableModel.py',
	raw = 1,
	extra_files = ['English.lproj'])
