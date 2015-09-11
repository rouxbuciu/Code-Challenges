from setuptools import setup

APP = ['fandango_recording.py']
OPTIONS ={'iconfile':'music_256.icns'}

setup(
      app = APP,
      options = {'py2app': OPTIONS},
      setup_requires = ['py2app'],
      )
