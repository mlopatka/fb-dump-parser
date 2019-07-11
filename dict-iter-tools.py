zip_file_loc = '/Users/mlopatka/Downloads/100719-1323-martinlo.zip'

D1 = {1: "/Users/mlopatka/Downloads/100719-1323-martinlo/payment_history"}

PATH_FOR_UNZIP = '/Users/mlopatka/fb-dmi/'
INFERRED_FEATURES = ["ads", "location", "security_and_login_information"]

print(D1)

import os
import zipfile
from pathlib import Path

acc = []

def unzip_fb_payload(path_to_payload_zip):
    print(path_to_payload_zip)
    global PATH_FOR_UNZIP
    archive = zipfile.ZipFile(path_to_payload_zip)

    for file in archive.namelist():
        archive.extract(file, PATH_FOR_UNZIP)

    #all_sub_dirs = [x[0] for x in os.walk(PATH_FOR_UNZIP)]
    keys = (next(os.walk(PATH_FOR_UNZIP))[1])
    dict_dir = {}

    for i in keys:
        dict_dir[i] = os.path.join(PATH_FOR_UNZIP, i)
    return dict_dir


# def dict_generator(key_list):
#     key_dict = {}
#     for i in range(len(key_list)):
#         key_dict[key_list[i]] = string_to_path(key_list[i])
#     print(key_dict)


def testitem():
    return True

def infoquantifier(p):
    # p needs to be the path to the directory at the level of the key (folder)

    sizes = []

    htmlfiles = [os.path.join(root, name)
                 for root, dirs, files in os.walk(p)
                 for name in files
                 if name.endswith((".html", ".htm"))]

    for indiv_file in htmlfiles:
        sizes.append(os.path.getsize(indiv_file))

    return sum(sizes)

def iterdict(d):
    global acc
    for k, v in d.items():
        if isinstance(v, dict):
            iterdict(v)
        else:
            if testitem(v):
                acc.append((k, infoquantifier(v)))
            else:
                acc.append((k, infoquantifier(v)))

print(unzip_fb_payload(zip_file_loc))
