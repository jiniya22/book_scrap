import requests

chaeking_url = "http://localhost:8080"


def get_id_by_isbn(isbn):
    book_id = None
    try:
        with requests.get(chaeking_url + "/v1/books/isbn13/" + isbn, verify=False, allow_redirects=False,
                          timeout=50) as response:
            if response.status_code == 200:
                if response.json() and 'data' in response.json() and response.json()['data'] is not None:
                    book_id = response.json()['data']['id']
    except requests.exceptions.SSLError as e:
        print("SSLError!!", e)
    except requests.Timeout as e:
        print("Timeout!!", e)
    return book_id


if __name__ == '__main__':
    print(get_id_by_isbn("9791164064410"))
