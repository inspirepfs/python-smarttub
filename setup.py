import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="python-smarttub",
    version="0.0.7",
    author="Matt Zimmerman",
    author_email="mdz@alcor.net",
    description="API to query and control hot tubs using the SmartTub system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mdz/python-smarttub",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'aiohttp>=3.0.0,<4.0.0',
        'pyjwt>=1.0.0,<3.0.0',
        'python-dateutil>=2.0.0,<3.0.0',
    ],
    # tests require python >=3.8
    tests_require=['pytest', 'pytest-asyncio', 'aresponses'],
    python_requires='>=3.7',
)
