from googletrans import Translator


class TransSystem(object):
    def __init__(self):
        pass

    def trans_from_en_to_ja(self, src):
        translator = Translator()
        trans_ja = translator.translate(src, dest='ja')
        return trans_ja.text

    def __del__(self):
        pass
