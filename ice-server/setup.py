#!/usr/bin/env python

#
# Copyright (c) 2018 Orange. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#

import os
from setuptools import setup, find_packages
import sys

if sys.version_info < (3, 0):
    sys.exit('VNF SDK ICE server requires Python 3.0+')

root_dir = os.path.dirname(__file__)
install_requires = []
extras_require = {}

with open(os.path.join(root_dir, 'requirements.txt')) as requirements:
    for requirement in requirements.readlines():
        # get rid of comments or trailing comments
        requirement = requirement.split('#')[0].strip()
        if not requirement:
            continue # skip empty and comment lines
        # dependencies which use environment markers have to go in as
        # conditional dependencies under "extra_require", see more at:
        # https://wheel.readthedocs.io/en/latest/index.html#defining-conditional-dependencies
        if ';' in requirement:
            package, condition = requirement.split(';')
            cond_name = ':{0}'.format(condition.strip())
            extras_require.setdefault(cond_name, [])
            extras_require[cond_name].append(package.strip())
        else:
            install_requires.append(requirement)

# read __version__
exec(open('./version.py').read())

setup(
    name='vnfsdk-ice-server',
    version= __version__,
    description='VNF SDK Heat validation REST server',
    license='Apache License Version 2.0',
    url='http://onap.org/',

    packages=find_packages('.'),

    package_dir={'heat_test': 'heat_test'},

    include_package_data=True,
    install_requires=install_requires,
    extras_require=extras_require)

