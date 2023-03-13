rm -R package/
rm package.zip
mkdir package/

cp README.md package/README.md
cp foldering_base.py package/foldering.py

zip -r package.zip package/
rm -R package/