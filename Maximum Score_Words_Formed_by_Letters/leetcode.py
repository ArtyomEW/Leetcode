import copy

count = 0
class Solution(object):
    def sort_dict(self, letters, score):
        arr = {}
        lst = []
        for i in letters:
            if i not in lst:
                lst.append(i)

        while True:
            if len(score) == len(lst):
                break
            score.remove(min(score))

        for i in zip(sorted(lst), score):
            arr[i[0]] = i[1]
        return arr

    def maxScoreWords(self, words, letters, score):
        global count
        count = len(words)
        result = 0
        result_arr = []
        score = [i for i in score if i != 0]
        res_dict = self.sort_dict(letters, score)
        while count != 0:
            st = ''
            lst_letters = copy.deepcopy(letters)
            for word in words:
                b = True
                for al in word:
                    if al in letters:
                        st += al
                        letters.remove(al)
                    else:
                        b = False
                        st = ''
                        break
                if b:
                    for i in st:
                        result += res_dict[i]
                    st = ''
            words.pop(0)
            count -= 1
            result_arr.append(result)
            letters = copy.deepcopy(lst_letters)
            result = 0
        return max(result_arr)




a = Solution()
print(a.maxScoreWords(words = ["baaa","aacc","ccbc","da","dbbc"], letters = ["a","a","a","c","c","c","c","c","d","d","d"],
                      score = [9,4,10,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))