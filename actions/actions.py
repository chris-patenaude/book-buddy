# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import EventType

dumby_data = [
    {"title": "The Way of Kings", "genre": "fantasy"},
    {"title": "We are Legion (We are Bob)", "genre": "sci-fi"},
    {"title": "Stranger in a Strange Land", "genre": "Romance"},
    {"title": "The Dark Tower", "genre": "Horrer"},
    {"title": "The DeVincci Code", "genre": "Mystery"},
]


class ValidateGenreForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_genre_form"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict
    ) -> List[EventType]:
        return []

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        if not slot_value:
            return {"genre": None}

        # Could also execute another action
        # using the dispatver, for example:
        # dispacher.utter_message(text=f"Success! You indicated that you like {genre} books.")
        return {"genre": slot_value}


class ActionSubmitGenreForm(Action):

    def name(self) -> Text:
        return "action_submit_genre_form"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict
    ) -> List[EventType]:
        genre = tracker.get_slot("genre")
        dispatcher.utter_message(
            text=f"{genre} is one of my favorite genres of book!")
        dispatcher.utter_message(text=f"Check out these titles ...")
        dispatcher.utter_message(text=f"TODO")
        return []
