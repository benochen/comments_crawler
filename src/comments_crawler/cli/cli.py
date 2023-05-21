
import sys
import os
from comments_crawler.service.google_client import google_client
import typer
from comments_crawler.exceptions.configuration_exception import configFileNotFoundException
import configparser
import traceback
app = typer.Typer()

def load_config_file(config_file:str):
    if config_file is not None:
        config_file=os.getcwd()+os.path.sep+"ressources/config.ini"
    print("ICI")
    print(config_file)
    if not os.path.exists(config_file):
        raise configFileNotFoundException("The file does not exis ")
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

@app.command()
def loadall(videoid:str=typer.Option("", help=("video to load")),config:str=typer.Option("",help=("config file"))):
    try:
        print(videoid)
        print("load")
        config_array=load_config_file(config)
        print(config_array["CLIENT_GOOGLE"]["API_VERSION"])
        client = google_client(config_array)
    except Exception as e:
        print(e)
        traceback.print_tb(e.__traceback__)


@app.command()
def loadcomments(videoid:str=typer.Option("", help=("video to load"))):
    print(videoid)
    print("load_comments")


def main_1():
    try:
        config_file=""
        if len(sys.argv)>=3 :
            config_file=sys.argv[2]
        video_id=sys.argv[1]


        config=load_config_file(config_file)
        client=google_client(config)
        comments_raw_json=client.load_comments(video_id)
    except Exception as e:
        print(e)

def main():
    app()

if __name__ == "__main__":
    sys.exit(main())