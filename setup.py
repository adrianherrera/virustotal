from setuptools import setup


setup(
    name='VirusTotal',
    description='Command-line script to interact with VirusTotal',
    long_description=open('README.md').read(),
    author='Adrian Herrera',
    url='https://github.com/adrianherrera/virustotal',
    version='0.11',
    license='GNU General Public License v3',
    install_requires=[
        'requests',
        'virustotal-api',
    ],
    scripts=[
        'vt_driver.py',
    ],
    entry_points={
        'console_scripts': [
            'virustotal = vt_driver:main',
        ]
    },
    classifiers=(
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Security',
    ),
)
