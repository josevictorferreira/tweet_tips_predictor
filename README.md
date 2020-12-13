## Tweet Tips Predictor
   - A micro service for checking if a tweet is a betting tip or not. The service uses Machine Learning for indentify and predict the result given the text of the tweet.

## Config and Build
   - Install docker on your machine.
   - In the root of the project, create and edit a `.env` file with the following variables:
   ```
FLASK_ENV=development
APP_HOST=localhost
APP_PORT=5000
PERMITTED_REMOTES=0.0.0.0,127.0.0.1,127.20.0.1
DATA_FILENAME=tweets.csv
MONGODB_URI=mongodb://mongodb:27017/
MONGODB_DATABASE=tweets
MONGODB_DATABASE_TEST=tweets_test
   ```
   - Inside the root of the project run $`docker compose up --build`.
   - Done. Check it in your browser `http://localhost:5000/`.


## Endpoint
   #### POST /predict

   Request:

   Content-Type: "application/json"
   ```json
   {
       "text": "A random text.",
       "tipster": "Myself"
   }
   ```

   Response:
   ```json
     {
       "result": false,
       "status": 200
     }
   ```