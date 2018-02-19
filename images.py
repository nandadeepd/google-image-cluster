import urllib.request
import cv2, re, pandas

regex = r'.*\/(.*)\.jpg'
url = 'http://mw2.google.com/mw-panoramio/photos/medium/60760466.jpg'
urllib.request.urlretrieve(url, "file_name.jpg")
getImage = lambda url : urllib.request.urlretrieve(url, filnam)
images = pandas.read_csv('index.csv')

def main():

	for index, row in images.iterrows():
		# print(index, row[1])

		# call getImage for row[1] here and it'll write to the file automatically. to get name, use the regex


if __name__ == '__main__':
	main()