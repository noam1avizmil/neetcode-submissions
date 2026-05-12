class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        return self.decode(s)

    def decode(self, s: str) -> str:
          result = ""
          while self.i < len(s) and s[self.i] != "]":
              if not s[self.i].isdigit():
                  result += s[self.i]
                  self.i += 1
              else:
                  k = 0
                  while s[self.i].isdigit():
                      k = k * 10 + int(s[self.i])
                      self.i += 1
                  self.i += 1                  # skip '['
                  inner = self.decode(s)
                  self.i += 1                  # skip ']'
                  result += inner * k
          return result


        