from setuptools import setup,find_packages

setup(
    name='Costina',
    version='0.0.3',
    keywords=('web','crawling'),
    description='A web crawling framework',
    license='GPL License',
    py_modules=['costina'],
    install_requires=['gevent','requests','bs4','leancloud-sdk'],
    author='Xiaozhe Yaoi@zhitan',
    author_email='xiaozhe.yaoi@gmail.com',
    packages=find_packages(),
    platforms='any',
    url='https://github.com/stevefermi/webcrawler',
)