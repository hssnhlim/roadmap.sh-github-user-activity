import requests

def main():
    url = 'https://api.github.com/users/kamranahmedse/events'
    get_request = requests.get(url)
    print(get_request.json())

if __name__ == '__main__':
    main()

