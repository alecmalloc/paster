# Paster <img src="app/clipboard.png" width="30">

Paster is a simple python lool that enables cross-platform clipboard sharing, similiar to that found in the
Apple ecosystem. It checks the local clipboard against a shared clipboard in MongoDB and makes sure that all 
clipboards contain the same value.


## Installation and setup

1. Clone the git repository install the project dependencies by running the following:

```pip install -r requirements.txt ```
2. Create a database in MongoDB and paste the credentials into the app/secrets_template.py file (make sure to paste the password into the uri string as well)
3. Cd into the app directory and run the app 

```cd app```
```python main.py```

## Running the script in the background

To run the script in the background, follow the instructions provided in the guide below:
* [Medium](https://medium.com/analytics-vidhya/easiest-way-to-run-a-python-script-in-the-background-4aada206cf29#:~:text=The%20easiest%20way%20of%20running,can%20use%20Windows%20Task%20Scheduler.&text=You%20can%20then%20give%20the,by%20giving%20the%20time%20particulars.)

## Resources and attributes

<a href="https://www.flaticon.com/free-icons/clipboard" title="clipboard icons">Clipboard icons created by Freepik - Flaticon</a>