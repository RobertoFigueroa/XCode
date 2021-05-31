from setuptools import setup, find_packages

setup(
    name = 'Hoopers Lib',
    version = '1.0',
    url = '',
    description = '',
    packages = find_packages(),
    install_requires = [
        # Github Private Repository
        'hopperslib @ git+ssh://git@github.com/RobertoFigueroa/hoppers-minimax-lib.git'
    ]
)