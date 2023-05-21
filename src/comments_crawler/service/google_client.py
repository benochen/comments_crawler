
from comments_crawler.exceptions.configuration_exception import missingapiKeyException


class google_client():
    def __init__(self,config):
        print("toto")
        self.config=config
        self.api_name=config["CLIENT_GOOGLE"]["api_name"]
        self.api_version=config["CLIENT_GOOGLE"]["api_version"]
        self.api_key=self.__load_api_key()

    def __load_api_key(self):
        if(self.config["CLIENT_GOOGLE"]["api_key"]):
            self.api_key=self.config["CLIENT_GOOGLE"]["api_key"]
        else:
            raise missingapiKeyException("API key is missing")

    def load_comments(self,videoid):
        print("load from video="+videoid)