# Architecture

<img width="1153" alt="Architecture" src="https://github.com/dfong0530/UChat/assets/68403991/2b714fc6-f87d-42eb-916c-9d94e9b2abc6">

## Data Flow

1. GC_Extension is activated

2. Internal API Endpoint targeted (/get_video_data/<videoID>)

3. Request Made to YouTube Data API

4. Model Predicts dislikes and sends data back to GC_Extension