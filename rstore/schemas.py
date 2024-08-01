import uuid

from pydantic import BaseModel

class Payload(BaseModel):
    raw: str


class Meta(BaseModel):
    uuid: str
    ts: int
    type: str


class ScanData(BaseModel):
    version: str
    format: str
    meta: Meta
    payload: Payload

    class Config:
        from_attributes = True

class ItemBase(ScanData):
    scan_data: ScanData

    class Config:
        from_attributes = True