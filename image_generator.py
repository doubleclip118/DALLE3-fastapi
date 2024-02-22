from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from fastapi.responses import FileResponse,JSONResponse,Response
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os
import openai
import base64
import json


load_dotenv()
client = OpenAI()

class image_in(BaseModel):
    name: str


openai.api_key = os.getenv('OPENAI_API_KEY')
    
app = FastAPI()

@app.post('/images_json')
async def image_gen(input:image_in):
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=input.name+"Draw the background White and realistically",
            size="1024x1024",
            quality="hd",
            n=1,
            style="vivid",
            response_format = "b64_json"   
            )
        response_data=response.data[0].b64_json
        # image_data_b64 = response['data'][0]['b64_json']


        # base64를 바이트로 디코딩
        image_bytes = base64.b64decode(response_data)
        
        # 이미지 바이트 데이터로 응답 생성
        return Response(content=image_bytes, media_type="image/png")
    except openai.OpenAIError as e:
        print(e)
        raise HTTPException(status_code=500, detail="OpenAI 에러 발생")
    
@app.post('/images_url')
async def image_gen(input:image_in):
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=input.name+"Draw the background White and realistically Just draw the object I'm talking about",
            size="1024x1024",
            quality="hd",
            n=1,
            style="vivid",
            response_format = "url"   
            )
        response_data=response.data[0].url
        return {"image_url":response_data}
    except openai.OpenAIError as e:
        print(e)
        raise HTTPException(status_code=500, detail="OpenAI 에러 발생")

    