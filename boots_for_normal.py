import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm

def getSample(n, mean=0, stdev=1):
    x = []
    for i in range(n):
        x.append(np.random.normal(mean, stdev))
    return x

def bootstrap(data):
    result = []
    for i in range(len(data)):
        n = np.random.randint(0, len(data))
        result.append(data[n])
    return result

def getBoots(data, boot_num=6):
    boots = []
    for i in range(boot_num):
        boots.append(sorted(bootstrap(data)))
    num_not_selected = []
    for boot in boots:
        count = 0
        for datum in data:
            for num in boot:
                if datum == num:
                    count += 1
                    break
        num_not_selected.append(len(data) - count)

    print(str(num_not_selected) + "samples are not selected from the data set.")
    print("The average number of samples not selected is: " +
            str(np.mean(num_not_selected)))
    print("The percentage of samples not selected is: " +
            str(np.mean(num_not_selected) / len(data) * 100)[0:5] + "%")
    return boots

def drawplot(original_data, boots):
    fig = plt.figure(figsize=(8,8))
    sorted_data = sorted(original_data)
    mu_origin, sigma_origin = norm.fit(sorted_data)
    pdf_origin = matplotlib.mlab.normpdf(sorted_data, mu_origin, sigma_origin)
    plt.plot(sorted_data, pdf_origin, '--', label="original", color='black',
                linewidth=2)
    for i in range(len(boots)):
        mu, sigma = norm.fit(boots[i])
        pdf = matplotlib.mlab.normpdf(boots[i], mu, sigma)
        plt.plot(boots[i], pdf, label="mu=" + str(mu)[0:5] + ", sigma=" +
                    str(sigma)[0:5])
        plt.legend(loc='best')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    print("----This program is an illustrator for bootstrapping----")
    print("The generated sample is normally distributed.")
    print("--------")
    try:
        while True:
            n = int(input("Please input the size of the sample data set(between 0 and 10000): "))
            if n >=0 and n <=10000:
                break
            else:
                print("Number out of range!")
        mu = float(input("Please input the mean of the distribution:"))
        sigma = float(input("Please input the standard deviation of the distribution:"))
        while True:
            num = int(input(
            "Please input the times of bootstrapping (between 0 and 10): "))
            if num >=0 and num <=10:
                break
            else:
                print("Number out of range!")
    except:
        print("Input error!")
    data = getSample(n, mean=mu, stdev=sigma)
    boots = getBoots(data, num)
    drawplot(data, boots)
