# Project Charter: The_Excuse_Mongoose

> Date(YYYY/MM/DD): 2021.10.11

## Project Summary

A web application that can be accesses by erveryone and produces a random funny Excuse out of a dataset.
The Excuse can be personalised or generic and can be displayed in different formats for easy sharing in social media.
The Excuse dataset can be updated by autghorized users.
Excuses can be provided with SFW and/or NFSW content.

## Project Goals

- Understand and Train Backend design (REST API)
  - Built a Back end as restful API in Python with Flask and FastAPI as Web Framework
  - Built a NoSQL database in MongoDB
  - Unit tests and Integration tests
  - Spec-driven development
  - Data Validation
  - Security Concepts
- Understand and train Web Application design
  - Built a Front end web application in REACT
  - Unit tests and Integration tests
  - Data Validation
  - Security Concepts
- Train Documentation integrated into the Process
  - Automated Documentation out of inline comments
  - OpenAPI Specification (OAS) parallel to the development
- Train different CI/CD methods
  - Git Workflow, specialy feature branching
  - Automated Testing
  - GitHub Actions to Deta
  - GitHub Actions to Docker
  - GitHub Actions to a Kubernetes Cluster

## Deliverables

### Backend Api/DB

An Api will be dployed to produce the content of the Excuses

1. Iteration will be a Flask based Python Api  
   1. Deployed to a Deta Micro server
   2. Data in the Deta Database spoken to with the SDK
   3. Deployed to Docker Container App and Db seperate
2. Iteration will be a FastAPI based Python API
   1. Deployed to a Deta Micro server
   2. Data in the Deta Database spoken to with the SDK
   3. Deployed to Docker Container App and Db seperate

#### RESTApi

HTTP Verb | URL Path | Purpose | Possible Parameter
------------ | ------------- | ------------- | -------------
GET | /excuses | List all possible Excuses | Class (NSFW/SFW)
GET | /excuses/generator | Get one random Excuse | Class (NSFW/SFW), Name (String, blank)
GET | /excuses/intros | List all Intros in Excuses | Class (NSFW/SFW)
GET | /excuses/intros/:id | Show a specific Intro in Excuses | -
PUT/PATCH | /excuses/intros/:id | Update a specific Intro in Excuses | JSON Payload with content (String) and CLass (NSFW/SFW)
DELETE | /excuses/intros/:id | Delete a specific Intro in Excuses | -
POST | /excuses/intros/new | Create a new Intro in Excuses | JSON Payload with content (String) and CLass (NSFW/SFW)
GET | /excuses/scapegoats | List all Scapegoats in Excuses | Class (NSFW/SFW)
GET | /excuses/scapegoats/:id | Show a specific Scapegoat in Excuses | -
PUT/PATCH | /excuses/scapegoats/:id | Update a specific Scapegoat in Excuses | JSON Payload with content (String) and CLass (NSFW/SFW)
DELETE | /excuses/scapegoats/:id | Delete a specific Scapegoat in Excuses | -
POST | /excuses/scapegoats/new | Create a new Intro in Excuses | JSON Payload with content (String) and CLass (NSFW/SFW)
GET | /excuses/delays | List all Delays in Excuses | Class (NSFW/SFW)
GET | /excuses/delays/:id | Show a specific Delay in Excuses | -
PUT/PATCH | /excuses/delays/:id | Update a specific Delay in Excuses | JSON Payload with content (String) and CLass (NSFW/SFW)
DELETE | /excuses/delays/:id | Delete a specific Delay in Excuses | -
POST | /excuses/delays/new | Create a new Intro in Excuses | JSON Payload with content (String) and CLass (NSFW/SFW)

### Parameters for an API concept

- Data format:
  - Support of JSON format
- Method structure (CRUD)
  - Read - GET:
    - List Endpoint:
    - Get Endpoint:
  - Update - PUT/POST/PATCH:
  - Create - POST/PUT:
  - Delete - DELETE:
- Data model
  - Excuses
    - class (SFW, NSFW, etc.)
    - content (The data)
    - order (Intros, Scapegoat, Delay)
    - Input id
    - Active <-> Not Active
- Authentication
  - Bearer token: append the token value to the text "Bearer " to the request Authorization header
  - Basic Auth: the Authorization header is going to pass the API a Base64 encoded string representing username and password values, appended to the text "Basic "
- Usage policies
  - Rights and quotas for developers should be easy to understand and work with.

### Frontend Webapp

### CI/CD Setup

## Scope and Exclusion

## Appendix
