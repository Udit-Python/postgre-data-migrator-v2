@echo [off]
python --version && ^
python -m pip install --upgrade pip --user && ^
echo "************** INSTALL DEPENDENCIES FOR Migration ******************************" && ^
python -m pip install -r requirement.txt --user
