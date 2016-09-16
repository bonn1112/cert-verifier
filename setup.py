import os
import uuid

from pip.req import parse_requirements
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

install_reqs = parse_requirements(os.path.join(here, 'requirements.txt'), session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs]

with open(os.path.join(here, 'README.md')) as fp:
    long_description = fp.read()

setup(
    name='cert-verifier',
    version='1.2.4',
    description='verifies blockchain certificates',
    author='MIT Media Lab Blockchain Certificates',
    tests_require=['tox'],
    url='https://github.com/blockchain-certificates/cert-verifier',
    license='MIT',
    author_email='certs@mit.edu',
    long_description=long_description,
    packages=find_packages(),
    install_requires=reqs
)
