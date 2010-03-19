#!/usr/bin/env python

"""
setup.py file for FreeLing extension
"""

from distutils.core import setup, Extension

swig_module = Extension('_FreeLing',
                           sources=['FreeLing.i'], swig_opts=['-c++'], 
                        libraries=['morfo', 'db_cxx', 
                                   'pcre', 'omlet',
                                   'fries', 'boost_filesystem-mt']
                           )

setup (name = 'FreeLing',
       version = '0.1',
       author      = "Supreet Sethi <supreet.sethi@gmail.com>",
       description = """FreeLing Morphological analyzer""",
       ext_modules = [swig_module],
       py_modules = ["FreeLing"],
       )
