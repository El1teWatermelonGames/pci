from setuptools import setup, find_packages

setup(
    name='pci',
    version='1.0',
    license='Apache 2.0',
    description='A simple image renderer & editor for the terminal using the .pci filetype',
    long_description=''.join(open('README.md', encoding='utf-8').readlines()),
    long_description_content_type='text/markdown',
    author='Elite Watermelon',
    author_email='elitewatermelongames@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='github.com/El1teWatermelonGames/pci',
    keywords=['pci', 'rem', 'pci rem'],
    install_requires=['keyboard', 'time'],
    entry_points={
        'console_scripts': [
            'pci=pci.__main__:main'
        ]
    },
)