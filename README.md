
# Book Buddy: Conversational AI with Rasa

## Installation
### Required Dependencies 
- python3 version: 3.7 or 3.8 
- pip3 version: latest
- rasa
  
### Windows
**Installing Rasa**
```powershell
    C:\path\to\project\root> pip3 install -U pip
    C:\path\to\project\root> pip3 install rasa
```

**Creating python environment**
```powershell
    C:\path\to\project\root> pip3 install rasa
    C:\path\to\project\root> python3 -m venv ./venv
```

### Linux / macOS
See official documentation [here](https://rasa.com/docs/rasa/installation/).

## Run Book
Start Bot Steps:
1. Activate virtual environment from project root:
    ```powershell
    .\venv\Scripts\activate
    ```
2. (optional after first setup) Train bot:
    ```powershell
    rasa train
    ```
3. start shell session:
    ```powershell
    rasa shell
    ```
    Or optionally start an interactive shell allowing for step by step training: 
    ```powershell
    rasa interactive
    ```

## Observations
### Development Strategy
- Trial and error was slow an inefficient took too long
- Used more of a read and design approach.
- Vocabulary was insufficient.
- Read documentation
- Watched a tutorial series to accomplish specific tasks

### Differences between a chat bot and a conversational AI

#### Chat Bots
Chat bots parse user commands from a string and execute said commands. Chat bots are really text versions of interfaces, so they don't pick up on more complex intents. For example:

    ```
    Bot:  Hi, how can I help you?
    Usr:  I'd like to book a reservation please, oh and can you tell me the time?
    Bot:  When would you like to book your reservation?
    ```

The bot recognizes the key word reservation and executes a call to the reservation functionality, but does not understand that the user also wished to know what time it was. Further, if the user used language that expressed the same idea but without the keyword (e.g. I'd like a room please) the intent might not be understood and be rejected.


#### Conversational AIs
Conversational AIs attempt to understand the users intent through machine learning rather then just looking for keywords in a string. Using the example from above, a conversational AI would extract 2 intents for the user: the initial intent to book a reservation, and a recursive intent to know what time it was, responding with something like:

    ```
    Bot:  Hi, how can I help you?
    Usr:  I'd like to book a reservation please, oh and can you tell me the time?
    Bot: It's 8:39AM
    Bot: When would you like to book your reservation?
    ```

You'll notice that first the AI responds with the time having understood that this was the most immediate intent of the user, then continued with the original conversation about booking a reservation.

### Why I think this technology could be useful
Conversational AI could be a game changer for use with online education. A conversational AI in conjunction with a application like piazza could be a perfect teaching assistant for students. 

1. Student asks a question to the bot
2. Bot understands and responds
3. or bot does not understand and forwards question to piazza once a instructor endorses the answer, bot knows what to respond next time.

### The limitations of conversational AIs
1. User engagement is low among older user. This may not be much of an issue for student user bases.
2. A lot of time and effort can be put into training. 
3. A lot of time and effort can be put into content generation (bot responses).
4. Would probably need a dedicated developer.

## Glossary

