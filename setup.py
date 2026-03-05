from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="kamibot",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "click>=8.0.0",
        "rich>=10.0.0",
        "pure-python-adb>=0.3.0.dev0",
        "uiautomator2>=2.16.0",
        "cryptography>=35.0.0",
        "pyyaml>=6.0",
        "requests>=2.27.0",
        "pillow>=9.0.0",
    ],
    entry_points={
        "console_scripts": [
            "kamibot=taktik.cli.main:cli",
            "kamibot-instagram=taktik.cli.main:instagram",
        ],
    },
    author="Kamiklankreatives LLC",
    author_email="kamiklankreatives@gmail.com",
    description="KamiBot — Instagram growth automation for artists and creatives by Kamiklankreatives LLC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/odoublexisthebest-droid/kamibot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: Multimedia :: Sound/Audio",
    ],
    keywords="instagram automation music hiphop creative artist bot kamibot kamiklankreatives",
)
