from setuptools import setup, find_packages

setup(
    name="packetminer",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "scapy",  # Required for PCAP processing
    ],
    entry_points={
        "console_scripts": [
            "packetminer=packetminer.cli:main_menu"  # CLI entry point
        ],
    },
    author="Marc Geggan (@HackerMarc)",
    description="A tool for extracting and sorting IP-MAC mappings from PCAP files",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
)
