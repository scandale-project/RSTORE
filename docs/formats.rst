Formats
=======

K/v story history of the IP scans/reported
------------------------------------------

hash table `h:` (history)
`````````````````````````

- `h:ipv4` / `h:ipv6`
- timestamp `epoch`
- value -> JSON raw result

domain name/hostname set `s:`-> `h:`
````````````````````````````````````

If there is a domain name or hostname set -> IPv4 or IPv6.

- `s:domain` and `s:hostname`
- value IPv4 or IPv6



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
