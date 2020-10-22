import os
import shutil
import time

def main():
    deleted_folders_count = 0
    deleted_files_count = 0
    path = input("/PATH_TO_DELETE ")
    days = 0
    fileorno= input("file or folder ")
    seconds = time.time() - (days * 24 * 60 * 60)
    print("TEst program")
    if os.path.exists(path):
        print(path+' is  found')
        for root_folder, folders, files in os.walk(path):
            #1. name=path+filenme
            #2. Create file name 
            #3. calculate ctime 
            #4. compare ctime
            #5. 
           
            if seconds >= get_file_or_folder_age(root_folder):
                if fileorno=="file" :
                    name = input("filename:")
                    folder=path+"/" + name
                    remove_file(folder)
                    deleted_folders_count += 1 
                elif fileorno=="folder":
                    remove_folder(path)
                    deleted_folders_count += 1       
                            
    else:
        print(path+' is not found')
 

def remove_folder(path):
	if not shutil.rmtree(path):
		print(path+" is removed successfully")
	else:
		print("Unable to delete the "+path)
  
def remove_file(path):
	if not os.remove(path):
     
		print(path+" is removed successfully")
	else:
		print("Unable to delete the "+path)

def get_file_or_folder_age(path):
	ctime = os.stat(path).st_ctime
	return ctime

if __name__ == '__main__':
	main()
 
                                    
                                    
 
"""
import os
import shutil
import time

def main():
	deleted_folders_count = 0
	deleted_files_count = 0
	path = input("/PATH_TO_DELETE ")
	days = 0
	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):
		for root_folder, folders, files in os.walk(path):
            print("root_" + root_folder +"Folder"+ folders + f )
			if seconds >= get_file_or_folder_age(root_folder):
				remove_folder(root_folder)
				deleted_folders_count += 1 
				break
			else:
				for folder in folders:
					folder_path = os.path.join(root_folder, folder)
					if seconds >= get_file_or_folder_age(folder_path):
						remove_folder(folder_path)
						deleted_folders_count += 1 
				for file in files:
					file_path = os.path.join(root_folder, file)
					if seconds >= get_file_or_folder_age(file_path):
						remove_file(file_path)
						deleted_files_count += 1 
                    else:
                        if seconds >= get_file_or_folder_age(path):
                            remove_file(path)
                            deleted_files_count += 1 
	else:
		print(path+' is not found')
	print("Total folders deleted: {deleted_folders_count}")
	print("Total files deleted: {deleted_files_count}")

def remove_folder(path):
	if not shutil.rmtree(path):
		print(path+" is removed successfully")
	else:
		print("Unable to delete the "+path)
  
def remove_file(path):
	if not os.remove(path):
		print(path+" is removed successfully")
	else:
		print("Unable to delete the "+path)

def get_file_or_folder_age(path):
	ctime = os.stat(path).st_ctime
	return ctime

if __name__ == '__main__':
	main()"""