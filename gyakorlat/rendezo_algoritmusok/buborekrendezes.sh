#! /bin/bash
a=(3 7 6 2 1 5 4)
echo ${a[*]}

for ((i=0;i<${#a[@]};i++))
do
for((j=0;j<${#a[@]};j++))
do
if ((${a[j]} > ${a[$((j+1))]}))
then
v=${a[$j]}
a[$j]=${a[$((j+1))]}
a[$((j+1))]=$v
fi
done
done
echo ${a[*]}
echo "End."
exit 0
