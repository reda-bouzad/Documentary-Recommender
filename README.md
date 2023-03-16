# Documentary-Recommender 🤖

## Description 🔥
This is a simple chatbot that can be used to answer questions about Documentaries , don't know what to watch ? , easy just ask the bot and he will help you figure it out 😆

## Installation 🔥
To install the chatbot, you will need to install the following packages:

```bash
git clone <url>
```
 
 
 
## Virtual Environment 🔥

```bash
py -m venv env
```

## Notice ‼️ 

```bash
Before running the app you need to install all the required dependencies 
```

## Usage 🔥

activate the virtual environment by running the following command:
```bash
env\Scripts\activate
```

run the chatbot by running the following command:
```bash
py manage.py runserver
```

To train the chatbot follow the steps below:

GOTO `app/management/commands/train.py` and add your list of questions and answers to the `conversation` list.

```python
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
]
```

and then run the following command:

```bash
py manage.py train
```



If you want to clear the database, run the following command:
* Note: this will clear the database from all the data that has been trained

```bash
py manage.py clear
```



## Contributing 🔥🔥
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

