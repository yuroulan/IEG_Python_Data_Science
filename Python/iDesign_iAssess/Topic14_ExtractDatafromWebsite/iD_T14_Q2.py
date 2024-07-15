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
import requests
import itertools 

userAgents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1"
]

userAgentCycle = itertools.cycle(userAgents)

def make_request(url):
    userAgent = next(userAgentCycle)

    headers = {
        'User-Agent' : userAgent
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.content.decode('utf-8')
        else:
            return f"Failed to retrieve content: Status code {response.status_code}"
    except Exception as e:
        return f"An error occured: {e}"

def main():
    url = input("Enter the URL to scrape:")
    scrapedData = make_request(url)

    print("Scraped Data: \n")
    print(scrapedData)

if __name__ == "__main__":
    main()
