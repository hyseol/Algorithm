def solution(genres, plays):
    count = {}
    for g, p in zip(genres, plays):
        count[g] = count.get(g, 0) + p 

    sorted_count = sorted(count, key= lambda x : count[x], reverse= True)

    song = {}
    for g, (i, p) in zip(genres, enumerate(plays)):
        if g not in song:
            song[g] = [(i, p)]
        else:
            song[g].append((i, p))

    answer = []
    for g in sorted_count:
        sorted_song = sorted(song[g], key= lambda x : (-x[1], x[0]))
        for s in sorted_song[:2]:
            answer.append(s[0])

    return answer