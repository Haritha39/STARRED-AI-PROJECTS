# STARRED-AI-PROJECTS
## Goal :
Extraction of projects which are starred and belonging to artificial intelligence .
## Requirements :
- python 3+ version
- mysql
- grafana
- pip3 install config/requirements.txt
## Execution : 
    python3 init.py
## Flow of execution :
1. Flask will start running on http://localhost:5000.
2. /ai is the API triggered by webhook configured with push event . Here gitlab-ce used for testing purpose.
3. Information from webhook data which is useful will be storing into database.
4. Webhook data will be sent to our classification model to classify into AI or non-AI project.
5. Project information will be retrieved from gitlab using access token to know whether it is starred or not and if then its star count will be returned.
6. This all information will be storing in database to draw statistics using grafana.
7. We check if project is both AI and starred then it will be in our count as STARRED-AI-PROJECT.









