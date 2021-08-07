# The_Excuse_Mongoose

A web based Excuse Generator as Proof of Concept

## Backend Api

An Api will be dployed to produce the content of the Excuses

### Flask Api on Deta

#### Requirments

> Later this will be excuted via [Deploy Deta Button](https://docs.deta.sh/docs/micros/deploy_to_deta_button)

##### 1. Install in CLI Deta tools

```=bash
curl -fsSL https://get.deta.dev/cli.sh | sh
```

```=psh
iwr https://get.deta.dev/cli.ps1 -useb | iex
```

##### 2. Logging in to Deta via the CLI

```=bash
deta login
```

#### Creating the Deta Server

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
