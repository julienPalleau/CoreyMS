list = ["/biocollections/antibodies/5", "/biocollections/antibodies/4", "/biocollections/antibodies/2",
        "/biocollections/antibodies/3", "/biocollections/antibodies/1", "/biocollections/antibodies/10",
        "/biocollections/antibodies/11"]
for line in sorted(list):
    result = line.split("/")
    print(result[0:-1])