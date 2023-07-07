import os, shutil, binascii


def sub_string_match(pattern, file_str):
    L =  len(pattern)
    pattern_hash = 0
    for k in range(L):
        pattern_hash = (pattern[k] + pattern_hash*10) % L
    sub_string_hash = 0
    for k in range(L):
        sub_string_hash = (ord(file_str[L-1-k]) + sub_string_hash*10) % L
    for t in range(len(input_file)-L+1):
        if(sub_string_2check == sub_string_hash): # hash matched
            o = 0
            for o in range(L): # check if they are identical in characters 
                if(input_file[t+o] != pattern[o]): break # not identical
            if(o == L): # each of their characters matched -> it's a virus
                return True

        sub_string_2check += (-int(str(sub_string_2check)[0])*(10**(L-1))*10 + file_str[t])


    return False    
def check_founded_pattern(patterns, index,step):
    # Check if virus files have patterns in common
    directory = f"Train\\Malware Sample\\{i}"
    start = j-step
    end = j
    pattern_similarity_occurred = [0 for i in range(len(patterns))]
    for i in range(start, end):
        file_add_2check = os.path.join(directory,os.listdir(directory)[j])
        file_str1 = unicode2hex_cleaned(file_add_2check)
        for j in range(len(patterns)):
            if(sub_string_match(patterns[j],file_str1)):
                pattern_similarity_occurred[j] += 1
    
    patterns = [patterns[i] for i in range(len(patterns)) if(pattern_similarity_occurred[i]>= int(0.2*len(step)))] # if a pattern exist in 20% of malvare files then it's virus pattern
    # Check if non-virus files have patterns not in common
    directory = "C:\git\Anti_Virus\Train\Benign"
    pattern_similarity_occurred = [0 for i in range(len(patterns))]
    for files in listdir(directory):      
        file_add_2check = os.path.join(directory,files)
        file_str1 = unicode2hex_cleaned(file_add_2check)
        for j in range(len(patterns)):
            if(sub_string_match(patterns[j],file_str1)):
                pattern_similarity_occurred[j] += 1
    
    patterns = [patterns[i] for i in range(len(patterns)) if(pattern_similarity_occurred[i] < int(0.2*len(step)))] # if a pattern exist in more than 20% of clean files then it's not virus pattern

def Find_similar_substring(file_ad1, file_ad2, patterns):
    file_str1 = unicode2hex_cleaned(file_ad1)
    file_str2 = unicode2hex_cleaned(file_ad2)
    Domain = min(len(file_str1),len(file_str2))
    lofss = 50 # length of substring to check
    similarity = ['0'*lofss] # check similarity , goes in periods of 50 characters
    min_pattern_length = 5 # min pattern length
    max_pattern_lenght = 20 # max pattern lenght
    i = 0
    while(i<D-50):
        similarity = ['1' for j in range(lofss) if(file_str1[i+j] == file_str2[i+j])]
        for k in range(min_pattern_length, max_pattern_lenght): # range of allowed length for pattern
            if('1'*k in similarity):
                index = similarity.index('1'*k)
                pattern = file_str1[i + index : i + index + k]
                if(pattern not in patterns):
                    patterns.append(pattern)
                

        i+=1

def unicode2hex_cleaned(file_add):
    file_hex_str = ""   
    with open(file_add, "rb") as file:
        file_hex_data = binascii.hexlify(file.read()) # convert to hex equivalent for simplification in calculation
        file_hex_str = file_hex_data.decode('utf-8')
        file_hex_str = file_hex_str[int(0.1*len(file_hex_str)):int(0.6*len(file_hex_str))] # no need to check all of the file beacause the important section of it, is it's first half
        for char in no_use_chars:
            file_hex_str = hex_str.replace(char, '')
        
    return file_hex_str


def find_pattern():
    Virus_patterns = []
    for i in range(20):
        directory = f"Train\\Malware Sample\\{i}"
        j = 0
        patternsOfrow = [] #similar substring (pattern) in a row(consequtive files) since consequtive files have the most similar patterns
        while(j<len(os.listdir(directory))-1): #check files in a row of size 15 since the consequtive files have the most similar patterns
            file2chek_add1 = os.path.join(directory,os.listdir(directory)[j])
            file2chek_add2 = os.path.join(directory,os.listdir(directory)[j+1])
            Find_similar_substring(file2chek_add1, file2chek_add2, patternsOfrow)
            j+=1
            if(j%15==0):
                j += 30
            check_founded_pattern(patternsOfrow, j)
            Virus_patterns[i].extend(patternsOftwo)

    with open('Viruses.txt', 'w') as file:
        for i in range(len(Virus_patterns)):
            for j in range(Virus_patterns[i]):
                file.writelines(Virus_patterns[i][j])


def Is_Virus(input_file, Virus_patterns):
    for i in range(len(Virus_patterns)):
        # Hashing & Matching
        if(sub_string_match(Virus_patterns[i], input_file)):
            return True
    return False


                
def Searching_for_virus(directory, Virus_patterns):

    no_use_chars = [str(hex(i))[2::] for i in range(20,47)]
    no_use_chars.extend([str(hex(i))[2::] for i in range(123, 192)])
    no_use_chars.append(str(hex(0))[2::])
    Virus_patterns = []
    with open('Viruses.txt') as file:
        Virus_patterns = file.readlines()

    for filename in os.listdir(directory):
        file2chek_add = os.path.join(directory,filename)

        file_hex_str = unicode2hex_cleaned(file2chek_add)

        if(Is_Virus(file_hex_str, Virus_patterns)):
            try:
                shutil.move(file2chek_add, f'.\Malware_files\{filename}')
            except:
                os.mkdir('\Malware_files')
                shutil.move(file2chek_add, f'.\Malware_files\{filename}')




# Pre-Process

Virus_patterns = []
find_pattern()


# Main-Process
directory = input()
Searching_for_virus
Searching_for_virus(directory, Virus_patterns)
