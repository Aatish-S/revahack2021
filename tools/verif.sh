dir=$1
username=$2
cd $dir 
output=$(python3 main.py laz_aats --command info)

cd ..
cd osin
touch $username.txt
name=$username.txt
echo $output | tee -a $name 
cd ..
