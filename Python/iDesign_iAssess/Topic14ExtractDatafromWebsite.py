# Problem 1
'''
Extracting Links

Write a python program to get the links used in the website and display the links. Python BeautifulSoub library is used to scrap contents from website.

Input format:
Html code is given as a part of template code. 
Output format:
Prints the links in a html content.
Sample Input and Output 1:

https://www.iana.org/domains/example
'''
from bs4 import BeautifulSoup

html = """
<html>
<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>"""



soup = BeautifulSoup(html, 'html.parser')
links = []

for tag in soup.find_all('a'):
    links.append(tag.get('href'))

for link in links:
    print(link)

# Problem 2
'''
User-Agent Rotation for Web Scraping

Implement a Python script that showcases User-Agent rotation for web scraping using the requests library. User-Agent rotation involves cycling through different User-Agent strings to mimic various browsers or devices during HTTP requests. This technique enhances anonymity and reduces the risk of detection while scraping web content.

Import the necessary libraries (requests and itertools).
Define a list of different User-Agent strings to rotate.
Implement a cyclic iterator using the cycle function from itertools for User-Agent rotation.
Create a function (make_request) that takes a URL, retrieves the next User-Agent string from the cyclic iterator, and sends an HTTP request with the chosen User-Agent header. Return the response content if the request is successful.
In the main function, prompt the user to input a target URL to scrape.
Call the make_request function with the provided URL and display the scraped data if the request was successful.

Sample input & output:

Enter the URL to scrape: 
http://httpbin.org/user-agent
Scraped Data:
{
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
'''