import matplotlib.pyplot as plt
import numpy as np

from PIL import Image

class Histogram_equalization:
    def __init__(self, name):
        self.image = Image.open(name)
        self.array = np.array(self.image)
        self.elements, self.elementsCounts = self.Calculate_frequency(self.array)
        
    def global_approach(self):
        self.show_histogram(self.elements, self.elementsCounts)
        self.Equalization(self.elements, self.elementsCounts)
        
    def Local_approach():
        height, width = image_array.shape[:2]

        block_size = height // 4 
        blocks = []
        for i in range(4):
            for j in range(4):
                block = image_array[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size]
                blocks.append(block)
                
        for i in range(len(blocks)):
            blocks[i] = Equalization(blocks[i])

        return np.vstack([np.hstack([blocks[4*i+j] for j in range(4)]) for i in range(4)])
    def Calculate_frequency(image_array):
        # sort elements
        unique_elements, counts = np.unique(image_array, return_counts=True)
        sort_index = np.argsort(unique_elements)
        unique_elements = unique_elements[sort_index]
        counts = counts[sort_index]
        return unique_elements, counts
        
            
    def Equalization(elements, counts):
        # Accumulate
        length = len(elements)
        for i in range(length-1):
            counts[i+1] += counts[i]

        # Equalization
        cdfMax = counts[length-1]
        cdfMin = counts[0]
        cdfRange = cdfMax - cdfMin
        for j in range(length):
            counts[j] = round( (counts[j] - cdfMin) / cdfRange * 255 )
        
        result_array = np.copy(image_array)
        for i in range(length):
            mask = (image_array == unique_elements[i])
            result_array[mask] = counts[i]
        
        return result_array

    def show_histogram(x, y):
        plt.bar(x, y)
        plt.title('Value Counts Histogram')
        plt.xlabel('Value')
        plt.ylabel('Count')

        # 显示图形
        plt.show()
        
Lena = Histogram_equalization("Lena.bmp")
Lena.global_approach()
Lena_Global = Image.fromarray(Equalization(Lena_array))
Lena_Global.save("Lena_Global.bmp")
Lena_Global.close()

Lena_Local = Image.fromarray(Local_Equalization(Lena_array))
Lena_Local.save("Lena_Local.bmp")
Lena_Local.close()
Lena.close()

# Peppers = Image.open("Peppers.bmp")

# Peppers_Global = Image.fromarray(Equalization(np.array(Peppers)))
# Peppers_Global.save("Peppers_Global.bmp")
# Peppers_Global.close() 

# Peppers_Local = Image.fromarray(Local_Equalization(np.array(Peppers)))
# Peppers_Local.save("Peppers_Local.bmp")
# Peppers_Local.close()

# Peppers.close()
