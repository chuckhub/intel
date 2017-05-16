import re,csv,urllib2
iplist=[]
url='https://check.torproject.org/exit-addresses'
page = urllib2.urlopen(url)
page_content = page.read()
iplist = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",page_content)
with open ('tor_exit_nodes.csv','w') as torcsv:
    fieldnames = ['IP']
    writer = csv.DictWriter(torcsv, fieldnames=fieldnames, lineterminator = '\n')
    writer.writeheader()
    for ip in iplist:
        writer.writerow({'IP': ip})
