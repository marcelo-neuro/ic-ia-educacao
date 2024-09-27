import cv2
import pytesseract


def extrai_texto(img_caminho):
    imagem = cv2.imread(img_caminho)
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_threshold = cv2.threshold(imagem_cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Usuario\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    return pytesseract.image_to_string(imagem_threshold)


cam = cv2.VideoCapture(1)

while True:
    ret, frame = cam.read()

    if not ret:
        print("Não pegou a camera")
        break

    cv2.imshow("Teste", frame)

    key = cv2.waitKey(0)
    if key % 256 == 27:
        print("Vazando")
        break

    elif key % 256 == 32:
        nome_imagem = "imagem_texto.png"
        cv2.imwrite(nome_imagem, frame)
        print(extrai_texto(nome_imagem))

cam.release()

cv2.destroyAllWindows()
