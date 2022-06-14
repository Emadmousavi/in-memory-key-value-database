from setuptools import setup, find_packages

setup(
    name='in-memory-key-value-db',
    version='1.0',
    description='A lightweight in-memory key-value store',
    author='Seyed Emad Mousavi',
    author_email='emadmoosavi79@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'kvdb-cli = kvdb.cli.run:main',
            'kvdb-server = kvdb.server.run:main'
        ]
    }
)