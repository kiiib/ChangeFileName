import requests
import os
import time

x = 193
for i in range(17, 120):
    print("i is " + str(i))
    for j in range(1, 13):
        print("j is " + str(j))
        time.sleep(0.3)
        url = 'https://www.link.jpg'
        root = "D://pics//"
        
        path = root + str(x) + '.jpg'
        x+=1
        print(path)
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(url)
                with open(path,'wb') as f:
                    f.write(r.content)
                    f.close()
                    print("save success")
            else:
                print("file exit")
        except:
            print("爬取失败")

