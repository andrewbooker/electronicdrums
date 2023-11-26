
# Electronic Drums #

### Introduction ###
The aim of this project is to manage kit configurations on the Roland SPD-SX drum unit.
Drum configurations, plus other signal routing and effects settings, are stored in the SPD-SX as xml files.
When connecting the unit via USB as an external drive (selecting `WAVE MGR` in the setup option), 
it is possible to access and inspect these files, and overwrite them to edit or create new drum kit configurations.
The function of this project is to support specifying kit sounds in json files (I have checked mine into the repo) and then upload them.
There is also a process for creating those json files from existing SPD-SX kits.

While connected via USB as an external drive, the SPD-SX cannot function as a drum module.
In order not to have to continuously connect and disconnect the USB lead manually in order to audition sounds having created them, the upload feature of this project includes a switchable USB connector, by means of a serial port (which can be a USB adapter).
Some specific hardware is required for this.
Wiring to follow.

Given the SPD-SX acts as a remote drive, whose files this project will overwrite, I have found it useful to copy the entire contents (max 4GB) onto the local hard disk, and then initialise a git repo there. This serves as a sandbox for checking the outcome of changes, and a backup. I have also initialsed a git repo on the SPD-SX drive, but this is mainly to watch for changes, and I have not used this much to preserve history. I would avoid adding wav files to either git repo.

## Uploading Kit sounds ##

The project supports two modes of upload:
1) uploading kits defined in json file
2) uploading a set of random kit definitions

### Uploading kits defined in JSON ###

Uploads are run from inside the `py` directory.

First, to configure whether to upload to the real SPD-SX or a local copy:

```commandline
cp exampleConfig.json config.json
```
and edit the `config.json` file to specify the `mediaLoc`. The project will write to files within a Roland/SPD-SX subdirectory.
Note git will ignore this file.

```commandline
./upload.py mab
```

### Downloading kit from SPD-SX ###

Downloading can be run from the top level project directory.

This process takes a kit file from the config location and writes it to the specified location. If the config location is the real SPD-SX and the serial port is available, it will attempt to mount and unmount either side of fetching the kit file.

```commandline
py/kitToJson.py kit068.spd somedir/somekit.json
```


### Comparing the machine config with a local backup config ###
This is useful for capturing any changes made by editing patches on the machine vs the last known state. A git diff on the machine remote drive (if you have initialised a git repo there) will also do this.

Call `py/diffKits.py` with the machine and local directory names, to which the application will append the path `Roland/SPD-SX/KIT`.

```commandline
py/diffKits.py /media/$USER/SPD-SX/ ~/Music/hardware/
```

