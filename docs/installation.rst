Installation
============

RSTORE is composed of two main components: a database backend powered by Kvrocks and a Web API relying on FastAPI.

Kvrocks
-------

Apache `Kvrocks <https://github.com/apache/incubator-kvrocks>`_ is a distributed key value NoSQL
database that uses RocksDB as storage engine and is compatible with Redis protocol.
Kvrocks intends to decrease the cost of memory and increase the capability while compared to Redis.

.. note::

    Kvrocks should be installed from the source, and the repository must
    be in one directory up as the one you will be cloning RSTORE into.

In order to compile kvrocks, you will need a few packages:

.. code-block:: bash

    sudo apt-get update
    sudo apt install git gcc g++ make cmake autoconf automake libtool python3 libssl-dev


.. code-block:: bash

    git clone --recursive https://github.com/apache/kvrocks.git
    cd kvrocks
    git checkout v2.9.0
    ./x.py build
    cd ..


FastAPI
-------

Clone the source code
``````````````````````

.. code-block:: bash

    $ git clone https://github.com/scandale-project/RSTORE
    $ cd RSTORE/
    $ poetry install
    $ cp instance/sample.py instance/config.py

This will install FastAPI with its dependencies.

Configuration
`````````````

.. code-block:: bash

    $ cp instance/sample.py instance/config.py

And configure it accordingly to your needs.


Usage
`````

.. code-block:: bash

    $ poetry shell
    $ uvicorn rstore.api:app
    INFO:     Started server process [18716]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)


For production you can use `Uvicorn <https://www.uvicorn.org>`_. It's up to you.


You can visit the pages:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc
