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

# Create an event adapter to handle events
slack_event_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], "/slack/events", app)

# Create a Slack client
client = WebClient(token=os.environ['SLACK_TOKEN'])

# Handle member joining event
@slack_event_adapter.on("team_join")
def handle_message(payload):
    event = payload.get('event', {})
    user = event.get('user')

    # Send a direct message to the user
    client.chat_postMessage(channel=user, text="Thanks for choosing Winbox!\n You will receive your notifications here.")

if __name__ == '__main__':
    app.run(debug=True)
