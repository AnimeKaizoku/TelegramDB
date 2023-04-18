import setuptools

with open('requirements.txt') as f:
    dependencies = [l.strip() for l in f]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='TelegramDB',
    version='1.0.0',
    description='A library that uses your telegram account as a database for your project.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GPLv3',
    author='Anony',
    author_email='contact@anonyindian.me',
    url='https://github.com/AnimeKaizoku/TelegramDB',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Typing :: Typed'
    ],
    install_requires=dependencies,
    python_requires='>=3.6'
)