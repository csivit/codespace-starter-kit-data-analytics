> Need to add header for Codespace

# Starter Kit for Data Analysis - Codespace 2017

Using this kit, one can do basic analysis on live data from Twitter. Twitter is an awesome playground for data analytics - with 500 million tweets a day, there's a lot of data to play around with.

Broken down into steps, this is the approach we have applied:

- get the Tweets
- extract the information
- perform analysis
- display an output

Our analysis is measuring how often some terms occur in a tweet - term frequency. It's a rough measure of how frequently something is talked about. There's lots more ways to do the same but this is meant to help get you started.

## Installation

Using Git: `git clone https://github.com/csivit/codespace-starter-kit-data-analytics`

Manually: Download the code as a zip file using the big green "Clone or Download" button above, on this page.

## Getting Started

To use this starter kit, you need to:

- Python<br>
  Download and Install Python from http://python.org
- `matplotlib` and `tweepy`<br>
  To install these, install Python then, open command prompt/terminal and run:

  ```
  pip install matplotlib tweepy
  ```

  > On a non windows OS, also pass --user parameter to pip
  >
  > ```
  > pip install --user matplotlib tweepy
  > ```

## Accessing Twitter

In order to get access to Twitter data in our code, we need to interact with the Twitter API. API is essentially a description of how software interacts with itself and with other software - it makes interaction with between different components possible.

### Registration

The first step is the registration of your app. Go to http://apps.twitter.com, log-in to Twitter (if you’re not already logged in) and register a new application. You can now choose a name and a description for your app (for example "Codespace Trial" or similar). You will receive a consumer key and a consumer secret: these are application settings that should always be kept private. From the configuration page of your app, you can also require an access token and an access token secret. Similarly to the consumer keys, these strings must also be kept private: they provide the application access to Twitter on behalf of your account. The default permissions are read-only, which is all we need in our case, but if you decide to change your permission to provide writing features in your app, you must negotiate and obtain a new access token.

Open up `tweet_dump.py` file of this kit and add the 4 values you received from Twitter during registration to it.

### Getting the tweets

We'll be using a Python Library - `tweepy` for interacting with Twitter's API. Tweepy provides a Streaming API to be able to read tweets as they are posted. To run the example provided - fetching all IPL tweets - run the following command on the command prompt/terminal:

```
python tweet_dump.py out.json
```

## Plotting

To create a plot using the results of our analysis, we will use `matplotlib`. To run the example provided - the frequencies of various words in our tweets - run the following command on the command prompt/terminal:

```
python tweet_term_frequency_plot.py out.json
```

## Where to from here

There's so many things you can do with Twitter data. From sentiment analysis to knowledge extraction, the list is endless. Both `matplotlib` and `tweepy` are well documented. Google is your friend.

Hopefully this was enough to get you jump-started on building that awesome product of yours!
