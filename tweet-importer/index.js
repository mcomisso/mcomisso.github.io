"use strict";

require('dotenv').config()
const _ = require('lodash');
var moment = require('moment');
var fs = require('fs');

var Twitter = require('twitter');

const api_key = process.env.CONSUMER_API_KEY
const api_secret = process.env.CONSUMER_API_SECRET
const access_token = process.env.TWITTER_ACCESS_TOKEN
const token_secret = process.env.TWITTER_TOKEN_SECRET

let client = new Twitter({
  consumer_key: api_key,
  consumer_secret: api_secret,
  access_token_key: access_token,
  access_token_secret: token_secret
})

const startupDate = Date.now();

function getTweetsFromDate(date) {
  console.log(date);
}

function datesOfPosts() {
  var posts = _.map(fs.readdirSync('./_posts'), (element) => { 
    console.log(element);
    fs.readFileSync('./_posts/'+ element);
  });
}

function fetchNewTweets() {
  
  var params = {
    user_id: process.env.TWITTER_USER_ID,
  };

  client.get('statuses/user_timeline', params, function (error, tweets, response) {
    if (error) {
      console.error(error);
    } else {
      tweets.forEach(tweet => {
        try {
          if (tweet.in_reply_to_status_id != null) { return }
          let date = moment(tweet.created_at, "EEE MMM dd HH:mm:ss Z yyyy");
          console.log(datesOfPosts());
          console.log(tweet);
        } catch (err) { console.error(err); }
      });
    }
  });
  
  getTweetsFromDate(startupDate);
}

fetchNewTweets();