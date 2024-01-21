import subprocess
import argparse
import os
import os.path as osp


def write_ui(uic_exe, uifile_path):
    if not osp.isfile(uifile_path):
        raise ValueError(".ui file does not exist: '{}'.".format(uifile_path))

    out_path = osp.join(osp.dirname(uifile_path),
                        "ui_{}.py".format(osp.splitext(osp.basename(uifile_path))[0]))
    ENCODING = 'utf-8'
    if osp.isfile(out_path):
        print("'{}' will be overwritten!".format(out_path))

    output = subprocess.check_output([uic_exe, uifile_path])
    output = output.decode(ENCODING)

    with open(out_path, 'w', encoding=ENCODING) as f:
        f.write(output)

    return {
        'out_path': out_path,
        'output': output,
        'encoding': ENCODING
    }


def main(opts):
    uic_exe = opts.pyside6_uic_executable

    os.chdir("scripts/ui")

    # *.ui -> *.py
    write_ui(uic_exe, "./create_args.ui")
    write_ui(uic_exe, "./export_metadata.ui")
    write_ui(uic_exe, "./modifydatetime.ui")
    write_ui(uic_exe, "./syncdatetime.ui")
    write_ui(uic_exe, "./remove_metadata.ui")
    write_ui(uic_exe, "./rename_photos.ui")
    mw = write_ui(uic_exe, "./MainWindow.ui")

    # Menubar on MacOS
    mw_mac_path = osp.join(osp.dirname(mw['out_path']), "ui_MainWindowMAC.py")
    if osp.isfile(mw_mac_path):
        print("'{}' will be overwritten!".format(mw_mac_path))

    with open(mw['out_path'], 'r', encoding=mw['encoding']) as mwf:
        with open(mw_mac_path, 'w', encoding=mw['encoding']) as macf:
            for line in mwf.readlines():
                if not line.strip().startswith("MainWindow.setMenuBar(self"):
                    macf.write(line + os.linesep)

    print("Done")

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=
        "Must be executed before starting UI via 'python scripts/pyexiftoolgui.py'."
        " Does the same thing as pycomp.sh, but in a cross-platform way.")

    ap.add_argument('--pyside6-uic_executable', default="pyside6-uic")

    args = ap.parse_args()
    main(args)
