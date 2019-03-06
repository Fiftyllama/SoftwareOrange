


from google_images_download import google_images_download
import sys,re,urllib.request,ssl,webbrowser,time#lib
import CONFIG




def imageget():

    response = google_images_download.googleimagesdownload()   #class instantiation

    arguments = {"keywords":"","limit":100,"size":"medium", "format":"jpg"} # enter keywords here to get 100 pictures using that keyword in a folder named after the keyword
    paths = response.download(arguments)   #passing the arguments to the function
    print(paths)   #printing absolute paths of the downloaded images


def keywordlistgenerator():
    dictionary=[]
    wordlistfile = open("simplewordlist.txt", mode='r', encoding='utf-8')
    for line in wordlistfile:
        dictionary.append(line.strip())
    wordlistfile.close()
    return dictionary
def imagedisplay():
    skip()





def main():
    imageget()




"""dic = keywordlistgenerator()
for line in dic:"""
    #webbrowser.open_new_tab(imgurls[0])



if __name__ == '__main__':
	main()
