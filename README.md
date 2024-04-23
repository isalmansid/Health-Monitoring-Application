# Health Monitoring Application Using machine learning and natural language prcessing

## Run Locally

Go to the project directory

Install dependencies

```bash
  pip install rasa
```

```bash
  pip install flask
```

```bash
  pip install requests
```

Go to rasabot directory

```bash
  cd rasabot
```

open terminal in this directory and run the following command to start rasa server

```bash
  rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
```

Go to web_app directory

```bash
  cd web_app
```

open terminal in this directory and run the following command to start flask server

```bash
    flask run
```

```bash
  cd health-monitoring-app
```

```bash
  npm run start
```



## Technologies used

**Client:** HTML,CSS,React.js

**Server:** Python Flask

**Framework:** Rasa
