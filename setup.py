from io import open
from os import path
from setuptools import find_packages, setup


# Get the long description from the README file.
current_dir = path.abspath(path.dirname(__file__))
with open(path.join(current_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='smart-string',
      version='0.0.9',
      description='Smart String implementation',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/markk2504/smart-string',
      author='Mark Kaplan',
      author_email='markk2504@gmail.com',
      license='MIT',
      # https://pypi.org/classifiers/
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries :: Python Modules',

          # Pick your license as you wish
          'License :: OSI Approved :: MIT License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2.7',
      ],
      #packages=['smart_str'],
      packages=find_packages(exclude=['tests']),
      install_requires=[
          'enum34',
      ],
      python_requires='==2.7.*',
      zip_safe=False)
