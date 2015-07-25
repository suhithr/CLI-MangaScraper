import os
from setuptool import setup, find_packages

#Function to read the README file
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mangascraper",
    version = "0.0.1",
    author = "Suhith Rajesh",
    author_email = "digitorq@gmail.com",
    description = ("A simple mangascraper with beautiful soup to scrape manga off of mangapanga.com"),
    long_description = read('README'),
    classifiers = [
        "Programming Language :: Python :: 2.7",
    ],
    packages = find_packages(),
)
