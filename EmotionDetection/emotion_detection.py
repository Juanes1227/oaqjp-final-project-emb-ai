import json
import requests

def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    scores = {}

    # Returning a dictionary containing emotion analysis results
    if response.status_code == 200:
        # Extracting emotion score from the response
        scores = formatted_response['emotionPredictions'][0]['emotion']

        dominant_emotion = max(scores, key=scores.get)

        #   Crear un nuevo diccionario que contenga los datos originales y el mayor sentimiento
        scores['dominant_emotion'] = dominant_emotion
    else:
        scores['dominant_emotion'] = None
    return scores
