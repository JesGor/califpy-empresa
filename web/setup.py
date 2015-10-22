from setuptools import setup

setup(name='web',
	version='0.0.1',
	description='Web para dar de alta a empresas que tendran asociadas varias calificaciones hechas por alumnos',
	url='https://github.com/JesGor/califpy-empresa',
	author='Jesus Prieto Lopez',
	author_email='jesusgorillo@gmail.com',
	license='GNU General Public License',
	packages=['web'],
	install_requires=[
		'django',
		'wheel',
	],
	zip_safe=False)
