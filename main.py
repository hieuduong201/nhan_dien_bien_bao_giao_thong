import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy
#load the trained model to classify sign
from keras.models import load_model
model = load_model('my_model.h5')

#dictionary to label all traffic signs class.
classes = {
    1: 'Giới hạn tốc độ (20km/h)',
    2: 'Giới hạn tốc độ (30km/h)',
    3: 'Giới hạn tốc độ (50km/h)',
    4: 'Giới hạn tốc độ (60km/h)',
    5: 'Giới hạn tốc độ (70km/h)',
    6: 'Giới hạn tốc độ (80km/h)',
    7: 'Hết giới hạn tốc độ (80km/h)',
    8: 'Giới hạn tốc độ (100km/h)',
    9: 'Giới hạn tốc độ (120km/h)',
    10: 'Cấm vượt',
    11: 'Cấm xe trên 3.5 tấn vượt',
    12: 'Ưu tiên tại ngã tư',
    13: 'Đường ưu tiên',
    14: 'Nhường đường',
    15: 'Dừng lại',
    16: 'Cấm các phương tiện',
    17: 'Cấm xe trên 3.5 tấn',
    18: 'Cấm vào',
    19: 'Chú ý chung',
    20: 'Khúc cua nguy hiểm bên trái',
    21: 'Khúc cua nguy hiểm bên phải',
    22: 'Khúc cua liên tiếp',
    23: 'Đường xóc',
    24: 'Đường trơn trượt',
    25: 'Đường hẹp bên phải',
    26: 'Đang thi công',
    27: 'Tín hiệu giao thông',
    28: 'Người đi bộ',
    29: 'Trẻ em băng qua đường',
    30: 'Xe đạp băng qua',
    31: 'Cẩn thận băng/tuyết',
    32: 'Động vật hoang dã băng qua',
    33: 'Hết giới hạn tốc độ và cấm vượt',
    34: 'Rẽ phải phía trước',
    35: 'Rẽ trái phía trước',
    36: 'Chỉ được đi thẳng',
    37: 'Đi thẳng hoặc rẽ phải',
    38: 'Đi thẳng hoặc rẽ trái',
    39: 'Đi bên phải',
    40: 'Đi bên trái',
    41: 'Vòng xuyến bắt buộc',
    42: 'Hết cấm vượt',
    43: 'Hết cấm xe trên 3.5 tấn vượt'
}
#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Nhận dạng biển báo giao thông ')
top.configure(background='#ffffff')

label=Label(top,background='#ffffff', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
# predict classes
    pred_probabilities = model.predict(image)[0]
    pred = pred_probabilities.argmax(axis=-1)
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#011638', text=sign) 
   

def show_classify_button(file_path):
    classify_b=Button(top,text="Nhận dạng",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#c71b20', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#c71b20', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Nhận dạng biển báo giao thông",pady=10, font=('arial',20,'bold'))
heading.configure(background='#ffffff',foreground='#364156')

heading1 = Label(top, text="Môn Học: Nhập môn trí tuệ nhân tạo",pady=10, font=('arial',20,'bold'))
heading1.configure(background='#ffffff',foreground='#364156')

heading2 = Label(top, text="Danh sách thành viên nhóm",pady=5, font=('arial',20,'bold'))
heading2.configure(background='#ffffff',foreground='#364156')

heading3 = Label(top, text="Văn Huy Du MSSV: 20119205",pady=5, font=('arial',20,'bold'))
heading3.configure(background='#ffffff',foreground='#364156')

heading.pack()
heading1.pack()
heading2.pack()
heading3.pack()
top.mainloop()
