# PyQT Style Sheet for UI: PR it's basically CSS
def style_sheet():
    return ('''
        QWidget {
            font-size: 15px;
            background-color: #222222;
        }
        QPushButton {
            height: 20px;
            color: black;
            background-color: QLinearGradient(
                           x1: 0,
                           x2: 1,
                           y1: 0,
                           y2: 1,
                           stop: 1 #252a34,
                           stop: 0.5 #ff2e63,
                           stop: 0 #ffff11
            );
            border-width: 2px;
            border-color: QLinearGradient(
                           x1: 0,
                           x2: 1,
                           y1: 0,
                           y2: 0,
                           stop: 0 #252a34,
                           stop: 0.5 #ff2e63,
                           stop: 1 #ffff11
            );
            border-style: inset;
            padding: 2px;
        }
        QPushButton:Pressed {
            background-color: QLinearGradient(
                           x1: 0,
                           x2: 1,
                           y1: 0,
                           y2: 1,
                           stop: 1 #342a25,
                           stop: 0.5 #632eff,
                           stop: 0 #11ffff
            );
        }
        QPushButton:hover {
            border-color: #22cccc;
        }
        QLineEdit {
            height: 20px;
            background-color: #eeeeee;
            border-width: 2px;
            border-color: QLinearGradient(
                           x1: 0,
                           x2: 1,
                           y1: 0,
                           y2: 0,
                           stop: 0 #252a34,
                           stop: 0.5 #ff2e63,
                           stop: 1 #ffff11
            );
            border-style: inset;
            padding: 2px;
        }
        QTabWidget {
            color: black;
            background-color: QLinearGradient(
                           x1: 0,
                           x2: 1,
                           y1: 0,
                           y2: 1,
                           stop: 1 #252a34,
                           stop: 0.5 #ff2e63,
                           stop: 0 #ffff11
            );
            border-color: QLinearGradient(
                           x1: 0,
                           x2: 1,
                           y1: 0,
                           y2: 0,
                           stop: 0 #252a34,
                           stop: 0.5 #ff2e63,
                           stop: 1 #ffff11
            );
        }
        QTabBar:Tab:selected {
            color: black;
            background-color: QLinearGradient(
                           x1: 0,
                           x2: 1,
                           y1: 0,
                           y2: 1,
                           stop: 1 #252a34,
                           stop: 0.5 #ff2e63,
                           stop: 0 #ffff11
            );
            border-color: QLinearGradient(
                           x1: 0,
                           x2: 1,
                           y1: 0,
                           y2: 0,
                           stop: 0 #252a34,
                           stop: 0.5 #ff2e63,
                           stop: 1 #ffff11
            );
        }
        ''')


# List of extensions for backup script to ignore
def backup_ignore_list():
    return [
        "exr",
        "obj",
        "fbx",
        "abc",
        "usd",
        "mp4",
        "png",
        "tiff",
        "jpg",
        "jpeg",
        "bgeo.sc",
        "vdb",
        "mov",
        "usda",
        "times",
        "mp3",
        "AAE",
        "aae",
        "MOV",
        "csv",
        "MXF",
        "mxf",
        "braw",
        "sidecar",
        "rat"
    ]
