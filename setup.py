from setuptools import find_packages, setup

version = '1.0'

# version go
urllib3 = 'urllib3==1.26.13'
tqdm = 'tqdm==4.64.1'
requests = 'requests==2.28.1'
# version end


setup(
    name='mok_doc',
    version=version,
    packages=find_packages(include=['mok_doc']),
    license='',
    author='Andrea Jacassi',
    author_email='',
    description='',
    url="",
    install_requires=[urllib3, tqdm, requests],
)
