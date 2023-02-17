# Project Proposal

Idea 1: App to find where your friends are studying on campus
Potential APIs: Gps/Google maps, Instagram messaging

Idea 2: Outdoor trip planner
Potential APIs: Weather API, trail conditions


Idea: An app to see where your friends are studying on campus (GPS coords/api, Google Maps, Instagram messaging)
We would be able to look at the location of our friends on where they study
We will be using instagram messaging to communicate with friends
- Database: 
    - store previous study locations of users
    - store “friends” or people that you like to study with a lot
    - study time/productivity time
- APIs: Google maps API 
    - Google maps API for location data
    - Instagram API to connect for messaging
- OAuth:
    - can sign in with your google or instagram account
- Decoupled architecture: 
    - front end: website/mobile app to check in when you’re studying/see where your friends are studying
    - back end: process CRUD requests and update database

Idea: Outdoor trip planner (weather api, trail conditions) An application that helps you plan outdoor trips by pulling in information about weather conditions, adventure locations, and providing recommendations for the user based on their interests (hiking/kayaking/skiing/etc)
- Database: Database will store previous trips that users have taken, contain user preferences, and saved/pinned spots to visit in the future
- APIs: 
    - ALL Trails API for looking at ideal trails 
    - NWS(National Weather Service) API for looking at for ideal weather conditions
- OAuth:
    - can sign in with your google account 
- Decoupled architecture: 
    - Front End: website/mobile app to collect details about trip requirements 
    - Back End: connect with APIs and pull trip recommendations for user trips
