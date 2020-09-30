import aiohttp


class BasicAuth(aiohttp.BasicAuth):

    def __init__(self, login, password, **kwargs):
        super(BasicAuth, self).__init__(str(login), str(password), **kwargs)
