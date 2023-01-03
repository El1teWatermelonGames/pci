from setuptools import setup, find_packages

setup(
    name='pci_rem',
    version='1.0',
    license='Apache 2.0',
    author='Elite Watermelon',
    author_email='elitewatermelongames@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='',
    keywords=['pci', 'rem', 'pci rem'],
    install_requires=['keyboard', 'time']
)