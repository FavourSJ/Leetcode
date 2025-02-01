class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort() #start with sorting products lexicographically
        ans = [] #creation of a list for the answer(s)
        left, right = 0, len(products) - 1 #represent the current window of product indices

        for i in range(len(searchWord)): #loop iterates over each character of the search word
            s = searchWord[i] #represents the current character
            sug = [] #store to hold up to three product suggestions

            #creating a narrow and refined search window
            # Skip products that are too short or whose character are less than 's'
            while left <= right and (len(products[left]) <= i or products[left][i] < s):
                left += 1
            # Skip products that are too long or whose character are more than 's'
            while left <= right and (len(products[right]) <= i or products[right][i] > s):
                right -= 1
            
            # Collect a maximum of three products from the search window
            for j in range(3):
                if left + j <= right:
                    sug.append(products[left + j]) # add them to the suggestion list
            ans.append(sug) #add the suggestion for the current prefix
        
        return ans
        