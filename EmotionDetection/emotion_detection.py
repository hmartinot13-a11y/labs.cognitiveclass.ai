import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
         myemotions = formatted_response['emotionPredictions'][0]['emotion']
         anger_score = myemotions['anger']
         disgust_score = myemotions['disgust']
         fear_score = myemotions['fear']
         joy_score = myemotions['joy']
         sadness_score = myemotions['sadness']
         score = max( myemotions.items(), key=lambda item: item[1] )
         print(f"dominante_emotion : {score}")
    elif  response.status_code == 400:
        return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
               }       
    else:
         print(f"status code is: {myemotions.status_code}") 
    return {
                "anger": anger_score,
                "disgust": disgust_score,
                "fear": fear_score,
                "joy": joy_score,
                "sadness": sadness_score,
                "dominant_emotion": score[0]
            }