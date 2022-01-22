.. _installation:

============
Installation
============

TelegramDB is a Python library, which means you need to download and install
Python from https://www.python.org/downloads/ if you haven't already. Once
you have Python installed, run:

.. code-block:: sh

    pip install TelegramDB

To install the latest version of library.


Installing Development Versions
===============================

If you want the *latest* unreleased changes,
you can run the following command instead:

.. code-block:: sh

    pip3 install -U https://github.com/AnimeKaizoku/TelegramDB/archive/master.zip

.. note::

    The development version may have bugs and is not recommended for production
    use. However, when you are `reporting a library bug`__, you should try if the
    bug still occurs in this version.

.. __: https://github.com/AnimeKaizoku/TelegramDB/issues/


Verification
============

To verify that the library is installed correctly, run the following command:

.. code-block:: sh

    python3 -c 'import telegramdb; print(telegramdb.__version__)'

The version number of the library should show in the output.