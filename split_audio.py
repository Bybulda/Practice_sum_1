from pydub import AudioSegment
import os


def fracture(path):
    t1 = 0  # Works in milliseconds
    t2 = 5000
    flag = 1
    counter = 1
    print('Working on file.....', path)
    *dr, name = path.split('/')
    name = name[:-4]
    try:
        newAudio = AudioSegment.from_wav(path)
        while flag:
            if t2 > len(newAudio):
                flag = 0
            else:
                if not os.path.isdir(f'{dr}/fractured/{name}'):
                    os.mkdir(f'{dr}/fractured/{name}')  # making a folder for pieces
                nwAudio = newAudio[t1:t2]
                nwAudio.export(f'{dr}/fractured/{name}/{name}-{counter}.wav',
                               format="wav")  # Export audio to a folder
                t1 += 5000
                t2 += 5000
                counter += 1
    except Exception as exc:
        print('An error has ocured, becouse of.....', exc)
        raise Exception
    if counter:
        print('File has been successfully fractured!')


