import os

# 8.2 - 109

def run(**args):
	print "[*] in dirlister module."
	files = os.listdir(".")
	
	return str(files)

 