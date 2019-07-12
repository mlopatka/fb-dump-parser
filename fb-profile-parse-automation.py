import csv
import os


PATH_FOR_UNZIP = 'path for the zip folder'

def acctocsv(acc):
    for cat in acc:
       if cat[0] in INFERRED_FEATURES:
           line = [0,0,cat[1],cat[0],'',dumpfile]
        else:
            line = [0,cat[1],0,cat[0],'',dumpfile]
        outfile_w.writerow(line)

def clean():
    import shutil
    for item in os.listdir('path for the zip folder'):
        if item[len(item)-4:] != '.zip':
            if item[len(item)-4:] == 'html': os.remove('path for the zip folder'+item)
            else: shutil.rmtree('path for the zip folder'+item)

outfile = open('path to the csv here','w')
outfile_w = csv.writer(outfile)

for dumpfile in os.listdir('path for the zip folder'):
    if dumpfile[len(dumpfile)-4:]== '.zip':
        acc = []
        dict_of_fb_stuff = unzip_fb_payload('path for the zip folder' +dumpfile)
        iterdict(dict_of_fb_stuff)
        acctocsv(acc)
        clean()

outfile.close()
