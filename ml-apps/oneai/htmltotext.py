
# get the api_key from oneai.com 
from config import api_key

# pip install oneai 
import oneai 

oneai.api_key = api_key 

pipeline = oneai.Pipeline(
  steps = [
    oneai.skills.HtmlToArticle(),
  ]
)

output = pipeline.run('https://en.wikipedia.org/wiki/Natural_language_processing')

print(output.html_article.text)
