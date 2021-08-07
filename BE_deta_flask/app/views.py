from app import app
from flask import render_template, request, jsonify, make_response
import datetime
import random
from deta import Deta
import os

@app.route('/', methods=["GET"])
def home():
    deta_path = os.getenv("DETA_PATH")
    deta_domain = f"https://{deta_path}.deta.dev"
    date_string = str(datetime.datetime.today().strftime('%Y-%m-%d'))
    #return f'<h1>First Try on API Design</h1><p>This site is a prototype API.</p><p>This has been called {date_string}</p></br><p><a href="https://eelv58.deta.dev/template">All Api Calls listed</a></p><p>Admin Email:  {admin_email}</p>'
    return render_template('docu.html')

@app.route('/docu')
def template():
    return render_template('docu.html')

# Helper function to check if item is present in db, else put it
# Returns a dict with either inserted or present 
def put_excuses(data):
    deta = Deta()
    excuses = deta.Base('excuses')
    fetch_result=excuses.fetch({"content": data["content"]})
    if not (fetch_result.count >0):
        try:
            put_data_result = excuses.put(data)
        except:
            return "Something went wrong"
        return {"inserted" :  put_data_result}
    else:
        return {"present" :  fetch_result.items[0]}
    

# A route to return all of the available entries in data.
@app.route('/api/v1/excuses/putall', methods=['GET'])
def api_put_all():
    """DESCRIPTION.
    ---
    get:
      description: Get all excuses in db
      security:
        - ApiKeyAuth: []
      responses:
        200:
          description: return all excuses
          content:
            application/json:
              schema: Excuse shemata
    """
    # Data
    data_excuses = [{ "order": "Intros", "content": "Sorry I can't come", "class": "SFW" }, { "order": "Intros", "content": "Please forgive my absence", "class": "SFW" }, { "order": "Intros", "content": "This is going to sound crazy but", "class": "SFW" }, { "order": "Intros", "content": "Get this:", "class": "SFW" }, { "order": "Intros", "content": "I can't go because", "class": "SFW" }, { "order": "Intros", "content": "I can't go because", "class": "SFW" }, { "order": "Intros", "content":"I know you're going to hate me but", "class": "SFW" }, { "order": "Intros", "content": "I was minding my own business and boom!", "class": "SFW" }, { "order": "Intros", "content": "I feel terrible but", "class": "SFW" }, { "order": "Intros", "content": "I regretfully cannot attend,", "class": "SFW" }, { "order": "Intros", "content": "This is going to sound like an excuse but", "class": "SFW" }, { "order": "Scapegoat", "content": "my nephew", "class": "SFW" }, { "order": "Scapegoat", "content": "the ghost of Hitler", "class": "NSFW" }, { "order": "Scapegoat", "content": "the Pope", "class": "SFW" }, { "order": "Scapegoat", "content": "my ex", "class": "SFW" }, { "order": "Scapegoat", "content": "high school marching band", "class": "SFW" }, { "order": "Scapegoat", "content": "a sad clown", "class": "SFW" }, { "order": "Scapegoat", "content": "the kid from Air Bud", "class": "SFW" }, { "order": "Scapegoat", "content": "a professional cricket team", "class": "SFW" }, { "order": "Scapegoat", "content": "my Tinder date", "class": "NSFW" }, { "order": "Delay", "content": "just shit the bed", "class": "NSFW" }, { "order": "Delay", "content": "died in front of me", "class": "SFW" }, { "order": "Delay", "content": "won't stop telling me knock knock jokes", "class": "SFW" }, { "order": "Delay", "content": "is having a nervous breakdown", "class": "SFW" }, { "order": "Delay", "content": "gave me syphilis", "class": "NSFW" }, { "order": "Delay", "content": "poured lemonade in my gas tank", "class": "SFW" }, { "order": "Delay", "content": "stabbed me", "class": "SFW" }, { "order": "Delay", "content": "found my box of human teeth", "class": "SFW" }, { "order": "Delay", "content": "stole my bicycle", "class": "SFW" }, { "order": "Delay", "content": "posted my nudes on Instagram", "class": "SFW" }]
    put_returns = []
    for elem in data_excuses:
        put_returns.append(put_excuses(elem))
    # Go through the list of dicts that was returned and sort them
    retun_dict={}
    retun_dict['present']=[]
    retun_dict['inserted']=[]
    for elem in put_returns:
        if 'present' in elem.keys():
            retun_dict['present'].append(elem['present'])
        elif 'inserted' in elem.keys():
            retun_dict['inserted'].append(elem['inserted'])
    response = make_response(jsonify({"content": retun_dict}))
    response.status_code = 200
    response.headers["Content-Type"] = "application/json"
    return response

# A route to return all of the available entries in data.
@app.route('/api/v1/excuses/all', methods=['GET'])
def api_all():
    deta = Deta()
    excuses = deta.Base('excuses')
    res = excuses.fetch()
    all_items = res.items
     # fetch until last is 'None'
    while res.last:
        res = excuses.fetch(last=res.last)
        all_items += res.items
    for elem in all_items:
        del elem['key']
    response = make_response(jsonify({"content": all_items}))
    response.status_code = 200
    response.headers["Content-Type"] = "application/json"
    return response

# A route to return a random excuse
@app.route('/api/v1/excuses/random', methods=['GET'])
def api_random():
    deta = Deta()
    excuses = deta.Base('excuses')
    #Fetch all excuses
    res = excuses.fetch()
    all_items = res.items
     # fetch until last is 'None'
    while res.last:
        res = excuses.fetch(last=res.last)
        all_items += res.items
    parts_exuses = {}
    parts_exuses['Intros']=[]
    parts_exuses['Scapegoat']=[]
    parts_exuses['Delay']=[]
    for elem in all_items:
        parts_exuses[elem['order']].append(elem['content'])
    random_excuse={}
    # Create a random excuse with random Intro Scapegoat and Delay
    random_excuse['excuse'] = f'{parts_exuses["Intros"][random.randint(0, len(parts_exuses["Intros"])-1)]} {parts_exuses["Scapegoat"][random.randint(0, len(parts_exuses["Scapegoat"])-1)]} {parts_exuses["Delay"][random.randint(0, len(parts_exuses["Delay"])-1)]}'
    response = make_response(jsonify(random_excuse))
    response.status_code = 200
    response.headers["Content-Type"] = "application/json"
    return response

# A route to return one personified excuse
@app.route('/api/v1/excuses/custom', methods=['GET'])
def api_custom():
    deta = Deta()
    excuses = deta.Base('excuses')
    #Fetch all excuses
    res = excuses.fetch()
    all_items = res.items
     # fetch until last is 'None'
    while res.last:
        res = excuses.fetch(last=res.last)
        all_items += res.items
    parts_exuses = {}
    parts_exuses['Intros']=[]
    parts_exuses['Scapegoat']=[]
    parts_exuses['Delay']=[]
    for elem in all_items:
        parts_exuses[elem['order']].append(elem['content'])
    custom_excuse={}
    # Check if a name was provided as part of the URL.
    # If name is provided, assign it to a variable.
    # If no name is provided, display an error in the browser.
    if 'name' in request.args:
        name_custom = str(request.args['name'])
        # Create with the given name a custome excuse with random Intro, Scapegoat and Delay
        custom_excuse['excuse'] = f'Dear {name_custom}, {parts_exuses["Intros"][random.randint(0, len(parts_exuses["Intros"])-1)]} {parts_exuses["Scapegoat"][random.randint(0, len(parts_exuses["Scapegoat"])-1)]} {parts_exuses["Delay"][random.randint(0, len(parts_exuses["Delay"])-1)]}'
    else:
        custom_excuse['error'] = "Error: No name provided. Please specify a name."
    #Create the response
    response = make_response(jsonify(custom_excuse))
    if 'error' in custom_excuse.keys():
        response.status_code = 400
    else:
        response.status_code = 200
    response.headers["Content-Type"] = "application/json"
    return response