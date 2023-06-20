Using ChatGPT and other Large Language Models (LLM's) for querying the internet in natural language is pretty cool, but how about your own company data?  The opportunities have immediate ROI.

Here's some examples.
* Imagine querying your employee intranet for a summary of what the CEO and senior leadership have been publishing lately?
* How about asking your user activity log data when someone last logged in, and what device and IP they were using?
* Or how about asking what your company password policy is, or to give details about acceptable use?

In this article, we will setup a web site that let's you do exactly that, your own company GPT bot, in only 32 lines of code.

If you want to "talk" to your company's data and get answer's in natural language, this is for you.

## Application overview

`app.py` is quite simple.  You feed it some company data.  In this example, i have downloaded several public security policies from purplesec and stored them into a `data` directory.  The app uses `llama_index` to load the files, then it will learn everything contained within those files, then it taps into OpenAI's GPT LLM, so that it can respond to your questions in natual language.

If you understand Google Search, ChatGPT and ChatBots, this is no different, except you get much better results, fine tuned and contextualised in normal human talk.

There's already "hundred's" of tutorials out there doing this, so i won't provide much more detail than the brief description above.

## Setup overview

Get a computer, get the latest Python, create a virtual environment and install the required modules (`llama_index`, `docx2txt`, `flask` and `python-dotenv`)

```
pip install llama_index docx2txt flask python-dotenv
```

Create a `.env` file and put in your `OPENAI_API_KEY=nnn`

Create an `app.py` file, this is the main application file.

I have used Flask for the web server and made use of its templates module and Bootsrap CSS for a little styling.

I used https://gpt-index.readthedocs.io/en/latest/getting_started/starter_example.html and https://gpt-index.readthedocs.io/en/latest/guides/tutorials/fullstack_app_guide.html to develop this solution.


For those that know how, you can clone https://github.com/adrwh/query-with-gpt.git and get running within minutes.

## Finished product

Query: Whats the minimum length for company passwords?

![]("/images/Whats-the-minimum-length-for-company-passwords.png")

Query: Do i need to use special characters in passwords?

![]("images/Do-i-need-to-use-special-characters-in-passwords.png")

Query: Can i use my work computer for gaming?

![]("images/Can-i-use-my-work-computer-for-gaming.png")