import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pip-package-demo', ##name of repo enclosing folder (pip-package-demo)
    version='0.0.2',
    author='Eduardo Gonzalez', ## your name
    author_email='glez.e.alejandro@gmail.com', ## your email
    description='Demo on pip package creation', ## description of package
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sandeepmj/pip-package-demo/tree/main',# url to repo
    project_urls = {
        "Bug Tracker": "https://github.com/sandeepmj/pip-package-demo/issues"
    }, ## url to issues page on your repo
    license='MIT',
    packages=['demo'], ## name of folder that holds the functions
    install_requires=[], ## names of packages required to run your functions
)