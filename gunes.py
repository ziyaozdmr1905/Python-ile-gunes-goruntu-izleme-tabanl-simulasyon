import cv2
import numpy as np
import math

width, height = 640, 480
frame = np.zeros((height, width, 3), dtype=np.uint8)

x = 50
y = height // 2

# Panelin sabit merkezi
px, py = width // 2, height - 80

while True:
    frame[:] = (0, 0, 0)

    # Güneş çiz
    cv2.circle(frame, (x, y), 40, (0, 255, 255), -1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        (cx, cy), radius = cv2.minEnclosingCircle(cnt)
        if radius > 20:
            cv2.circle(frame, (int(cx), int(cy)), 5, (0, 0, 255), -1)
            cv2.putText(frame, f"Gunes: {int(cx)}, {int(cy)}",
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 255, 255), 2)

            # PANELİN AÇISINI HESAPLA
            angle = math.atan2(cy - py, cx - px)
            angle_deg = math.degrees(angle)

            # Panel boyutları
            panel_w, panel_h = 160, 60
            rect = np.array([
                [-panel_w//2, -panel_h//2],
                [ panel_w//2, -panel_h//2],
                [ panel_w//2,  panel_h//2],
                [-panel_w//2,  panel_h//2]
            ])

            # Rotasyon matrisi
            M = cv2.getRotationMatrix2D((0,0), angle_deg, 1.0)
            rotated_rect = np.dot(rect, M[:,:2].T)

            # Panelin merkeze göre konumu
            rotated_rect[:,0] += px
            rotated_rect[:,1] += py
            rotated_rect = rotated_rect.astype(int)

            # 🔹 GÖLGE HESABI
            sun_vector = np.array([cx - px, cy - py])
            panel_vector = np.array([math.cos(angle), math.sin(angle)])  # panelin baktığı yön
            sun_norm = sun_vector / np.linalg.norm(sun_vector)
            panel_norm = panel_vector / np.linalg.norm(panel_vector)
            dot = np.dot(sun_norm, panel_norm)  # cos(θ)
            brightness = int(100 + 100 * max(0, dot))  # 100-200 arası parlaklık

            panel_color = (brightness, brightness//2, 50)  # mavi tonları

            # Mavi cam dolgusu
            cv2.fillPoly(frame, [rotated_rect], panel_color)
            cv2.polylines(frame, [rotated_rect], True, (255, 255, 255), 2)  # beyaz çerçeve

            # Panel hücrelerini çiz (ızgara efekti)
            steps_x, steps_y = 4, 2
            for i in range(1, steps_x):
                p1 = rect[0] + (i * panel_w // steps_x, 0)
                p2 = rect[3] + (i * panel_w // steps_x, 0)
                line = np.dot([p1, p2], M[:,:2].T)
                line[:,0] += px
                line[:,1] += py
                cv2.line(frame, tuple(line[0].astype(int)), tuple(line[1].astype(int)), (255, 255, 255), 1)

            for j in range(1, steps_y):
                p1 = rect[0] + (0, j * panel_h // steps_y)
                p2 = rect[1] + (0, j * panel_h // steps_y)
                line = np.dot([p1, p2], M[:,:2].T)
                line[:,0] += px
                line[:,1] += py
                cv2.line(frame, tuple(line[0].astype(int)), tuple(line[1].astype(int)), (255, 255, 255), 1)

            # Açıyı yaz
            cv2.putText(frame, f"Aci: {int(angle_deg)} derece",
                        (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

    cv2.imshow("Gunes Takip + Panel Gölge Efekti", frame)

    # Gunes hareket etsin
    x += 5
    if x > width - 50:
        x = 50

    if cv2.waitKey(100) & 0xFF == 27:
        break

cv2.destroyAllWindows()
