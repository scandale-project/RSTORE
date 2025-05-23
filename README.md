# RSTORE - Report Storage and Tracking of Observations and Records Efficiently

## Presentation

[RSTORE](https://github.com/scandale-project/RSTORE)
is a libre software which is providing a backend architecture
for the reporting and tracking of observations and records efficiently.
It is composed of:

- a documented HTTP API;
- a database backend based on [kvrocks](https://kvrocks.apache.org)

The API is based on the [FastAPI](https://fastapi.tiangolo.com) framework
well known for its excellent performance and [Pydantic](https://pydantic.dev)
for the data validation.

A [documentation](https://rstore.readthedocs.io) is available with more information.

### Why RSTORE ?

As a CSIRT, we manage a substantial volume of scan results, notifications, and reports,
which often overwhelm our ticketing system.
To address this, we decided to develop our own tool for quick and efficient lookup of all
notifications related to our activities.


## Installation

See the [installation section](https://rstore.readthedocs.io/en/latest/installation.html) of the documentation.


## License

RSTORE is distributed under the terms of the
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html).

- Copyright (C) 2024-2025 [CIRCL - Computer Incident Response Center Luxembourg](https://www.circl.lu)
- Copyright (C) 2024-2025 [Cédric Bonhomme](https://www.cedricbonhomme.org)
