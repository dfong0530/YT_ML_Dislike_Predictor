from flask import Flask
import requests
import json
import os
from dotenv import load_dotenv
from typing import Dict
from joblib import load
from flask_cors import CORS
import pandas as pd


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

load_dotenv()

api_key = os.getenv('YT_API_KEY')
model = load('yt_dislike_model.joblib')

scaler = load('scaler.joblib') 


@app.route('/get_video_data/<videoID>')
def GetData(videoID: str) -> Dict[str, int]:

    try:

        url = f'https://www.googleapis.com/youtube/v3/videos?id={videoID}&key={api_key}&part=snippet,statistics'

        req = requests.get(url)
        data = req.json()

        view_count = int(data["items"][0]["statistics"]["viewCount"])
        like_count = int(data["items"][0]["statistics"]["likeCount"])


        input_data = pd.DataFrame([[view_count, like_count]], columns=['views', 'likes'])

        # scale the input data
        input_data = pd.DataFrame(scaler.transform(input_data), columns=input_data.columns)

        dislike_count = int(model.predict(input_data))

        return {"status": 200, "view_count" : view_count, "like_count" : like_count, "dislike_count": dislike_count}
    
    except:
        
        return {"status": 500, "view_count" : -1, "like_count" : -1, "dislike_count": -1}



if __name__ == '__main__':
    app.run(debug=False)
