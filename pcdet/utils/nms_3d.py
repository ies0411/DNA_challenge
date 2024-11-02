import numpy as np
from .nms import custom_nms


def nms(
    original_boxes,
    iou_thres_same_class,
    iou_thres_different_class,
):
    boxes_probability_sorted = original_boxes[np.flip(np.argsort(original_boxes[:, 0]))]
    selected_boxes = []
    for bbox in boxes_probability_sorted:
        if bbox[0] > 0:
            selected_boxes.append(bbox)
            for other_box in boxes_probability_sorted:
                converted_iou_threshold = (
                    iou_thres_same_class
                    if bbox[-2] == other_box[-2]
                    else iou_thres_different_class
                )
                if (
                    other_box[-1] != bbox[-1]
                    and custom_nms.iou(bbox[1:-2], other_box[1:-2])
                    > converted_iou_threshold
                ):
                    other_box[0] = 0
    return selected_boxes
