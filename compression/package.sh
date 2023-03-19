rm -R package_compression/
rm package_compression.zip
mkdir package_compression/

cp compression/README.md package_compression/README.md
cp video_compression.py package_compression/foldering.py

zip -r package_compression.zip package_compression/
rm -R package_compression/