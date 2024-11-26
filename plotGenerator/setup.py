from setuptools import setup, find_packages

setup(
    name='plotGenerator',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'opencv-python'
    ],
    entry_points={
        'console_scripts': [
            'plotGenerator=plotGenerator:main',
        ],
    },
    test_suite='test',
    python_requires='>=3.7, <4',
)