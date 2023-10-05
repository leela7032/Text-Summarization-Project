import setuptools


with open("README.md", "r", encoding="utf-8") as f:
    long_description =f.read()
    
__version__="0.0.0"

REPO_NAME="Text-Summarizer-Project"
AUTHOR_USER_NAME="leela7032"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="leelamadhav459@gmail.com"
    
    
    
setuptools.setup(

    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leela7032/Text-Summarizer-Project",
    project_urls={
      
      "Bug Tracker": f"https://github.com/leela7032/Text-Summarization/issues",
      
         
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")







)    