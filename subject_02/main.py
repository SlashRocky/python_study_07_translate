import eel
from googletrans import Translator


def main():
    eel.init("web")
    eel.start("index.html")


@eel.expose
def trans_from_en_to_ja(src):
    translator = Translator()
    trans_ja = translator.translate(src, dest='ja')
    return trans_ja.text


if __name__ == '__main__':
    main()
