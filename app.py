import requests, os, uuid, json, http.client
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, redirect, url_for, request, render_template, session
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
    orignal_text = request.form['text']
    target_language = request.form['language']

    # Load the values from the .env
    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['LOCATION']
    
    # setup the header information which includes our subscription key
    payload = "{\"0\":\"{\",\"1\":\"\\n\",\"2\":\" \",\"3\":\" \",\"4\":\"\\\"\",\"5\":\"f\",\"6\":\"r\",\"7\":\"o\",\"8\":\"m\",\"9\":\"\\\"\",\"10\":\":\",\"11\":\" \",\"12\":\"\\\"\",\"13\":\"e\",\"14\":\"n\",\"15\":\"_\",\"16\":\"G\",\"17\":\"B\",\"18\":\"\\\"\",\"19\":\",\",\"20\":\"\\n\",\"21\":\" \",\"22\":\" \",\"23\":\"\\\"\",\"24\":\"t\",\"25\":\"o\",\"26\":\"\\\"\",\"27\":\":\",\"28\":\" \",\"29\":\"\\\"\",\"30\":\"d\",\"31\":\"e\",\"32\":\"_\",\"33\":\"D\",\"34\":\"E\",\"35\":\"\\\"\",\"36\":\",\",\"37\":\"\\n\",\"38\":\" \",\"39\":\" \",\"40\":\"\\\"\",\"41\":\"d\",\"42\":\"a\",\"43\":\"t\",\"44\":\"a\",\"45\":\"\\\"\",\"46\":\":\",\"47\":\" \",\"48\":\"\\\"\",\"49\":\"L\",\"50\":\"o\",\"51\":\"n\",\"52\":\"d\",\"53\":\"o\",\"54\":\"n\",\"55\":\" \",\"56\":\"i\",\"57\":\"s\",\"58\":\" \",\"59\":\"t\",\"60\":\"h\",\"61\":\"e\",\"62\":\" \",\"63\":\"c\",\"64\":\"a\",\"65\":\"p\",\"66\":\"i\",\"67\":\"t\",\"68\":\"a\",\"69\":\"l\",\"70\":\" \",\"71\":\"a\",\"72\":\"n\",\"73\":\"d\",\"74\":\" \",\"75\":\"l\",\"76\":\"a\",\"77\":\"r\",\"78\":\"g\",\"79\":\"e\",\"80\":\"s\",\"81\":\"t\",\"82\":\" \",\"83\":\"c\",\"84\":\"i\",\"85\":\"t\",\"86\":\"y\",\"87\":\" \",\"88\":\"o\",\"89\":\"f\",\"90\":\" \",\"91\":\"E\",\"92\":\"n\",\"93\":\"g\",\"94\":\"l\",\"95\":\"a\",\"96\":\"n\",\"97\":\"d\",\"98\":\" \",\"99\":\"a\",\"100\":\"n\",\"101\":\"d\",\"102\":\" \",\"103\":\"o\",\"104\":\"f\",\"105\":\" \",\"106\":\"t\",\"107\":\"h\",\"108\":\"e\",\"109\":\" \",\"110\":\"U\",\"111\":\"n\",\"112\":\"i\",\"113\":\"t\",\"114\":\"e\",\"115\":\"d\",\"116\":\" \",\"117\":\"K\",\"118\":\"i\",\"119\":\"n\",\"120\":\"g\",\"121\":\"d\",\"122\":\"o\",\"123\":\"m\",\"124\":\".\",\"125\":\"\\\"\",\"126\":\",\",\"127\":\"\\n\",\"128\":\" \",\"129\":\" \",\"130\":\"\\\"\",\"131\":\"p\",\"132\":\"l\",\"133\":\"a\",\"134\":\"t\",\"135\":\"f\",\"136\":\"o\",\"137\":\"r\",\"138\":\"m\",\"139\":\"\\\"\",\"140\":\":\",\"141\":\" \",\"142\":\"\\\"\",\"143\":\"a\",\"144\":\"p\",\"145\":\"i\",\"146\"}"
    headers = {
    'x-rapidapi-key': key,
    'x-rapidapi-host': "lingvanex-translate.p.rapidapi.com",
    'Content-Type': "application/json"
    }
    # Create the body of the request with the text to be translated
    # body=[{'text':orignal_text}]
    conn = http.client.HTTPSConnection("lingvanex-translate.p.rapidapi.com")
    conn.request("POST", "/translate", payload, headers=headers)
    res = conn.getresponse()
    data = res.read()
    translated_text = data.decode("utf-8")
    # translated_text = translator_response[0]['translations'][0]['text']
    # Call and render template passing the translated text,original text, and target language to the template
    return render_template(
        'results.html',
        translated_text=translated_text,
        orignal_text=orignal_text,
        target_language=target_language
    )