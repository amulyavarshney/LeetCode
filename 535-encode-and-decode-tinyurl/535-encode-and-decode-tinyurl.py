class Codec:
    def __init__(self):
        self.urls = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        if key in self.urls:
            key = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        self.urls[key] = longUrl
        return "http://tinyurl.com/" + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[shortUrl.split('/')[-1]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))