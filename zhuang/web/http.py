import urllib.request


class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, url, obj_data=""):
        req = urllib.request.Request(self.base_url + url)
        req.add_header(
            "Content-Type", "application/x-www-form-urlencoded;charset=utf-8")

        form_data = urllib.parse.urlencode(obj_data)
        form_data = form_data.encode('utf-8')

        res = urllib.request.urlopen(req, form_data)

        return res.read().decode()
