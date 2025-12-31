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
    
    # Extracting sentiment label and score from the response
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
         emotions = formatted_response['emotionPredictions'][0]['emotion']
         #anger_score = emotions['anger']
         #print(f"emotion anger is: {anger_score}")
         #disgust_score = emotions['disgust']
         #fear_score = emotions['fear']
         #joy_score = emotions['joy']
         #print(f"emotion joy is: {joy_score}")
         #sadness_score = emotions['sadness']
         #dominante_emotion = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)
         #print(f"The dominante value is {dominante_emotion}")
         score = max( emotions.items(), key=lambda item: item[1] )
         print(f"dominante_emotion : {score}")
    else:
         print(f"status code is: {response.status_code}") 
    return {
                'emotions': emotions.items(),
                'dominant_emotion': (([score]))
                #'anger': anger_score,
                #'disgust': disgust_score,
                #'fear': fear_score,
                #'joy': joy_score,
                #'sadness': sadness_score,
                #'dominant_emotion': dominante_emotion
            }