import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import ticker as tick
import sys
import seaborn as sns
sns.set_style("whitegrid")





if __name__ == '__main__':
        #print(sys.argv)
        stat_average_data = []
        cm = mpl.cm.gist_rainbow
        n_colors = len(sys.argv[1:])
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_color_cycle([cm(1.*i/n_colors) for i in range(n_colors)])
        list_a = []

        for i in sys.argv[1:]:
                raw_data = np.loadtxt(i,delimiter = '\t')
                array_y = np.asarray(raw_data[180:].T[1])
                #print(array_y)
                #print(max(array_y))
                list_a.append(max(array_y))
        #print(max(list_a))

        



        for i in sys.argv[1:]:
                raw_data = np.loadtxt(i,delimiter = '\t')
                analysis_x = np.asarray(raw_data[180:].T[0])
                analysis_y = np.asarray(raw_data[180:].T[1])

                normalized_y = []

                for v in analysis_y:
                        #print(v)
                        s = v/max(list_a)
                        #print(s)
                        normalized_y.append(s)
                #plt.plot(analysis_x,normalized_y,label = i)
                plt.plot(analysis_x,normalized_y,label = i)

        #plt.gca().xaxis.set_major_locator(tick.MultipleLocator(10))
        plt.title("Absorbance spectrum")
        plt.xlabel("wavelength(nm)")
        plt.ylabel("Absorbance")
        plt.ylim([0,1.05])
        plt.xlim([400,700])
        plt.legend()
        plt.show()


