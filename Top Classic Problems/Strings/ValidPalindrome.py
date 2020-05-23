        for i in string.punctuation:
            if i in s:
                s = s.replace(i, " ")
        
        s = s.replace(" ", "")
        
        if not s:
            return True
        
        return True if s.lower() == s[::-1].lower() else False
        
           