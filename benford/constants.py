DIGS = {1: 'F1D', 2: 'F2D', 3: 'F3D', 22: 'SD', -2: 'L2D'}

SEC_ORDER_DIGS = {key: f'{val}_sec' for key, val in DIGS.items()}

REV_DIGS = {'F1D': 1, 'F2D': 2, 'F3D': 3, 'SD': 22, 'L2D': -2}

LEN_TEST = {1: 9, 2: 90, 3: 900, 22: 10, -2: 100}

TEST_NAMES = {'F1D': 'First Digit Test', 'F2D': 'First Two Digits Test',
         'F3D': 'First Three Digits Test', 'SD': 'Second Digit Test',
         'L2D': 'Last Two Digits Test',
         'F1D_sec': 'First Digit Second Order Test',
         'F2D_sec': 'First Two Digits Second Order Test',
         'F3D_sec': 'First Three Digits Second Order Test',
         'SD_sec': 'Second Digit Second Order Test',
         'L2D_sec': 'Last Two Digits Second Order Test',
         'F1D_Summ': 'First Digit Summation Test',
         'F2D_Summ': 'First Two Digits Summation Test',
         'F3D_Summ': 'First Three Digits Summation Test',
         'Mantissas': 'Mantissas Test'
         }

# Critical values for Mean Absolute Deviation
MAD_CONFORM = {1: [0.006, 0.012, 0.015], 2: [0.0012, 0.0018, 0.0022],
            3: [0.00036, 0.00044, 0.00050], 22: [0.008, 0.01, 0.012],
            -2: None, 'F1D': 'First Digit', 'F2D': 'First Two Digits',
            'F3D': 'First Three Digits', 'SD': 'Second Digits'}

# Color for the plotting
COLORS = {'m': '#00798c', 'b': '#E2DCD8', 's': '#9c3848',
          'af': '#edae49', 'ab': '#33658a', 'h': '#d1495b',
          'h2': '#f64740', 't': '#16DB93'}

# Critical Z-scores according to the confindence levels
CONFS = {None: None, 80: 1.285, 85: 1.435, 90: 1.645, 95: 1.96,
         99: 2.576, 99.9: 3.29, 99.99: 3.89, 99.999: 4.417,
         99.9999: 4.892, 99.99999: 5.327}

P_VALUES = {None: 'None', 80: '0.2', 85: '0.15', 90: '0.1', 95: '0.05',
            99: '0.01', 99.9: '0.001', 99.99: '0.0001', 99.999: '0.00001',
            99.9999: '0.000001', 99.99999: '0.0000001'}

# Critical Chi-Square values according to the tests degrees of freedom
# and confidence levels
CRIT_CHI2 = {8: {80: 11.03, 85: 12.027, 90: 13.362, 95: 15.507,
                 99: 20.090, 99.9: 26.124, 99.99: 31.827, None: None,
                 99.999: 37.332, 99.9999: 42.701, 99.99999: 47.972},
             9: {80: 12.242, 85: 13.288, 90: 14.684, 95: 16.919,
                 99: 21.666, 99.9: 27.877, 99.99: 33.72, None: None,
                 99.999: 39.341, 99.9999: 44.811, 99.99999: 50.172},
             89: {80: 99.991, 85: 102.826, 90: 106.469, 95: 112.022,
                  99: 122.942, 99.9: 135.978, 99.99: 147.350,
                  99.999: 157.702, 99.9999: 167.348, 99.99999: 176.471,
                  None: None},
             99: {80: 110.607, 85: 113.585, 90: 117.407,
                  95: 123.225, 99: 134.642, 99.9: 148.230,
                  99.99: 160.056, 99.999: 170.798, 99.9999: 180.792,
                  99.99999: 190.23, None: None},
             899: {80: 934.479, 85: 942.981, 90: 953.752, 95: 969.865,
                   99: 1000.575, 99.9: 1035.753, 99.99: 1065.314,
                   99.999: 1091.422, 99.9999: 1115.141,
                   99.99999: 1137.082, None: None}
             }

# Critical Kolmogorov-Smirnov values according to the confidence levels
# These values are yet to be divided by the square root of the sample size
CRIT_KS = {80: 1.073, 85: 1.138, 90: 1.224, 95: 1.358, 99: 1.628,
           99.9: 1.949, 99.99: 2.225, 99.999: 2.47,
           99.9999: 2.693, 99.99999: 2.899, None: None}
