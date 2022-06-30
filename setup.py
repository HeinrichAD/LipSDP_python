from setuptools import setup


# read version file
# exec(open("src/version.py").read())
__version__ = "0.0.1-dev"


def readme():
    with open("README.md", "r") as f:
        return f.read()


extras_require = {
    "dev": [
        "matplotlib==3.1.1",
        "torch",
        "torchsummary",
        "torchvision",
    ],
}

setup(
    name="lipsdp",
    # author="arobey1",  # "trevoravant",
    # author_email="arobey1@github.com",
    version=__version__,  # type: ignore # noqa F821
    description="LipSDP - Python",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/HeinrichAD/LipSDP_python",
    packages=["lipsdp"],
    package_dir={
        "lipsdp": 'src/lipsdp',
    },
    # include_package_data=True,
    python_requires=">=3.7",
    install_requires=[
        "cvxopt",  # solver
        "cvxpy",
        # "mosek",  # solver
        # "kiwisolver==1.1.0",
        "numpy==1.17.3",
        "scipy==1.3.1",
    ],
    extras_require=extras_require,
    classifiers=[
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        # "License :: OSI Approved :: GNU General Public License",
        # "Topic :: Scientific/Engineering",
    ],
)
