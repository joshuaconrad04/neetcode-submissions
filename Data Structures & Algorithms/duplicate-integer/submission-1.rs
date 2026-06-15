use std::collections::HashMap;

impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {

        let mut vals: HashMap<i32, i32> = HashMap::new();
        for v in nums{
            if vals.contains_key(&v){
                return true
            }
            vals.insert(v, 0);
    }
    false
}
}
