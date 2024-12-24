from setuptools import find_packages
from setuptools import setup

setup(name='headsup',
      version="0.0.0",
      description="Heads-up Chatbot",
      license="MIT",
      author="brvsf",
      #url="https://github.com/brvsf/heads-up",
      packages=find_packages(),
      test_suite="tests",
      include_package_data=True,
      zip_safe=False)
