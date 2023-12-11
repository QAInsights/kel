from setuptools import setup, find_packages
from src.kel import __version__ as kel_version
with open("requirements.txt") as f:
    required = f.read().splitlines()


setup(
    name="kel",
    version=kel_version.__version__,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    url="https://kel.qainsights.com",
    license="MIT",
    author="NaveenKumar Namachivayam",
    data_files=[("", ["requirements.txt", "config.toml"])],
    author_email="",
    description="AI assistant in your CLI.",
    install_requires=required,
)
