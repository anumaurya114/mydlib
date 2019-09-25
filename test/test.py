
import mydlib 

import os 


#print(os.listdir(directory))


def test():
	#This is example for downloading single book from libgen.
	print("starting downlad test")
	book_name = "the road to reality"
	mydlib.get_book_libgen(book_name,auto=False)
	print("book downloaded...")
	



	directory = '../book_lib'
	txt_file = 'txt_file.txt'
	catalogue_dir = 'catalogue_dir'
	
	#for scanning your local library and saving it's information in catalogue 'catalogue_dir' 
	print("directory traversal catalogue test ...")
	mydlib.create_catalogue(directory,catalogue_dir)
	print("created catalogue by directory traversal...")
	print("starting to create library using catalogue file 'catalogue_dir'")
	mydlib.create_library(catalogue_dir)
	print("library creation completed")


	#creating catalogue file using txt_file and saving to 'catalogue_txt'
	catalogue_txt = 'catalogue_txt'
	print("txt file reading catalogue test ...")
	mydlib.create_catalogue(txt_file, catalogue_txt)
	print("created catalogue by reading txt file")
	print("starting to created library using catalogue file 'catalogue_txt'")
	mydlib.create_library(catalogue_txt)
	print("library creation completed")


test()
