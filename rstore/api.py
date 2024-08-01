import sys
from ast import literal_eval
from typing import Any
from typing import Dict
from typing import List

from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi import Response
from fastapi import status
from fastapi.openapi.utils import get_openapi
from fastapi.security import HTTPBasic
from fastapi.security import HTTPBasicCredentials

from rstore import schemas

try:
    from instance import config
except Exception:
    from instance import sample as config

security = HTTPBasic()

app = FastAPI()

http_security = Depends(security)

def verification(creds: HTTPBasicCredentials = http_security):
    """Verify the credentials via HTTP Basic Authentication method."""
    if not config.AUTHENTICATION_REQUIRED:
        return True
    username = creds.username
    password = creds.password
    if username in config.USERS and password == config.USERS[username]["password"]:
        return True
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )

def custom_openapi() -> Dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="RSTORE",
        version="0.1.0",
        summary="Report Storage and Tracking of Observations and Records Efficiently",
        description="Backend API for collecting data.",
        contact={
            "name": "Computer Incident Response Center Luxembourg",
            "url": "https://www.circl.lu",
            "email": "info@circl.lu",
        },
        license_info={
            "name": "GNU Affero General Public License v3.0 or later",
            "identifier": "AGPL-3.0-or-later",
            "url": "https://www.gnu.org/licenses/agpl-3.0.en.html",
        },
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://www.circl.lu/assets/images/circl-logo.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


#
# Item
#

@app.get("/items/", response_model=list[schemas.ItemBase])
def read_items(
    skip: int = 0,
    limit: int = 100,
    q: str = "",
) -> List[schemas.ItemBase]:
    items = []
    return items