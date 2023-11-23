import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="Amazon Scraper CLI",
    version="0.0.1",
    author="Joseph Bronsten",
    author_email="josephbronsten@gmail.com",
    description=("A CLI tool used to track the prices of products on Amazon.com"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joseph-bronsten/",
    project_urls={
        "Bug Tracker": "https://github.com/liuzheng1990/python_packaging_demo/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "typer", "bs4", "rich"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "scraper = scraper.cli",
        ]
    }
)