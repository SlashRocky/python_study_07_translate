import eel
import desktop
import trans

# インスタンス生成
trans_system = trans.TransSystem()


@eel.expose
def trans_from_en_to_ja(src):
    return trans_system.trans_from_en_to_ja(src)


# GUI生成
app_name = "web"
end_point = "index.html"
size = (920, 290)
desktop.start(app_name, end_point, size)
