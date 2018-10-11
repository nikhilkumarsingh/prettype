# -*- coding: utf-8 -*-
from setuptools import setup


def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except Exception as e:
        print(e)


setup(name='prettype',
      version='1.0.0',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      keywords='unicode styled text keyboard typing tkinter copy paste',
      description='An easy to use text stylizer for your desktop!',
      long_description=readme(),
      url='https://github.com/nikhilkumarsingh/prettype',
      author='Nikhil Kumar Singh',
      author_email='nikhilksingh97@gmail.com',
      license='MIT',
      packages=['prettype'],
      install_requires=['xerox', 'pynput'],
      entry_points="""
        [console_scripts]
        prettype = prettype.prettype:main
        """,
      include_package_data=True,
      zip_safe=False)
