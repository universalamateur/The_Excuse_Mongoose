# Deploying Python Backend Api for The Excuse Mongoose on Deta with Flask

## Deploy steps first actions

### 1. Check the deploy server details

```=bash
deta auth disable
```

### 2. Opening Your Micro To the Public if necessary

```=bash
deta auth disable
```

### 3. Prepare the Deploy

Create a file, *requirements.txt*, which tells Deta which dependencies to install.

#### Requirments

- Flask
- Deta

### 4. Deploying Local Changes

Use a deta deploy command in the folder *BE_deta_flask* to update your Micro.

```=bash
deta deploy
```

### 5. Visiting the Endpoint

under *`https://<path>.deta.dev`* out of the *`deta details`* command the app is visible

## Additional Info

We need to call our app instance *app* and it has to be in a file called *main.py*, which is the only required file for a Python Micro. Of course we can add more files and folders.

## Base Structure

HomeDir
|-app
|-app-tepmplates
|-app-tepmplates-home.html
|-app-__init.py__
|-app-views.py
|-main.py

- main.py just imports the module app `from app import app`
- *-app-__init.py__* imports flask and views.py
- *-app-views.py* has the triggers in it, which are shown in different http calls and imports templates to work with it

## Database

### Database excuses on deta.sh

[Internal link](https://web.deta.sh/home/universalamateur/default/bases/excuses)

#### wrokign queries

```=other
{"class": "SFW", "order": "Intros"}
```
