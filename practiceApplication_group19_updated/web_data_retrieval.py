from urllib.request import urlopen

class WebDataRetriever:
    def fetch_web_data(self, url):
        try:
            with urlopen(url) as response:
                content = response.read().decode('utf-8')
                return content  # Return the content for further processing
        except Exception as e:
            print(f"Error fetching web data: {e}")
            return ""
