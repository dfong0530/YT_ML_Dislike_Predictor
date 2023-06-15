# YT_ML_Dislike_Predictor

https://github.com/dfong0530/UChat/assets/68403991/bb0003df-36f6-4621-98a9-da439748818a

### <pre>[Demo Video](https://www.youtube.com/watch?v=qso32-_gCZ8)         [Google Chrome Extension](https://uchat-client.netlify.app/)           [Architecture](https://github.com/dfong0530/YT_ML_Dislike_Predictor/tree/main/Architecture_Diagram)</pre>

###### Developer: David Fong

### Inspiration

As 2022 drew to a close, YouTube declared its decision to eliminate the dislike button, a move aimed at fostering respectful engagement between viewers and content creators and curtailing instances of dislike attacks or harassment.

This change, however, was met with substantial push back from the YouTube community. My project aims to predict dislikes on you tube videos based on historic data of likes, dislikes and views from previous you tube videos.


### What is does

This is a Google Chrome Extension, that predicts the number of dislikes on a you tube videos. Your current window must be on a you tube video before activating the extension.



### How I built it

##### ML (Python, Sklearn, Pandas)

1. I downloaded a csv file from Kaggle. The dataset included columns, with likes, views, and dislikes scrapped from the you tube api.


2. I used pandas to analyze and vizualize the data. For my EDA, I removed, negative, null, and outliers from my dataset.

3. After, I ran a multiple regression algorithm to create my model, which was then saved using joblib.


##### API (Python, Flask, You_Tube_Data_API_V3)

4. I created an internal API using flask. 

I have a single endpoint: '/get_video_data/{videoId}', which returns the likes, dislikes, and views of a you tube video given the videoId.

5. The api, loads in the ml models, when the request is targeted, it makes a request to the you_tube_data api to retrieve the likes and views of the video. It then uses the ml model to predict the number of dislikes.

7. I hosted the api using fly.io


##### GC Extension


6. I created the html and css files for the popup.

7. Then I created the js code to scrape the videoId from the url, and made a request to retrieve the number of dislikes for the video, and then updated the DOM once the data was retrieved.

8. Made the extension public

---


### Installation

1. git clone

2. Navigate to source directory

3. Create virtual env and activate virtual env

4. pip install -r requirements.txt

5. Create .env file in API/ and add 'YT_API_KEY=YOUR_API_KEY'

###### API

- cd API
- python app.py

###### ML

- cd ML
- python ml.py


###### Google Chrome Extension

- Activate API
- cd GC_Extension
- Go Live

