from setuptools import setup, find_packages
import os

def read_file(filename):
    """Helper function to read a file into a string."""
    base_path = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base_path, filename), 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name='AeroCast',
    version='0.1.1',
    description='A Python package for providing weather information for airports.',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/Rbtsv2/AeroCast',
    author='Charles FOURNIER',
    author_email='charles.fournier@fih.digital',
    license_files=['LICENSE'],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
    ],
    keywords=['weather', 'airport', 'METAR', 'TAF', 'aviation', 'forecast'],
    install_requires=['requests', 'gtts', 'playsound3', 'Babel'],
    python_requires='>=3.7',
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'aerocast = aerocast.__main__:main'
        ]
    }
)