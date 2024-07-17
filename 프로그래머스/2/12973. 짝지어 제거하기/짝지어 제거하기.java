import java.util.*;

class Solution
{
    public int solution(String s)
    {
        int answer = 0;
        ArrayList<Character> alp = new ArrayList<>();
        
        for (int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if (alp.isEmpty()){
                alp.add(ch);
                continue;
            }
            
            if (alp.get(alp.size() - 1) == ch){
                alp.remove(alp.size() - 1);
            }else{
                alp.add(ch);
            }
        }
        
        
        return (alp.isEmpty())? 1 : 0;
    }
}