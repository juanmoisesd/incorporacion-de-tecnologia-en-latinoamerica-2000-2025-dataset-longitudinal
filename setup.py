from setuptools import setup, find_packages
setup(
    name="incorporacion-de-tecnologia-en-latinoamerica-2000-2025-dataset-longitudinal",
    version="1.0.0",
    description="Dataset longitudinal (2000-2025) sobre indicadores de adopción de tecnología digital en 21 países de",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/incorporacion-de-tecnologia-en-latinoamerica-2000-2025-dataset-longitudinal",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="cc0, citation, cyberaddiction, dataset, digital-health, fair-data, iberoamerica, juan-moises-de-la-serna, latam, latin-america, open-data, open-science, orcid, research, tech-adoption, technology, zenodo, zenodo, open-data",
)