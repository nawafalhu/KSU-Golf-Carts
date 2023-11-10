import json
with open('D:\\lab7_files\\TweetsPart1.txt', 'r') as file1:
    result1 = [json.loads(x) for x in file1.readlines()]
out_file1 = open('D:\\lab7_files\\Output_File.txt', 'a')
for i in range(len(result1)):
        if 'created_at' in result1[i]:
            out_file1.write('created_at : ' + str(result1[i]['created_at']))
            out_file1.write(',')
            out_file1.write('Text : ' + str(result1[i]['text'].encode('ascii', 'ignore')))
            out_file1.write(',')
            out_file1.write('User Name : ' + str(result1[i]['user']['screen_name']))
            out_file1.write('\n')

out_file1.close()
with open('D:\\lab7_files\\TweetsPart2.txt', 'r') as file2:
    result2 = [json.loads(x) for x in file2.readlines()]
out_file2 = open('D:\\lab7_files\\Output_File.txt', 'a')
for i in range(len(result2)):
        if 'created_at' in result2[i]:
            out_file2.write('created_at : ' + str(result2[i]['created_at']))
            out_file2.write(',')
            out_file2.write('Text : ' + str(result2[i]['text'].encode('ascii', 'ignore')))
            out_file2.write(',')
            out_file2.write('User Name : ' + str(result2[i]['user']['screen_name']))
            out_file2.write('\n')

out_file2.close()
with open('D:\\lab7_files\\TweetsPart3.txt', 'r') as file3:
    result3 = [json.loads(x) for x in file3.readlines()]
out_file3 = open('D:\\lab7_files\\Output_File.txt', 'a')
for i in range(len(result3)):
        if 'created_at' in result3[i]:
            out_file3.write('created_at : ' + str(result3[i]['created_at']))
            out_file3.write(',')
            out_file3.write('Text : ' + str(result3[i]['text'].encode('ascii', 'ignore')))
            out_file3.write(',')
            out_file3.write('User Name : ' + str(result3[i]['user']['screen_name']))
            out_file3.write('\n')

out_file3.close()



