import os

def rename_files():
    #1 get files from a folder
    file_list =  os.listdir(r'C:\Users\Dominic Jay\Documents\Repository\pythonpsm\prank')
    print file_list
    saved_path = os.getcwd()
    print 'Current Working Directory: ' + saved_path
    os.chdir(r'C:\Users\Dominic Jay\Documents\Repository\pythonpsm\prank')
    for file_name in file_list:
        print 'Old Name- ' + file_name
        print 'New Name- ' + file_name.translate(None,'0123456789')
        os.rename(file_name, file_name.translate(None,'0123456789'))
    #2 for each file, rename filename
    os.chdir = saved_path


rename_files()