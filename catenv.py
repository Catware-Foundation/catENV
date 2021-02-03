
#
# Defintions
#
import os
from subprocess import check_output

import numpy as np
import requests


def strike(text):
    text = list(str(text))
    txt = ""
    for a in text:
        txt += "&#0822;" + a
    log("Issued strike() with parameter: {}. Output: {}".format(str(text), str(txt + "&#0822;")))
    return txt + "&#0822;"

def messagecust(message, peer_id):
    log("Issued messagecust() with parameters: {} {}. No output.".format(str(message), str(peer_id)))
    vk.messages.send(random_id=randd.randint(-2147483647, 2147483647),peer_id=peer_id, message=str(message), dont_parse_links=1)

def RSSParse(txt):
    news = []
    for q in parse(txt)["entries"]:
        news.append({"title": q["title"], "link": q["link"], "description": q["title_detail"]["value"]})
    log("Issued RSSParse() with parameter: {}. Output is too long to be catenv.logged.".format(str(txt)))
    return news

def log(text):
    try:
        txt = "[ " + str("-".join(deunix(time.time()))) + " UTC ] [" + str(__name__) + "] [" + str(__file__) + "] " + text + "\n"
    except:
        txt = "[ " + str("-".join(deunix(time.time()))) + " UTC ] [" + str(__name__) + "] [" + str(__file__) + "] Здесь могла бы быть ваша реклама..." + "\n"
    PlusWrite(txt, "tmp/syscatenv.log.txt")

def HostToIp(host):
    log("Issued HostToIp() with " + str(host) + "parameter. Output: " + str(gethostbyname(host)))
    return gethostbyname(host)

def percent(frst, scnd):
    coef = 100 / frst
    gets = scnd * coef
    log("Issued percent() with parameters: {} {}. Output: {}".format(str(frst), str(scnd), str(gets)))
    return gets

def getid(sname):
    unamea = vk.users.get(user_ids=sname)
    log("Issued getid() with parameter {}. Output: {}".format(sname, str(unamea[0]['id'])))
    return unamea[0]['id']

def getmention(uid):
    unamee = vk.users.get(user_id=uid)[0]
    log("Issued getmention() with parameter {}. Output: {}".format(str(uid), "[id" + str(unamee["id"]) + "|" + unamee["first_name"] + " " + unamee["last_name"] + "]"))
    return "[id" + str(unamee["id"]) + "|" + unamee["first_name"] + " " + unamee["last_name"] + "]"

def getname(uid):
    unamee = vk.users.get(user_id=uid)[0]
    log("Issued getname() with parameter: {}. Output: {}".format(str(uid), str(unamee["first_name"] + " " + unamee["last_name"])))
    return unamee["first_name"] + " " + unamee["last_name"]

def deunix(integer):
    return datetime.datetime.utcfromtimestamp(integer).strftime('%Y %m %d %H %M %S').split(" ")

def exit():
    pass

def Geocode(address):
    json1 = convertjson(Get("https://nominatim.openstreetmap.org/search?q="+ address.replace(" ", "+") + "&format=geojson"))
    log("Issued Geocode() with parameter: {}. Output: {}".format(str(address), str([json1["features"][0]["geometry"]["coordinates"][1], json1["features"][0]["geometry"]["coordinates"][0], json1["features"][0]["properties"]["display_name"]])))
    return [json1["features"][0]["geometry"]["coordinates"][1], json1["features"][0]["geometry"]["coordinates"][0], json1["features"][0]["properties"]["display_name"]]

def convertjson(jsond):
    return loads(jsond)

def translate(text, lang):
    return translator.translate(text, dest = str(lang)).text

def input(text):
    exec(ReadFF("lib/catapi-io.py"))
    message(str(text))
    edit("stage", "wait:" + identificator)

def Voice(path):
    upload_url = vk.docs.getMessagesUploadServer(type="audio_message", peer_id=event.object["peer_id"])['upload_url']
    request = requests.post(upload_url, files={'file': open(path, 'rb')}).json()
    save = vk.docs.save(file=request['file'])['audio_message']
    d = 'doc' + str(save['owner_id']) + '_' + str(save['id'])
    vk.messages.send(peer_id=event.object["peer_id"], attachment=d, random_id=randd.randint(-2147483647, 2147483647), dont_parse_links=1)

def RandomInt(first, second):
    return randd.randint(first, second)

def catenvtest():
    print("", end="")

def succ():
    print("[ \033[92mok\033[0m ]")

def failcomplete():
    print("[\033[31mfail\033[0m]")

def procmsg(text):
    #rows, columns = os.popen('stty size', 'r').read().split()
    #intm = int(columns) - 13 - len(text)
    #txt = " " * intm
    #print("\033[94m>>>\033[0m " + text + "..." + txt, end="")
    #нахуй оно надо?
    #оставил для сохранения совместимости
    print(text)

def PlusWrite(text, target):
    file = open(str(target), 'a', encoding='utf-8')
    file.write(str(text))
    file.close()
    #catenv.log("Issued PlusWrite() with parameters: {} {}. No output.".format(str(text), str(target))) <- 22 августа на этом месте произошла чуть ли не смертельная авария,
    #                                                                                               в которой котопай чуть не умер, зато впервые словил Фатал Пайтен
    #                                                                                               Еррор из за рекурсии.

def Output(text): # Alternative to print()
    sys.stdout.write(str(text) + '\n')

def Get(url): # A get requests
    try:
        return get(url).text
        catenv.log("Issued Get() with URL {}".format(url))
    except Exception as e:
        catenv.log("Error in Get(). " + str(e))
        return None

def ShortUrl(url):
    log("Issued ShortUrl() with URL: " + str(url))
    return Get("https://clck.ru/--?url=" + url)

def InstallPackage(text): # Install Python Package (PIP)
    log("[CatEnv / InstallPackage()] Installing " + text)
    os.system("pip3 install " + text + " -" + "-user")

def ReadFF(file): # Read From File
    #нахуя экзепшены ловить тут?
    #это же библиотека
    log("Reading {}...".format(file))
    Ff = open(file, 'r', encoding='UTF-8')
    Contents = Ff.read()
    Ff.close()
    #такое впизду
    #log("File content:\n=====================\n" + Contents + "\n=====================")
    return Contents

def CallSystem2(command):
    log("Issued CallSystem2() with command: " + command)
    os.system(str(command))

def CallSystem(command): # Call system shell
    log("Issued CallSystem() with command: " + command)
    return str(check_output(str(command), shell=False))

def Run(file): # Run a Python script in isolator suqa
    log("Running " + file + "in isolator.")
    exec(ReadFF(str(file)))

def RunThread(id, method, args): # Run a any method in thread
    exec(str(id) + ' = Thread(' + str(method) + ', args=' + str(args))
    exec(str(id) + '.start()')

def convertint(intg): # Converting seconds to verbal notation
    minutes = round(intg / 60, 1)
    hours = round(minutes / 60, 1)
    days = round(hours / 24, 1)
    minutes = str(minutes)[:-2]
    hours = str(hours)[:-2]
    days = str(days)[:-2]
    if int(minutes) > 60:
        minutes = int(minutes) - int(hours) * 60
        minutes = str(minutes)
    if int(hours) > 24:
        hours = int(hours) - int(days) * 24
        hours = str(hours)
    log("Issued convertint() with " + str(intg) + ". Out: " + str(days) + ' дней ' + str(hours) + ' часов ' + str(minutes) + ' минут ')
    return str(days) + ' дней ' + str(hours) + ' часов ' + str(minutes) + ' минут '

def Download(url, fn): # Download a file from any URL
    f = open(fn, 'wb')
    f.write(requests.get(url).content)
    f.close()
    log("Used Download() with URL: " + str(url) + " and fname: " + fn)

def InfoMsg(text): # INFO message
    print("[ info ] " + text)

def FailMsg(text): # FAIL message
    print("[ fail ] " + text)

def OkMsg(text): # OK message
    print("[ ok ] " + text)

def EventMsg(text): # EVENT message
    print("[ event ] " + text)

def Similar(first, second): # Similar strings
    if not len(first) == len(second):
        return False
    if len(first) - sum(l1==l2 for l1, l2 in zip(first, second)) > 3:
        return False
    return True

def TextToBits(text, encoding='utf-8', errors='surrogatepass'): # Text to 101010010100101
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    log("Issued TextToBits() with text: " + text + ". Out: " + str(bits.zfill(8 * ((len(bits) + 7) // 8))))
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def TextFromBits(bits, encoding='utf-8', errors='surrogatepass'): # Text from 10101001010101
    try:
        n = int(bits, 2)
        log("Issued TextFromBits. Out: " + n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors))
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    except:
        return 'error'

def CreateFile(name): # Create a file
    k = name
    f = open(str(k), 'w')
    f.close()
    log("Created a file with name: " + name)
    
def Save(): # Save handle data
    try:
        config_file = open('config.txt', 'w')
        config_file.write(str(tiki) + '\n')
        config_file.write(str(zarplata) + '\n')
        config_file.write(str(surrogate) + '\n')
        config_file.write(str(pmsg) + '\n')
        config_file.write(str(symbols) + '\n')
        config_file.write(str(sendm))
        config_file.close()
    except Exception as e:
        mta('Ошибка записи! ' + str(e) + '\n Аварийный выход!')
        #exit()

def Reverse(s): # Reverse text (Text -> txeT)
    log("Issued Reverse() with text: " + s)
    return s[::-1]

def Vinpad(text): # Convert russian name to accusative
    if text.endswith('а'):
        text = text[:-1]
        text = text + 'у'
    if text.endswith('я'):
        text = text[:-1]
        text = text + 'ю'
    if text.endswith('й'):
        text = text[:-1]
        text = text + 'я'
    if text.endswith('к'):
        text = text + 'а'
    if text.endswith('ц'):
        text = text + 'а'
    if text.endswith('к'):
        text = text + 'а'
    if text.endswith('н'):
        text = text + 'а'
    if text.endswith('г'):
        text = text + 'а'
    if text.endswith('ш'):
        text = text + 'а'
    if text.endswith('щ'):
        text = text + 'а'
    if text.endswith('з'):
        text = text + 'а'
    if text.endswith('х'):
        text = text + 'а'
    if text.endswith('ф'):
        text = text + 'а'
    if text.endswith('ы'):
        text = text + 'ов'
    if text.endswith('в'):
        text = text + 'а'
    if text.endswith('п'):
        text = text + 'а'
    if text.endswith('р'):
        text = text + 'а'
    if text.endswith('о'):
        text = text[:-1]
        text = text + 'а'
    if text.endswith('л'):
        text = text + 'а'
    if text.endswith('д'):
        text = text + 'а'
    if text.endswith('ж'):
        text = text + 'а'
    if text.endswith('ч'):
        text = text + 'а'
    if text.endswith('с'):
        text = text + 'а'
    if text.endswith('м'):
        text = text + 'а'
    if text.endswith('т'):
        text = text + 'а'
    if text.endswith('ь'):
        text = text[:-1]
        text = text + 'я'
    if text.endswith('б'):
        text = text + 'а'
    return str(text)

def RandomLetter():
    letters = ['q', 'Q', 'w', 'W', 'e', 'E', 'r', 'R', 't', 'T', 'y', 'Y', 'u', 'U', 'i', 'I', 'o', 'O', 'p', 'P', 'a', 'A', 's', 'S', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'z', 'Z', 'x', 'X', 'c', 'C', 'v', 'V', 'b', 'B', 'n', 'N', 'm', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    b = letters[randd.randint(0, len(letters)-1)]
    log("Issued RandomLetter(). Out: " + b)
    return b

def mta(text,noLinks=0):
    random_id = randd.randint(-2147483647, 2147483647)
    try:
        vk.messages.send(
            random_id=random_id,
            user_ids=admins,
            message=str(text)[:4000],
            dont_parse_links=1
            )
        log("Sended an message to admins: " + str(text))
    except Exception as e:
        FailMsg('Не удалось вызвать MTA: ' + str(e))

def writeTo(text, target):
    file = open(str(target), 'w', encoding='utf-8')
    file.write(str(text))
    file.close()
    log("Wrote <" + str(text) + "> to " + target)

def message(text):
    text = str(text)
    try:
        if str(user_id) in ReadFF("trollmode.txt"):
            splitted_list = ReadFF("trollmode.txt").split("\n")
            index = [i for i,x in enumerate(splitted_list) if str(parameter.split(";")[0]) in x][0]
            messagecust(splitted_list[index].split(";")[1], peer_id)
        else:
            if len(str(text)) > 2000 and ReadFF("from.txt") == "chat":
                if "#testing" not in ReadFF('commands/' + ids[commands.index(x)] + '.py'):
                    messagecust("Во избежание спама отправил результат работы в лс, >2000 символов не пройдут", ReadFF("peer_id.txt"))
                    messagecust(str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], user_id)
                    PlusWrite(str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], "usr/lastoutput.txt")
                else:
                    if outputd == False:
                        messagecust("Во избежание спама отправил результат работы в лс, for great justice!", ReadFF("peer_id.txt"))
                        messagecust("Внимание: команда может нестабильно работать.\n\n" + str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], user_id)
                    PlusWrite("Внимание: команда может нестабильно работать.\n\n" + str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], "usr/lastoutput.txt")
            else:
                if "#testing" not in ReadFF('commands/' + ids[commands.index(x)] + '.py'):
                    if outputd == False:
                        messagecust(str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], peer_id)
                    PlusWrite(str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], "usr/lastoutput.txt")
                else:
                    if outputd == False:
                        messagecust("Внимание: команда может нестабильно работать.\n\n" + str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], peer_id)
                    PlusWrite("Внимание: команда может нестабильно работать.\n\n" + str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], "usr/lastoutput.txt")
        log("Sent message: " + text + ", Peer ID: " + str(event.object["peer_id"]))
    except Exception as e:
        mta(e)

def picture(text, text2):
    random_id = randd.randint(-2147483647, 2147483647)
    pic = str(text)
    message("Loading...")
    try:
        try:
            attachments = []
            upload = VkUpload(vk_session)
            image_url = pic
            image = session.get(image_url, stream=True)
            photo = upload.photo_messages(photos=image.raw)[0]
            attachments.append(
                'photo{}_{}'.format(photo['owner_id'], photo['id'])
            )
            vk.messages.send(
            random_id=random_id,
            peer_id=ReadFF('peer_id.txt'),
            message=str(text2).replace("vto.pe", '').replace("vkbot.ru", '')[:4000],
            attachment=','.join(attachments),
			dont_parse_links=1
            )
            log("Sent picture. URL = " + image_url)
        except Exception:
            message(str(text2))
    except Exception as e:
        mta(e)

def picturedata(text, text2):
    random_id = randd.randint(-2147483647, 2147483647)
    pic = str(text)
    message("Loading...")
    try:
        try:
            attachments = []
            upload = VkUpload(vk_session)
            photo = upload.photo_messages(photos=text)[0]
            attachments.append(
                'photo{}_{}'.format(photo['owner_id'], photo['id'])
            )
            vk.messages.send(
            random_id=random_id,
            peer_id=ReadFF('peer_id.txt'),
            message=str(text2).replace("vto.pe", '').replace("vkbot.ru", '')[:4000],
            attachment=','.join(attachments),
			dont_parse_links=1
            )
            log("Issued picturedata(). Path: " + text)
        except Exception as e:
            message(str(text2 + '\n///' + str(e) + '///'))
    except Exception as e:
        message('picture error: ' + str(e))

def resize_image(input_image_path, output_image_path, size):
    try:
        original_image = Image.open(input_image_path)
        width, height = original_image.size
        resized_image = original_image.resize(size)
        width, height = resized_image.size
        resized_image.save(output_image_path)
        return "ok"
    except Exception as e:
        return str(e)

def quad_as_rect(quad):
    if quad[0] != quad[2]: return False
    if quad[1] != quad[7]: return False
    if quad[4] != quad[6]: return False
    if quad[3] != quad[5]: return False
    return True

def quad_to_rect(quad):
    assert(len(quad) == 8)
    assert(quad_as_rect(quad))
    return (quad[0], quad[1], quad[4], quad[3])

def rect_to_quad(rect):
    assert(len(rect) == 4)
    return (rect[0], rect[1], rect[0], rect[3], rect[2], rect[3], rect[2], rect[1])

def shape_to_rect(shape):
    assert(len(shape) == 2)
    return (0, 0, shape[0], shape[1])

def griddify(rect, w_div, h_div):
    w = rect[2] - rect[0]
    h = rect[3] - rect[1]
    x_step = w / float(w_div)
    y_step = h / float(h_div)
    y = rect[1]
    grid_vertex_matrix = []
    for _ in range(h_div + 1):
        grid_vertex_matrix.append([])
        x = rect[0]
        for _ in range(w_div + 1):
            grid_vertex_matrix[-1].append([int(x), int(y)])
            x += x_step
        y += y_step
    grid = np.array(grid_vertex_matrix)
    return grid

def distort_grid(org_grid, max_shift):
    new_grid = np.copy(org_grid)
    x_min = np.min(new_grid[:, :, 0])
    y_min = np.min(new_grid[:, :, 1])
    x_max = np.max(new_grid[:, :, 0])
    y_max = np.max(new_grid[:, :, 1])
    new_grid += np.random.randint(- max_shift, max_shift + 1, new_grid.shape)
    new_grid[:, :, 0] = np.maximum(x_min, new_grid[:, :, 0])
    new_grid[:, :, 1] = np.maximum(y_min, new_grid[:, :, 1])
    new_grid[:, :, 0] = np.minimum(x_max, new_grid[:, :, 0])
    new_grid[:, :, 1] = np.minimum(y_max, new_grid[:, :, 1])
    return new_grid

def grid_to_mesh(src_grid, dst_grid):
    assert(src_grid.shape == dst_grid.shape)
    mesh = []
    for i in range(src_grid.shape[0] - 1):
        for j in range(src_grid.shape[1] - 1):
            src_quad = [src_grid[i    , j    , 0], src_grid[i    , j    , 1],
                        src_grid[i + 1, j    , 0], src_grid[i + 1, j    , 1],
                        src_grid[i + 1, j + 1, 0], src_grid[i + 1, j + 1, 1],
                        src_grid[i    , j + 1, 0], src_grid[i    , j + 1, 1]]
            dst_quad = [dst_grid[i    , j    , 0], dst_grid[i    , j    , 1],
                        dst_grid[i + 1, j    , 0], dst_grid[i + 1, j    , 1],
                        dst_grid[i + 1, j + 1, 0], dst_grid[i + 1, j + 1, 1],
                        dst_grid[i    , j + 1, 0], dst_grid[i    , j + 1, 1]]
            dst_rect = quad_to_rect(dst_quad)
            mesh.append([dst_rect, src_quad])
    return mesh

import time
import datetime
log("Initialized CatENV")
