import time
import tkinter
import threading

#创建应用程序窗口，
root = tkinter.Tk()
root.title('点击按钮定时关闭窗口')
root['width'] = 400
root['height'] = 300
root.resizable(False,False)

#
richText = tkinter.Text(root,width=380)
richText.place(x=10,y=10,width=380,height=280)
richText.insert('0.0','假设阅读需要10秒')

lbTime = tkinter.Label(root,fg='red',anchor='w')
lbTime.place(x=10,y=250,width=150)


def autoClose():

    for i in range(3):
        print(i)
        lbTime['text'] = '距离窗口关闭还有{}秒'.format(3-i)
        time.sleep(1)
    root.destroy()
    print('destroy')

#
print("123")
start_time=time.time()
t = threading.Thread(target=autoClose,args=())
t.start()

print("启动")
root.mainloop()
print("After 启动")

print("END")