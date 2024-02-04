
def runfile():
    try:
        f = open('taskfile2.txt', 'x')
    except:
        print('file already exists')
        f = open('taskfile2.txt', 'r')
        if(f.read() != ''):
            print('creating..')
            b = open('taskfile2.txt', 'a')
            b.write('\n one after another word')
            b.close()
        else:
            print('closed')
            f.close()
                



runfile()