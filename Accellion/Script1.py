from __future__ import division
class CropRatio:
    def __init__(self):
        self._crops = {}
        self._total_weight = 0
        print(self._total_weight)

    def add(self, name, crop_weight):
        curr_crop_weight = 0

        curr_crop_weight = curr_crop_weight + crop_weight
        print "The first current weight", curr_crop_weight

        self._total_weight += curr_crop_weight
        if name not in self._crops.values():
            self._crops[name] = self._total_weight

    def proportion(self, name):
        return self._crops[name]/self._total_weight


# To see the output, uncomment the lines below:
crop_ratio = CropRatio()

crop_ratio.add('Wheat', 5)
crop_ratio.add('Wheat', 4)
crop_ratio.add('Rice', 1)

out = crop_ratio.proportion("Wheat")
print "The ratio portion",out
