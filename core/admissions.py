from typing import Optional

from pydantic import BaseModel

class AdmissionReview(BaseModel):
    apiVersion: str
    uid: Optional[str] = None
    kind: Optional[dict] = None
    resource: dict
    subResource: Optional[dict] = None
    requestKind: Optional[dict] = None
    requestResource: Optional[dict] = None
    requestSubResource: Optional[str] = None
    name: str
    namespace: str
    operation: str
    userInfo: dict
    object: Optional[dict] = None
    oldObject: Optional[dict] = None
    options: Optional[dict] = None
    dryRun: Optional[bool] = None

class AdmissionResponse(BaseModel):
    """ We want something like this
        {
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
            "uid": "<value from request.uid>",
            "allowed": true
        }
        }
    """
    apiVersion: str
    kind: str
    response: Response
    
class Response(BaseModel):
    uid: str
    allowed: bool