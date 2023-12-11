from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()


setup(
    name="kel",
    version="0.0.2",
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
