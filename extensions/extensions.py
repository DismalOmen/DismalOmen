x = input("File name: ").rstrip()

end = ("gif", "jpg", "jpeg", "png", "pdf", "txt", "zip")

if x.endswith("jpg"):
    print("image/jpeg")

elif x.endswith("png"):
    print("image/",x[-3:], sep="")

elif x.endswith("gif"):
    print("image/",x[-3:], sep="")

elif x.endswith("jpeg"):
    print("image/",x[-4:], sep="")

elif x.endswith("pdf"):
    print("application/pdf")

elif x.endswith("PDF"):
    print("application/pdf")

elif x.endswith("txt"):
    print("text/plain")

elif x.endswith("zip"):
    print("application/",x[-3:], sep="")

else:
    print("application/octet-stream")


