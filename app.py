import fastapi
from fastapi import FastAPI,Request
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration,T5Tokenizer
from fastapi.templating import Jinja2Templates
import torch
import re
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app=FastAPI(title="Text Summarizer App", description="Text Summarization using T5",version=1.0)


model=T5ForConditionalGeneration.from_pretrained("svk260404/text-summarizer-t5")
tokenizer=T5Tokenizer.from_pretrained("svk260404/text-summarizer-t5")


# Device

if torch.backends.mps.is_available():
    device=torch.device("mps")

elif torch.cuda.is_available():
    device=torch.device("cuda")

else:
    device="cpu"


model.to(device)


templates =Jinja2Templates(directory=".")


class DialogueInput(BaseModel):
    dialogue:str



def  clear_punc(text):
    text=re.sub(r"\r\n"," ",text)   #/r ,/n
    text=re.sub(r"\s+"," ",text)   # void space
    text=re.sub(r"<.*?>"," ",text) # html tag <p> <h1>
    text=text.strip().lower()
    return text

def summarize_dialogue(dialogue:str)-> str:
    dialogue=clear_punc(dialogue)
    
    inputs=tokenizer(dialogue,padding="max_length",max_length=512,truncation=True,return_tensors="pt").to(device)
    
    model.to(device)
    targets=model.generate(input_ids=inputs["input_ids"],
                           attention_mask=inputs["attention_mask"],
                           max_length=150,
                           num_beams=4,
                           early_stopping=True)
    
    # decode

    summary=tokenizer.decode(targets[0],skip_special_tokens=True)
    return summary

# API endpoints

@ app.post("/summarize/")
async def summarize(dialogue_input:DialogueInput):
    summary=summarize_dialogue(dialogue_input.dialogue)
    return {"summary":summary}


@ app.get("/",response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse(name="index.html",request=request)
