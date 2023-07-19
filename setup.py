from setuptools import find_packages, setup


# version go
requests = 'requests==2.28.1'
pandas = 'pandas==2.0.0'
# version end

# start
requires_dict = {
'mok_doc': [requests, pandas],
'mok_doc.__init__': [],
'mok_doc.first_level.__init__': [],
'mok_doc.first_level.postprocess': [],
'mok_doc.first_level.preprocess': [],
'mok_doc.first_level.second_level.__init__': [],
'mok_doc.first_level.second_level.analitics': [],
'mok_doc.first_level_second.__init__': [],
'mok_doc.first_level_second.api': [],
'mok_doc.first_level_second.errors_hand': [],
'mok_doc.mok_content': [pandas],
'mok_doc.mok_content2': [requests],
}
# stop

version = []
with open("hive/version.py", "r") as f:
    for line in f:
        version.append(str(line.strip()))

version = version[0].split("'")[1]

setup(
    name='mok_doc',
    version=version,
    packages=find_packages(include=['mok_doc']),
    license='',
    author='Andrea Jacassi',
    author_email='',
    description='',
    url="",
    extras_require=requires_dict,
    install_requires=[],
)
