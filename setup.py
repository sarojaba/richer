from setuptools import setup, find_packages

setup(
    name = 'richer',
    version = '0.1.6',
    description = 'Table renderer for dataclass using Rich',
    author = 'sarojaba',
    author_email = 'sarojaba@gmail.com',
    url = 'https://github.com/sarojaba/richer',
    download_url = 'https://github.com/sarojaba/richer',
    install_requires = ['rich'],
    packages = find_packages(exclude = []),
    keywords = ['table'],
    python_requires = '>=3.7',
    package_data = {},
    zip_safe = False,
    classifiers = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)