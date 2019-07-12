source ../venv/bin/activate

for prob in 0.4 0.5 0.6 0.7
do
    for compat in 3 4 5 6 7
    do    
        python postproc.py $prob $compat
        python plot.py
        python eval_iou_accuracy.py >> eval/evaluate"$prob"_"$compat".txt
    done
done