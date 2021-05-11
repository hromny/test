import requests

def main():
    url = 'https://www.youmzi.com/hot/'
    req = requests.get(url,params=None)
    html = req.text

if __name__ == '__main__':
    main()