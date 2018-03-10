from PIL import Image
import imagehash
import sys
hash = imagehash.average_hash(Image.open('D:\pythonspace\learnpy\h1.jpg'))
print(hash)
otherhash = imagehash.average_hash(Image.open('D:\pythonspace\learnpy\h2.jpg'))
print(otherhash)