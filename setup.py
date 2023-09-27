import os
import setuptools

def read_readme() -> str:
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    with open(readme_path) as f:
        return f.read()

setuptools.setup(
    name="clockdeco",
    version="0.0.1",
    description="A simple decorator to print elapsed time on function call",
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author="Admir Trakic",
    url = "https://gitlab.com/atrakic/clockdeco",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
        "Operating System :: OS Independent"
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
