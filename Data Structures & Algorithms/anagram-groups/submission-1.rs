use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {

    let mut map: HashMap<[i32; 26], Vec<String>> = HashMap::new();

    for word in strs {

        let mut tmp = [0i32; 26];
       
        for c in word.chars(){
            let position = (c as u32 - 'a' as u32) as usize;
            tmp[position as usize]+=1;
        }

        map.entry(tmp).or_insert_with(Vec::new).push(word);
    }

    map.into_values().collect()
    }
}
