sizes=(10 100 1000 10000 100000 1000000 10000000)
exp_type="random_gaussian"
for size in "${sizes[@]}"; do
    echo "Running randomized QS with size=$size"
    python main.py --size "$size" --low 0 --up 100000000 --seed 42 --alg_type "Randomized" --exp_type "$exp_type"
done

for size in "${sizes[@]}"; do
    echo "Running vanilla QS with size=$size"
    python main.py --size "$size" --low 0 --up 100000000 --seed 42 --alg_type "Deterministic" --exp_type "$exp_type"
done

echo "Finish running experiment"
# -------------------------------------------- #
echo "Start plotting"

python plot.py --exp_type "$exp_type"

echo "Finish plotting"

