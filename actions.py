"""
Custom actions for Rasa's Recruiting Bot
"""

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import random

from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


# If True, ask for the user's name each time before checking their status
FORGETFUL = False


class ActionCheckStatus(Action):

    def name(self):
        return "action_check_status"

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
            utterance = f'There are no positions available.'
        dispatcher.utter_message(utterance)


class ApplicationStatusForm(FormAction):
    """Form for handling application status requests"""

    def __init__(self, forgetful=FORGETFUL, *args, **kwargs):
        self.forgetful = forgetful
        super().__init__(*args, **kwargs)

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "application_status_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["PERSON"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "PERSON": [
                # if the user has already entered their name in the message
                self.from_entity(entity="PERSON"),
                # if we have to ask them for it explicitly, they may not
                # capitalize it, and it won't be detected as a PERSON, so just
                # use whatever they say
                self.from_text()
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once all the slots are filled, greet the user and reset the slots

        Note: in a real application, the slot resetting should happen after
        ActionCheckStatus, since presumably that action would use this slot.
        """

        person = tracker.get_slot("PERSON")
        parts = person.split(' ')
        firstname = parts[0].capitalize()
        dispatcher.utter_message(f'Hi {firstname}! Let me check that for you')
        if self.forgetful:
            # erase name so user can ask again for someone else
            return [SlotSet('PERSON', None)]
        return []
