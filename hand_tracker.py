import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)


def get_hands_position(imagem_path):
    imagem = cv2.flip(cv2.imread(imagem_path), 1)
    results = hands.process(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
    if not results.multi_hand_landmarks:
        return [[0, 0, 0, 0], [0, 0, 0, 0]]

    altura_imagem, largura_imagem = imagem.shape

    coordenadas_maos = []

    i = 0
    for hand_landmarks in results.multi_hand_landmarks:
        coordenadas_maos[i] = [hand_landmarks.landmarks[mp_hands.HandLandmark.THUMB_TIP].x * largura_imagem,
                               hand_landmarks.landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * altura_imagem]

        coordenadas_maos[i][2] = ((hand_landmarks.landmarks[mp_hands.HandLandmark.PINKY_TIP].x * largura_imagem) -
                                  coordenadas_maos[i][0])
        coordenadas_maos[i][3] = ((hand_landmarks.landmarks[mp_hands.HandLandmark.WRIST].y * altura_imagem) -
                                  coordenadas_maos[i][1])

        i += 1
    return coordenadas_maos
