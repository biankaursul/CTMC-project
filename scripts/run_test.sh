#!/bin/bash

BEST_EXP=exp4
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -e|--exp) BEST_EXP="$2"; shift ;;
        -n|--name) NAME="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

set -x

python /home/wg49/ctmc/yolov5/test.py --data /home/wg49/ctmc/data/YOLO/ctmc-$NAME.yaml --img-size 400 --save-txt \
  --batch-size 32 --save-conf --conf-thres 0.1 --single-cls  --weights /home/wg49/ctmc/yolov5/runs/train/$BEST_EXP/weights/best.pt \
  --project ctmc-runs --name $NAME --exist-ok
