import os

from setuptools import setup


def load_readme():
    PROJECT_DIR = os.path.dirname(__file__)
    readme_file = "README.rst"
    try:
        return open(os.path.join(PROJECT_DIR, readme_file), 'r').read()
    except Exception:
        raise RuntimeError("Cannot find readme file {fname}.".format(
            fname=readme_file))


def load_version():
    """Open and parse out the version number from the _version.py module.

    Inspired by http://stackoverflow.com/a/7071358
    """
    import re
    version_file = "bitmerchantx/_version.py"
    version_line = open(version_file).read().rstrip()
    vre = re.compile(r'__version__ = "([^"]+)"')
    matches = vre.findall(version_line)
    if matches and len(matches) > 0:
        return matches[0]
    else:
        raise RuntimeError(
            "Cannot find version string in {version_file}.".format(
                version_file=version_file))

version = load_version()
long_description = load_readme()

setup(
    name='bitmerchantx',
    version=version,
    description="BitCore BTX merchant tools",
    long_description=long_description,
    author='David Bergen',
    author_email='david.bergen@gmx.net',
    url='https://github.com/dalijolijo/bitmerchantx',
    download_url=(
        'https://github.com/dalijolijo/bitmerchantx/tarball/v%s' % version),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    packages=[
        'bitmerchantx',
        'bitmerchantx.wallet',
    ],
    package_data={'': ['AUTHORS', 'LICENSE']},
    include_package_data=True,
    license='MIT License',
    tests_require=[
        'coverage',
        'nose',
        'mock>=1.0.1',
        # For test vector generation script
        'bunch>=1.0.1',
        'python-bitcoinrpc>=0.1',
        # For bip32 test vector generation
        'pycoin>=0.26',
    ],
    test_suite="tests",
    install_requires=[
        'base58>=0.2.1',
        'ecdsa>=0.10',
        'six>=1.5.2',
        'cachetools>=1.1.1',
    ]
)
