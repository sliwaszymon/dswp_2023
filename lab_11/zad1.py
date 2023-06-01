import re

nums = re.compile('\d+')
nums3digs = re.compile('\d{3,}')
ipv4s = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
blwords = re.compile('[A-Z][a-z]+')
lines4w = re.compile('.+\s.+\s.+\s.+\n')
urls = re.compile('[https://|http://].+[/]')

num_list, num3dig_list, ipv4_list, blword_list, line4w_list, url_list = [], [], [], [], [], []
with open('strings.txt', 'r', newline='', encoding='utf-8') as file:
    for line in file:
        num_list.append(re.findall(nums, line))
        num3dig_list.append(re.findall(nums3digs, line))
        ipv4_list.append(re.findall(ipv4s, line))
        blword_list.append(re.findall(blwords, line))
        line4w_list.append(re.findall(lines4w, line))
        url_list.append(re.findall(urls, line))

print([val for val in num_list if list(val) != []])
print([val for val in num3dig_list if list(val) != []])
print([val for val in ipv4_list if list(val) != []])
print([val for val in blword_list if list(val) != []])
print([val for val in line4w_list if list(val) != []])
print([val for val in url_list if list(val) != []])