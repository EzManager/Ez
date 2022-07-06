from setuptools import setup, find_packages

setup_requires = []
install_requires = []
dependency_links = []

setup(
    name='ezmanager',
    version='0.0.0a1',
    license='MIT',
    url='https://github.com/EzManager/Ez',
    description='Easily usable tools for programming',
    author='ForestHouse',
    author_email='foresthouse2316@gmail.com',
    packages=['ez'],
    setup_requires=setup_requires,
    install_requires=install_requires,
    dependency_links=dependency_links,
    scripts=[],
)
