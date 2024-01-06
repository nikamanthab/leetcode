class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # time - O(n), Space - O(n)
        s = []
        for tok in tokens:
            if tok not in ["+", "-", "*", "/"]:
                s.append(int(tok))
                continue
            
            y,x = int(s.pop()), int(s.pop())
            if tok == "+":
                s.append(x+y)
            elif tok == "-":
                s.append(x-y)
            elif tok == '*':
                s.append(x*y)
            elif tok == "/":
                s.append(x/y)
        return int(s[-1])