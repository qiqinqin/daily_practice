try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description':'DAILY_PRACTICE',
    'author':'QinQin',
    'url':'https://github.com/qiqinqin/daily_practice',
    'author_email':'18010430624@163.com',
  
]

setup(**config)
