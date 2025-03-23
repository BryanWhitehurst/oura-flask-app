This app is responsible for returning an Oura user's daily sleep metrics
To run the application follow these steps: 

1. Ensure docker is installed
2. Run command: 
    docker build -t oura-flask-app .
3. After the app is built, run command:
    docker run -d -p 5000:5000 --restart=always --env API_KEY=your-oura-api-key oura-flask-app