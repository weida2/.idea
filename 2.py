from wx import *

i = 2

app = App()
app.MainLoop()


def nmsl():
    global i
    i += 1
    if i % 2 == 0:
        MessageBox('是否重启？ 重启请按 ALT + F4 or nmSL', "NMsl警告", OK | ICON_WARNING)
    else:
        MessageBox('即将爆炸， 请立即重启', '崩溃警告', OK | ICON_WARNING)


        while True:
            nmsl()

nmsl()