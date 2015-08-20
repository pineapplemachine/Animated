import os
import struct
import argparse
import json



def __main__(args):
    entries = []
    
    print('Loading input files.')
    
    for path in args.input:
        if not os.path.isfile(path):
            print('Failed to load input file "%s".' % path)
        elif path.endswith('.lmp'):
            entries.append(loadanimlmp(path))
            print('Loaded input file "%s".' % path)
        elif path.endswith('.json'):
            entries.extend(convertanim(loadanimjson(path)))
            print('Loaded input file "%s".' % path)
            
    print('Saving data to output file "%s".' % path)
    saveentries(entries, args.output)
    
    print('All done!')



def loadanimjson(path):
    with open(path, 'rb') as jsonfile:
        return json.load(jsonfile)
        
def loadanimlmp(path):
    with open(path, 'rb') as lmpfile:
        return lmpfile.read()[:-1]
        
def saveentries(entries, path):
    data = b''.join(entries)
    data = bytes(data)
    data += chr(255)
    with open(path, 'wb') as lmpfile:
        lmpfile.write(data)



textypedict = {
    'flat': 0,
    'tex': 1,
    'texdecal': 3
}

def convertanim(anim):
    data = []
    nullchr = chr(0)
    
    for textype, starttex, endtex, delay in anim:
        entry = b''
        textypebyte = textypedict.get(textype, textype)
        entry += chr(textypebyte)               # Byte representing anim type
        entry += endtex.ljust(9, nullchr)   # Padded null-terminated string for ending texture
        entry += starttex.ljust(9, nullchr) # Padded null-terminated string for starting texture
        entry += struct.pack('<I', delay)   # Get a little-endian four-byte representation of the frame delay count
        data.append(entry)
    
    return data



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='output lmp file path', type=str, default='ANIMATED.lmp')
    parser.add_argument('-i', '--input', help='input json or lmp file paths', type=str, nargs='+', default=['ANIMATED.json', 'VANILLA.lmp'])
    args = parser.parse_args()
    
    __main__(args)
