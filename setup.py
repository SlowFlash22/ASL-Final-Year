import setuptools

setuptools.setup(
    name='audio-speech-to-sign-language-converter',
    version='0.1.0',
    description='Python project',
    author='Prajjwal, Vaidik',
    author_email='emailforprajjwal@gmail.com',
    url='https://github.com/SlowFlash22/HandSpeak',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)