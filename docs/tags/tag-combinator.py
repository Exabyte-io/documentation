import os


# Enter keywords associated with tag file of interest, and present within its pathname. All common files in the way will also be added.
# For example, to retrieve the tags associated with bandstructure calculations listed in bandstructure.md file one would insert the following keywords: dft, electronic, bandstructure.
# ALL entered keywords have to be contained within pathname of file of interest

list_keywords=raw_input('enter keywords for video separated by commas: ').split(',')
for i in range(len(list_keywords)):
    list_keywords[i]=list_keywords[i].strip()

common_file=open('all.md')
list_lines=common_file.readlines()
common_tags=[None]*len(list_lines)
for i in range(len(list_lines)):
    common_tags[i]= list_lines[i].strip()


other_tags=[]
list_files=[]
for path, subdirs, files in os.walk('.'):
    for name in files:
        list_files.append(os.path.join(path, name).strip())



#check for duplicate tags
all_tags=[]
for i in range(len(list_files)):
  if list_files[i][-3:]=='.md':
    common_file = open(list_files[i])
    list_lines = common_file.readlines()
    for j in range(len(list_lines)):
        all_tags.append(list_lines[j].strip().strip(',').lower())

duplicate=[]
for i in range(len(all_tags)):
    if all_tags.count(all_tags[i])>1 and all_tags[i] not in duplicate:
        print 'duplicate found: '+all_tags[i]
        duplicate.append(all_tags[i])



for i in range(len(list_files)):
    list_path= list_files[i].split('/')
    for j in range(len(list_path)):
        list_path[j]= list_path[j].replace('.md','')
    if [list_path[j] in list_keywords  for j in range(len(list_path))] == [True]*len(list_keywords):
        common_file = open(list_files[i])
        list_lines = common_file.readlines()
        for k in range(len(list_lines)):
            other_tags.append(list_lines[k].strip())

tags_full_list= common_tags+other_tags
for i in range(len(tags_full_list)):
    print tags_full_list[i]
