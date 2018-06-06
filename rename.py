import os
def rename():
    list1=os.listdir(r"C:\Users\eshu\Desktop\New folder (4)")
    path=os.getcwd()
    print("Chech the working directory" + path)
    os.chdir(r"C:\Users\eshu\Desktop\New folder (4)")

    for name in list1:
        os.rename(name,name.translate(None, "0123456789"))
    os.chdir(path)
rename()
