import requests
from urllib import parse


def get_url_encode(params):
    return parse.urlencode(params, encoding='UTF-8', doseq=True)


def check_response(response):
    if str(response.status_code)[0] == "5":
        raise Exception("API 요청 중 오류가 발생했습니다.\n응답 내용: " + str(response.content))


def get_json_from_request(url, params):
    request_url = f"{url}?{get_url_encode(params)}"
    response = requests.get(request_url)
    check_response(response)

    return response.json()


def get_content_from_request(url, params):
    request_url = f"{url}?{get_url_encode(params)}"
    response = requests.get(request_url)
    check_response(response)

    return response.content


def post_request(url, params):
    response = requests.post(url, json=params)
    check_response(response)

    return response.content
