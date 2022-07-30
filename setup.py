from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='getBlock',
      version='0.1',
      description='Get details about a block provided in hex',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Ethereum :: Validator',
      ],
      keywords='ethereum validator',
      author='Hawk94',
      author_email='tom@miller.mx',
      license='MIT',
      packages=['get_block'],
      install_requires=[
          'markdown',
      ],
      entry_points={
          'console_scripts': ['getBlock=get_block.cli:main'],
      },
      include_package_data=True,
      zip_safe=False)
