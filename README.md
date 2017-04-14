# Twitter Data Analysis with Python

Twitter is a pretty awesome platform if you think about it. With 500 million tweets a day, there's a lot of data to play around with. And, that's what we're can do.

To do this, we need to:

- get the Tweets
- extract the information
- perform analysis
- display an output

For the purposes of this starter kit, we'll be checking how often some terms occur in a tweet - term frequency. There's lots more to do but this should get you started.

## Installation

To obtain this code:

- If the word "git" makes sense to you, just clone this repository.
- Just download the code as a zip file using the big green "Clone or Download" button above, on this page.

To use this starter kit, you need to install Python. Download and Install Python from http://python.org

> When installing on Python on Windows, make sure to check Add Python to environment variables.

Further, you'll need to install 2 Python packages. To do so, open command prompt/terminal and run:

```
pip install matplotlib tweepy
```

> On non windows platforms, also pass --user parameter to pip
>
> ```
> pip install --user matplotlib tweepy
> ```

## Accessing Twitter

In order to get access to Twitter data in our code, we need to interact with the Twitter API.

<dt>API (Application Programming Interface)</dt>
<dd>
  <i>A set of functions and procedures that allow the creation of applications which access the features or data of an operating system, application, or other service.</i>

  This is how software interacts within itself and with other software - by knowing how to interact with between various components.
</dd>

### Registration

The first step is the registration of your app. Go to http://apps.twitter.com, log-in to Twitter (if you’re not already logged in) and register a new application. You can now choose a name and a description for your app (for example "Codespace Trial" or similar). You will receive a consumer key and a consumer secret: these are application settings that should always be kept private. From the configuration page of your app, you can also require an access token and an access token secret. Similarly to the consumer keys, these strings must also be kept private: they provide the application access to Twitter on behalf of your account. The default permissions are read-only, which is all we need in our case, but if you decide to change your permission to provide writing features in your app, you must negotiate and obtain a new access token.

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

Hopefully this was enough to get you jump-started to building that awesome product of yours!
