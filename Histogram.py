import numpy as np
from skimage import exposure, io
import matplotlib.pyplot as plt
import cv2


image_path = '/home/hero/Documents/DIP-Homework/Homework2/Requirement/third/{}.bmp'


def plot_histogram(image_path, image_name, flag):
    plt.figure('Histogram')
    plt.title(image_name)
    image = io.imread(image_path)
    if flag:
        form = '22'
        plt.subplot(form + str(1))
        plt.imshow(image, plt.cm.gray)
        plt.subplot(form + str(2))
        arr = image.flatten()
        plt.xlim(right=256)
        n, bins, patches = plt.hist(arr, bins=256, color='red')
        plt.subplot(form + str(3))
        equalized_image = exposure.equalize_adapthist(image)*256
        arr_equalized = equalized_image.flatten()
        plt.imshow(equalized_image, plt.cm.gray)
        plt.subplot(form + str(4))
        plt.xlim(right=256)
        n_e, bins_e, patches_e = plt.hist(arr_equalized, bins=256, color='red')
        plt.savefig('/home/hero/Documents/DIP-Homework/Homework2/Content/task2/{}.jpg'.format(image_name))
    else:
        form = '12'
        plt.subplot(form + str(1))
        plt.xlabel('Origin Image')
        plt.imshow(image, plt.cm.gray)
        plt.subplot(form + str(2))
        plt.xlabel('Histogram')
        arr = image.flatten()
        n, bins, patches = plt.hist(arr, bins=256, color='red')
        plt.xlim(right=256)
        plt.savefig('/home/hero/Documents/DIP-Homework/Homework2/Content/task1/{}.jpg'.format(image_name))


def task(flag):
    for i, image_name in enumerate(image_names):
        plot_histogram(image_path.format(image_name), image_name, flag)


def matching(image_name):
    if image_name == 'citywall':
        form = '32'
        order = 2
    elif image_name == 'lena':
        form = '42'
        order = 3
    elif image_name == 'elain':
        form = '42'
        order = 3
    elif image_name == 'woman':
        form = '32'
        order = 2

    # get origin image histogram
    plt.figure('Histogram')
    plt.title(image_name)
    origin_image = io.imread(image_path.format(image_name))
    plt.subplot(form + str(1))
    plt.imshow(origin_image, plt.cm.gray)
    plt.subplot(form + str(2))
    arr_origin = origin_image.flatten()
    plt.xlim(right=256)
    n_origin, bins_origin, patches_origin = plt.hist(arr_origin, bins=256, color='red')
    Gz = []
    for i in range(256):
        Gz.append(255*sum(n_origin[(i+1):])/(origin_image.shape[1]*origin_image.shape[0]))
    Gz = np.array(list(reversed(Gz)))

    # get other image
    for j in range(order):
        image = io.imread(image_path.format(image_name+str(j+1)))
        arr = image.flatten()
        plt.subplot(form + str(4+2*j))
        plt.xlim(right=256)
        equalized_image = exposure.equalize_adapthist(image) * 256
        arr_equalized = equalized_image.flatten()
        n, bins, patches = plt.hist(arr, bins=256, color='red')
        n_e, bins_e, patches_e = plt.hist(arr_equalized, bins=256, color='red')
        Sk = []
        Sk2Zq = []
        for i in range(256):
            Sk.append(255 * sum(n[(i + 1):]) / (image.shape[1] * image.shape[0]))
        Sk = np.array(list(reversed(Sk)))
        for k in range(256):    # 对Sk进行循环获取映射Sk->Zq
            minimum = min(abs(Gz-Sk[k]))
            target = []
            for q in range(256):
                if abs(Gz[q]-Sk[k]) == minimum:  # 找最小距离的Zq
                    target.append(q)
            Sk2Zq.append(min(target))
        Sk2Zq = np.array(Sk2Zq)
        result = np.zeros(256)
        for k, m in enumerate(Sk2Zq):
            result[m] = result[m] + n[k]
        # plt.xlim(right=256)
        # plt.ylim(top=256)
        plt.plot(result)

        plt.subplot(form + str(3+2*j))
        image_array = np.array(image)
        plt.imshow(Sk2Zq[image_array.astype('int64')], plt.cm.gray)
    plt.savefig('/home/hero/Documents/DIP-Homework/Homework2/Content/task3/{}2.jpg'.format(image_name))


def local_histogram(image_name):
    image_path = '/home/hero/Documents/DIP-Homework/Homework2/Requirement/{}.bmp'.format(image_name)
    # k0, k1, k2, E = 0.4, 0.02, 0.4, 4.0
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # height, width = image.shape[0], image.shape[1]
    # new_image = np.zeros((height, width, 3), dtype='uint8')
    # (mean, stddv) = cv2.meanStdDev(image)
    # mean, stddv = mean[0][0], stddv[0][0]
    # for x in range(height-7):
    #     for y in range(width-7):
    #         (local_mean, local_stddv) = cv2.meanStdDev(image[x:x+7, y:y+7])
    #         local_mean, local_stddv = local_mean[0][0], local_stddv[0][0]
    #         if (local_mean <= k0*mean) & (k1*stddv <= local_stddv <= k2*stddv):
    #             new_image[x, y] = E*image[x, y]
    #        else:
    #             new_image[x, y] = image[x, y]
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(7, 7))  # 定义CLAHE
    result = clahe.apply(gray_image)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task4/{}.bmp'.format(image_name), result)


def check(x):
    peak = 0
    for i in range(1, len(x)-1):
        if x[i-1] <= x[i] >= x[i+1]:
            peak += 1
    if peak == 2:
        return 1, peak
    else:
        return 0, peak

def segment_double(image_name):
    image_path = '/home/hero/Documents/DIP-Homework/Homework2/Requirement/{}.bmp'.format(image_name)
    image = cv2.imread(image_path)
    height, width = image.shape[0], image.shape[1]
    hist, arr = np.histogram(image, bins=256)
    for i in range(1000):
        result, number = check(hist)
        if result:
            temp = 0
            for j in range(1, len(hist) - 1):
                if hist[j - 1] <= hist[j] >= hist[j + 1]:
                    temp += j
            M = temp/number
            print(M)
            break
        else:
            for j in range(2, len(hist)-2):
                hist[j] = (hist[j-2] + hist[j-1] + hist[j] + hist[j+1] + hist[j+2])/5

    _, new_image = cv2.threshold(image, M, 255, cv2.THRESH_BINARY)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task5/{}_doublePeak.bmp'.format(image_name), new_image)
    cv2.imshow('new_image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def segment_iteration(image_name):
    image_path = '/home/hero/Documents/DIP-Homework/Homework2/Requirement/{}.bmp'.format(image_name)
    image = cv2.imread(image_path)
    height, width = image.shape[0], image.shape[1]
    hist, arr = np.histogram(image, bins=256)
    arr = arr.astype(np.uint8)
    T = round((max(arr) + min(arr))/2)
    for i in range(1000):
        Ab, count_b = 0, 0
        Af, count_f = 0, 0
        for x in range(256):
            for y in range(256):
                if image[x, y, 0] <= T:
                    Ab += image[x, y, 0]
                    count_b += 1
                else:
                    Af += image[x, y, 0]
                    count_f += 1
        Ab /= count_b
        Af /= count_f
        if T == round((Ab + Af)/2):
            print('Get the threshold!')
            break
        else:
            T = round((Ab + Af)/2)
            print(T)
    cv2.namedWindow("new_image", 0)
    cv2.resizeWindow("new_image", 640, 480)
    _, new_image = cv2.threshold(image, T, 255, cv2.THRESH_BINARY)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task5/{}_iteration.bmp'.format(image_name), new_image)
    cv2.imshow('new_image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def segment_OSTU(image_name):
    image_path = '/home/hero/Documents/DIP-Homework/Homework2/Requirement/{}.bmp'.format(image_name)
    image = cv2.imread(image_path)
    height, width = image.shape[0], image.shape[1]
    hist, arr = np.histogram(image, bins=256, density=1)
    g = []
    for i in range(1, 257):
        w0 = sum(hist[:i])
        u0 = 0
        for j in range(i):
            u0 += j*hist[j]
        w1 = sum(hist[i:256])
        u1 = 0
        for j in range(i, 256):
            u1 += j*hist[j]
        g.append(w0*w1*(u0-u1)*(u0-u1))
    T = g.index(max(g))
    print(T)
    cv2.namedWindow("new_image", 0)
    cv2.resizeWindow("new_image", 640, 480)
    _, new_image = cv2.threshold(image, T, 255, cv2.THRESH_BINARY)
    cv2.imshow('new_image', new_image)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task5/{}_OSTU.bmp'.format(image_name), new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_names = ['elain', 'elain1', 'elain2', 'elain3', 'lena', 'lena1', 'lena2', 'lena3',
              'woman', 'woman1', 'woman2', 'citywall', 'citywall1', 'citywall2']

# task1
# task(1)

# task2
# matching('lena')
# matching('elain')
# matching('woman')
# matching('citywall')

# task3
# local_histogram('lena')
# local_histogram('elain')

# task4
# segment_double('elain')
# segment_iteration('elain')
# segment_OSTU('elain')

# task5
# segment_double('woman')
# segment_iteration('woman')
# segment_OSTU('woman')
