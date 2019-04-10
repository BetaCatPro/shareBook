import requests


class HTTP:

    @staticmethod
    def get(url, return_json=True):
        res = requests.get(url)
        if res.status_code == 200:
            if return_json:
                return res.json()
            else:
                return res.text
        else:
            if return_json:
                return {}
            else:
                return ''
