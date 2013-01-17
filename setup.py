from setuptools import setup

setup(
    name = 'dj_autotest',
    version = '0.1',
    description = "App to run tests automatically when the file is changed",
    author = 'Edgar Latorre Romero',
    author_email = 'edgar.romero@dp6.com.br',
    url = '',
    license = 'GPL',
    packages = ['dj_autotest'],
    package_data={'dj_autotest': ['management/*.py', 'management/commands/*']},

    zip_safe=False,

    install_requires=[
        'watchdog',
    ],
)
