# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import random


class ActionCheckStatus(Action):

    def name(self):
        return "action_check_status"

    def slot_mappings(self):
        return { "name": self.from_text(intent=None)}

    def run(self, dispatcher, tracker, domain):
        # return a random status, just a mockup
        statuses = ["received", "rejected", "interview", "unknown"]
        status = random.choice(statuses)
        return [SlotSet("status", status)]


class ActionCheckPositions(Action):

    def name(self):
        return "action_check_positions"

    def run(self, dispatcher, tracker, domain):
        # return hard-coded open positions, this would normally come from an API
        positions = { 
            "technical": [
                "machine learning engineer",
                "ML product success engineer"
            ],
            "business": []
        }
        position_type = tracker.get_slot("role_type")
        if position_type == "any":
            relevant_positions = positions["technical"] + positions["business"]
        else:
            relevant_positions = positions.get(position_type, [])
        return [SlotSet("positions", relevant_positions)]


class ActionUtterPositions(Action):

    def name(self):
        return "action_utter_positions"

    def run(self, dispatcher, tracker, domain):
        positions = tracker.get_slot("positions")
        # capitalize if not already
        positions = [
            ' '.join([
                w.title() if w.islower() else w for w in position.split()
            ])
            for position in positions
        ]
        role_type = tracker.get_slot("role_type")
        if len(positions) > 1:
            all_but_last = ', '.join(positions[:-1])
            last = positions[-1]
            utterance = f'{all_but_last} and {last} are the open positions.'
        elif positions:
            utterance = f'{positions[0]} is the only open position.'
        else:
            utterance = f'There are no {role_type} positions available.'
        dispatcher.utter_message(utterance)
