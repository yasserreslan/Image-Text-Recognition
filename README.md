# Image to Text Converter

This image to text converter uses a video provided for the challenge among with the detection area marked in red.

## Overview
This tool was created with help of Google's optical character recognition engine Tesseract with support for unicode and the ability to recognize more than 100 languages. For this task we will use custom configurations for Tesseract and image preprocessing appropriate for the trained model.


## Usage
After cloning the repository enter the following commands into the command shell of your virtual environment.

```bash
pip install -r requirements.txt
python main.py
```

Upon running the previous commands into your command shell, Pytube will be responsible of downloading the appropriate video required for the image conversion test. Running time may differ based on internet speeds since download is required.

Once the download is complete you will be met with the full video required for this task and a window showing the preprocessed image opened using OpenCv.The results will appear directly on the command line while the video runs on a frame by frame basis minding. Text may be repeated since the text in the desired frame is the same for longer periods of time and the test is done frame by frame.


## Errors
Common errors occur within the Pytube library. In case of errors please execute the following commands on command shell

```bash
python -m pip install git+https://github.com/Zeecka/pytube@fix_1060
python -m pip install --upgrade pytube
```


## References 
This code is written in accordance to the PEP8 Style Guide for Python Code

[PEP8](https://www.python.org/dev/peps/pep-0008/)
