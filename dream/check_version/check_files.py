import requests, hashlib, json, os

def check_version(files):
    dic = {}
    for file in files:
        if os.path.exists(file):
            with open(file, 'r') as fd:
                hash_file = hashlib.md5(fd.read().encode('utf-8')).hexdigest()
            dic[file] = hash_file
        else:
            dic[file] = ''
    r = requests.post("http://127.0.0.1:5000/", data=dic)
    fil = r.json()
    for file, text in fil.items():
        if text == 'ok':
            pass
        else:
            with open(file, 'w') as fd:
                fd.write(text)

if __name__ == '__main__':
    r = requests.post("http://127.0.0.1:5000/", data={'files': True})
    files = r.json()
    print(files)
    check_version(files)
    # for a in files:
        # check_version(a)
    exit()
