# Assessing Public Opinion on Electric Vehicles Using Twitter Data
 ## Overview
 The electric vehicle (EV) market has seen exponential growth in recent years. But what do people really think about electric vehicles? To find out, we analyzed Twitter data using Natural Language Processing (NLP) techniques. Twitter provides a unique platform to gather real-time opinions from a diverse range of people. Through sentiment analysis, we can gauge public perception of EVs and compare the sentiment scores across different EV makes and models. So, let's dive in and discover what people are saying about the future of transportation!

 ## Problem Statement
 This project aims to provide valuable insights into the public's perception of EVs and help identify areas of improvement for EV manufacturers. The results of this project can also inform marketing and communication strategies for Tesla and other EV manufacturers.

 ## Data Collection
 For this project, data were collected from Twitter using the snscraper Python library. A list of keywords that includes the names of various electric vehicle (EV) makes and models such as Tesla, Model X, Model Y, BMW i3, and Mercedes EQS were created. To ensure that all relevant tweets are captured, different variations of the make and model names, including abbreviations and misspellings were considered.

For this project, tweets posted between January 1, 2020 and April 9, 2022, were scraped using a custom script that takes advantage of the Twitter Search API. Search was limited to English-language tweets to ensure the accuracy of sentiment analysis. For each tweet, the full text, the date and time it was posted, the username of the person who posted it, and the tweet ID were captured.

Here is an example of how to use dataScraper.py script file in repo:

`python dataScraper.py [Text] [Lang] [Until] [Since]`

## Data Preprocessing
- Text Cleaning: To remove any unnecessary information or noise from the tweet text, all URLs, mentions, hashtags, and special characters were removed using regular expressions.Also, all text was converted to lowercase to standardize the format.
- Filtering: Any tweets that did not mention a specific electric vehicle make or model were filtered out. 
- Hashtag analysis: Most commonly used hashtags were found and some advertisement tweets were identified and removed.

## Exploratory Data Analysis
Below, you can see the proportion of each make of car's tweets to other competitors over time. Go ahead and select different makes from the drop down menu on the right and see the trend over different time spans by changing the date on the horizental axis! Try it on fullscreen mode!

<div class='tableauPlaceholder' id='viz1681672375167' style='position: relative'><noscript><a href='#'><img alt='Popularoty of EV Makes on Twitter Over Time ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PopularityofEVMakesOverTime&#47;PopularotyofEVMakesOverTime&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PopularityofEVMakesOverTime&#47;PopularotyofEVMakesOverTime' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PopularityofEVMakesOverTime&#47;PopularotyofEVMakesOverTime&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1681672375167');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

## Sentiment Analysis
To perform sentiment analysis on the scraped tweets, the pre-trained "cardiffnlp/twitter-roberta-base-sentiment" model from the Hugging Face Transformers library was used. This model was fine-tuned on a large corpus of Twitter data and has been shown to perform well on sentiment analysis tasks. Here is the [link](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment).

AutoTokenizer and TFAutoModelForSequenceClassification classes from the Transformers library were used to load and initialize the model. Each tweet's text was passed through the model and received a sentiment score ranging from 0 (negative sentiment) to 1 (positive sentiment). TensorFlow was used to run the model and get the sentiment scores.


After obtaining the sentiment scores, the compound sentiment score for each EV make and model was calculated. Also some exploratory data analysis was conducted to identify the most commonly discussed makes and models on Twitter and to visualize the overall sentiment distribution and see the trends over time. The results of the sentiment analysis provide valuable insights into public opinion on electric vehicles and can be used to inform business decisions in the EV industry.



