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