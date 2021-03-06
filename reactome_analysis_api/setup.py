# coding: utf-8

from setuptools import setup, find_packages

NAME = "reactome_analysis_api"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion", "flask", "swagger-ui-bundle >= 0.0.2", "reactome_analysis_utils", "prometheus_client"]

setup(
    name=NAME,
    version=VERSION,
    description="REACTOME Analysis Service",
    author_email="",
    url="",
    keywords=["Swagger", "REACTOME Analysis Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['reactome_analysis_api=reactome_analysis_api.__main__:main']},
    long_description="""\
    This is a REACTOME analysis service. It provides gene set analysis methods whose results can be visualized using the REACTOME pathway browser.
    """
)

