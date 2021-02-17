import os

directory = os.getcwd()

files = os.listdir(directory)
print(files)


def delete_mark():
    for file in files:
        if file.endswith('.svg'):
            path = file
            with open(path, 'r') as f
            data = f.read()
            j, k = 0, 0
            for i in range(len(data)):
                if data[i] == '<' and data[i + 1] == 't' and data[i + 2] == 'e':
                    if j == 0:
                        j = i
                    else:
                        continue
                if data[i] == '>' and data[i - 1] == 't' and data[i - 2] == 'x':
                    k = i + 1
            text = data[j: k]
            upd_data = data.replace(text, '')
            with open(path, 'w') as f
            f.write(upd_data)
            f.close()
        else:
            continue

delete_mark()

