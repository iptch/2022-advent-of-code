tesseract scan.jpg stdout > fun.py
tail -n +4 fun.py > fun_clean.py
sed -i 's/YY/  /g' fun_clean.py
python3 fun_clean.py
