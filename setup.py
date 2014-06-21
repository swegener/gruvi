#
# This file is part of gruvi. Gruvi is free software available under the
# terms of the MIT license. See the file "LICENSE" that was provided
# together with this source file for the licensing terms.
#
# Copyright (c) 2012-2013 the gruvi authors. See the file "AUTHORS" for a
# complete list.

from __future__ import absolute_import, print_function

import os
import sys
import textwrap
import json
import re

from setuptools import setup, Extension

# CFFI is needed to call setup() and therefore it needs to be installed before
# this setup script can be run. Look in the version history for this file for a
# hack to install it automatically. However for now let's keep it simple and
# just require the user to install it.

try:
    import cffi
except ImportError:
    sys.stderr.write('Error: CFFI (required for setup) is not available.\n')
    sys.stderr.write('Please use "pip install cffi", or equivalent.\n')
    sys.exit(1)

re_int = re.compile('^(\d*).*$')
cffi_ver = tuple((int(re_int.sub('0\\1', x)) for x in cffi.__version__.split('.')))
if cffi_ver < (0, 8):
    sys.stderr.write('Error: CFFI (required for setup) is too old.\n')
    sys.stderr.write('Please install at least version 0.8.\n')
    sys.exit(1)


PY2 = sys.version_info[0] == 2

version_info = {
    'name': 'gruvi',
    'version': '0.9.3.dev',
    'description': 'Synchronous evented IO with pyuv and fibers',
    'author': 'Geert Jansen',
    'author_email': 'geertj@gmail.com',
    'url': 'https://github.com/geertj/gruvi',
    'license': 'MIT',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ]
}

topdir, _ = os.path.split(os.path.abspath(__file__))


def update_version():
    """Update the _version.py file."""
    fname = os.path.join('.', 'gruvi', '_version.py')
    try:
        with open(fname) as fin:
            current = fin.read()
    except IOError:
        current = None
    # json.dumps will produce valid Python for version_info
    new = textwrap.dedent("""\
            # This file is autogenerated. Do not edit.
            version_info = {0}
            """).format(json.dumps(version_info, indent=4, sort_keys=True,
                                   separators=(',', ': ')))
    if current == new:
        return
    tmpname = '{0}.{1}-tmp'.format(fname, os.getpid())
    with open(tmpname, 'w') as fout:
        fout.write(new)
    os.rename(tmpname, fname)
    print('Updated _version.py')


def main():
    os.chdir(topdir)
    update_version()
    sys.path.append('gruvi')
    import http_ffi, jsonrpc_ffi
    ext_modules = [http_ffi.ffi.verifier.get_extension(),
                   jsonrpc_ffi.ffi.verifier.get_extension()]
    # On Windows, don't compile _sslcompat by default. Windows doesn't have a
    # system provided OpenSSL, and the official Python builds for Windows use a
    # static version of OpenSSL that is built duing the Python build process.
    # No shared library or headers are provided for it, so it's alsmost
    # impossible to match it. If you really want _sslcompat on Python 2.x on
    # Windows, your best bet is to compile Python from source, keep the OpenSSL
    # temporary build, and link against that.
    if PY2 and not sys.platform.startswith('win'):
        ext_modules.append(Extension('_sslcompat', ['gruvi/_sslcompat.c'],
                                     libraries=['ssl', 'crypto']))
    sys.path.pop()
    setup(
        packages = ['gruvi', 'gruvi.txdbus'],
        install_requires = ['cffi', 'fibers', 'pyuv', 'six'],
        ext_package = 'gruvi',
        ext_modules = ext_modules,
        **version_info
    )


if __name__ == '__main__':
    main()
