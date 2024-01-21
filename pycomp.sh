#!/bin/sh
# Small shell script to do some of the dirty work for me.
# 20121212, V 1.0, HvdW. 

cd scripts/ui
pyside6-uic create_args.ui > ui_create_args.py
pyside6-uic export_metadata.ui > ui_export_metadata.py
pyside6-uic modifydatetime.ui > ui_modifydatetime.py
pyside6-uic syncdatetime.ui > ui_syncdatetime.py
pyside6-uic remove_metadata.ui > ui_remove_metadata.py
pyside6-uic rename_photos.ui > ui_rename_photos.py
pyside6-uic MainWindow.ui > ui_MainWindow.py
sed -e "s+MainWindow.setMenuBar(self+#MainWindow.setMenuBar(self+" ui_MainWindow.py > ui_MainWindowMAC.py
