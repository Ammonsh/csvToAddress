from sys import argv

inFile = argv[1]
outFile = argv[2]


with open(inFile) as data:
    with open(outFile, 'w') as out:
        headerItems = data.readline().rstrip("\n").split(",")
        for line in data:
            lineItems = line.rstrip("\n").split(",")
            name = lineItems[1]
            address1 = lineItems[3]
            address2 = lineItems[4]
            city = lineItems[5]
            state = lineItems[6]
            zipCode = lineItems[7]

            if address2 == "":
                out.write(name + "\n" + address1 + "\n" + city + ", " + state + " " + zipCode + "\n\n")
            else:
                out.write(name + "\n" + address1 + "\n" + address2 + "\n" + city + ", " + state + " " + zipCode + "\n\n")

            