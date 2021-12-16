# Welcome to Comunica Dev API

The Comunica Dev API is a aplications based on SQL and Flask, to manage the Comunica Dev aplication.

To use follow the instructions below.

The entire application is contained within the `app` folder.

`riquerements.txt` is a colletction with all frameworks needed to run te aplication.

The `migrations` folder heave the database configs.

IMPORTANT: Don't forget populate your `.env` file according the `.env.example` file.


    [ BASE URL: https://comunica-dev-api.herokuapp.com/api ]
# 
## Install

To init the aplication run those commands in your terminal

    pip install -r requirements.txt
##
    flask db upgrade

## Run the app

    flask run

#
# Docs
Below you will find the endpoints divided by the api sessions:


- [Users](./documentation/users.md)
- [Address](./documentation/address.md)
- [Categories](./documentation/categories.md)
- [Leads](./documentation/leads.md)
- [lessons](./documentation/lessons.md)
- [captchas](./documentation/captchas.md)
