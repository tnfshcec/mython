from setuptools import setup
from mython import VERSION_NUMBER

with open("README.md", "r") as fh:
    long_description = fh.read()

# Install python package, scripts and manual pages
setup(name="mython",
      version=VERSION_NUMBER,
      author="TNFSHCEC",
      author_email="tnfshcec@gm.tnfsh.tn.edu.tw",
      license="MIT",
      description="CodE Dream! It's Mython!!!!!",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/tnfshcec/mython",
      scripts=["scripts/my2py", "scripts/mython", "scripts/py2my"],
      data_files=[("man/man1", ["etc/mython.1", "etc/py2my.1", "etc/my2py.1"])],
      packages=["mython"],
      zip_safe=False)
