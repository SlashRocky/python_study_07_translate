from googletrans import Translator


class TransSystem(object):
    def __init__(self):
        pass

    def trans_from_en_to_ja(self, src_text, src_lang, dest_lang):
        translator = Translator()
        trans = translator.translate(src_text, src=src_lang, dest=dest_lang)
        return trans.text

    def __del__(self):
        pass
