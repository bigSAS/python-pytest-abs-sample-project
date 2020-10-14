import os, shutil
from datetime import datetime


FILES = ['report.html', 'report.json', 'run.log']
ROOT = os.path.dirname(os.path.abspath(__file__))


def makedir() -> str:
    timestamp = datetime.now().strftime('%Y-%m-%d__%H%M%S%f')
    folder = f'{ROOT}/reports/{timestamp}'
    os.mkdir(folder)
    print('Report folder:', folder)
    return folder


if __name__ == "__main__":
    dir = makedir()
    for file in FILES:
        old = f'{ROOT}/{file}'
        new = f'{dir}/{file}'
        shutil.move(old, new)
        print('Saved:', new)
    with open('last_report.txt', 'w', encoding='utf-8') as lr:
        lr.write(dir.replace('\\', '/'))
    print('Last report dir saved in last_report.txt')
