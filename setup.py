from setuptools import setup, find_packages

reqs = [
    "bokeh",
    "numpy",
    "pandas",
    "scikit-learn",
    "yaml"
]

conda_reqs = [
    "bokeh",
    "numpy",
    "pandas",
    "scikit-learn",
    "yaml"
]

test_pkgs = []

setup(
    name="fisheye",
    python_requires='>3.4',
    description="Python package for computer vision experiments",
    url="https://github.com/neumj/fisheye",
    install_requires=reqs,
    conda_install_requires=conda_reqs,
    test_requires=test_pkgs,
    packages=find_packages(),
    include_package_data=True
)

