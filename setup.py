from setuptools import setup, find_packages

setup(
    name="nesteddataclasses",
    version='1.0',
    description='for nested dataclass',
    author='mububoki',
    author_email='mububoki@gmail.com',
    url='https://github.com/mububoki/nested-dataclasses',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
