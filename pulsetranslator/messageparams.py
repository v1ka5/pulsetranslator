# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import re


buildtypes = [ 'opt', 'debug', 'pgo' ]

def guess_platform(builder):
    for platform in sorted(platforms.keys(), reverse=True):
        if platform in builder:
            return platform

    for key in platforms:
        for os in platforms[key]:
            if os in builder:
                return os

def convert_os(data):
    if re.search(r'OS\s*X\s*10.5', data['buildername'], re.I):
        return 'leopard'
    if re.search(r'OS\s*X\s*10.6', data['buildername'], re.I):
        return 'snowleopard'
    if re.search(r'OS\s*X\s*10.7', data['buildername'], re.I):
        return 'lion'
    if re.search(r'OS\s*X\s*10.8', data['buildername'], re.I):
        return 'mountainlion'
    if re.search(r'WINNT\s*5.2', data['buildername'], re.I):
        return 'xp'
    return 'unknown'

os_conversions = {
    'leopard-o': lambda x: 'leopard',
    'tegra_android-o': lambda x: 'tegra_android',
    'macosx': convert_os,
    'macosx64': convert_os,
    'win32': convert_os,
}

platforms = {
    'linux64-rpm': ['fedora64'],
    'linux64': ['fedora64', 'ubuntu64'],
    'linuxqt': ['fedora'],
    'linux-rpm': ['fedora'],
    'linux': ['fedora', 'linux', 'ubuntu32'],
    'win32': ['xp', 'win7', 'win8'],
    'win64': ['w764'],
    'macosx64': ['macosx64', 'snowleopard', 'leopard', 'lion', 'mountainlion'],
    'macosx': ['macosx', 'leopard'],
    'android-noion': ['tegra_android-noion'],
    'android-xul': ['tegra_android-xul'],
    'android-armv6': ['tegra_android-armv6'],
    'android-x86': ['android-x86'],
    'android': ['tegra_android', 'panda_android'],
    'ics_armv7a_gecko': ['fedora-b2g', 'ubuntu64-b2g'],
}

tags = [
        '',
        'build',
        'dep',
        'dtrace',
        'l10n',
        'nightly',
        'nomethodjit',
        'notracejit',
        'release',
        'shark',
        'spidermonkey',
        'valgrind',
        'warnaserr',
        'warnaserrdebug',
        'xulrunner',
       ]
