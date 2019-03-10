from setuptools import setup


dependencies = ["requests", "mypy", "aiohttp"]


dev_dependencies = ["black"]


setup(
    name="apap",
    version="0.0.1",
    author="mtwtkman",
    author_email="yo@mtwtkman.dev",
    packages=["apap"],
    extras_require={"dev": dev_dependencies},
    install_requires=dependencies,
    license="WTFPL",
    url="https://github.com/mtwtkman/apap",
    classifiers=["Programming Language :: Python :: 3.7"],
)
