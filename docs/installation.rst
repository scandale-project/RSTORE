Installation
============

FastAPI
-------

.. code-block:: bash

    $ poetry install
    $ cp instance/sample.py instance/config.py

This will install FastAPI with its dependencies.


.. code-block:: bash

    $ poetry shell
    $ rstore.api:app
    INFO:     Started server process [18716]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)


For production you can use `Uvicorn <https://www.uvicorn.org>`_. It's up to you.


You can visit the pages:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc
