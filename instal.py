from requests import get
AminoLab=open("AminoLab.py","a+")
AminoLab.write(get("https://raw.githubusercontent.com/l0v3m0n3y/AminoLab/main/AminoLab.py").text)
objects=open("objects.py","a+")
objects.write(get("https://raw.githubusercontent.com/l0v3m0n3y/AminoLab/main/objects.py").text)
headers=open("headers.py","a+")
headers.write(get("https://raw.githubusercontent.com/l0v3m0n3y/AminoLab/main/headers.py").text)
exception=open("exception.py","a+")
exception.write(get("https://raw.githubusercontent.com/l0v3m0n3y/AminoLab/main/exception.py").text)