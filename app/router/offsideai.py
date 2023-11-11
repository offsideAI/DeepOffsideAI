import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response, Query, UploadFile, File 
import database, models
# from sqlalchemy.orm import Session
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
import oauth2
import openai
import base64

router = APIRouter(
    tags = ['offsidei']
)

###############################################################################
## OpenAI

@router.get('/offsideai/jsonfunctioncalling')
def dojsonfunctioncalling(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    query: str = Query(..., description="The content to send to the OpenAI model")
):
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages = [
            {
                "role": "system",
                "content": "Generate JSON response"   
            },
            {
                "role": "user",
                "content": query
                
            }
        ],
        response_format={ "type": "json_object" }
    )
    return response.choices[0].message.content

@router.get('/offsideai/functioncalling')
def dofunctioncalling(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    query: str = Query(..., description="The content to send to the OffsideAI model")
):
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages = [
            {
                "role": "system",
                "content": "Generate regular response"   
            },
            {
                "role": "user",
                "content": query
                
            }
        ]
    )
    return response.choices[0].message.content

@router.post('/offsideai/vision')
async def dovisionmagic(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    # query: str = Query(..., description="The content to send to the OffsideAI model"),
    image: UploadFile = File(..., description="Image file to be processed")
    
):
    client = openai.OpenAI()
    
    # Read the image file and convert it to BASE64
    image_content = await image.read()
    base64_image = base64.b64encode(image_content).decode('utf-8')
    query: str = "What's in this image?"
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages = [
            {
                "role": "user",
                "content": [
                    {
                     "type": "text",
                     "text": 
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        } 
                    }
                ]
            }
        ],
        max_tokens = 300
    )
    # print(response.choices[0].message.content)
    return response.choices[0].message.content