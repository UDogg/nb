
 

box = "./box-1.txt"#Enter your path here
def cleanse(box):
    
    clientList=[]#deliverable list for client.
    strcmp = ""#string to compare with list
    contents=open(box,'r')
    lst=contents.readline()
    while lst!='':
        row=[]#add to clientlist row by row
        if lst[0] not in strcmp[0:len(strcmp)]:
            strcmp += lst
            for val in lst.strip().split():
                if val.isdigit():#check for integers
                    row.append(int(val))
                else:
                    row.append(str(val))
            clientList+=[row]
        lst=contents.readline()#reads next line where control ended.
    return clientList
    
def color_count(li):
    ret = []
    a = li
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if len(a[j]) < len(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                #bubble sorting just in case the sorted list is required later.
    maximum_balls = a[0][0]
    ret.append(maximum_balls)
    minimum_balls = a[n-1][0]
    ret.append(minimum_balls)
    return ret
    
def main():
    print(cleanse(box))
    print(color_count(cleanse(box)))
main()
