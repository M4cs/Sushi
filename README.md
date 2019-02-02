<p align="center">
  <img src="https://image.prntscr.com/image/EQlC-Ph1SLSRjV7BVGGAKA.png" alt="screenshot">
</p>
<p align="center">
  <h1 align="center">Sushi | Cross-Platform GUI for TSSChecker</h1>
</p>

## Changelog:

### 1.0.1~beta:

- Fixed some bugs
- Switched from os.system() to subprocess.check_output() in order to output logs to a window instead of using terminal to see reuslts. ***Testing only on Windows, no clue if MacOS works but it should.***

## About Sushi:

Sushi is the compliment to my other project ["EGTR"](https://github.com/M4cs/EGTR-Futurestore). It is a program that offers a GUI and ease of use along with extra features to TSSChecker. It works on all **Windows and MacOS** platforms. Once a Linux binary has been compiled I will release it for that as well. I named this Sushi because SHSH looks kind of like Sushi so fuck it.

## Usage:

### Saving Blobs:

To save your blobs input a version to save or choose latest version then, just enter your ECID, Device Model, and Boardconfig (not needed for most devices but makes it easier). Once you have all input field set press start and refer to your terminal for output. The blobs should save in your ./download/ folder within the Sushi directory.

### Checking Signed Firmware:

Sushi also comes with a feature to check what firmwares are still signed for your device. To do so click the "Status" button and enter your Device Model. This will run a search and display any signed firmware's available for your device. This will also show what firmwares will be saved when saving blobs.

## Getting Started:

### Requirements:

There are a few requirements you need in order to get Sushi working perfectly. In order to get started, make sure you have the following programs installed:

- git
- Python 3.6+
- Pip for Python3

### Installation:

Once you have these programs installed run the following commands:

```
git clone https://github.com/M4cs/Sushi.git Sushi
cd Sushi
pip3 install -r requirements.txt
python3 sushi.py
```

This should start the program up. It will take a second as it has to download TSSChecker before continuing.

When you first open Sushi you will not have any preset configuration to the program. After running the program successfully once you will be asked to save your configuration. If you would like to save whatever ECID, Device ID, and Boardconfig you have you can simply do so by choosing yes when asked.
