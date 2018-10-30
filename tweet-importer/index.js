"use strict";

require('dotenv').config()
const _ = require('lodash');

var fs = require('fs');
var Twitter = require('twitter');
const loki = require('lokijs');

var db = new loki('twitter.json', {
  autoload: true,
  autoloadCallback: databaseInitialize,
  autosave: true,
  autosaveInterval: 4000
});

function databaseInitialize() {
  var entries = db.getCollection("tweets");
  if (entries === null) {
    entries = db.addCollection("tweets", {
      unique: ['created_at']
    });
  }
}

const api_key = process.env.TWITTER_API_KEY
const api_secret = process.env.TWITTER_API_SECRET
const access_token = process.env.TWITTER_ACCESS_TOKEN
const token_secret = process.env.TWITTER_TOKEN_SECRET

let client = new Twitter({
  consumer_key: api_key,
  consumer_secret: api_secret,
  access_token_key: access_token,
  access_token_secret: token_secret
})


function fetchNewTweets() {
  var params = {
    user_id: process.env.TWITTER_USER_ID
  };

  client.get('statuses/user_timeline', params, function (error, tweets, response) {
    var dbtweets = db.getCollection("tweets");

    tweets.forEach(tweet => {
      try {
        dbtweets.insert(tweet);
      } catch (err) {}
    });

    db.saveDatabase();
  });
}

setInterval(fetchNewTweets, 60000 * 60);