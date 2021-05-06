import os
from io import StringIO
import sys
import numpy as np
import pandas as pd

YOLO_SRC="/home/wg49/ctmc/yolov5/ctmc-runs-m/"
YOLO_DST="/home/wg49/ctmc/data/YOLO/detections/"

THRESH = sys.argv[2] if len(sys.argv) > 2 else 0.3
for seq in os.listdir(YOLO_SRC):
  print("Processing {}".format(seq))
  seq_dir = os.path.join(YOLO_SRC, seq, "labels")

  files = sorted(os.listdir(seq_dir))

  all_lines = []
  for f in files:
    pred = os.path.join(seq_dir, f)
    frame = str( int(f[:-4]) )
    lines = [frame + " " + l.strip() for l in open(pred).readlines() ]
    all_lines.extend(lines)

  f = StringIO("\n".join(all_lines))

  df = pd.read_csv(f, sep=' ', header=None, \
        names=["frame","class", "xc", "yc", "w", "h", "conf"] )

  print(df.shape)
  df = df[ df["conf"] > THRESH ]
  df["bb_left"] = (df["xc"] - df["w"] * 0.5) * 400
  df["bb_top"] = (df["yc"] - df["h"] * 0.5) * 320
  df["bb_width"] = df["w"] * 400
  df["bb_height"] = df["h"] * 320

  for field in ["bb_left", "bb_top", "bb_width", "bb_height"]:
    df[field] = df[field].round(0).astype(int)

  # 0 1 2 3 4 5 6
  # class xcenter ycenter width height conf (YOLO format)
  # <frame>, <id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, (Deepsort detection input format)
  # (xcenter - width / 2), (ycenter - height / 2)
  # multiply x by 400. multiply y by 320.

  print(df.head())
  print("merging {} frame predictions".format(len(os.listdir(seq_dir))))
  print(" {} lines in total ".format(len(df)))

  dst_dir = os.path.join(YOLO_DST, seq)
  if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

  dst_gt_dir = os.path.join(dst_dir, "gt")
  if not os.path.exists(dst_gt_dir):
        os.makedirs(dst_gt_dir)

  dst_file = os.path.join(dst_gt_dir, "gt.txt")
  df["x"] = -1
  df["y"] = -1
  df["z"] = -1
  df.to_csv(dst_file, sep=",", index=False, header=False, columns=["frame", \
  "class", "bb_left", "bb_top", "bb_width", "bb_height", "conf", "x", "y", "z"] )
  print("done writing to file {}".format(dst_file))




    

