import cv2
image = cv2.imread("source/rail.png")
i = 0
j = 0
file = open("source/heigth.txt", "a")

while j < len(image.view()[i]):
    if(i > 0 and str(image.view()[i - 1][j]) == "[  0   0 250]"):
        i -= 1
    elif(not(str(image.view()[i][j]) == "[  0   0 250]") and i < 231 and str(image.view()[i + 1][j]) == "[  0   0 250]"):
        i += 1
    file.write("row : " + str(j) + "heigth : " + str(231 - i))
    file.close()
    j += 1


