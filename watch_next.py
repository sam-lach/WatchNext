import spacy
nlp = spacy.load('en_core_web_md')
# Populate movies dictionary
movies_desc = {}
with open("movies.txt","r") as movies_list:
    for line in movies_list:
        movies_desc[line[0:7]] = line[9:].strip("\n")

planet_hulk = nlp("""Will he save their world or destory it?
When the Hulk becomes too dangerous for the Earth,
the Illuminati trick Hulk into a shuttle and launch him into space
to a planet where the Hulk can live in peace. Unfortunately, Hulk
land on the planet Sakaar where he is sold into slavery and trained as
a gladiator.""")

# Populate a similarity dictionary using NLP
movies_smlrty = {}
for movie in movies_desc:
    movies_smlrty[movie] = nlp(movies_desc[movie]).similarity(planet_hulk)

top_match = max(movies_smlrty, key=movies_smlrty.get)
print("The most similar film to \"Planet Hulk\" is :", top_match)