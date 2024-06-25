from setuptools import setup, find_packages

setup(
    name='RandomUAgents',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author='70L0-0j0',
    author_email='70L0-0j0@lamia.xyz',
    description='Library for fetching random user agents based on device type (desktop, mobile, etc.).',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/70L0-0j0/RandomUAgents',  # URL of the project repository
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
