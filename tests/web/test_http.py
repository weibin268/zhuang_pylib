import unittest
from zhuang.web.http import HttpClient


class TestHttpClient(unittest.TestCase):

    def test_post(self):
        client = HttpClient("https://www.baidu.com");
        result = client.post("","")
        print(result)
        self.assertEqual(1,1,'error')

    def test_a(self):
        print('123')

if __name__ == '__main__':
    unittest.main()
