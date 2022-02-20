from re import match

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from core.admissions import AdmissionReview, AdmissionResponse, Response

app = FastAPI()


@app.post("/validate")
async def validate(rev: AdmissionReview):
    rev_dict = rev.dict()
    adm_response = None
    if match(pattern='[pizza]', string=rev_dict.name):
        r = Response(
            uid=rev_dict.uid,
            allowed=True
        )
        adm_response = AdmissionResponse(
            apiVersion=rev_dict.apiVersion,
            kind=rev_dict.kind,
            response=r
        )
    return JSONResponse(content=jsonable_encoder(adm_reponse))
