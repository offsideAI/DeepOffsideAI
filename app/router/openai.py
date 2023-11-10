import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response, Query
import database, models
# from sqlalchemy.orm import Session
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
import oauth2
import openai

router = APIRouter(
    tags = ['openai']
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

@router.get('/offsideai/vision')
def dovisionmagic(
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
                "role": "user",
                "content": [
                    {
                     "type": "text",
                     "text": "What's in this image?"   
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                        } 
                    }
                ]
            }
        ],
        max_tokens = 300
    )
    return response.choices[0].message.content