from collections import deque
import cv2 as cv

def draw_landmarks(image, landmark_point):
    if len(landmark_point) > 0:
        # Thumb
        cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[3]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[3]),
                (245,66,230), 2)
        cv.line(image, tuple(landmark_point[3]), tuple(landmark_point[4]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[3]), tuple(landmark_point[4]),
                (245,66,230), 2)

        # Index finger
        cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[6]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[6]),
                (245,66,230), 2)
        cv.line(image, tuple(landmark_point[6]), tuple(landmark_point[7]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[6]), tuple(landmark_point[7]),
                (245,66,230), 2)
        cv.line(image, tuple(landmark_point[7]), tuple(landmark_point[8]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[7]), tuple(landmark_point[8]),
                (245,66,230), 2)

        # Middle finger
        cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[10]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[10]),
                (245,66,230), 2)
        cv.line(image, tuple(landmark_point[10]), tuple(landmark_point[11]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[10]), tuple(landmark_point[11]),
                (245,66,230), 2)
        cv.line(image, tuple(landmark_point[11]), tuple(landmark_point[12]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[11]), tuple(landmark_point[12]),
                (245,66,230), 2)

        # Ring finger
        cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[14]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[14]),
                (245,66,230), 2)
        cv.line(image, tuple(landmark_point[14]), tuple(landmark_point[15]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[14]), tuple(landmark_point[15]),
                (245,66,230), 2)
        cv.line(image, tuple(landmark_point[15]), tuple(landmark_point[16]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[15]), tuple(landmark_point[16]),
                (245,66,230), 2)

        # Little finger
        cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[18]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[18]),
                (245,66,230), 2)
        cv.line(image, tuple(landmark_point[18]), tuple(landmark_point[19]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[18]), tuple(landmark_point[19]),
                (245,66,230), 2)
        cv.line(image, tuple(landmark_point[19]), tuple(landmark_point[20]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[19]), tuple(landmark_point[20]),
                (245,66,230), 2)

        # Palm
        cv.line(image, tuple(landmark_point[0]), tuple(landmark_point[1]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[0]), tuple(landmark_point[1]),
                (245,66,230), 2)
        cv.line(image, tuple(landmark_point[1]), tuple(landmark_point[2]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[1]), tuple(landmark_point[2]),
                (245,66,230), 2)
        cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[5]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[5]),
                (245,66,230), 2)
        cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[9]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[9]),
                (245,66,230), 2)
        cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[13]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[13]),
                (245,66,230), 2)
        cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[17]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[17]),
                (245,66,230), 2)
        cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[0]),
                (245,117,66), 6)
        cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[0]),
                (245,66,230), 2)

    # Key Points
    for index, landmark in enumerate(landmark_point):
        if index == 0:  # 手首1
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 1:  # 手首2
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 2:  # 親指：付け根
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 3:  # 親指：第1関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 4:  # 親指：指先
            cv.circle(image, (landmark[0], landmark[1]), 8, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 8, (245,117,66), 1)
        if index == 5:  # 人差指：付け根
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 6:  # 人差指：第2関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 7:  # 人差指：第1関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 8:  # 人差指：指先
            cv.circle(image, (landmark[0], landmark[1]), 8, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 8, (245,117,66), 1)
        if index == 9:  # 中指：付け根
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 10:  # 中指：第2関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 11:  # 中指：第1関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 12:  # 中指：指先
            cv.circle(image, (landmark[0], landmark[1]), 8, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 8, (245,117,66), 1)
        if index == 13:  # 薬指：付け根
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 14:  # 薬指：第2関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 15:  # 薬指：第1関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 16:  # 薬指：指先
            cv.circle(image, (landmark[0], landmark[1]), 8, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 8, (245,117,66), 1)
        if index == 17:  # 小指：付け根
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 18:  # 小指：第2関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 19:  # 小指：第1関節
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (245,117,66), 1)
        if index == 20:  # 小指：指先
            cv.circle(image, (landmark[0], landmark[1]), 8, (245,66,230),
                      -1)
            cv.circle(image, (landmark[0], landmark[1]), 8, (245,117,66), 1)

    return image