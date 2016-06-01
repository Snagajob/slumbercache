import os
import sys
from setuptools import setup

install_requires = ["requests"]
tests_require = ["mock", "unittest2"]

base_dir = os.path.dirname(os.path.abspath(__file__))

version = "0.1.0"

if sys.argv[-1] == 'publish':
    os.system("git tag -a %s -m 'v%s'" % (version, version))
    os.system("python setup.py sdist bdist_wheel upload -r pypi")
    print("Published version %s, do `git push --tags` to push new tag to remote" % version)
    sys.exit()

if sys.argv[-1] == 'syncci':
    os.system("panci --to=tox .travis.yml > tox.ini");
    sys.exit();

setup(
    name = "slumbercache",
    version = version,
    description = "A library that makes consuming a REST API easier and more convenient with Cache",
    long_description="\n\n".join([
        open(os.path.join(base_dir, "README.rst"), "r").read(),
        open(os.path.join(base_dir, "CHANGELOG.rst"), "r").read()
    ]),
    url = "http://github.com/snagajob/slumbercache",
    author = "Salar Rahmanian",
    author_email = "opensource@softinio.com",
    maintainer = "Salar Rahmanian",
    maintainer_email = "opensource@softinio.com",
    packages = ["slumbercache"],
    zip_safe = False,
    install_requires = install_requires,
    tests_require = tests_require,
    test_suite = "tests.get_tests",
)
