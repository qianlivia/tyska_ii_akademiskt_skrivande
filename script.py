import os
import sys
import pyclan
import pprint
import re
pp = pprint.PrettyPrinter()

# In folder "deu", iterate through and open every .cha files as a dataframe
deu_folder_path = 'deu'
eng_folder_path = 'eng'
folders = [deu_folder_path, eng_folder_path]

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

clan_files = [[], []]
for folder_path in folders:
    blockPrint()
    successful_files = 0
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.cha'):
            file_path = os.path.join(folder_path, file_name)
            try:
                clan_file = pyclan.ClanFile(file_path)
                print(file_path)
                
                # Check if empty
                is_empty = None
                for line in clan_file.line_map:
                    if line.content is not None:
                        continue
                    if "notrans" in line.line:
                        is_empty = True
                        
                if not is_empty:
                    clan_files[folders.index(folder_path)].append(clan_file)
                    successful_files += 1
            except Exception as e:
                print(f'Error in opening file {file_path}: {e}')
    enablePrint()
    print(f'Successfully opened {successful_files} files in folder {folder_path}')
# Now you have a list of dataframes, you can perform further operations on them
clan_file = clan_files[1][10]

# print(len(clan_files[1]))
for line in clan_file.line_map[0:150]:
    print (line.line)
    
random_clanline = clan_file.line_map[149]
pp.pprint(random_clanline.__dict__)
print(random_clanline.content)


# Beath and laughter
# German and English
for j in range(2):
    breaths = 0
    laughter = 0
    num_lines = 0
    num_dialogues = len(clan_files[j])
    # Iterate through dialogues
    for i in range(0, num_dialogues):
        len_d = len(clan_files[j][i].line_map)
        num_lines += len_d
        for line in clan_files[j][i].line_map:
            if line.content is None:
                continue
            if "&=breath" in line.content:
                breaths += 1
            if "&=laugh" in line.content:
                laughter += 1
    print(f"{j}, Average frequency of breaths per person: {breaths/num_dialogues/2}, average laughter: {laughter/num_dialogues/2}")
    

# Hesitations
hes_deu = ["&+äh", "&+mm", "&+ähm", "&+hm", "&+ha", "&+ei", "&+uh", "&+hä", "&+ho", "&+uff", "&+oi", "&+huh", "&+bah", "&+ui"]
hesitations = 0
for i in range(0, len(clan_files[0])):
    for line in clan_files[0][i].line_map:
        if line.content is None:
            continue
        if any(word in line.content for word in hes_deu):
            hesitations += 1
print(f"German, Hesitations: {hesitations/len(clan_files[0])/2}")

hes_eng = ["&-uh", "&-um", "&-eh", "&-mm", "&-hm", "&-ah", "&-huh", "&-ha", "&-er", "&-oof", "&-hee", "&-ach", "&-eee", "&-ew"]
hesitations = 0
for i in range(0, len(clan_files[1])):
    for line in clan_files[1][i].line_map:
        if line.content is None:
            continue
        if any(word in line.content for word in hes_eng):
            hesitations += 1
print(f"English, Hesitations: {hesitations/len(clan_files[0])/2}")

# Backchannels
bc_deu = ["absolut", "na", "ja", "also", "ah", "oah", "ach", "ach so", "gut", "oh", "o", "ha", "hm", "okay", "genau", "uhm", "was", "tatsächlich", "aha", "mhmh", "hmm", "mhm", "genau", "das stimmt", "m", "stimmt", "richtig", "klasse", "klar", "cool", "ist cool", "schön", "wow", "krass", "super", "geil", "süß", "wie süß", "toll", "klasse", "sauber", "spannend", "natürlich", "bestimmt", "eben", "sicher", "sicherlich", "boah", "echt", "heftig", "komisch", "schrecklich", "wirklich", "yes", "no", "nein", "äh", "mm", "ähm", "hm", "ei", "uh", "hä", "ho", "uff", "oi", "huh", "bah", "ui", "nä", "freilich", "mein gott", "gott", "fantastisch", "wunderbar", "naja", "so", "och", "wie bitte", "bitte", "bitte was", "was bitte", "was denn", "wie toll", "nee", "ne", "gell", "nja", "wahnsinn", "grauenvoll", "schade", "furchtbar", "jawohl", "nicht", "nö", "das ist", "prima", "nett", "ist"]
bc_eng = ["absolutely", "ach", "ah", "ah-hah", "aha", "ahah", "aw", "aww", "eeh", "eh", "ew", "exactly", "gee", "golly", "goodness", "gosh", "he", "hee", "hm", "huh", "huh-hm", "huh-huh", "huh-oh", "huh-uh", "indeed", "interesting", "jee", "jeez", "m-kay", "m-m", "m-yeah", "mhm", "mm", "mmm", "nah", "nice", "no", "nuh", "nuh-uh", "oh", "okay", "ok", "oof", "ooh", "ow", "pardon", "really", "right", "sorry", "sure", "true", "ugh", "uh", "uh-hah", "uh-hm", "uh-ho", "uh-huh", "uh-oh", "uh-uh", "uh hah", "uh huh", "uhhm", "uhhuh", "um", "wah", "well", "what", "why", "wooh", "wow", "yah", "yao", "yea", "yea-m", "yeah", "yep", "yes", "yuck", "yuh", "yup", "ha", "er", "seriously", "nay", "yay", "yapp", "god", "my god", "my gosh", "jesus", "christ", "of course", "but of course", "so", "how cool", "how exciting", "exciting", "scary", "how nice", "how cool", "uhhuh", "good", "wonderful", "how wonderful", "not nice", "i see", "great", "awesome", "amazing", "super", "sick", "haha", "heh", "meh", "for real", "that is good", "oh my", "i know", "ohgod", "mygod", "neat", "mm-hm", "terrible", "pretty much", "sweet", "marvelous", "no way", "weird", "i'm glad", "it's hard", "obviously", "that's", "oops", "whoops", "too bad", "not", "ohmygod", "my goodness", "ohmygosh", "cool", "oh i see", "alright"]
num_bc = 0
for i in range(0, len(clan_files[0])):
    for line in clan_files[0][i].line_map:
        if line.content is None:
            continue
        line_content = line.content
        line_content = " ".join([word for word in line_content.split() if not word.startswith('&=')])
        
        # Remove words that start with a special character
        line_content = re.sub(r'(&-|&\+|&=|&!=)', '', line_content)
        line_content = re.sub(r'@[^\s]+', '', line_content)
        # Remove punctuations except ' and -
        line_content = re.sub(r'[^\w\s\'-]', '', line_content)
        line_content = re.sub(r'xxx', '', line_content)
        
        if line_content.endswith('laufend'):
            line_content = line_content[:-7].strip()
        
        line_content = line_content.lower()
        line_content = line_content.strip()
        
        if line_content in bc_deu or all(word in bc_deu for word in line_content.split()):
            num_bc += 1
print(f"German, Backchannels: {num_bc/len(clan_files[0])/2}")

num_bc = 0
for i in range(0, len(clan_files[1])):
    for line in clan_files[1][i].line_map:
        if line.content is None:
            continue
        line_content = line.content
        line_content = " ".join([word for word in line_content.split() if not word.startswith('&=')])
        
        # Remove words that start with a special character
        line_content = re.sub(r'(&-|&\+|&=|&!=)', '', line_content)
        line_content = re.sub(r'@[^\s]+', '', line_content)
        # Remove punctuations except ' and -
        line_content = re.sub(r'[^\w\s\'-]', '', line_content)
        line_content = re.sub(r'xxx', '', line_content)
        
        line_content = line_content.lower()
        line_content = line_content.strip()
        if line_content.endswith('laughing'):
            line_content = line_content[:-8].strip()
        if line_content.endswith('laugh'):
            line_content = line_content[:-5].strip()
        if line_content.endswith('distorted'):
            line_content = line_content[:-9].strip()
        if line_content.endswith('distort'):
            line_content = line_content[:-8].strip()
        if line_content.endswith('smiles'):
            line_content = line_content[:-6].strip()
        if line_content.endswith('groaning'):
            line_content = line_content[:-8].strip()
        if line_content.endswith('whispering'):
            line_content = line_content[:-10].strip()
            
        if line_content in bc_eng or all(word in bc_eng for word in line_content.split()):
            num_bc += 1
            
print(f"English, Backchannels: {num_bc/len(clan_files[1])/2}")

# Questions
q_deu = ["was", "wann", "wer", "wo", "warum", "wie", "wozu", "wen", "wem", "wohin", "woher", "was für", "welcher", "welche", "welches", "weswegen", "weshalb", "mit wem", "woran", "worüber", "worin", "womit", "wofür", "wogegen", "wessen", "worauf", "wovon", "worunter", "wovor", "wobei", "wodurch", "wie viel", "wie vieler", "wie vielen", "wie viele", "wieso", "inwiefern", "inwieweit"]
q_eng = ["what", "when", "how", "where", "who", "why", "which", "whose", "whom", "in what", "to what", "for what", "with what", "in which", "to which", "in what way", "to what extent", "in what respect", "to what degree"]
question_words = [q_deu, q_eng]

for i in range(2):
    num_q_1 = 0
    num_q_2 = 0
    num_q_3 = 0
    num_q = 0
    num_non_q = 0
    qw = question_words[i]
    for j in range(0, len(clan_files[i])):
        for line in clan_files[i][j].line_map:
            if line.content is None:
                continue
            if "?" not in line.content:
                num_non_q += 1
                continue
            line_content = line.content
            num_q += 1
            
            line_content = " ".join([word for word in line_content.split() if not word.startswith('&=')])
            
            # Remove words that start with a special character
            line_content = re.sub(r'(&-|&\+|&=|&!=|<|>)', '', line_content)
            line_content = re.sub(r'@[^\s]+', '', line_content)
            # Remove punctuations except ' and -
            line_content = re.sub(r'[^\w\s\'-?]', '', line_content)
            line_content = re.sub(r'xxx', '', line_content)
            
            line_content = line_content.lower()
            line_content = line_content.strip()
            
            # If ine_content starts with any of the words in the list q_deu
            if (any(line_content.startswith(word + " ") for word in qw) or any(" " + word + " " in line_content for word in qw) or any(word + "'" in line_content for word in qw)) \
                and not line_content.endswith("oder was ?") and not line_content.endswith("or what ?") and not line_content.endswith("oder wie ?"):
                num_q_1 += 1
            elif " oder " in line_content and not line_content.endswith(" oder ?") and not line_content.startswith("oder ") and not line_content.endswith(" oder so ?") and not line_content.endswith("oder was ?") and not line_content.endswith("oder wie ?") or \
                " or " in line_content and not line_content.endswith(" or ?") and not line_content.startswith("or ") and not line_content.endswith(" or no ?") and not line_content.endswith(" right ?") and not line_content.endswith("or what ?"):
                num_q_2 += 1
            else:
                num_q_3 += 1
            
            
    print(f"{i}, Questions: {num_q_1/len(clan_files[i])/2}")
    print(f"{i}, Questions: {num_q_2/len(clan_files[i])/2}")
    print(f"{i}, Questions: {num_q_3/len(clan_files[i])/2}")
    print(f"{i}, All questions: {num_q/len(clan_files[i])/2}")
    
# Interruptions
for i in range(2):
    count = 0
    for j in range(0, len(clan_files[i])):
        for line in clan_files[i][j].line_map:
            if line.content is None:
                continue
            if "+/" in line.content:
                count += 1
    print(f"{i}, Interruptions: {count/len(clan_files[i])/2}")
    
# Overlaps
for i in range(2):
    count_overlap = 0
    count_pause = 0
    for j in range(0, len(clan_files[i])):
        prev_speaker = None
        prev_content = None
        prev_end = 0
        curr_speaker = None
        for line in clan_files[i][j].line_map:
            if line.content is None:
                continue
            curr_speaker = line.tier[0]
            curr_start = line.onset
            
            line_content = line.content
            line_content = " ".join([word for word in line_content.split() if not word.startswith('&=')])
            
            # Remove words that start with a special character
            line_content = re.sub(r'(&-|&\+|&=|&!=|<|>)', '', line_content)
            line_content = re.sub(r'@[^\s]+', '', line_content)
            line_content = re.sub(r'[^\w\s\'-]', '', line_content)
            line_content = re.sub(r'xxx', '', line_content)
            
            line_content = line_content.lower()
            line_content = line_content.strip()
            
            if prev_speaker is not None and prev_speaker != curr_speaker and line_content != "" and prev_content != "":
                if curr_start - prev_end < 100:
                    count_overlap += 1
                    # print(prev_speaker)
                    # print(prev_content)
                    # print(prev_end)
                    # print(curr_speaker)
                    # print(line_content)
                    # print(curr_start)
                    # print()
                elif curr_start - prev_end > 500:
                    count_pause += 1
                    
            prev_speaker = curr_speaker
            prev_end = line.offset
            prev_content = line_content
            
                
    print(f"{i}, Overlaps: {count_overlap/len(clan_files[i])/2}")
    print(f"{i}, Pauses: {count_pause/len(clan_files[i])/2}")
    
    
# Utterance length and dialogue length
for i in range(2):
    utterance_length = 0
    num_lines = 0
    for j in range(0, len(clan_files[i])):
        for line in clan_files[i][j].line_map:
            if line.content is None:
                continue
            line_content = line.content
            line_content = " ".join([word for word in line_content.split() if not word.startswith('&=')])
            
            # Remove words that start with a special character
            line_content = re.sub(r'(&-|&\+|&=|&!=|<|>)', '', line_content)
            line_content = re.sub(r'@[^\s]+', '', line_content)
            # Remove punctuations except ' and -
            line_content = re.sub(r'[^\w\s\'-]', '', line_content)
            line_content = re.sub(r'xxx', '', line_content)
            
            line_content = line_content.lower()
            line_content = line_content.strip()
            
            if line_content != "":
                # print(line_content)
                num_lines += 1
                utterance_length += len(line_content.split())
    print(f"{i}, Average utterance length: {utterance_length/num_lines}")
    print(f"{i}, Average dialogue length: {num_lines/len(clan_files[i])/2}")