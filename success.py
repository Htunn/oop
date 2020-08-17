# success function

def success(dedication, persistence, passion):
    dedication += 1 # dedicate yourself
    persistence += 1 # be persisten
    passion = True # have passion

    if passion == True:
        magic = dedication + persistence
        return magic
    else:
        magic = 0
        return magic
    
su = success(7, 7, True)
print(su)