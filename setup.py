from setuptools import setup

setup(name='random_poem',
    version='1.0',
    description='Returns a random poem from poetry foundation',
	url='https://github.com/kartikye/random_poem/',
	author='Kartikye Mittal',
    author_email='kartikye.mittal+random_poem@gmail.com',
    license='MIT',
    packages=['random_poem'],
    zip_safe=False,
    python_requires='>=3',
    install_requires=[
		'beautifulsoup4',
		'requests'
	])