### Making Huffman Tree Generator in Python by Kevin Chin 11/08/2018
### This code takes a text file and turns it into a Huffman Tree


### Put the name of the text file to convert into binary here (in quotations)
textToConvert = 'perfect-edsheeran.txt'



### ======= CLASSES ========
class Char:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
#Char is Char(String, Natural)
# interp. a character with the string of the character and it's frequency

class Group:
    def __init__(self, frequency, left, right):
        self.frequency = frequency
        self.left = left
        self.right = right
#Group is Group(Natural, Char or Group, Char or Group)
# interp. a group of two Char
# the group's frequency is the sum of the two children frequencies
### =========================



##store the text file into a single string variable
with open(textToConvert, 'r') as mytext:
    text = mytext.read()

LOC = [] #create an empty list of characters

##Function to get the frequency for a character
def getFrequency():
    if len(LOC) is 0: #check if LOC is empty
        return 1
    else:
        for item in LOC: #check if same character already exists
            if item.character is c:
                newFrequency = item.frequency + 1 #new frequency is the old frequency + 1
                LOC.remove(item)                  #remove the old item since new item with updated frequency will be added.
                return newFrequency               #return the updated frequency
        return 1 #case when same character doesn't already exist

##Iterate on each character of text string,
for c in text:
    LOC.append(Char(c, getFrequency()))


##Function to sort list in order of increasing frequency
def orderListByFrequency(loc):
    returnFreq = lambda char : char.frequency
    loc.sort(key=returnFreq)
    #this works on lists containing Group too bcs Group also has .frequency


#sort in order of frequency before starting to make the tree
orderListByFrequency(LOC)

### === CREATE THE TREE ===
while len(LOC) > 1:                                  #loop until there is only one item left in the list
    sumFreq = LOC[0].frequency + LOC[1].frequency
    LOC.append(Group(sumFreq, LOC[0], LOC[1]))       #Group the first two items and add them to the list
    del LOC[0:2]                                     #delete first two items after using them
    orderListByFrequency(LOC)                        #re-order the list by frequency


MasterTree = LOC[0]  #create a MasterTree variable that is the encoding key
del LOC[:] #delete LOC so it doesn't use more memory
### =======================


### The generated Huffman Tree is a class Group
### Group is Group(Natural, Char or Group, Char or Group)
### interp. the starting point of a Huffman tree


## Stuff for Debugging
#print(MasterTree)
#print(MasterTree.frequency)

#print(len(LOC))
#for i in LOC:
#    print(i.character + " : " + str(i.frequency))