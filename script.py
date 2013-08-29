# Copyright (c) 2013 happyCoda. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

#!/usr/bin/env python

import os, urllib2

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
			dir_path = root + '/' + dir_name

			if not os.path.exists(dir_path):
				os.makedirs(dir_path)
				if type(val) == dict:
					make_dirs(val)
				elif type(val) == list:
					for fname in val:

						if fname == 'normalize.css':
							normalize_url = urllib2.urlopen('http://necolas.github.io/normalize.css/2.1.3/normalize.css');
							normalize_data = normalize_url.read();
							make_file(dir_path + '/' + fname, normalize_data)
						elif fname == 'jquery.js':
							jquery_url = urllib2.urlopen('http://code.jquery.com/jquery-2.0.3.min.js');
							jquery_data = jquery_url.read();
							make_file(dir_path + '/' + fname, jquery_data)
						else:
							make_file(dir_path + '/' + fname)	

	if m['root_files']:
		root_files = m['root_files']

		for rfname in root_files:
			file_path = root + '/' + rfname
			if not os.path.exists(file_path):
				make_file(file_path)
	

	


	


def make_file(path, data=None):
	new_file = open(path, 'w')

	if not data == None:
		new_file.write(data)

	new_file.close()
		
make_dirs(dir_file_map)