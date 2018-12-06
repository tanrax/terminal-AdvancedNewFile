from setuptools import setup
setup(
  name = 'advance-touch',
  py_modules=['advance_touch'],
  version = '1.0.2',
  python_requires='>3.6',
  description = 'Fast creation of files and directories. Mimics the operation of AdvancedNewFile (Vim plugin)',
  author = 'Andros Fenollosa',
  author_email = 'andros@fenollosa.email',
  url = 'https://github.com/tanrax/terminal-AdvancedNewFile',
  keywords = ['touch', 'mkdir', 'advance', 'vim'],
  classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
  ),
  install_requires=[
      'Click>=6.7',
  ],
  entry_points='''
      [console_scripts]
      ad=advance_touch:advance_touch
  '''
)
