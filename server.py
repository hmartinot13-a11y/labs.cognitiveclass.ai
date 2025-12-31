''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using emotion_detector()
        function. The output returned shows emotions and its 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    items_list = list(response['emotions']) #print(items_list[0])
    #for key, value in items_list:
    #    print(f"{key}: {value}")
    #items_list1 = list(response['dominant_emotion']) #print(items_list[1])
    #for key, value in items_list:
    #    print(f"dominante_emotion:{key}")
    return {items_list[0]}
    #label = response['label']
    #score = response['score']
    #if label is None:
    #return "Invalid input! Try again."
    #return {f"The given text has been identified as
    #{label.split('_')[1]} with a score of {score}."}

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
