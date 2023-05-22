"""a module to manage files easily"""

import os
import zipfile
from typing import Union


def prefix_delete(path: str, prefix: str) -> None:
    """
    delete same prefix of mass files in one folder

    :param path: folder where to look at files (without subfolders)
    :param prefix: prefix to remove to files
    """
    if not (isinstance(path, str) and isinstance(prefix, str)):
        raise TypeError("arguments' types are not valid")

    # create a list with all the filenames in folder 'path'
    files = os.listdir(path)

    for current in files:
        if current[:len(prefix)] == prefix:
            try:
                os.rename(os.path.join(path, current),
                          os.path.join(path, current[len(prefix):]))
            except FileExistsError:
                print(f"Unable to rename file '{current}' because the file already exists. Skipping...")
    return


def suffix_delete(path: str, suffix: str) -> None:
    """
    delete same suffix of mass files in one folder

    :param path: folder where to look at files (without subfolders)
    :param suffix: suffix to remove to files
    """
    if not (isinstance(path, str) and isinstance(suffix, str)):
        raise TypeError("arguments' type are not valid")

    # create a list with all the filenames in folder 'path'
    files = os.listdir(path)

    for current in files:
        filename, ext = os.path.splitext(current)
        if filename[-len(suffix):] == suffix:
            try:
                os.rename(os.path.join(path, current),
                          os.path.join(path, filename[:-len(suffix)] + ext))
            except FileExistsError:
                print(f"Unable to rename file '{current}' because the file already exists. Skipping...")
    return


def rename(path: str, old: str, new: str) -> None:
    """
    rename all files in the specified folder

    :param path: folder where to look at files (without subfolders)
    :param old: string to replace
    :param new: replacement string
    """
    if not (isinstance(path, str) and isinstance(old, str) and isinstance(new, str)):
        raise TypeError("arguments' type are not valid")

    # create a list with all the filenames in folder 'path'
    files = os.listdir(path)

    for current in files:
        if old in current:
            try:
                os.rename(os.path.join(path, current),
                          os.path.join(path, current.replace(old, new)))
            except FileExistsError:
                print(f"Unable to rename file '{current}' because the file already exists. Skipping...")


def lower(path: str) -> None:
    """
    rename all files in the folder to lowercase

    :param path: folder where to look at files (without subfolders)
    """
    if not (isinstance(path, str)):
        raise TypeError("arguments' type are not valid")

    # create a list with all the filenames in folder 'path'
    files = os.listdir(path)

    for current in files:
        try:
            os.rename(os.path.join(path, current),
                      os.path.join(path, current.lower()))
        except FileExistsError:
            print(f"Unable to rename file '{current}' because the file already exists. Skipping...")


def upper(path: str) -> None:
    """
    rename all files in the folder to uppercase

    :param path: folder where to look at files (without subfolders)
    """
    if not (isinstance(path, str)):
        raise TypeError("arguments' type are not valid")

    # create a list with all the filenames in folder 'path'
    files = os.listdir(path)

    for current in files:
        try:
            os.rename(os.path.join(path, current),
                      os.path.join(path, current.upper()))
        except FileExistsError:
            print(f"Unable to rename file '{current}' because the file already exists. Skipping...")


def char_delete(path: str, substring: str, maxcount: int = 0) -> None:
    """
    delete filename up to a certain substring (included)

    :param path: folder where to look at files (without subfolders)
    :param substring: string to search for in filename
    :param maxcount: maximum number of files to process (0 for infinite)
    """

    if not (isinstance(path, str) and isinstance(substring, str)):
        raise TypeError("arguments' types are not valid")

    # create a list with all the filenames in folder 'path'
    files = os.listdir(path)
    counter = 0

    for current in files:  # for each file in the folder
        if substring in current:  # only check those with the substring in the filename
            counter += 1
            # if the substring is in it then get the index of the first occurence
            index = current.index(substring)
            try:  # and try to rename it
                os.rename(os.path.join(path, current),
                          os.path.join(path, current[index + len(substring):]))
            except FileExistsError:
                print(
                    f"Unable to rename file '{current}' because the file already exists. Skipping...")

            if counter >= maxcount > 0:
                return


def char_nbr_delete(path: str, char_nbr: int, maxcount: int = 0) -> None:
    """
    delete n characters at the beggining of the filename

    :param path: folder where to look at files (without subfolders)
    :param char_nbr: number of characters to delete
    :param maxcount: maximum number of files to process (0 for infinite)
    """

    if not (isinstance(path, str) and isinstance(char_nbr, int)):
        raise TypeError("arguments' types are not valid")

    # create a list with all the filenames in folder 'path'
    files = os.listdir(path)
    counter = 0

    for current in files:
        try:
            counter += 1
            os.rename(os.path.join(path, current),
                      os.path.join(path, current[char_nbr:]))
        except FileExistsError:
            print(f"Unable to rename file '{current}' because the file already exists. Skipping...")

        if counter >= maxcount > 0:
            return


def search(path: str, keyword: str, subfolder: bool = False) -> tuple:
    """
    search for a keyword in the specified folder

    :param path: folder where to look at files
    :param keyword: keyword to search for
    :param subfolder: whether to look at subfolders
    :return: tuple containing search results as (folders, files)
    """

    if not (isinstance(path, str) and isinstance(keyword, str) and isinstance(subfolder, bool)):
        raise TypeError("arguments' types are not valid")

    folder_results = list()
    files_results = list()

    if subfolder:
        folders, files = list_files(path)
    else:
        folders = [dirname for dirname in os.listdir(path) if os.path.isdir(os.path.join(path, dirname))]
        files = [filename for filename in os.listdir(path) if os.path.isfile(os.path.join(path, filename))]

    for dirname in folders:
        if keyword in dirname:
            folder_results.append(os.path.join(path, dirname))

    for filename in files:
        if keyword in filename:
            files_results.append(os.path.join(path, filename))

    return folder_results, files_results


def replace_in_file(path: Union[str, list], old: str, new: str) -> None:
    """
    replaces every occurence of {old} to {new} for every files in {path}

    :param path: folder where to look for files, can be a list or a string to a folder or file
    :param old: string to replace
    :param new: replacement string
    """
    if isinstance(path, list):
        filenames = path
    elif isinstance(path, str):
        if os.path.isdir(path):
            filenames = list_files(path)[1]
        else:
            filenames = [path]
    else:
        raise TypeError("arguments' types are not valid")

    for filename in filenames:
        with open(filename, 'r') as f:
            txt = f.read()
        if new not in txt:  # if new not already replaced
            txt = txt.replace(old, new)  # replace old by new
        else:
            continue

        with open(filename, 'w') as f:
            f.write(txt)

    return


def copy(source_path: str, target_path: str, replace: bool = False) -> int:
    """
    Copy a file from {source_path} to {target_path}

    Returns 1 if file already exists
    Returns 0 if no error occured
    """
    if not (isinstance(source_path, str) and isinstance(target_path, str)):
        raise TypeError("arguments' types are not valid")

    if not os.path.exists(source_path):
        raise FileNotFoundError()

    if os.path.exists(target_path):
        if replace:
            pass
        else:
            return 1
    else:
        os.system(f"mkdir {os.path.dirname(target_path)}")

    source_file = open(source_path, mode='rb')
    target_file = open(target_path, mode='wb')

    size = divmod(os.path.getsize(source_path), 1024)

    for _ in range(size[0]):
        target_file.write(source_file.read(1024))
    else:
        target_file.write(source_file.read(size[1]))

    source_file.close()
    target_file.close()
    return 0


def safe_delete(source_path: str) -> None:
    """delete a file permanently without confirmation"""
    with open(source_path, mode='wb') as f:
        f.write(b"\x00")  # wipe all file content
    # then delete the file without the original content to make sure no data can be recovered
    os.remove(source_path)
    return


def move(source_path: str, target_path: str) -> None:
    """copy a file from {source_path} to {target_path} then deletes {source_path}"""
    copy(source_path, target_path)
    safe_delete(source_path)
    return


def list_files(dirpath: str = ".", count: bool = False) -> tuple:
    """list all files and folder in the {dirpath} folder and all subfolders"""
    if count:
        folders = 0
        files = 0
    else:
        folders = list()
        files = list()

    for dirpath, dirnames, filenames in os.walk(dirpath):
        if count:
            folders += len(dirnames)
            files += len(filenames)
        else:
            folders.extend(["".join([dirpath, os.sep, dirname]) for dirname in dirnames])
            files.extend(["".join([dirpath, os.sep, filename]) for filename in filenames])

    return folders, files


def zip_files(files: list, target_path: str) -> None:
    """zip every {files} to {target_path}"""
    with zipfile.ZipFile(target_path, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_file:
        for file in files:
            zip_file.write(file)

    return


def unzip_file(zip_path: str, target_path: str) -> "list with extracted files":
    """unzip every file in {zip_path} to {target_path}"""
    with zipfile.ZipFile(zip_path, mode='r') as zip_file:
        zip_file.extractall(target_path)

    return zip_file.namelist()
