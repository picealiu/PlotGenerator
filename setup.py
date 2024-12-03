from setuptools import setup, find_packages

setup(
    name='plotGenerator_PL',
    version='1.0',
    include_package_data=True,
    author='PiceaLiu',
    license="MIT",
    url='https://github.com/picealiu/PlotGenerator.git',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'opencv-python'
    ],
    entry_points={
        'console_scripts': [
            'plotGenerator=plotGenerator.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite='test',
    python_requires='>=3.7, <4',
)
