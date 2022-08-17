# A shelf tool for Houdini 19 to increment and save the currently open file.
# The version does not have to be qat the end of the file name.
# If there is no versioning, a 3 digit counter starting at 1 will be appended to the original filename.
# Examples: file_v1.hip -> file_v2.hip, file.hip -> file.001.hip, file.009.hip -> file.010.hip
# filename001_sometext.hip -> filename002_sometext.hip

# author: Monika Hedman <monika@monikahedman.com>

import os
import re

def increment(path):
    fn, ext = os.path.splitext(path)
    fn_nums = [n for n in re.finditer('[0-9]+', fn)]
    if not fn_nums:
        return f'{fn}.001{ext}'

    curr_version = fn_nums[-1].group(0)
    span = fn_nums[-1].span()
    new_version = int(curr_version) + 1
    len_padding = len(curr_version) - len(str(new_version))
    vstring = f"{'0'*len_padding}{new_version}"
    return f'{fn[:span[0]]}{vstring}{fn[span[1]:]}{ext}'


def main():
    curpath = hou.hipFile.name()
    newpath = increment(curpath)
    
    hou.hipFile.setName(newpath)
    hou.hipFile.save()

main()
