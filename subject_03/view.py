import eel
import desktop
import trans

# インスタンス生成
trans_system = trans.TransSystem()


@eel.expose
def trans_from_en_to_ja(src_text, src_lang, dest_lang):
    return trans_system.trans_from_en_to_ja(src_text, src_lang, dest_lang)


# GUI生成
app_name = "web"
end_point = "index.html"
size = (920, 390)
desktop.start(app_name, end_point, size)
