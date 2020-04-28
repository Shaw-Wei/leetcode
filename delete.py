import csv    #加载csv包便于读取csv文件
csv_file=open('02423647.csv')    #打开csv文件
csv_reader_lines = csv.reader(csv_file)   #逐行读取csv文件
date=[]    #创建列表准备接收csv各行数据
renshu = 0
for one_line in csv_reader_lines:
    date.append(one_line)    #将读取的csv分行数据按行存入列表‘date’中
    renshu = renshu + 1    #统计行数（这里是学生人数）

print(date[9688])

i = 9688
for i in range(9688,18462):

   # print(i)
    m =(i - 9688)%4
  #  print(m)
    if m != 0:
        date[i] = []




with open('new.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    for row in date:
        writer.writerow(row)

