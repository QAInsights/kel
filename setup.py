with open('requirements.txt') as f:
    required = f.read().splitlines()

from setuptools import setup

setup(
    name='kel',
    version='0.0.1',
    packages=['app', 'app.gpt', 'app.utils', 'app.config', 'app.inputs', 'app.assistant', 'app.constants'],
    url='https://kel.qainsights.com',
    license='MIT',
    author='NaveenKumar Namachivayam',
    data_files=[('', ['requirements.txt', 'config.toml'])],
    author_email='',
    description='AI assistant in your CLI.',
    install_requires=required,
)
