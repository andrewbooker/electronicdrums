#! /bin/bash


loc=/media/$USER/SPD-SX/Roland/SPD-SX/WAVE

declare -A groups=([93]="no" [94]="cy" [95]="pe" [96]="pr" [97]="pt" [98]="lf" [99]="bd")

locp=$loc/PRM
for n in $(ls -w1 $locp)
do
    if [ $n \> 92 ]
    then
        pre=${groups[$n]}
        pre1=$(printf "%d" "'${pre:0:1}")
        pre2=$(printf "%d" "'${pre:1:1}")
        for fn in $(ls -w1 $locp/$n)
        do
            nu=$((48 + ${fn:0:1}))
            nl=$((48 + ${fn:1:1}))            
            sed -i -E "s/<Nm0>98<\/Nm0>/<Nm0>$pre1<\/Nm0>/ ; s/<Nm1>100<\/Nm1>/<Nm1>$pre2<\/Nm1>/ ; s/<Nm10>([0-9]{2})<\/Nm10>/<Nm10>${nu}<\/Nm10>/ ; s/<Nm11>([0-9]{2})<\/Nm11>/<Nm11>${nl}<\/Nm11>/" $locp/$n/$fn
        done
    fi
done
