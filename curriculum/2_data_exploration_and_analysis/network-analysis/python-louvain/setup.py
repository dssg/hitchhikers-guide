from setuptools import setup

setup(
    name="python-louvain",
    version="0.4",
    author="Thomas Aynaud",
    author_email="taynaud@gmail.com",
    description="Louvain algorithm for community detection",
    license="BSD",
    url="http://perso.crans.org/aynaud/communities/",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
    ],

    packages=['community'],
    install_requires=[
        "networkx",
    ],

    scripts=['bin/community']
)
