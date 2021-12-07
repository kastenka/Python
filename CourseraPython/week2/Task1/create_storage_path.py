import tempfile  # This module creates temporary files and directories
import os  # os.path — Common pathname manipulations


# gettempdir() - Return the name of the directory used for temporary files
tempdir = tempfile.gettempdir()

# os.path.join(path, *paths)  - join one or more path components intelligently.
storage_path = os.path.join(tempdir, "storage.data")
print(storage_path)  # C:\Users\masha\AppData\Local\Temp\storage.data

storage_path = os.path.join(tempdir, "StorageDir", "some.data")
print(storage_path)  # C:\Users\masha\AppData\Local\Temp\StorageDir\some.data