## Working with files and directories using pathlib

### Challenge

List the 'type_fire' and 'type_flying' folders, which are inside the pokemon folder, if there are '.json' files inside these folders, create a new folder called weak_against_electric and copy these files to this folder.

### Solution 01

```
import os
import shutil
from glob import glob
from os import path
```

This is the standard solution using Python's native API.

However, it doesn't have good readability and the Glob method does not handle changing paths on different operating systems. 

eg: code written on a windows PC may not run on a linux server because they have different directory structure

### Solution 02

```
from pathlib import Path
from shutil import rmtree
```

This solution uses a module 'pathlib' that offers a good standard solution to manipulate files/folders on Windows paths on a Unix machine (or vice versa)

### Solution 03

```
from pathlib3x import Path
```

That solution has the same performance and is also compatible with windows, linux and mac as solution 02. But has better readability and uses only 1 module. So it will be easier to maintain this code.
