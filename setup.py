from collections import defaultdict
from pathlib import Path

from setuptools import find_packages, setup


def load_requirements(path: Path):
    requirements = defaultdict(list)
    with path.open("r") as fp:
        reqs_type = "base"
        for line in fp.readlines():
            if line.startswith("## extras:"):
                reqs_type = line.partition(":")[-1].strip()
            if line.startswith("-r"):
                requirements += load_requirements(line.split(" ")[1].strip())["base"]
            else:
                requirement = line.strip()
                if requirement and not requirement.startswith("#"):
                    requirements[reqs_type].append(requirement)
    return requirements


readme = Path("README.md").read_text(encoding="UTF-8")

requirements = load_requirements(Path(__file__).parent / "requirements.txt")

setup(
    author="Jay Qi",
    author_email="jayqi.opensource@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description=("Render reproducible examples of Python code for sharing."),
    entry_points={"console_scripts": ["reprex=reprexlite.cli:app"]},
    extras_require={k: v for k, v in requirements.items() if k != "base"},
    install_requires=requirements["base"],
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    name="reprexlite",
    packages=find_packages(exclude=["tests"]),
    project_urls={
        "Bug Tracker": "https://github.com/jayqi/reprexlite/issues",
        "Documentation": "https://jayqi.github.io/reprexlite/",
        "Source Code": "https://github.com/jayqi/reprexlite",
    },
    url="https://github.com/jayqi/reprexlite",
    version="0.4.2",
)
