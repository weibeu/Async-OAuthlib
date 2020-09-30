import aiohttp


class BasicAuth(aiohttp.BasicAuth):

    def __new__(cls, login, password, **kwargs):
        return super(BasicAuth, cls).__new__(cls, str(login), str(password), **kwargs)
