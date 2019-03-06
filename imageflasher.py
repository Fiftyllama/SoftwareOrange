import os,webbrowser,sys,time
import CONFIG
def main():
    import os
rootdir = os.path.dirname(os.path.realpath(__file__)) + "/downloads/"
print(rootdir)
webbrowser.open_new_tab('https://www.youtube.com/watch?v=0MCnnfXPSHw')
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        webbrowser.open_new_tab(os.path.join(subdir, file))


if __name__ == '__main__':
	main()




#file = '"'+file+'"'
#imgpath = os.path.join(subdir, file)
#command = "xdg-open " + imgpath
#print(command)
#os.system(command)
