import eel
from googletrans import Translator


def main():
    eel.init("web")
    eel.start("index.html")


@eel.expose
def trans_from_en_to_ja(src_text, src_lang, dest_lang):
    translator = Translator()
    trans = translator.translate(src_text, src=src_lang, dest=dest_lang)
    return trans.text


if __name__ == '__main__':
    main()
