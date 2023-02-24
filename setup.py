from setuptools import setup, find_packages
import os


def clean_dist():
    dist_path = 'dist'
    if os.path.isdir('dist'):
        files = [f for f in os.listdir(dist_path) if os.path.isfile(os.path.join(dist_path, f))]
        for file in files:
            os.remove(os.path.join(dist_path, file))


def read_file(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


def upload_to_pypi():
    os.system("twine upload dist/*")


clean_dist()


setup(
    name='dictipy',
    version="0.0.1",
    author='Gioele Crispo',
    author_email='crispogioele@gmail.com',
    package_dir={'chunkipy': 'chunkipy'},
    packages=find_packages('.'),
    # scripts=['bin/script1', 'bin/script2'],
    url='https://github.com/gioelecrispo/chunkipy.git',
    license='MIT',
    license_file='LICENSE',
    platform='any',
    description='Chunkipy is an easy-to-use library for chunking text based on the tokenizer function you provide.',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    install_requires=read_file('requirements.txt').splitlines(),
    python_requires='>=2.7',
    package_data={
        # '': ['package_data.dat'],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)


#upload_to_pypi()

