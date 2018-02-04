class images:
    def __init__(self, url="link", votes=3, unique_id):
        self.url = url
        self.votes = votes
        self._id = unique_id


    def getURL(self):
        return self.url


    def getVotes(self):
        return self.votes

    #associate user with image id