from setuptools import setup

setup(
    name="enum-spatial",
    version="0.1",
    author=u"Jeff Albrecht",
    author_email="geospatialjeff@gmail.com",
    install_requires=[
        "pygeos @ git+https://github.com/pygeos/pygeos#egg=pygeos",
    ],
)