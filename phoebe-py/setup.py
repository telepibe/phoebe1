from distutils.core import setup, Extension
import setuptools
import numpy 

with open('README.md', 'r') as ld:
    long_description = ld.read()

setuptools.setup(
    name='PHOEBE legacy python wrapper',
    version='1.0',
    author='Andrej Prsa',
    author_email='aprsa@villanova.edu',
    description='PHOEBE legacy python wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://phoebe-project.org',
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'Environment :: X11 Applications',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics'
    ],

)

backend = Extension('phoebeBackend',
                    sources = ['phoebe_backend.c'],
		    libraries = ['phoebe'],
                    include_dirs=[numpy.get_include()])
                    
setup (name = 'PHOEBE backend',
       version = '0.40',
       description = 'PHOEBE python package',
       ext_modules = [backend])
