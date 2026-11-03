from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:

        # Start with an empty string
        res = ""

        # Visit every word in the list
        for s in strs:

            # Add:
            # length + "#" + actual word
            #
            # Example:
            # s = "neet"
            # len(s) = 4
            # res becomes "4#neet"
            res += str(len(s)) + "#" + s

        # Return the encoded string
        return res

    def decode(self, s: str) -> List[str]:

        # Store decoded words here
        res = []

        # i points to the beginning of
        # the next length prefix
        i = 0

        # Continue until the string ends
        while i < len(s):

            # j searches for the separator "#"
            j = i

            # Move j until "#" is found
            while s[j] != "#":
                j += 1

            # Extract the number before "#"
            # Example: "4#neet"
            # s[0:1] = "4"
            # int("4") = 4
            length = int(s[i:j])

            # Read exactly 'length' characters
            # after the separator
            res.append(s[j + 1 : j + 1 + length])

            # Move i to the beginning
            # of the next encoded word
            i = j + 1 + length

        return res