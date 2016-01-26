import requests

class parse_request:

    def __init__(self):
        __name__ == "__main__"

    def get_all_in_parse(self):

        url = "https://api.parse.com/1/classes/Test"
        self.log("url: " + url)

        headers = {
            'x-parse-application-id': "65zUyO2ZViKCw89Wqx7i79CClHy93FZemrqYahOK",
            'x-parse-rest-api-key': "ftB5oD3aLAAgqEFacL35dQ4HU2GNd0bRYyM0jdd6",
            'content-type': "application/json"
            }

        self.log("Starting request...")
        response = requests.request("GET", url, headers=headers)
        self.log("Request done...")

        return response.text

    def log(self, toLog):
        print("--> " + toLog)

    def test(self, toLog):
        return toLog
