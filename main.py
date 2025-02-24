import json
import os
import time
import streamlit as st

import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI()
model = "gpt-4-1106-preview"