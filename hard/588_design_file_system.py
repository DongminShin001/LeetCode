"""
588. Design In-Memory File System
Difficulty: Hard
Companies: Google

Problem:
Design an in-memory file system that supports:
  - ls(path): If path is a file, return [filename]. If a directory, return
    sorted list of its contents (files and directories).
  - mkdir(path): Create the directory path, including all missing parent dirs.
  - addContentToFile(filePath, content): Create the file (and any missing
    parent dirs) and append content to it.
  - readContentFromFile(filePath): Return the file's content as a string.

Examples:

1. mkdir("/a/b/c")
   ls("/")       -> ["a"]
   ls("/a/b")    -> ["c"]
   ls("/a/b/c")  -> []

2. addContentToFile("/a/b/c/d", "hello")
   ls("/")            -> ["a"]
   ls("/a/b/c")       -> ["d"]
   readContentFromFile("/a/b/c/d") -> "hello"

3. addContentToFile("/file", "content1")
   addContentToFile("/file", "content2")
   readContentFromFile("/file") -> "content1content2"  (content is appended)

4. mkdir("/dir1/dir2")
   addContentToFile("/dir1/file1", "data")
   ls("/dir1") -> ["dir2", "file1"]  (sorted alphabetically)

5. ls("/")  on fresh system
   -> []  (root directory is empty)
   mkdir("/x")
   ls("/")
   -> ["x"]
"""
