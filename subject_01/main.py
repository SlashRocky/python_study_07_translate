from googletrans import Translator


class Trans(object):
    def __init__(self):
        self.translator = Translator()

    def translation(self):

        string_en = input("\n翻訳したい英文を入力して下さい。\n\n")
        trans_ja = self.translator.translate(string_en, dest='ja')
        print(trans_ja.text)

    def __del__(self):
        pass


if __name__ == '__main__':
    trans = Trans()
    trans.translation()
    del trans
