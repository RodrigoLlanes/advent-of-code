from setuptools import find_packages, setup

setup(
    name='pycp',
    packages=find_packages(include=['pycp']),
    version='0.0.1',
    description='A python library for competitive programming',
    author='Rodrigo Llanes Lacomba',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
