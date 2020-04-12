#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="pynotes",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='Smart note management system',
    author='Michael Bergmann',
    author_email='michael.bergmann2304@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(),
    install_requires=[
        "docutils",
        "pygments",
        "pypiwin32",
        "kivy_deps.sdl2==0.1.*",
        "kivy_deps.glew==0.1.*",
        "kivy_deps.gstreamer==0.1.*",
        "kivy_deps.angle==0.1.*",
        "kivy_examples",
        "kivy",
    ],
    test_suite='nose.collector',
    tests_require=['nose', 'mock']
)
