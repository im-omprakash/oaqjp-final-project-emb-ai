import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting emotions and score from the response and storing in the dict
    if response.status_code == 200:
        emotion_dict = {
        'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
        'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
        'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
        'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
        'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness']}
        dominant_emotion = max(emotion_dict, key=emotion_dict.get)
        emotion_dict['dominant_emotion'] = dominant_emotion
        return emotion_dict

    else:
        emotion_dict = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None}
        dominant_emotion = None
        emotion_dict['dominant_emotion'] = dominant_emotion
        return emotion_dict