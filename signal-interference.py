"""Calculate the signal/interference ratio for a network with 3 links""" 

class Links():

    def __init__(self, gains, noise, target_sirs):
        # gains is a 3x3 matrix for 3 links
        self.gains = gains

        # noise is a 3 element vector of noise for each link
        self.noise = noise

        # target_ratios is the vector of desired `sir`
        # (signal/interference ratios)
        self.target_sirs = target_sirs


    def update_power(self, start_powers, iterations=1):
        pass

    def compute_new_sirs(self, start_powers):
        a_gain = self.gains[0][0]
        b_gain = self.gains[1][1]
        c_gain = self.gains[2][2]

        a_power, b_power, c_power = start_powers
        a_noise, b_noise, c_noise = self.noise

        a_measured_sir = a_power * a_gain / ((self.gains[0][1] * b_power) + (self.gains[0][2] * c_power) + a_noise)
        b_measured_sir = b_power * b_gain / ((self.gains[1][0] * a_power) + (self.gains[1][2] * c_power) + b_noise)
        c_measured_sir = b_power * c_gain / ((self.gains[2][0] * a_power) + (self.gains[2][1] * b_power) + c_noise)

        new_a = target_sirs[0] / a_measured_sir * a_power
        new_b = target_sirs[1] / b_measured_sir * b_power
        new_c = target_sirs[2] / c_measured_sir * c_power

        print("A: {}, B: {}, C: {}".format(new_a, new_b, new_c))

gains = [[1, .2, .1], [.2, .9, .3], [.2, .2, 1]]
noise = [.1, .1, .1]
target_sirs = [1.5, 3.0, 1.5]

links = Links(gains, noise, target_sirs)
links.compute_new_sirs([1, 1, 1])




