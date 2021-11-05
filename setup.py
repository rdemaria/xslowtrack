import setuptools
import sys

requirements = {"install": ["numpy"]}

setuptools.setup(
    name="xslowtrack",
    version="0.0.0",
    description="6D Tracking Code",
    author="Riccardo De Maria, Giovanni Iadarola",
    author_email="riccardo.de.maria@cern.ch",
    url="https://github.com/rdemaria/xline",
    packages=["xslowtrack", "xslowtrack.be_beamfields"],
    package_dir={"xslowtrack": "xslowtrack"},
    requirements = requirements["install"]}
)
