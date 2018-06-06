class Decoder(object):
    """
    直接从百度图片下载的url是经过加密的
    解码器将加密url解码成原来的url
    """
    def __init__(self):
        self.str_table = {
            '_z2C$q': ':',
            '_z&e3B': '.',
            'AzdH3F': '/'
        }

        self.char_table = {
            'w': 'a',
            'k': 'b',
            'v': 'c',
            '1': 'd',
            'j': 'e',
            'u': 'f',
            '2': 'g',
            'i': 'h',
            't': 'i',
            '3': 'j',
            'h': 'k',
            's': 'l',
            '4': 'm',
            'g': 'n',
            '5': 'o',
            'r': 'p',
            'q': 'q',
            '6': 'r',
            'f': 's',
            'p': 't',
            '7': 'u',
            'e': 'v',
            'o': 'w',
            '8': '1',
            'd': '2',
            'n': '3',
            '9': '4',
            'c': '5',
            'm': '6',
            '0': '7',
            'b': '8',
            'l': '9',
            'a': '0'}
        self.char_table = {ord(key): ord(value) for key, value in self.char_table.items()}

    def decode_url(self, pic_url):
        for key, value in self.str_table.items():
            pic_url = pic_url.replace(key, value)
        return pic_url.translate(self.char_table)



