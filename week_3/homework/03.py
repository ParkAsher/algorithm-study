genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    
    genre_total_play_dict = {}                      # 장르별 총 재생횟수 합계 딕셔너리

    genre_index_play_dict = {}                      # 장르 내에서 곡의 재생횟수 저장 딕셔너리

    for i in range(len(genre_array)) :
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_dict[genre] = [[i, play]]
        else :
            genre_total_play_dict[genre] += play
            genre_index_play_dict[genre].append([i, play])


    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    result = []
    for genre, _value in sorted_genre_play_array:
        index_play_array = genre_index_play_dict[genre]
        sorted_by_play_and_index_play_index_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        for i in range(len(sorted_by_play_and_index_play_index_array)):
            if i > 1:
                break
            result.append(sorted_by_play_and_index_play_index_array[i][0])
    return result



print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!