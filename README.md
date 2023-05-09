# Paster <img src="app/clipboard.png" width="30">

Paster is a simple python lool that enables cross-platform clipboard sharing, similiar to that found in the
Apple ecosystem. It checks the local clipboard against a shared clipboard in MongoDB and makes sure that all 
clipboards contain the same value.


## Installation and setup

1. Clone the git repository install the project dependencies by running the following:
```pip install -r requirements.txt```
2. Create a database in MongoDB and paste the credentials into the app/secrets_template.py file
3. Rename secrets_template.py to secrets.py
4. Test the script by executing the following command:
```python app/main.py```

## Running the script in the background

To run the script in the background, follow the instructions provided in the guide below:
* [Medium](https://github.com/mobxjs/mobx)

## Resources and attributes

<a href="https://www.flaticon.com/free-icons/clipboard" title="clipboard icons">Clipboard icons created by Freepik - Flaticon</a>