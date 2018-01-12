from setuptools import setup


setup(name='cryptopia',
      version='0.1',
      description='API for Cryptopia Exchange',
      keywords='Cryptopia cryptocoin',
      url='https://github.com/edilio/cryptopia',
      author='DEGConnect',
      author_email='info@degconnect.com',
      license='MIT',
      packages=["cryptopia", ],
      install_requires=[
          'requests==2.18.1',
      ],
      zip_safe=False
      )

