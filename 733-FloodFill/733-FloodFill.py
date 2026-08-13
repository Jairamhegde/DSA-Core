# Last updated: 8/13/2026, 8:22:33 PM
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        initial_color = image[sr][sc]

        self.dfs(image,sr,sc,color,initial_color)

        return image

    def dfs(self,image,sr,sc,color,initial_color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != initial_color or image[sr][sc] == color:
            return
        image[sr][sc] = color
        self.dfs(image,sr+1,sc,color,initial_color)
        self.dfs(image,sr-1,sc,color,initial_color)
        self.dfs(image,sr,sc+1,color,initial_color)
        self.dfs(image,sr,sc-1,color,initial_color)

        



        
        