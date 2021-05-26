# ----------------
#  Challenge
# ----------------
class Challenge:
    def convertion(self, msg):
        vocales = list("aeiouAEIOU")

        sanitizer = lambda val : '*' if not val in vocales and val !=' ' else val
        result = [sanitizer(i) for i in msg]
        #print('_'.join(result).replace(" ", "_"))
        return ''.join(result).replace(" ", "_")
        

        
