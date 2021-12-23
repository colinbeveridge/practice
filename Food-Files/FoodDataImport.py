# file for importing food files and creating four lists

# define import function
def load_words(filename):
    with open(filename) as word_file:
        valid_words = list(word_file.read().splitlines())

    return valid_words

def make_lists(file_path,file_names):
    # function that takes general path and file names and imports and puts into lists
    # initialize spot for data
    datalists = []

    # count through file names, loading each one and putting in the list of data lists
    for name in file_names:
        fullpath = file_path+name
        entry = load_words(fullpath)
        datalists.append(entry)
    
    return datalists

def make_keys(datalists):
    # takes list of data lists, makes all entries capital and takes out headers
    keys = []
    for data in datalists:
        keys.append(data[0])
    print(keys)
    return keys

def clean_data(datalists):
    # function that cleans up data
    for listcount,data in enumerate(datalists):
        # remove blank line
        data.remove('')

        # delete headers, already made into keys
        del data[0]

        # standardize all entries to capital letters
        for entry in data:
            entry = entry.upper()

        # logic to find weird values in first list
        if listcount == 0:
            data[-1] = 'Sriracha'
            data[data.find('SALMON2')] = 'SALMON'
        
        else:
            for i in range(len(data)):
                if data[i] != 'YES' and data[i] != 'NO':
                    print(data[i])
        

    
    



# run code in main
if __name__ == '__main__':

    # define full path to this folder
    file_path = R'C:\Users\cbevr\OneDrive\Documents\GitHub\practice\Food-Files'

    # file names
    foodnames = R'\foods.txt'
    highfiber = R'\highfiber.txt'
    lowfat = R'\lowfat.txt'
    low_glycemic_index = R'\low-glycemic-index.txt'

    file_names = [foodnames,highfiber,lowfat,low_glycemic_index]

    datalists = make_lists(file_path,file_names)
    keys = make_keys(datalists)
    cleanlists = clean_data(datalists)



