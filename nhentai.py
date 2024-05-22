try:
    import requests
    import tkinter as tk
    from tkinter import Button, Label
    from PIL import Image, ImageTk
    import io
    from colorama import init, Fore
    import pyperclip
    import threading
except ModuleNotFoundError:
    print("[ERROR] Module Not Found")


def load_link(value):
    pyperclip.copy(value)
    root = tk.Tk()
    Label(root, text="copied to clipboard").pack()
    Button(root , text="ok", command=root.destroy).pack()
    root.mainloop()


init(convert=True)



root = tk.Tk()
root.title("lol...")
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

main_data = []

def returnObject(arr):
    link = "https://wholesomelist.com/api/random/"
    ans = requests.get(link)
    data = ans.json()
    
    # print(Fore.YELLOW + "[INFO] fetching links: " + var + Fore.RESET)
    arr.append({"link": data["entry"]["link"], "title": data["entry"]["title"], "image" : data["entry"]["image"]})


# for i in range(5):
#    


print(main_data)

for i in range(5):
    t1 = threading.Thread(target=returnObject,args=(main_data,), daemon=True)
    t1.start()
    t1.join()

    print(main_data)
    var = main_data[i]["link"]
    value2 = main_data[i]["title"]
    image = main_data[i]["image"]

    button = tk.Button(frame, text=var, command=lambda v=var: load_link(v))
    label1 = tk.Label(frame, text=value2)

    image_data = requests.get(image).content
    image1 = Image.open(io.BytesIO(image_data))
    image1 = image1.resize((125, 150))
    img = ImageTk.PhotoImage(image1)
    photo = tk.Label(frame, image=img)
    photo.image = img

    button.grid(row=i, column=0, padx=5, pady=5, sticky="w")
    label1.grid(row=i, column=1, padx=5, pady=5, sticky="w")
    photo.grid(row=i, column=2, padx=5, pady=5, sticky="w")

    
  
root.mainloop()

