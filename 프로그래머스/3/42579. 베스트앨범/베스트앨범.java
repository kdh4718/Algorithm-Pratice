import java.util.*;

class Solution {
    static class Song {
    int id;
    int plays;
    
    Song(int id, int plays) {
        this.id = id;
        this.plays = plays;
        }
    }
    
    public int[] solution(String[] genres, int[] plays) {
        HashMap<String, Integer> genreTotal = new HashMap<>();
        Map<String, List<Song>> genreToSongs = new HashMap<>();
        
        for (int i = 0; i < genres.length; i++){
            String genre = genres[i];
            int play = plays[i];

            genreTotal.put(genre, genreTotal.getOrDefault(genre, 0) + play);
            genreToSongs.putIfAbsent(genre, new ArrayList<>());
            genreToSongs.get(genre).add(new Song(i, play));
        }
        
        List<String> sortedGenres = new ArrayList<>(genreTotal.keySet());
        sortedGenres.sort((g1, g2) -> genreTotal.get(g2) - genreTotal.get(g1));

        List<Integer> result = new ArrayList<>();

        for (String genre : sortedGenres) {
            List<Song> songList = genreToSongs.get(genre);

            songList.sort((s1, s2) -> {
                if (s2.plays != s1.plays) return s2.plays - s1.plays;
                return s1.id - s2.id;
            });

            result.add(songList.get(0).id);
            if (songList.size() > 1) {
                result.add(songList.get(1).id);
            }
        }

        return result.stream().mapToInt(i -> i).toArray();
    }
}