class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        goal_freq = Counter(s1)
        window = defaultdict(int)
        l=0
        goal_frequency_counts = len(goal_freq)
        current_freq = 0

        for r, char in enumerate(s2):
            window[char] += 1
            if window[char] == goal_freq[char]:
                current_freq += 1

            if (1+r-l) < len(s1):
                continue

            if (1+r-l) > len(s1):
                val_to_be_removed = s2[l]
                if window[val_to_be_removed] == goal_freq[val_to_be_removed]:
                    current_freq -= 1
                window[val_to_be_removed] -= 1
                l+=1
            
            if goal_frequency_counts == current_freq:
                return True
        return False


        