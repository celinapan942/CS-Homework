# the "r" reads the document

f = open ("data.txt", "r")

movie_attributes = []
movie_data = []
by_year = {}
by_director = {}
by_actress = {}
by_actor = {}

import codecs
text = 0
'''
lines = []

with open ("japanese.txt", "r", encoding = "utf-8") as f:
    for line in f.readlines():
        line = line.strip()
        line = line.split (". ")
        line = list(line)
        lines.append (line)
print (lines)


with open ("japanese.txt", "r", encoding = "utf-8") as f:
    text = ""
    for line in f.readlines():
        text += line.strip()
    
    sentences=[]
    for sentence in text.split("."):        
        sentences.append(sentence)

for i in sentences:
    print (i)
'''

with open ("data.txt", "r", encoding = "utf-8") as f:
    first_line = f.readline()
    for attribute in first_line.split(";"):
        attribute = attribute.strip()
        movie_attributes.append(attribute)    
    #print (movie_attributes)
    
    f.readline()
    
    for line in f.readlines():
        line = line.strip()
        line = line.replace("\t", "")
        line = line.split (";")
        line = tuple(line)
        movie_data.append (line) 
    print (movie_data)
    #print (len(movie_data))
    
with codecs.open ("movies.tsv", "w", encoding = "utf-8") as f:
    for movie in movie_data:
        for item in movie: 
            item = item.replace("\t", "")
            f.write(item + "\t")
        f.write("\n")

#BY YEAR           
for movie in movie_data: 
    print (movie[0])
    by_year[movie[0]] = []

for movie in movie_data:
    by_year[movie[0]] += [movie]

with open ("by_year.pickle", "wb") as f:
    pickle.dump(by_year, f)

#print (by_year["1991"])

#BY DIRECTOR
for movie in movie_data: 
    print (movie[6])
    by_director[movie[6]] = []

for movie in movie_data:
    by_director[movie[6]] += [movie]

#print (by_director["Almodóvar Pedro"])

#BY ACTRESS
for movie in movie_data: 
    #print (movie[5])
    by_actress[movie[5]] = []

for movie in movie_data:
    by_actress[movie[5]] += [movie]

#print (by_actress["Abril Victoria"])

#BY ACTOR
for movie in movie_data: 
    #print (movie[4])
    by_actor[movie[4]] = []

for movie in movie_data:
    by_actor[movie[4]] += [movie]

#print (by_actor["Banderas Antonio"])
    
def avgmoviebyyear (year):
    avg_by_year = {}
    for year in by_year:
        count = len(by_year[year])
        time = 0
        for movie in by_year[year]:
            if len(movie[1]) > 0:
                time += int(movie[1])
            else:
                count -= 1
        average = time / count 
        avg_by_year[year] = average
    
    print (avg_by_year)

avgmoviebyyear(1991)

#Number of Movies per year
def noofmoviesbyyear (yr):
    count = len(by_year[yr])
    print(count)
    
noofmoviesbyyear("1953")