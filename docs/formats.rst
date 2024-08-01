Formats
=======

Data from the scans
-------------------

Data from the various scanning tools is stored to the following format.


.. code-block:: json

    {
        "version": "1",
        "format": "scanning",
        "meta": {
            "uuid": "<UUID>",
            "source": "<source>",
            "ts": "date",
            "type": "nmap-scan"
        },
        "payload": {
            "raw": "<base64-encoded-string>"
        }
    }
