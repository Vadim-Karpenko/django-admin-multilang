import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
    
setuptools.setup(
     name='django-admin-multilang',  
     version='1.0.5',
     author="Karpenko Vadim",
     author_email="j.rell@protonmail.com",
     description="A very simple Django application that adds the ability on the admin page to select a language manually.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Vadim-Karpenko/django-admin-multilang",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )