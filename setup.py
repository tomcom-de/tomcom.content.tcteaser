from setuptools import setup, find_packages

version = '4.3.0.1'

tests_require = [
    'plone.app.testing',
    'pyquery'
    ]

setup(name='tomcom.content.tcteaser',
      version=version,
      description='',
      long_description=open("README.rst").read(),
      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      keywords='tomcom plone',
      author='tomcom GmbH',
      author_email='mailto:info@tomcom.de',
      url='https://github.com/tomcom-de/tomcom.content.tcteaser',
      license='GPL2',
      packages=find_packages(),
      namespace_packages=['tomcom','tomcom.content'],
      include_package_data=True,
      install_requires=[
        'setuptools',
      ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require,
                     ),
      zip_safe=False,
      entry_points='''
[z3c.autoinclude.plugin]
target = plone
''',
)