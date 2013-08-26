# Copyright (c) 2013 happyCoda. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

#!/usr/bin/env python

import os

# dirs = ['root', 'root/css', 'root/js', 'root/i']
# files = {'css': , 'js': }

dir_file_map = {'root': 'root', 'nodes': {'css': ['style.css', 'normalize.css'], 'js': ['jquery.js', 'app.js'], 'i': []}, 'root_files': ['index.html']}



def make_dirs(m):
	val = None

	if m['root']:
		root = m['root']

		if not os.path.exists(root):
			os.makedirs(root)

	if m['nodes']:
		nodes = m['nodes']

		for dir_name in nodes:
			val = nodes[dir_name]
			os.makedirs(root + '/' + dir_name)
			if type(val) == dict:
				make_dirs(val)
			elif type(val) == list:
				for fname in val:
					make_file(root + '/' + dir_name + '/' + fname)

	if m['root_files']:
		root_files = m['root_files']

		for rfname in root_files:
			make_file(root + '/' + rfname)
	

	

	


def make_file(path):
	new_file = open(path, 'w')
	new_file.close()
		
make_dirs(dir_file_map)