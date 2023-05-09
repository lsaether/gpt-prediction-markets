import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# openai.api_key  = os.getenv('OPENAI_API_KEY')
openai.api_key = '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'

def get_prediction_markets(linklist, model="gpt-3.5-turbo"):
    prompt = f'''
        I will need you to take the list of links that I will provide you (at the end of this message, \
        delimited by triple backticks), process their content, and based on this, prepare questions for prediction \
        markets. The information that you must provide must be structured in JSON format and must contain the \
        following keys (in addition, I will provide specifications for each one): \
        - question: statement detailing the event \
        - type of market: here you must specify if the market is binary, categorical or scalar \
        - tokens: if the market is binary or categorical, it specifies all the possible scenarios of the event. \
        If it is scalar, it provides a minimum and maximum value according to the news in question \
        - End Date: this date must be prior to the occurrence of the event, specified in YYYY-MM-DDTHH:MM format \
        in UTC time (for example, if an event occurs on April 12, 2023 at 3:30 p.m. in UTC time). UTC, the closing \
        date must be before 2023-04-12T15:30:00) \
        - Note: a brief description of the market should go here, giving context of the event covered, the meaning \
        of each of the tokens (possible outcomes), and a data source that can be used to find this information. \
        Ideally, this source should be a publicly accessible database, API, or Python code. \
        
        Market Creation Best Practices and Checklist \

        All markets should observe our rules described here: https://docs.zeitgeist.pm/docs/learn/market-rules. \
        The title of the market should either be a statement ("Musk steps down as CEO of Twitter before the end \
        of 2023 (UTC)"), an object ("US Dollar Currency Index at the end of 2023 (UTC)") or a question ("Will \
        Putin remain in power until the end of 2023 (UTC)?"). Prefer statements over questions, except if the \
        topic of the market is controversial. \

        Market Descriptions are usually split into two parts: 1) A general description which clarifies what \
        the market is about and what the recent developments in the matter were. The description will usually \
        specify a high-level description of how the market will work. 2) The resolution criteria, which specify \
        how exactly the market will resolve. \


        ```{linklist}```
    '''
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, #degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

