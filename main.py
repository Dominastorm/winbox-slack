import os
from pathlib import Path
from dotenv import load_dotenv
from slack import WebClient

# Load .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = WebClient(token=os.environ['SLACK_TOKEN'])

client.chat_postMessage(channel='#test', text='Hello world!')
