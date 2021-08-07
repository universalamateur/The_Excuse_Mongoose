# Deploying Python Backend Api for The Excuse Mongoose on Deta with Flask

## Flask Api on Deta

### Requirments

> Later this will be excuted via [Deploy Deta Button](https://docs.deta.sh/docs/micros/deploy_to_deta_button)

#### 1. Create a Deta Account

[Here you can create an account.](https://web.deta.sh/)

#### 2. Install in CLI Deta tools

```=bash
curl -fsSL https://get.deta.dev/cli.sh | sh
```

```=psh
iwr https://get.deta.dev/cli.ps1 -useb | iex
```

#### 3.. Logging in to Deta via the CLI

```=bash
deta login
```

### Creating the Deta Server

- From thw working base directory of the project The_Excuse_Mongoose

```=bash
mkdir BE_deta_flask
deta new --python --project The_Excuse_Mongoose --name BE_deta_flask ./BE_deta_flask
```

- The answer in this case:

```=json
{
        "name": "BE_deta_flask",
        "runtime": "python3.7",
        "endpoint": "https://kaq96k.deta.dev",
        "visor": "enabled",
        "http_auth": "disabled"
}
```

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

#### Requirment Python

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
