class Solution:
    def compress(self, chars: List[str]) -> int:
        # Initialize pointers and get array length
        read_index = 0  # Pointer to read characters
        write_index = 0  # Pointer to write compressed result
        array_length = len(chars)
      
        # Process all characters in the array
        while read_index < array_length:
            # Find the end of the current character group
            group_end = read_index + 1
            while group_end < array_length and chars[group_end] == chars[read_index]:
                group_end += 1
          
            # Write the character to the compressed position
            chars[write_index] = chars[read_index]
            write_index += 1
          
            # Calculate the count of consecutive characters
            count = group_end - read_index
          
            # If count > 1, write the count digits
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write_index] = digit
                    write_index += 1
          
            # Move to the next group of characters
            read_index = group_end
      
        # Return the length of the compressed array
        return write_index

        # T: O(n)
        # S: O(1)