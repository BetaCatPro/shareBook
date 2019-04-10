from httpUtils import HTTP


class YunShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def serarch_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        res = HTTP.get(url)
        return res

    @classmethod
    def serarch_by_keyword(cls, keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword, count, start)
        res = HTTP.get(url)
        return res
