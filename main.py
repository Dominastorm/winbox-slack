import os
from pathlib import Path
from dotenv import load_dotenv
from slack import WebClient
from flask import Flask
from slackeventsapi import SlackEventAdapter

# Load .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], "/slack/events", app)

slack_web_client = WebClient(token=os.environ['SLACK_TOKEN'])

slack_web_client.chat_postMessage(channel='#test', text='Hello world!')

if __name__ == '__main__':
    app.run(debug=True)