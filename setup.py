from setuptools import setup

setup(
    name='ReachAnalysis',
    version='0.1.0',
    description='A python library for ETL real-time analysis pipeline , '
                'compatible with the ReachMaster experimental paradigm and the ReachProcess ETL pipeline.',
    url='https://github.com/throneofshadow/ReachAnalysis',
    author='Brett Nelson',
    author_email='bnelson@lbl.gov',
    license='BSD-3-Clause-LBNL',
    packages=['ReachAnalysis'],
    install_requires=['pandas', 'matplotlib.pyplot', 'unittest',
                      'numpy', 'os', 'pdb', 'ffmpeg'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)