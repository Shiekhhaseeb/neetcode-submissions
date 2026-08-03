class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         # Dictionary:
        # Key   -> Character frequency (fingerprint)
        # Value -> List of anagrams
        res = defaultdict(list)

        # Visit every word
        for s in strs:

            # Create a frequency array for 26 letters
            count = [0] * 26

            # Count every character in the word
            for c in s:

                # Convert character into index
                # a -> 0
                # b -> 1
                # c -> 2
                # ...
                # z -> 25
                count[ord(c) - ord("a")] += 1

            # Convert list to tuple because
            # lists cannot be dictionary keys
            res[tuple(count)].append(s)

        # Return all groups of anagrams
        return list(res.values())