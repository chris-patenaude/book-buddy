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

ACCEPTED_GENRES = [
    "fantasy",
    "sci-fi",
    "horrer",
    "mystery",
    "romance"
]

dumby_data = [
    {"title": "The Way of Kings", "genre": "fantasy", "author": "Brandon Sanderson"},
    {"title": "We are Legion (We are Bob)",
     "genre": "sci-fi", "author": "Dennis E Taylor"},
    {"title": "Stranger in a Strange Land",
        "genre": "romance", "author": "Robert A. Heinlein"},
    {"title": "The Dark Tower", "genre": "horrer", "author": "Steven King"},
    {"title": "The DeVincci Code", "genre": "mystery", "author": "Dan Brown"},
    {"title": "Project Hail Mary", "genre": "sci-fi", "author": "Andy Weir"},
    {"title": "The Fifth Season", "genre": "fantasy", "author": "N. K. Jemisin"},
    {"title": "Columbus Day", "genre": "sci-fi", "author": "Craig Alanson"},
    {"title": "The Bridge Kingdom", "genre": "romance",
        "author": "Danielle L. Jensen"},
    {"title": "The Three-Body Problem", "genre": "horrer", "author": "Cixin Liu"},
]


def fetchData():
    return dumby_data


def clean_input(input):
    return "".join([c for c in input if c.isalpha()]).lower()


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

    def validate_genre(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        if not slot_value:
            return {"genre": None}
        genre = clean_input(slot_value)
        if genre not in ACCEPTED_GENRES or len(genre) == 0:
            dispatcher.utter_message(
                text=f"Sorry, I didn't understand, \"{slot_value}.\"")
            return {"genre": None}
        return {"genre": genre}


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
        book_data = fetchData()
        filtered_book_data = filter(
            lambda book: book["genre"] == genre, book_data)
        dispatcher.utter_message(
            text=f"{genre} is one of my favorite genres of book!")
        dispatcher.utter_message(text=f"Check out these titles ...")
        dispatcher.utter_message(text=f"\n")
        for book in filtered_book_data:
            dispatcher.utter_message(
                text=f"\"{book['title']},\" by {book['author']}")
        return []
