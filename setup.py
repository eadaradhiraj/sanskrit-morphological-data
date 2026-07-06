from setuptools import setup

setup(
    name="skt-morph", # The public name for pip
    version="0.1.0",
    description="A Sanskrit Morphological Engine and Reverse-Lookup Dictionary",
    author="Eadara Dhiraj",
    url="https://github.com/eadaradhiraj/sanskrit-morphological-data", 
    packages=["skt_morph"], # Explicitly points to your code folder
    include_package_data=True, # Tells pip to read MANIFEST.in
    install_requires=[], 
)