def netamount(amt, gst=18):
    return amt+amt*gst/100
print("laptop price", netamount(40000))
print("basket price", netamount(300, 5))
print("gun price", netamount(200, 7))