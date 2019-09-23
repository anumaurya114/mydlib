import setuptools

with open("README.md",'r') as fh:
	long_description = fh.read()


setuptools.setup(

	name='mydlib',  

	version='0.2',


	author="Anurag Maurya",

	author_email="anumaurya114@gmail.com",

	description="A library (books) creator and simple libgen book downloader.",

	long_description=long_description,

	long_description_content_type="text/markdown",

	url="https://github.com/anuragmaurya/mydlib",

	packages=setuptools.find_packages(),

	classifiers=[

				"Programming Language :: Python :: 3",
				"License :: OSI Approved :: MIT License",
     ],

 )
