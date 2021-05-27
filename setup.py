import setuptools

setuptools.setup(
    name="nearest-string",
    version="1.0.0",
    python_requires='>3.7',
    description="finding nearest string with input at text integration levenshtein distance algorithm",
    long_description_content_type="text/markdown",
    url="https://github.com/nguyenhiepvan/nearest-string",
    author="Nguyen Van Hiep",
    author_email="nguyenhiepvan.bka@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    include_package_data=True,
    install_requires=[
        "numpy"
    ],
    entry_points={
        'console_scripts': [
            'nearest_string = nearest_string:main'
        ],
    }
)