class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using a dictionary to map a sorted tuple of characters
        anagrams = defaultdict(list)

        # iterate through the string input
        for s in strs:
            # sort the characters in each string
            key = tuple(sorted(s))
            # append the original string to the list corresponding to this key
            anagrams[key].append(s)

    # at this point all strings that are anagrams of 's' will share the same key

        # return all the grouped anagrams list
        return list(anagrams.values())