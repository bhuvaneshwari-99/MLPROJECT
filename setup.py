from setuptools import find_packages, setup
from typing import List

# lines that start with '-e' or contain VCS urls should be ignored by
# install_requires (they are used by pip when installing from a requirements
# file). Also ignore comments and blank lines.
EDITABLE_PREFIX = '-e'
VCS_KEYWORDS = ('git+', 'http://', 'https://')

def get_requirements(file_path: str) -> List[str]:
    """Return a list of requirements from a file.

    This will strip whitespace, ignore empty lines and comments, and skip
    editable or VCS entries which are not valid values for install_requires.
    """
    requirements: List[str] = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for raw in f:
            req = raw.strip()
            if not req or req.startswith('#'):
                continue
            # Skip editable or VCS/url requirements which pip understands but
            # setuptools' install_requires does not.
            if req.startswith(EDITABLE_PREFIX) or any(k in req for k in VCS_KEYWORDS):
                continue
            requirements.append(req)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Bhuvaneshwari",
    author_email="lbhuvaneshwari729@gmail.com",
    packages=find_packages(where="src"),  # looks inside src/
    package_dir={"": "src"},
    install_requires=get_requirements("requirements.txt")
 )
