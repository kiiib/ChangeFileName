import os;

def reName():
    path = "\\YourPath\\";

    fileList = os.listdir(path);
    for files in fileList:
        Olddir = os.path.join(path, files); #原来的文件路径
        if os.path.isdir(Olddir):   # 如果是文件夹跳过
            continue;
        fileName = os.path.splitext(files)[0];   #文件名
        fileType = os.path.splitext(files)[1];   #文件扩展名

        if fileName.find('#') >= 0:     #如果文件名中含有#
            Newdir = os.path.join(path, fileName.split('#')[0] + "  " + fileName.split('#')[1] + fileType); #新的文件路径
            if not os.path.isfile(Newdir):
                os.rename(Olddir, Newdir);  #重命名

reName();