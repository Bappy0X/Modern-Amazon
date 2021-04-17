> This is the back-end API

Built with Python/Flask

## Deploying via Heroku CLI

1. Install the Heroku CLI with npm because the windows install is entirely blocked
```
npm install heroku
```
2. Log in to the CLI
```
heroku login
```
3. Initialise a new git and add remove
```
git init
heroku git:remote -a modern-amazon
```
4. Commit changes and deploy
```
git add .
git commit -am "Add stuff"
git push heroku master
```