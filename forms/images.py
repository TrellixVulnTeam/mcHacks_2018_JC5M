class images:
    def __init__(self, url="link", votes=3):
        self.url = url
        self.votes = votes


    def getURL(self):
        return self.url


    def getVotes(self):
        return self.votes

    #associate user with image id