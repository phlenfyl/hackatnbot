# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from userauth.views import LoginView

class UserAuthentication(Action):

    def name(self) -> Text:
        return "action_user_authentication"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        

        dispatcher.utter_message(text="Hello World!")

        return []
