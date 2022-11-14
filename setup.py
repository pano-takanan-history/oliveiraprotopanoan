from setuptools import setup
import json

with open("metadata.json", encoding="utf-8") as fp:
    metadata = json.load(fp)

setup(
    name='lexibank_oliveiraprotopanoan',
    py_modules=['lexibank_oliveiraprotopanoan'],
    include_package_data=True,
    url=metadata.get("url",""),
    zip_safe=False,
    entry_points={
        'lexibank.dataset': [
            'oliveiraprotopanoan=lexibank_oliveiraprotopanoan:Dataset',
        ]
    },
    install_requires=[
        "pylexibank>=3.0.0",
        "cldfbench==1.13.0",
        "pycldf==1.29.0",
        "csvw==3.1.3",
        "pyconcepticon==3.0.0",
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
