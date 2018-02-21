import urllib.request
import cv2, pandas

getImage = lambda url, name : urllib.request.urlretrieve(url, str(name) + str('.jpg'))
images = pandas.read_csv('index.csv')

def main():

	for index, row in images.iterrows():
		getImage(row[1], index)
		
if __name__ == '__main__':
	main()